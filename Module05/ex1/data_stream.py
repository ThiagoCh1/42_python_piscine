from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        filtered_list = []
        for item in data_batch:
            if isinstance(item, str) and criteria in item:
                filtered_list += [item]
        return filtered_list

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Generic"
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.last_avg = 0.0
        self.total_readings = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        total = 0.0
        count = 0
        allowed = "0123456789.-"

        for item in data_batch:
            try:
                if "temp" in item:
                    num_str = ""
                    parsing = False
                    for char in item:
                        if char in allowed:
                            parsing = True
                            num_str += char
                        elif parsing:
                            break

                    if num_str != "" and num_str != ".":
                        val = float(num_str)
                        total += val
                        count += 1
            except ValueError:
                pass

        if count > 0:
            self.last_avg = total / count
        self.total_readings = count

        return (f"Stream ID: {self.stream_id}, Type: Environmental Data\n"
                f"Processing sensor batch: {data_batch}\n"
                f"Sensor analysis: {count} readings processed, "
                f"avg temp: {self.last_avg}\n")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "critical":
            filtered = []
            allowed = "0123456789.-"
            for item in data_batch:
                try:
                    if "temp" in item:
                        num_str = ""
                        parsing = False
                        for char in item:
                            if char in allowed:
                                parsing = True
                                num_str += char
                            elif parsing:
                                break
                        if num_str != "" and num_str != ".":
                            val = float(num_str)
                            if val > 80.0:
                                filtered += [item]
                except ValueError:
                    pass
            return filtered
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Sensor",
            "last_average": self.last_avg,
            "batch_size": self.total_readings
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.net_flow = 0
        self.operations = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        flow = 0
        count = 0

        for item in data_batch:
            count += 1
            try:
                val = 0
                if "buy" in item:
                    num_part = item[5:]
                    val = int(num_part)
                    flow += val
                elif "sell" in item:
                    num_part = item[6:]
                    val = int(num_part)
                    flow -= val
            except ValueError:
                pass

        self.net_flow = flow
        self.operations = count

        return (f"Stream ID: {self.stream_id}, Type: Financial Data\n"
                f"Processing transaction batch: {data_batch}\n"
                f"Transaction analysis: {count} operations, "
                f"net flow: {flow:+} units\n")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            filtered = []
            for item in data_batch:
                try:
                    val = 0
                    if "buy" in item:
                        num_part = item[5:]
                        val = int(num_part)
                    elif "sell" in item:
                        num_part = item[6:]
                        val = int(num_part)

                    if val > 500:
                        filtered += [item]
                except ValueError:
                    pass
            return filtered
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Transaction",
            "net_flow": self.net_flow,
            "operations": self.operations
        }


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.error_count = 0
        self.total_events = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        count = 0
        errors = 0

        for item in data_batch:
            count += 1
            if "error" in item:
                errors += 1

        self.total_events = count
        self.error_count = errors

        return (f"Stream ID: {self.stream_id}, Type: System Events\n"
                f"Processing event batch: {data_batch}\n"
                f"Event analysis: {count} events, {errors} error detected\n")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Event",
            "error_count": self.error_count,
            "total_events": self.total_events
        }


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: Dict[str, DataStream] = {}

    def add_stream(self, stream: DataStream) -> None:
        self.streams[stream.stream_id] = stream

    def process_stream(self, stream_id: str,
                       data_batch: List[Any]) -> Optional[str]:
        if stream_id in self.streams:
            stream = self.streams[stream_id]
            return stream.process_batch(data_batch)
        return None

    def manage_batch(self, batch_data: Dict[str, List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")

        sensor_alerts = 0
        large_transactions = 0

        for stream_id, data in batch_data.items():
            self.process_stream(stream_id, data)

            if stream_id in self.streams:
                stream = self.streams[stream_id]
                stats = stream.get_stats()
                s_type = stats["type"]

                if s_type == "Sensor":
                    count = stats["batch_size"]
                    print(f"- Sensor data: {count} readings processed")

                    critical_list = stream.filter_data(data, "critical")
                    for _ in critical_list:
                        sensor_alerts += 1

                elif s_type == "Transaction":
                    ops = stats["operations"]
                    print(f"- Transaction data: {ops} operations processed")

                    large_list = stream.filter_data(data, "large")
                    for _ in large_list:
                        large_transactions += 1

                elif s_type == "Event":
                    evts = stats["total_events"]
                    print(f"- Event data: {evts} events processed")

        print("Stream filtering active: High-priority data only")
        print(f"Filtered results: {sensor_alerts} critical sensor alerts, "
              f"{large_transactions} large transaction")
        print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    print("CODE NEXUS POLYMORPHIC STREAM SYSTEM")

    processor = StreamProcessor()

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    processor.add_stream(sensor)
    sensor_data = ["temp: 22.5", "humidity: 65", "pressure: 1013"]
    print(sensor.process_batch(sensor_data))

    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    processor.add_stream(trans)
    trans_data = ["buy: 100", "sell: 150", "buy: 75"]
    print(trans.process_batch(trans_data))

    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    processor.add_stream(event)
    event_data = ["login", "error", "logout"]
    print(event.process_batch(event_data))

    batch_input = {
        "SENSOR_001": ["temp: 85.0", "temp: 92.0"],
        "TRANS_001": ["buy: 200", "sell: 50", "buy: 50", "buy: 1000"],
        "EVENT_001": ["system_start", "check_disk", "disk_ok"]
    }

    processor.manage_batch(batch_input)
