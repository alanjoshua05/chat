import streamlit as st
from datetime import datetime

# Data structure to store messages
messages = []

# Streamlit app layout
st.title("Messenger App")

# User input for message
message_input = st.text_input("Type a message:")

# Display messages
if st.button("Send"):
    if message_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        messages.append({"time": current_time, "text": message_input, "sender": "You"})
        st.text_area("Chat", value="\n".join([f"{msg['time']} - {msg['sender']}: {msg['text']}" for msg in messages]))

# Simulate receiving a message
received_message = "Hello there!"
messages.append({"time": datetime.now().strftime("%H:%M:%S"), "text": received_message, "sender": "Friend"})

# Display received messages
st.text_area("Chat", value="\n".join([f"{msg['time']} - {msg['sender']}: {msg['text']}" for msg in messages]))
