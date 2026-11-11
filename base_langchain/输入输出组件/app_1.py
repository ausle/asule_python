
import os
from dotenv import load_dotenv
from langchain_classic.chains.question_answering.refine_prompts import chat_qa_prompt_template
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder

from base_langchain.chapter02.article_generator.app import topic

#默认情况下，load_dotenv() 通常会从脚本执行时的目录向上查找 .env 文件。
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
    model="deepseek-v4-flash",
    temperature=0.9,
    extra_body={"thinking": {"type": "disabled"}},
)

# Langchain提供了很多种提示词类，其中最常用的就是：PromptTemplate。
# 一、PromptTemplate
prompt_template=PromptTemplate.from_template(
    template="请把这段文字翻译成法语：{text}"
)

prompt = prompt_template.format(text='我真的很喜欢朱珠')
# answer = llm.invoke(prompt).content
# print(answer)

# RunnableSequence 可将复杂的LLM任务拆分为更小的、可重复使用的模块。
# 使用 “|” 运算符来创建RunnableSequence，用来组合多个runnable。
chain=  prompt_template | llm
reply1=chain.invoke({"text": "我真的很喜欢朱珠"})
print(reply1)


# 二、ChatPromptTemplate
# 创建聊天提示词模板时
# system用于设定AI的角色和背景，user是人类的输入的内容。ChatPromptTemplate将组合这些信息，一起发给大模型。
chat_prompt_template1=ChatPromptTemplate.from_messages([
    ("system","你是一个擅长讲儿童睡前小故事的AI助手，你熟悉格林童话、小王子等优秀儿童文学，你讲的故事必须符合儿童审美和寓教于乐。"),
    ("user","请给我一个关于{topic}的故事吧，200字以内")
])
#
reply2=chat_prompt_template1.invoke({"topic":"马斯克"})
print(reply2)


# 三、MessagesPlaceholder
# 如果希望在messages列表的指定位置插入消息，可以使用MessagesPlaceholder来实现
chat_prompt_template2=ChatPromptTemplate.from_messages([
    ("system","你是一个擅长讲成人笑话的AI助手，你熟悉各种成人内容，你讲的故事必须符合好色之人的审美。"),
    MessagesPlaceholder("message")
])

# 声明了一个message
prompt_template2=PromptTemplate.from_template(
    template="请给我一个关于{topic}的故事吧，200字以内"
)
prompt_message_2=prompt_template2.format(topic="雷军")
chat_prompt_template3=chat_prompt_template2.invoke({
    "message": [HumanMessage(content=prompt_message_2)]
})

reply3=llm.invoke(chat_prompt_template3)
print(reply3)















