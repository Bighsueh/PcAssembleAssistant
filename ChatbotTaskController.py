from state.UserQueryFlow import UserQueryFlow

class ChatbotTaskController:
    def __init__(self):
        self.flows = {'user_query': UserQueryFlow(self)}
        self.current_flow = None

    def start_flow(self, flow_name):
        self.current_flow = self.flows.get(flow_name)
        if not self.current_flow:
            raise ValueError("流程未找到")

    def handle_input(self, user_input):
        if self.current_flow:
            return self.current_flow.handle_input(user_input)
        else:
            raise Exception("尚未開始任何流程")

    def change_flow(self, flow_name):
        self.current_flow = None
        return "流程完成！"
