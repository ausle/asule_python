import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# 默认从当前目录下的.env文件加载环境变量
load_dotenv()
# 从环境变量中获取openai的api key
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
    # 创建一个提示词模版，langchain提供了提示词模板功能：PromptTemplate
    prompt_template = PromptTemplate.from_template("请用{language}根据话题：{topic}编写{count}个有创意的标题")
    # 格式化提示词并添加变量
    prompt = prompt_template.format(topic=topic, count=1, language='中文')
    # 因为 ChatOpenAI.invoke() 返回的是消息对象，调用部分需要取 .content：
    title = llm.invoke(prompt).content
    # 将AI生成的标题输出到网页上
    st.write('生成的标题如下:\r' + title)
    if title:
        # 创建生成文章的提示词模版
        prompt_template = PromptTemplate.from_template(
            "请根据标题：{title}，生成一篇论述清晰的{language}文章，字数{chars}个字以内, 如果超出请进行精简。"
        )
        prompt = prompt_template.format(title=title, language='中文', chars=800)
        # 必须设置大一点的最大token数，否则生成的文章内容会被截断
        article = llm.invoke(prompt, max_tokens=4000).content
        print(article)
        st.write('生成的文章内容：\r' + article)
        
