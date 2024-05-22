from state.State import FlowState
from task.UsageTask import UsageTask
from task.BrandPreferenceTask import BrandPreferenceTask

# 用戶查詢流程
class UserQueryFlow(FlowState):
    def __init__(self, controller):
        super().__init__(controller)
        self.tasks = [
            UsageTask(),
            BrandPreferenceTask(),
            # BudgetTask(),
            # AdditionalRequirementsTask()
        ]
        self.current_task_index = 0

    def handle_input(self, user_input):
        task = self.tasks[self.current_task_index]
        if task.check_requirement(user_input):
            response = task.process(user_input)
            if self.current_task_index < len(self.tasks) - 1:
                self.current_task_index += 1
                return response
            else:
                self.controller.change_flow(None)
                return response + " 我們將根據您的需求推薦適合的產品。"
        else:
            return "請提供有效的回答以便進行下一步。"

    def go_to_next_task(self):
        pass