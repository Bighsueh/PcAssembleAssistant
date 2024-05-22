from task.Task import Task
# 詢問主要用途
class UsageTask(Task):
    def check_requirement(self, user_input):
        return True  # 假設任何輸入都是有效的

    def process(self, user_input):
        return f"您的主要用途是：{user_input}。請問您對品牌有何偏好？"
