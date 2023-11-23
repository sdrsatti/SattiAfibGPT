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

assistant = client.beta.assistants.create(
    name="SattiAfibAI",
    instructions="You are a senior electrophysiologist with a specialized interest in the management of atrial fibrillation. Give complete and through answers using the files uploaded and only answer medical questions. Use all the files list for the best answer. List the name of the file used as a source used at the end of the response.",
    tools=[{"type": "retrieval"}],
    file_ids=['file-6CknLux1aKEpnQsnNWu1gXru','file-KK2ftqNAy2k4fuDdDpye33ID','file-lLyLrzE8DotbloC2fuuKQOcT','file-file-uzNb2OTrHeoJd0SF2mVSada8'],
    model="gpt-4-1106-preview"
)

thread = client.beta.threads.create()

def getanswer(question):

  message = client.beta.threads.messages.create(
      thread_id=thread.id,
      role="user",
      content= question
  )

  run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Give complete and through answers using the files uploaded and only answer medical questions"
  )

  while run.status != "completed":
      time.sleep(1)
      run = client.beta.threads.runs.retrieve(
      thread_id=thread.id,
      run_id=run.id
  )

  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )

  answer = messages.data[0].content[0].text.value

  return(answer)


st.set_page_config(page_title='Satti Afib GPT', page_icon=':robot')


st.header('Satti Afib GPT')
st.write('by S. D. Satti, MD, FACC, FHRS - me@sattimd.com')
st.write("This is an extension of OpenAI's ChatGPT with additional training using atrial fibrillation guidelines.")
st.write('')

input_prompt = st.text_area(label='What is your query:', key='user_input')

prompt = input_prompt

if st.button(label='Submit'):
    if input_prompt != '':
        st.write("Thinking...(May take up to a minute.)")
        answer = getanswer(prompt)
        st.write(answer)

