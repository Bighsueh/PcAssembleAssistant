from abc import ABC, abstractmethod

class Task(ABC):
    @abstractmethod
    def check_requirement(self, user_input):
        pass

    @abstractmethod
    def process(self, user_input):
        pass