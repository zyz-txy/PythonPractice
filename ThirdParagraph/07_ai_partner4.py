import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

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

#保存会话信息
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "personality": st.session_state.personality,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        # 创建文件夹保存会话信息
        if not os.path.exists("sessions"):
            os.makedirs("sessions")
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

#生成会话标识函数
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#加载所有会话列表信息
def load_sessions():
    session_list = []
    #加载sessions目录下的所有文件
    if os.path.exists("sessions"):
        for file in os.listdir("sessions"):
            if file.endswith(".json"):
                filename = file[:-5]
                session_list.append(filename)
    return session_list

#加载指定回话
def load_session(session):
    try:
        if os.path.exists(f"sessions/{session}.json"):
            # 读取会话数据
            with open(f"sessions/{session}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
            st.session_state.nick_name = session_data["nick_name"]
            st.session_state.personality = session_data["personality"]
            st.session_state.current_session = session_data["current_session"]
            st.session_state.messages = session_data["messages"]
    except Exception as e:
        st.error(f"加载会话出错!{e}")

#大标题
st.title("AI智能伴侣")
#logo
st.logo("resources/logo.png")
#系统提示词
system_prompt = """
    你叫 %s, 现在你是用户的真实伴侣, 请完全代入伴侣角色。:
    规则:
        1. 每次只回1条消息
        2. 禁止任何场景或状态描述性文字
        3. 匹配用户的语言
        4. 回复简短, 像微信聊天一样
        5. 有需要的话可以用❤️等emoji表情
        6. 用符合伴侣性格的方式对话
        7. 回复的内容, 要充分体现伴侣的性格特征
    伴侣性格:
        - %s
    你必须严格遵守上述规则来回复用户。
"""


#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#昵称输入框
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"

#性格输入框
if "personality" not in st.session_state:
    st.session_state.personality = "活泼开朗的台湾姑娘"

#会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

#左侧侧边栏-with是stramlit里面用于创建一个侧边栏的上下文管理器
with st.sidebar:
    #会话信息
    st.subheader("AI控制面板")
    #新建会话按钮
    if st.button("新建对话",icon = "✏️",width="stretch"):#和父元素宽度一致
        #1保存当前回话信息
        save_session()
        #2创建新的会话
        #如果存在聊天信息，则创建新的会话
        if st.session_state.messages :
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            #st.rerun()
    #会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1,col2 = st.columns([4,1])  # 创建两列
        with col1:
            #加载指定会话信息
            #三元运算符，如果按钮被点击，则加载会话信息并重新运行 -->语法：值1 if 条件 else 值2
            if st.button(session,width="stretch",icon = "📒",type = "primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            #删除指定会话信息
            #所有的组件都得有唯一标识，可以用key区别
            if st.button("",width = "stretch",icon = "❌️",key = session):
                pass

    #伴侣信息
    st.subheader("伴侣信息")
    #昵称输入框
    st.session_state.nick_name = st.text_input("昵称🙃",placeholder="请输入伴侣昵称",value=st.session_state.nick_name)
    #性格输入框
    st.session_state.personality = st.text_area("性格😉",placeholder="请输入伴侣性格",value=st.session_state.personality)

#展示聊天信息
st.text(f"会话名称{st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

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

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            # 系统提示词
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.personality)},
            # 用户提示词
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

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

    #保存会话信息到文件中
    save_session()