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

thread = "thread_rD5dHciiKtGlqyTis02B9iB2"

def getanswer(question):

  message = client.beta.threads.messages.create(
      thread_id=thread,
      role="user",
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


st.set_page_config(page_title='Satti Afib ChatGPT', page_icon=':robot')


st.header('Satti Afib ChatGPT')
st.write('by S. D. Satti, MD, FACC, FHRS - me@sattimd.com')
st.write("This is an extension of OpenAI's ChatGPT with additional training using atrial fibrillation guidelines.")
st.write('')

base_prompt = "Give specific answers. In a separate paragraph, at the end give an itemized list the individual references for the following: "
input_prompt = st.text_area(label='What is your query:', key='user_input')

prompt = input_prompt

if st.button(label='Submit'):
    if input_prompt != '':
        st.write("Thinking...")
        answer = getanswer(prompt)
        st.write(answer)

=======

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



#OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    # api_key="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",
)

assistant = "asst_E8wDEsIHWMxQRuWDYiEmL88R"

thread = "thread_rD5dHciiKtGlqyTis02B9iB2"

def getanswer(question):

  message = client.beta.threads.messages.create(
      thread_id=thread,
      role="user",
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




st.set_page_config(page_title='Satti Afib ChatGPT', page_icon=':robot')


st.header('Satti Afib ChatGPT')
st.write('by S. D. Satti, MD, FACC, FHRS - me@sattimd.com')
st.write("This is an extension of OpenAI's ChatGPT with additional training using atrial fibrillation guidelines.")
st.write('')

base_prompt = "Give specific answers. In a separate paragraph, at the end give an itemized list the individual references for the following: "
input_prompt = st.text_area(label='What is your query:', key='user_input')

prompt = input_prompt

if st.button(label='Submit'):
    if input_prompt != '':
        st.write("Thinking...")
        answer = getanswer(prompt)
        st.write(answer)

