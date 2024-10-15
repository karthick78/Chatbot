import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage

from langchain.chat_models import ChatOpenAI
import os
from langchain.llms import OpenAI

st.set_page_config(page_title="Conversation Q&A ChatBot")
st.header("Hey, Let's Chat")

from dotenv import load_dotenv
load_dotenv()

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="You are an comedian AI assitant")
    ]

chat=ChatOpenAI(temperature=0.5)



def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=str(question)))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    #llm=OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),model_name="gpt-3.5-turbo-instruct", temperature=0.7)
    return answer.content
  

input=st.text_input("Input: ", key="input")
response=get_chatmodel_response(input)
submit=st.button("Ask the question")


if submit:
    st.subheader("The Response is")
    st.write(response)
