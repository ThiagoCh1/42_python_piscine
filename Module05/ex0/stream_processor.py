from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    @abstractmethod
    def validate(self, data: Any) -> str:
        pass
    def format_output(self, result: str) -> str:
        return result

class NumericProcessor(DataProcessor):

class TextProcessor(DataProcessor):