import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["gemini_api"])

def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("from now your name is CMA , Iam a Anime AI Assistant  , your real name is mareeswaran and reply to this in short: "+txt)
    return response.text




st.title("CMA Anime Ai Assistant")

command = st.chat_input("how can I help you?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])


if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":command})
    if "hello" in command or "hi" in command:
        with st.chat_message("BOT"):
            st.write("Hi otaku!, how are you? need an anime recommendation, ask me im here for you")
            st.session_state.message.append({"role":"BOT","message":"Hi otaku!, how are you? need an anime recommendation, ask me im here for you"})
    elif "who" in command:
        with st.chat_message("BOT"):
            st.write("Im CMA AI Assistant")
            st.session_state.message.append({"role":"BOT","message":"Im CMA Anime AI Assistant"})
    elif "image" in command or "picture" in command or "photo" in command:
        with st.chat_message("BOT"):
            st.write("Sorry, i Can not provide images, im can only give informations as a text")
            st.session_state.message.append({"role":"BOT","message":"Sorry, i Can not provide images, i can only give informations as a text"})
    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})




print(st.session_state.message)
