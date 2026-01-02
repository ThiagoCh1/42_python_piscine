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

        avg = 0.0
        if count > 0:
            avg = total / count

        return f"Processed {count} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        is_empty = True
        for _ in data:
            is_empty = False
            break
        if is_empty:
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

        char_count = 0
        word_count = 0
        in_word = False

        for char in data:
            char_count += 1
            if char != ' ':
                if not in_word:
                    word_count += 1
                    in_word = True
            else:
                in_word = False

        return f"Processed {char_count} characters, {word_count} words"

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        if data == "":
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

        level = ""
        message = ""
        temp_buffer = ""
        found_split = False

        for char in data:
            if found_split:
                message += char
            else:
                if char == ' ':
                    if temp_buffer != "" and temp_buffer[-1] == ':':
                        level = temp_buffer[:-1]
                        found_split = True
                    else:
                        temp_buffer += char
                else:
                    temp_buffer += char

        if level == "ERROR":
            return f"[ALERT] ERROR level detected: {message}"
        return f"[{level}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        if data == "":
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

    idx = 0
    for processor in processors:
        current_data = data_list[idx]
        result = processor.process(current_data)
        print("Result " + str(idx + 1) + ": " + result)
        idx += 1


if __name__ == "__main__":
    main()
