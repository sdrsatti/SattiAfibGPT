# ''' 
# This program is uploaded to git and then pushed to https://sattiafibchatgpt.streamlit.app
# After this program is saved, run from cmd from this directory:
#     git commit -a -m "First"
#     git push
# This is will update git and then automatically update streamlit.
# '''


from openai import OpenAI
import streamlit as st
import time


client = OpenAI()

assistant = "asst_E8wDEsIHWMxQRuWDYiEmL88R"

#thread = "thread_7erFEqjw4i4wvLD0jWmMp6Wi"

thread = client.beta.threads.create()

def getanswer(question):

  message = client.beta.threads.messages.create(
      thread_id=thread,
      role="user",
      #file_ids=['file-6CknLux1aKEpnQsnNWu1gXru','file-KK2ftqNAy2k4fuDdDpye33ID','file-lLyLrzE8DotbloC2fuuKQOcT','file-fSx8VveL93DeI3nDLU19z09p'],
      content= question
  )

  run = client.beta.threads.runs.create(
    thread_id=thread,
    assistant_id=assistant,
    instructions="Give complete and through answers using the files uploaded and only answer medical questions"
  )

  while run.status != "completed":
      time.sleep(1)
      run = client.beta.threads.runs.retrieve(
      thread_id=thread,
      run_id=run.id
  )

  messages = client.beta.threads.messages.list(
    thread_id=thread
  )

  answer = messages.data[0].content[0].text.value

  return(answer)


st.set_page_config(page_title='Satti Afib GPT', page_icon=':robot')


st.header('Satti Afib GPT')
st.write('by S. D. Satti, MD, FACC, FHRS - me@sattimd.com')
st.write("This is an extension of OpenAI's ChatGPT with additional training using atrial fibrillation guidelines.")
st.write('')

base_prompt = "Give specific answers. In a separate paragraph, at the end give an itemized list the individual references for the following: "
input_prompt = st.text_area(label='What is your query:', key='user_input')

prompt = input_prompt

if st.button(label='Submit'):
    if input_prompt != '':
        st.write("Thinking...(May take up to a minute.)")
        answer = getanswer(prompt)
        st.write(answer)

