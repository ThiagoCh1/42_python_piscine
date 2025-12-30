from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return "Universal output: " + result


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error in the validation"
        count = 0
        total = 0
        for num in data:
            count += 1
            total += num
        avg = total / count
        text = f"Processed {count} numeric values, sum={total}, avg={avg}"
        return text

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        if not data:
            return False
        for num in data:
            if type(num) is not int:
                return False
        return True

    def format_output(self, result: str) -> str:
        return "Output: " + result


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error in the validation"
        count = len(data)
        words = len(data.split())
        text = f"Processed {count} characters, {words} words"
        return text

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        if not data:
            return False
        if type(data) is not str:
            return False
        return True

    def format_output(self, result: str) -> str:
        return "Output: " + result


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error in the validation"

        level, message = data.split(": ", 1)

        if level == "ERROR":
            return f"[ALERT] ERROR level detected: {message}"
        return f"[{level}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        if not data:
            return False
        if type(data) is not str:
            return False
        if ": " not in data:
            return False
        return True

    def format_output(self, result: str) -> str:
        return "Output: " + result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    numeric = NumericProcessor()
    print("Initializing Numeric Processor...")
    numbers = [1, 2, 3, 4, 5]
    print("Processing data:", numbers)
    if numeric.validate(numbers):
        print("Validation: Numeric data verified")
    else:
        print("Validation: Numeric data invalid")
    print(numeric.format_output(numeric.process(numbers)) + "\n")

    text = TextProcessor()
    print("Initializing Text Processor...")
    message = "Hello Nexus World"
    print('Processing data: "' + message + '"')
    if text.validate(message):
        print("Validation: Text data verified")
    else:
        print("Validation: Text data invalid")
    print(text.format_output(text.process(message)) + "\n")

    log = LogProcessor()
    print("Initializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    print('Processing data: "' + log_data + '"')
    if log.validate(log_data):
        print("Validation: Log entry verified")
    else:
        print("Validation: Log entry invalid")
    print(log.format_output(log.process(log_data)) + "\n")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data_list = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready"
    ]

    for i in range(len(processors)):
        result = processors[i].process(data_list[i])
        print("Result " + str(i + 1) + ": " + result)


if __name__ == "__main__":
    main()
