#streamlit是一个用于快速基于python代码构建web网页的python库（数据科学及机器学习领域）

#安装streamlit（终端运行pip install streamlit）

#在python文件中引入streamlit模块
import streamlit as st

#基于streamlit提供的API来构建Web应用
st.title("基于streamlit的Web应用")
st.header("Streamlit 一级标题")
st.header("Streamlit 二级标题")

#运行程序：streamlit run xxx.py（在终端运行该命令即可启动streamlit服务）

#设置页面配置
st.set_page_config(
    #页面标题
    page_title="Streamlit入门",
    page_icon="🧊",
    #布局 #wide 铺满 / centered 中心
    layout="centered",
    #控制侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.itcast.cn',
        'Report a bug': "https://www.itcast.cn",
        'About': "# 这是一个Streamlit的入门页面~"
    }
)

#段落文字
st.write("布偶猫，又称“布拉多尔猫”，常被爱猫人士亲昵地称为“猫中仙女”或“小狗猫”。它凭借仙女般的颜值和温顺如布偶的性格，在全球范围内赢得了无数家庭的喜爱。")
st.write("布偶猫最令人过目不忘的，是那双深邃的湛蓝色眼睛，仿佛蕴藏着星辰大海。它属于中长毛猫，被毛丰厚柔滑，触感如兔毛般细腻。其最典型的特征是重点色——身体部分为浅色，而面部、耳朵、四肢和尾巴等末端颜色较深，这种独特的“面具”更添几分神秘。它体格健壮，是现存体型最大、体重最重的猫种之一，成年公猫体重甚至可达7-10公斤，但优雅的体态让它毫不显笨拙。")
st.write("如果说外表是它的通行证，那性格就是它的必杀技。布偶猫以极度温顺和忍耐著称，它们非常亲近人类，喜欢黏在主人身边，会像小狗一样在门口迎接你回家，甚至乐意被你抱在怀里。它天性安静，叫声轻柔，不会随意上蹿下跳搞破坏。对孩子和其他宠物也表现出极大的友善和包容，是理想的家庭伴侣猫。")

#图片
st.image("resources/vscode_background.png")#如果是从当前目录的话可以省略第一个./

#音频
st.audio("./resources/music.mp3")

#视屏
st.video("./resources/video.mp4")

#Logo
st.logo("resources/logo.png")

#表格
students_data = {
    "姓名": ["王林","Alice", "Bob", "Charlie"],
    "年龄": [19,25, 30, 35],
    "城市": ["哈尔滨", "New York", "Los Angeles", "Chicago"],
    "性别": ["男","女", "男", "男"]
}
st.table(students_data)

#输入框

#普通输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名是：{name}")

#单选按钮
gender = st.radio("请选择性别", ["男", "女","不愿透露"],index = 2)
st.write(f"您选择的性别是：{gender}")

age = st.number_input("请输入年龄")
st.write(f"您输入的年龄是：{age}")
city = st.selectbox("请选择城市", ["哈尔滨", "New York", "Los Angeles", "Chicago","不愿透露"],index = 4)
st.write(f"您选择的城市是：{city}")

#密码输入框
password = st.text_input("请输入密码", type="password")
st.write(f"您输入的密码是：{password}")