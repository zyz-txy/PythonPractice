import streamlit as st
import os
from openai import OpenAI

#设置页面配置
st.set_page_config(
    #页面标题
    page_title="AI智能伴侣",
    page_icon="🤖",
    #布局 #wide 铺满 / centered 中心
    layout="wide",
    #控制侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI智能伴侣")
#logo
st.logo("resources/logo.png")
#系统提示词
system_prompt = "You are a helpful assistant"

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else :
    #     st.chat_message("assistant").write(message["content"])

#创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY环境变量的名字，值就是你的API密钥）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#聊天框
prompt = st.chat_input("请输入您的问题：")
if prompt:
    st.chat_message("user").write(prompt)
    print("--->调用AI大模型，提示词：",prompt)
    # 保存用户提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与AI大模型进行交互
    # print([
    #     {"role": "system", "content": system_prompt},
    #     *st.session_state.messages
    # ])  日志调试

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            # 系统提示词
            {"role": "system", "content": system_prompt},
            # 用户提示词
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果（非流式输出解析方式）
    # print("<-----------大模型返回结果----------->", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    #流式输出解析方式
    response_message = st.empty()#创建一个空组件，用于展示大模型返回结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})
