import streamlit as st
from datetime import datetime
from streamlit_elements import elements, dashboard, mui, nivo
from streamlit_elements import dashboard
from openai import OpenAI

st.set_page_config(layout="wide")
# StreamlitのサイドバーでOpenAIのAPIキーを設定
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
 
st.title("Gamification")
# メッセージの初期状態を設定
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# 質問を入力
example = "例：より多くのクーポンを獲得してしまう体験を作りたい。"
prompt = st.text_input('ゲーミフィケーションメカニズムを利用して実現したい体験を入力してください', placeholder=example)

if prompt:
    st.write(prompt)
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    msg1=0
    msg2=0
    msg3=0
    msg4=0
    msg5=0
    msg6=0
    msg7=0
    msg8=0
    msg9=prompt
    client = OpenAI(api_key=openai_api_key)
    perspectives = ['進展性', '希少性', '創造性','固有性','社会性','偶発性','忌避性','保持性']  # 例として3つの異なる観点
    with st.spinner('考えています...'):
        for i, perspective in enumerate(perspectives, start=1):
            modified_prompt = f'{prompt} \n\n### {perspective}の観点では、この体験を実現させるのにどのようアイディアが考えられる？一つ教えて。'
            response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": modified_prompt}])
            msg = response.choices[0].message.content
            if perspective=='進展性':
                msg1=msg
            elif perspective=='希少性':
                msg2=msg
            elif perspective=='創造性':
                msg3=msg
            elif perspective=='固有性':
                msg4=msg
            elif perspective=='社会性':
                msg5=msg
            elif perspective=='偶発性':
                msg6=msg
            elif perspective=='忌避性':
                msg7=msg
            elif perspective=='保持性':
                msg8=msg

            
            
        def create_chart(KEYNAME, CARD_TITLE, TEXT):
            with mui.Card(key=KEYNAME, sx={"display": "flex", "flexDirection": "column"}):
                mui.CardHeader(title=CARD_TITLE, subheader=TEXT, className="draggable")

        ### ----- Graph Visualization（グラフの可視化） ----- ###
        with elements("dashboard"):
            # default layout setting（デフォルトレイアウトの設定）
            layout = [
                # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
                dashboard.Item("進展性", 0, 0, 3, 2),
                dashboard.Item("希少性", 3, 0, 3, 2),
                dashboard.Item("創造性", 6, 0, 3, 2),
                dashboard.Item("固有性", 0, 2, 3, 2),
                dashboard.Item("タイトル", 3, 2, 3, 2),
                dashboard.Item("社会性", 6, 2, 3, 2),
                dashboard.Item("偶発性", 0, 4, 3, 2),
                dashboard.Item("忌避性", 3, 4, 3, 2),
                dashboard.Item("保持性", 6, 4, 3, 2)]  # 修正した位置を指定

            with dashboard.Grid(layout, draggableHandle=".draggable"):
                create_chart(KEYNAME="進展性", CARD_TITLE="進展性", TEXT=msg1)
                create_chart(KEYNAME="希少性", CARD_TITLE="希少性", TEXT=msg2)
                create_chart(KEYNAME="創造性", CARD_TITLE="創造性", TEXT=msg3)
                create_chart(KEYNAME="固有性", CARD_TITLE="固有性", TEXT=msg4)
                create_chart(KEYNAME="タイトル", CARD_TITLE="体験名", TEXT=msg9)
                create_chart(KEYNAME="社会性", CARD_TITLE="社会性", TEXT=msg5)
                create_chart(KEYNAME="偶発性", CARD_TITLE="偶発性", TEXT=msg6)
                create_chart(KEYNAME="忌避性", CARD_TITLE="忌避性", TEXT=msg7)
                create_chart(KEYNAME="保持性", CARD_TITLE="保持性", TEXT=msg8)
                

        tryagain = st.button('やり直す', type="primary")
        save = st.button('結果を保存する', type="primary")
        if tryagain:
            perspectives = ['進展性', '希少性', '創造性','固有性','社会性','偶発性','忌避性','保持性','確率性']  # 例として3つの異なる観点
            with st.spinner('もう一度考えています...'):
                for i, perspective in enumerate(perspectives, start=1):
                    modified_prompt = f'{prompt} \n\n### {perspective}の観点では、この体験を実現させるアイディアをもう一度考えて。一つ教えて。'
                    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": modified_prompt}])
                    msg = response.choices[0].message.content
                    if perspective=='進展性':
                        msg1=msg
                    elif perspective=='希少性':
                        msg2=msg
                    elif perspective=='創造性':
                        msg3=msg
                    elif perspective=='固有性':
                        msg4=msg
                    elif perspective=='社会性':
                        msg5=msg
                    elif perspective=='偶発性':
                        msg6=msg
                    elif perspective=='忌避性':
                        msg7=msg
                    elif perspective=='保持性':
                        msg8=msg
                    elif perspective=='確率性':
                        msg9=msg

            def create_chart(KEYNAME, CARD_TITLE, TEXT):
                with mui.Card(key=KEYNAME, sx={"display": "flex", "flexDirection": "column"}):
                    mui.CardHeader(title=CARD_TITLE, subheader=TEXT, className="draggable")

            ### ----- Graph Visualization（グラフの可視化） ----- ###
            with elements("dashboard2"):
                # default layout setting（デフォルトレイアウトの設定）
                layout = [
                    # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
                    dashboard.Item("進展性", 0, 0, 3, 2),
                    dashboard.Item("希少性", 3, 0, 3, 2),
                    dashboard.Item("創造性", 6, 0, 3, 2),
                    dashboard.Item("固有性", 0, 2, 3, 2),
                    dashboard.Item("社会性", 3, 2, 3, 2),
                    dashboard.Item("偶発性", 6, 2, 3, 2),
                    dashboard.Item("忌避性", 0, 4, 3, 2),
                    dashboard.Item("保持性", 3, 4, 3, 2),
                    dashboard.Item("確率性", 6, 4, 3, 2)]  # 修正した位置を指定

                with dashboard.Grid(layout, draggableHandle=".draggable"):
                    create_chart(KEYNAME="進展性", CARD_TITLE="進展性", TEXT=msg1)
                    create_chart(KEYNAME="希少性", CARD_TITLE="希少性", TEXT=msg2)
                    create_chart(KEYNAME="創造性", CARD_TITLE="創造性", TEXT=msg3)
                    create_chart(KEYNAME="固有性", CARD_TITLE="固有性", TEXT=msg4)
                    create_chart(KEYNAME="社会性", CARD_TITLE="社会性", TEXT=msg5)
                    create_chart(KEYNAME="偶発性", CARD_TITLE="偶発性", TEXT=msg6)
                    create_chart(KEYNAME="忌避性", CARD_TITLE="忌避性", TEXT=msg7)
                    create_chart(KEYNAME="保持性", CARD_TITLE="保持性", TEXT=msg8)
                    create_chart(KEYNAME="確率性", CARD_TITLE="確率性", TEXT=msg9)

                
