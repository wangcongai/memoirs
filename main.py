import os
import sys
from openai import OpenAI

from chat_gpt import dialog
from config import config
from config.logger import logger, log_directory, file_name


def initiate_dialog():
    """
    初始化对话信息，告诉chatgpt场景，问题，以及回答方法
    :return:
    """
    logger.info("SYSTEM: %s " % MyDialog.system_message.get('content'))
    with open('../original_memoirs.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        content = ("以下是完整原始文本，修改后的回忆录共分5个章节，每个章节需要有1个自己的子标题。修改后的回忆录需要包含原始文本里的所有事实陈述，"
                   "在此基础上，需要体现作者优秀的文学素养，饱满的感情和清晰的逻辑。请先输出第一个章节的改写") + content
    MyDialog.create_user_message(original_text=content)
    logger.info("USER: %s" % MyDialog.user_message.get('content'))


def interact_with_gpt():
    logger.info('以下开始调用%s进行推理\n' % config.MODEL)

    # 调用OpenAI的chat.completions.create接口，生成助手的消息，即水下机器人的动作
    gpt_response = client.chat.completions.create(model=config.MODEL,
                                                  messages=MyDialog.dialog,
                                                  temperature=config.TEMPERATURE)
    assistant_message = gpt_response.choices[0].message.content
    assistant_message = assistant_message.replace("\n", "")
    logger.info("Chatgpt输出第1部分: %s" % assistant_message)
    MyDialog.create_assistant_message(response=assistant_message)

    MyDialog.create_user_message(original_text="下面请输出修改的第2部分")
    gpt_response = client.chat.completions.create(model=config.MODEL,
                                                  messages=MyDialog.dialog,
                                                  temperature=config.TEMPERATURE)
    assistant_message = gpt_response.choices[0].message.content
    assistant_message = assistant_message.replace("\n", "")
    logger.info("Chatgpt输出第2部分: %s" % assistant_message)
    MyDialog.create_assistant_message(response=assistant_message)

    MyDialog.create_user_message(original_text="下面请输出修改的第3部分")
    gpt_response = client.chat.completions.create(model=config.MODEL,
                                                  messages=MyDialog.dialog,
                                                  temperature=config.TEMPERATURE)
    assistant_message = gpt_response.choices[0].message.content
    assistant_message = assistant_message.replace("\n", "")
    logger.info("Chatgpt输出第3部分: %s" % assistant_message)
    MyDialog.create_assistant_message(response=assistant_message)

    MyDialog.create_user_message(original_text="下面请输出修改的第4部分")
    gpt_response = client.chat.completions.create(model=config.MODEL,
                                                  messages=MyDialog.dialog,
                                                  temperature=config.TEMPERATURE)
    assistant_message = gpt_response.choices[0].message.content
    assistant_message = assistant_message.replace("\n", "")
    logger.info("Chatgpt输出第4部分: %s" % assistant_message)
    MyDialog.create_assistant_message(response=assistant_message)

    MyDialog.create_user_message(original_text="下面请输出修改的第5部分")
    gpt_response = client.chat.completions.create(model=config.MODEL,
                                                  messages=MyDialog.dialog,
                                                  temperature=config.TEMPERATURE)
    assistant_message = gpt_response.choices[0].message.content
    assistant_message = assistant_message.replace("\n", "")
    logger.info("Chatgpt输出第5部分: %s" % assistant_message)
    MyDialog.create_assistant_message(response=assistant_message)


if __name__ == '__main__':
    # 初始化OpenAI客户端
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    # 初始化ChatGpt对话对象
    MyDialog = dialog.ChatGptDialog()
    initiate_dialog()
    interact_with_gpt()
    logger.info('程序结束')
