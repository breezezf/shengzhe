#我的主页
import base64
import streamlit as st
from PIL import Image
import wordcloud

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

bar_bg('月.jpg')
page_bg('水.jpg')

page = st.sidebar.radio("首页", ["发帖", "发现好友", "我的好友", "个人主页", "小程序"])

#侧边功能
def page_1():
    #发帖
    st.title('留言区')
    with open("leave_messages.txt", 'r', encoding='utf-8') as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == "阿短":
            with st.chat_message("🌚"):
                st.write(i[1], ":", i[2])
        elif i[1] == '编程猫':
            with st.chat_message("🌝"):
                st.write(i[1], ":", i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
    with open('leave_messages.txt', 'w', encoding='utf-8') as f:
        message = ''
        for i in messages_list:
            message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
        message = message[:-1]
        f.write(message)
def page_2():
    #发现好友
    with st.chat_message("🌞"):
        st.write("小火龙")
    with st.chat_message("🌟"):
        st.write("小火熊")
    with st.chat_message("🐔"):
        st.write("超级无敌宇宙霹雳霸王龙")
def page_3():
    #我的好友
    with st.chat_message("🌚"):
        st.write("阿短")
    with st.chat_message("🌝"):
        st.write("编程猫")
def page_4():
    #个人主页
    tab1,tab2,tab3 = st.tabs(['头像', '昵称', '个性签名'])
    d = ":green[人]"
    with tab1:
        st.image("头像.jpg")
        with open("头像.jpg", 'rb') as f:
            mymp3 = f.read()
        st.download_button(
            label = ':orange_heart:点击下载我可爱的头像:orange_heart:',
            data = mymp3,
            file_name = "可爱的熊二.jpg"
        )
    with tab2:
        st.title(d)
    with tab3:
        st.title("看啥看，暗恋我啊？我没有签名，滚")
def page_5():
    #小程序
    tab1,tab2,tab3 = st.tabs([":sunglasses:图片处理小程序:sunglasses:",":full_moon_with_face:智能英语词典:full_moon_with_face:", ":orange_heart:万能搜索器进入链接:orange_heart:"])
    with tab1:
        #图片处理
        uploaded_file = st.file_uploader(":last_quarter_moon_with_face:图片传送门:first_quarter_moon_with_face:", type=['png', 'jpeg', 'jpg'])
        if uploaded_file:
            #获取图片信息
            file_name = uploaded_file.name
            file_type = uploaded_file.type
            file_size = uploaded_file.size
            img = Image.open(uploaded_file)
            tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["原图","改色1","改色2","改色3","改色4","上天"])
            with tab1:
                st.image(img)
            with tab2:
                st.image(img_change(img, 0, 2, 1))
            with tab3:
                st.image(img_change(img, 1, 0, 2))
            with tab4:
                st.image(img_change(img, 1, 2, 0))
            with tab5:
                st.image(img_change(img, 2, 1, 0))
            with tab6:
                st.image(img_change(img, 2, 2, 2))
    with tab2:
        #智慧词典
        with open("words_space.txt", 'r', encoding='utf-8') as f:
            words_list = f.read().split('\n')
        for i in range(len(words_list)):
            words_list[i] = words_list[i].split('#')
        words_dict = {}
        for i in words_list:
            words_dict[i[1]] = [int(i[0]), i[2]]
        with open("check_out_times.txt", 'r', encoding='utf-8') as f:
            times_list = f.read().split('\n')
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])
        word = st.text_input("请输入要查询的单词")
        if word in words_dict:
            st.write(words_dict[word])
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            with open('check_out_times.txt', 'w', encoding='utf-8') as f:
                message = ''
                for k, v in times_dict.items():
                    message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                f.write(message)
            st.write('查询次数：', times_dict[n])
    with tab3:
        st.link_button(":orange_heart:可爱的小百度:orange_heart:", "https://www.baidu.com/")
    tab4, tab5 = st.tabs([":hankey:豪庭的阴乐:hankey:", ":rose:自动生成词云图:rose:"])
    with tab4:
        st.write("lalala")
        with open('1.mp3', 'rb') as f:
                mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.write("广西大师")
        with open('2.mp3', 'rb') as f:
                mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.write("see you again")
        with open('3.mp3', 'rb') as f:
                mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        e = ":green[下面的是真好听]"
        st.subheader(e)
        st.write("that girl")
        with open('4.mp3', 'rb') as f:
                mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.write("多远都要在一起")
        with open('5.mp3', 'rb') as f:
                mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=10)
    with tab5:
        uploaded_file = st.file_uploader('你小子给我上传txt文件嗷')
        if uploaded_file is not None:
            str_data = uploaded_file.read().decode('utf-8')
            st.image(ciyun(str_data))
        else:
            pass

def ciyun(str):
    font = 'anna.ttf'
    w = wordcloud.WordCloud(width = 600, height = 400, font_path = font, max_words = 50).generate(str)
    w.to_file('ciyun.png')
    img = Image.open('ciyun.png')
    return img

def img_change(img, rc, gc, bc):
    #图片处理
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获得RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (b, g, r)
    return img

if page == "发帖":
    page_1()
elif page == "发现好友":
    page_2()
elif page == "我的好友":
    page_3()
elif page == "个人主页":
    page_4()
elif page == "小程序":
    page_5()