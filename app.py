import streamlit as st
from openai import OpenAI
import json
import os
from Prompts import  GenerateGoalPromptwithPD, GenerateSurveyQuestions, GenerateSurveyQuestions2, GenerateSurveyQuestions3

# Define a class to manage session state
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Initialize session state
session_state = SessionState(response=None)

st.sidebar.title('About This App')

st.sidebar.markdown('This application has two sections:')
st.sidebar.markdown('1. User can Generate Goals by giving the Persona and domain and then can use the generated/suggested goals to generate survey questions.')
st.sidebar.markdown('2. User can straightaway enter the Goals and can get the survey questions generated for 3 iterations[~15 Seconds to generate].')

# Add link to the prompts file
st.sidebar.markdown('[Prompts File](https://github.com/imSrbh/MetaformsAISurvey/blob/master/Prompts.py)')
st.sidebar.markdown('[GitHub Repo](https://github.com/imSrbh/MetaformsAISurvey/)')

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

import streamlit as st




# Streamlit App
st.title("Survey Questions Generator")
# Initialize OpenAI client
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")
    st.stop()
client = OpenAI(api_key=openai_api_key)

def openai_function(prompt):
    system_msg = 'You are a helpful assistant for providing or answering the information based on the given prompt'
    response = client.chat.completions.create(model="gpt-3.5-turbo-1106",
                                              messages=[
                                                  {"role": "system",
                                                      "content": system_msg},
                                                  {"role": "user",
                                                      "content": prompt}
                                              ])

    return response.choices[0].message.content



# Get user input for Persona and Domain

persona = st.text_input("Enter Persona (e.g., Marketing Manager/Retail Store Manager):")
domain = st.text_input("(Optional) Enter Domain (e.g., Sales/Marketing/Retail):")
final_prompt = GenerateGoalPromptwithPD.format(persona=persona, domain=domain)


# # Button to generate goals
# if st.button("Generate Goals"):
#     response = openai_function(final_prompt)
#     # response=list(response)
#     st.write("Suggested Goals:")
#     # st.write(response)
#     st.write(session_state.response)

# Button to generate goals
if st.button("Generate Goals"):
    try:
        session_state.response = openai_function(final_prompt)
        if session_state.response:
            st.write("Suggested Goals:")
            st.write(session_state.response)
        else:
            st.write("No response received.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


st.write("Or")
st.write("---")
# Get user input for Goal
goal = st.text_input("Paste any one goal generated or your own")

# Button to generate survey questions
# if st.button("Generate Survey Questions"):
#     st.write("Iteration1")
#     goal_prompt = GenerateSurveyQuestions.format(goal=goal)
#     questions = openai_function(goal_prompt)
#     st.write(questions)
#     st.write("---")
#     st.write("Iteration2")
#     goal_prompt2 = GenerateSurveyQuestions2.format(goal=goal)
#     questions2 = openai_function(goal_prompt2)
#     st.write(questions2)
#     st.write("---")
#     st.write("Iteration3")
#     goal_prompt3 = GenerateSurveyQuestions3.format(goal=goal)
#     questions3 = openai_function(goal_prompt3)
#     st.write(questions3)

if st.button("Generate Survey Questions"):
    if not goal:
        st.warning("Please enter a goal first.")
    else:
        # Generate survey questions for three iterations
        goal_prompt = GenerateSurveyQuestions.format(goal=goal)
        questions1 = openai_function(goal_prompt)

        goal_prompt2 = GenerateSurveyQuestions2.format(goal=goal)
        questions2 = openai_function(goal_prompt2)

        goal_prompt3 = GenerateSurveyQuestions3.format(goal=goal)
        questions3 = openai_function(goal_prompt3)

        # Create tabs for each iteration
        with st.expander("Iteration 1"):
            st.write(questions1)

        with st.expander("Iteration 2"):
            st.write(questions2)

        with st.expander("Iteration 3"):
            st.write(questions3)