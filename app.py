import streamlit as st
from openai import OpenAI
import json
import os
from Prompts import GenerateSurveyQuestions, GenerateGoalPromptwithPD
# Set up OpenAI API key
# OpenAI.api_key = os.getenv("OPENAI_API_KEY")
OpenAI.api_key = st.sidebar.text_input("Enter your OpenAI API Key")

# Initialize OpenAI client
client = OpenAI()

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

# Streamlit App
st.title("Survey Question Generator")

# Get user input for Persona and Domain
persona = st.text_input("Enter Persona (e.g., Marketing Manager/Retail Store Manager):")
domain = st.text_input("Enter Domain (e.g., Sales/Marketing/Retail):")
final_prompt = GenerateGoalPromptwithPD.format(persona=persona, domain=domain)


# Button to generate goals
if st.button("Generate Goals"):
    response = openai_function(final_prompt)
    st.sidebar.subheader("Suggested Goals:")
    st.sidebar.write(response)

st.write("---")
# Get user input for Goal
goal = st.text_input("Paste any one goal generated above")

# Button to generate survey questions
if st.button("Generate Survey Questions"):
    goal_prompt = GenerateSurveyQuestions.format(goal=goal)
    questions = openai_function(goal_prompt)
    st.write(questions)
