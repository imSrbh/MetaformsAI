# Directory Structure  
`Prompts.py`: Contains all the prompts  
`GenerateGoalPromptwithPD: Based on Persona and Domain Generate Few Goals`  
`GenerateSurveyQuestions: Analyze the Selected Goal and generate list of questions for a survey`  

`app.py`: Streamlit application to use prompts and make openAI fn call to get the response  

# How to run  
### Install the dependencies  
`pip3 install -r requirements.txt`  

### Run the streamlit app  
`streamlit run app.py`