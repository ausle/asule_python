import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
# 你安装的是 LangChain 1.x，新版已经把旧版的 LLMChain、SequentialChain 移到了 langchain-classic。
from langchain_classic.chains import LLMChain, SequentialChain
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
    model="deepseek-v4-flash",
    temperature=0.9,
    extra_body={"thinking": {"type": "disabled"}},
)

# 设置页面显示的标题
st.title('热门文章AI生成器')
# 生成一个文本框，里面带有提示信息
topic = st.text_input('请输入你想写的话题：')

if topic:
    # 创建一个提示词模版
    prompt = """
              你是一个擅长编写各种文体的自媒体编辑，
              请用{language}根据话题：{topic}编写1个有创意的标题。
              """
    prompt_to_create_title = PromptTemplate(
        input_variables=["topic", "language"],
        template=prompt)
    # 创建一个生成title的chain
    chain_to_create_title = LLMChain(llm=llm,
                                     prompt=prompt_to_create_title,
                                     output_key="title", verbose=True)
    # 创建生成文章的提示词模版
    prompt_template_for_article = """
           你是一个擅长编写各种文体的自媒体编辑，
           请根据标题：{title}，生成一篇论述清晰的{language}文章，字数{chars}个字以内, 如果超出请进行精简。
           """
    prompt_to_create_article = PromptTemplate(
        input_variables=["title", "language", "chars"],
        template=prompt_template_for_article)

    # 创建一个生成文章正文的chain
    chain_to_create_article = LLMChain(llm=llm, prompt=prompt_to_create_article, output_key="article")

    ##### langchain顺序链
    # 多链进行合并，组合成一个顺序链，会按照顺序链中顺序，执行大模型任务。
    # 这样的好处是什么？
    # SequentialChain还提供复杂的业务流程、条件分支、循环等控制。
    overall_chain = SequentialChain(
        chains=[chain_to_create_title, chain_to_create_article],
        input_variables=["topic", "language", "chars"],
        output_variables=["title", "article"],
        verbose=True
    )
    response = overall_chain.invoke({"topic": topic, "language": "中文", "chars": "100"})
    # 将AI生成的标题输出到网页上
    st.write('生成的标题如下:\r' + response["title"])
    st.write('生成的文章内容：\r' + response["article"])
