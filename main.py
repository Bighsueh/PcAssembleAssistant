from ChatbotTaskController import ChatbotTaskController

controller = ChatbotTaskController()
controller.start_flow('user_query')
print(controller.handle_input("辦公室使用"))
print(controller.handle_input("Apple"))
print(controller.handle_input("20000元以下"))
print(controller.handle_input("輕便易攜"))
