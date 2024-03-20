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
    perspectives = ['進展性', '希少性', '創造性','固有性','社会性','偶発性','忌避性','保持性']  # 例として3つの異なる観点
    for i, perspective in enumerate(perspectives, start=1):
        st.subheader(f'Section {i}: {perspective}')
        modified_prompt = f'{prompt} \n\n### {perspective}の観点ではどのようものが考えられる？'
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": modified_prompt}])
        msg = response.choices[0].message.content
        st.write(msg)
        
        
