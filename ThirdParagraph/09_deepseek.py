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

# ------------- 工具函数 -------------

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
        if not os.path.exists("session_ds"):
            os.makedirs("session_ds")
        with open(f"session_ds/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

#生成会话标识函数
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# [优化] 按文件名中的时间戳倒序排序（越新的越靠前）
def load_sessions():
    session_list = []
    if os.path.exists("session_ds"):
        for file in os.listdir("session_ds"):
            if file.endswith(".json"):
                filename = file[:-5]
                session_list.append(filename)
        # 时间格式可直接字符串比较，倒序排列
        session_list.sort(reverse=True)
    return session_list

# [优化] 重命名当前会话为当前时间戳（仅在聊天后调用）
def rename_current_session():
    old_name = st.session_state.current_session
    new_name = generate_session_name()
    if old_name == new_name:
        return  # 同一秒内重复调用则跳过
    # 先确保以旧名称保存
    save_session()
    old_path = f"session_ds/{old_name}.json"
    new_path = f"session_ds/{new_name}.json"
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
    st.session_state.current_session = new_name
    # 用新名称再保存一次，保证文件内容与状态一致
    save_session()

#加载指定回话
def load_session(session):
    try:
        if os.path.exists(f"session_ds/{session}.json"):
            # 读取会话数据
            with open(f"session_ds/{session}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
            st.session_state.nick_name = session_data["nick_name"]
            st.session_state.personality = session_data["personality"]
            st.session_state.current_session = session_data["current_session"]
            st.session_state.messages = session_data["messages"]
    except Exception as e:
        st.error(f"加载会话出错!{e}")

#删除会话
def delete_session(session_name):
    try:
        if os.path.exists(f"session_ds/{session_name}.json"):
            os.remove(f"session_ds/{session_name}.json")
            # [优化] 删除当前会话后立即创建新空会话并保存
            if session_name == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_name()
                save_session()
    except Exception as e:
        st.error(f"会话不存在！{e}")

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

# ------------- 状态初始化 -------------
# [优化] 初始状态集中管理
if "messages" not in st.session_state:
    st.session_state.messages = []

if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"

if "personality" not in st.session_state:
    st.session_state.personality = "活泼开朗的台湾姑娘"

if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()
    save_session()  # [优化] 初始化立即存盘

# ------------- 侧边栏（提前渲染，交互优先） -------------
with st.sidebar:
    # ========== 自定义样式（仅影响侧边栏） ==========
    st.markdown("""
    <style>
    /* 让侧边栏整体更有呼吸感 */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        box-shadow: 2px 0 10px rgba(0,0,0,0.05);
    }
    /* 当前会话高亮按钮：浅蓝色 */
    [data-testid="stSidebar"] button[kind="primary"] {
        background-color: #b3d9ff !important;   /* 浅蓝 */
        border-color: #b3d9ff !important;
        color: #1a1a1a !important;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.2s;
    }
    /* 普通按钮 */
    [data-testid="stSidebar"] button[kind="secondary"] {
        border-radius: 8px;
        transition: all 0.2s;
    }
    /* 悬停效果 */
    [data-testid="stSidebar"] button:hover {
        background-color: #e6f2ff !important;
        border-color: #b3d9ff !important;
        color: #000 !important;
    }
    /* 删除按钮单独调整，避免被通用样式影响 */
    [data-testid="stSidebar"] button[kind="secondary"]:has(span:empty) {
        /* 针对只有图标没有文字的删除按钮，最小化 */
        padding: 0.2rem 0.4rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.subheader("AI控制面板")

    # 新建会话按钮
    if st.button("新建对话", icon="✏️", width="stretch"):  # 和父元素宽度一致
        save_session()                # 1保存当前回话信息
        st.session_state.messages = [] # 2创建新的会话
        st.session_state.current_session = generate_session_name()
        save_session()
        st.rerun()  # [优化] 立即重跑，阻止主区域执行

    st.text("会话历史")
    session_list = load_sessions()  # [优化] 按时间倒序排列
    for session in session_list:
        col1, col2 = st.columns([4, 1])  # 创建两列
        with col1:
            # 加载指定会话信息
            # 三元运算符，如果按钮被点击，则加载会话信息并重新运行
            if st.button(session, width="stretch", icon="📒",
                         type="primary" if session == st.session_state.current_session else "secondary"):
                save_session()  # [优化] 切换前保存当前进度
                load_session(session)
                st.rerun()      # [优化] 单次重跑
        with col2:
            # 删除指定会话信息
            if st.button("", width="stretch", icon="❌️", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()      # [优化] 单次重跑

    st.divider()
    st.subheader("伴侣信息")

    # [优化] 修改伴侣设定仅更新并保存，不触发 rerun，更不会重命名
    new_nick = st.text_input("昵称🙃", placeholder="请输入伴侣昵称",
                             value=st.session_state.nick_name)
    new_personality = st.text_area("性格😉", placeholder="请输入伴侣性格",
                                   value=st.session_state.personality)
    if new_nick != st.session_state.nick_name or new_personality != st.session_state.personality:
        st.session_state.nick_name = new_nick
        st.session_state.personality = new_personality
        save_session()  # 静默保存，不影响聊天

# ------------- 主区域 -------------
st.title("AI智能伴侣")
st.logo("resources/logo.png")
st.caption(f"当前会话：{st.session_state.current_session}")

#展示聊天信息
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

    # [优化] 用最新时间重命名文件，然后重跑，侧边栏会自动置顶并高亮当前会话
    rename_current_session()
    st.rerun()