import streamlit as st
from openai import OpenAI

# StreamlitのサイドバーでOpenAIのAPIキーを設定
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
 
st.title("Gamification")

# メッセージの初期状態を設定
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# 質問を入力
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    perspectives = ['進展性', '希少性', '創造性']  # 例として3つの異なる観点
    for i, perspective in enumerate(perspectives, start=1):
        st.subheader(f'Section {i}: {perspective}')
        modified_prompt = f'{prompt} \n\n### から見た{perspective}の視点は？'
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": modified_prompt}])
        msg1 = response.choices[0].message.content
        
        

    row1 = st.columns(3)
    row1[0].markdown(msg1)
    row2 = st.columns(3)

    for col in row1 + row2:
        tile = col.container
        tile.title(":balloon:")
        