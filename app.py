import streamlit as st
import asyncio
import pytchat

async def read_chat(video_id):
    chat = pytchat.create(video_id)
    messages = []
    while chat.is_alive():
        for c in chat.get().items:
            messages.append(f"{c.author.name}: {c.message}")
        await asyncio.sleep(1)
    return messages

def start_reading(video_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(read_chat(video_id))

# Giao diện Streamlit
st.title("YouTube Live Chat Reader")
video_id = st.text_input("Nhập Video ID:")

if st.button("Start"):
    if video_id:
        chat_messages = start_reading(video_id)
        for msg in chat_messages:
            st.write(msg)
    else:
        st.warning("Vui lòng nhập Video ID hợp lệ!")
