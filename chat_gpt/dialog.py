import numpy as np

from three_dimentions.tools.functions import distance


class ChatGptDialog:
    # 初始化方法
    def __init__(self):
        self.system_message = {"role": "system",
                               "content": "现在有一篇四千字左右的第一人称回忆录，需要用更好的文笔和更清晰的逻辑进行重新撰写。"
                                          "注意，需要保留回忆录里陈述的所有事件。请按照章节结构，输出新修改的回忆录。"}
        self.user_message = dict()
        self.assistant_message = dict()
        self.dialog = [self.system_message]

    def create_user_message(self, original_text):
        user_content = original_text
        self.user_message = {"role": "user",
                             "content": user_content}
        self.dialog.append(self.user_message)

    def create_assistant_message(self, response):
        """
        基于本地引擎推理结果，或者chatgpt返回的assistant结果，重新格式化，并加入chatgpt的对话记录中
        :param response:
        :return:
        """
        self.assistant_message = {"role": "assistant", "content": response}
        self.dialog.append(self.assistant_message)
