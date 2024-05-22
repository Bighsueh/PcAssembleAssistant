from abc import ABC, abstractmethod

# 狀態模式實現的 FlowState 抽象基類
class FlowState(ABC):
    def __init__(self, controller):
        self.controller = controller

    @abstractmethod
    def handle_input(self, user_input):
        pass

    def go_to_next_task(self):
        pass