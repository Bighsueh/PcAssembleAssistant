from task.Task import Task
# 詢問品牌偏好
class BrandPreferenceTask(Task):
    def check_requirement(self, user_input):
        return True

    def process(self, user_input):
        return f"您偏好的品牌是：{user_input}。請問您的預算範圍是多少？"