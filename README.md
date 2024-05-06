
>Live URL: [Survey Questions Generator](https://surveyquestiongenerator.streamlit.app/)

## Directory Structure  
- `Prompts.py`: Contains prompts  
`GenerateGoalPromptwithPD: Based on Persona and Domain Generate Few Goals`    
`GenerateSurveyQuestions/GenerateSurveyQuestions2/GenerateSurveyQuestions3: Analyze the Selected Goal and generate list of questions for a survey`  

- `app.py`: Streamlit application to use prompts and make openAI fn call to get the response  

## How to run locally
### Install the dependencies  
`pip3 install -r requirements.txt`  

### Run the streamlit app  
`streamlit run app.py`  

Make sure you have OpenAI API Key.

---

### Here is my initial attempt at designing the prompt:

Initial Prompt Design:

```python
GenerateSurveyQuestions = f'''
Task: Generate a set of 8-12 survey questions based on the given goal.

Instructions:
1. The questions should be clear, concise, and unbiased.
2. Include different types of questions such as multiple-choice, rating scales, open-ended, etc.
3. Present the questions in a numbered or bulleted list format.

Goal: {{goal}}

For example, if the goal is "To understand customer satisfaction with our product/service," the generated survey questions could be:

- On a scale of 1 to 5 (where 1 is "Very Dissatisfied" and 5 is "Very Satisfied"), how satisfied are you with our product/service overall?
- What do you like most about our product/service?
- What do you like least about our product/service?
- How likely are you to recommend our product/service to a friend or colleague? (Scale of 1 to 5, where 1 is "Not at all likely" and 5 is "Extremely likely")
- Which of the following best describes your experience with our customer support? (Multiple choice: Excellent, Good, Average, Poor, Never used)
- If you have interacted with our customer support, please rate your satisfaction with their service. (Scale of 1 to 5, where 1 is "Very Dissatisfied" and 5 is "Very Satisfied")
- Are there any additional features or improvements you would like to see in our product/service? (Open-ended)
- Please provide any additional comments or feedback you may have. (Open-ended)
'''
```

Rationale:
- The prompt provides clear instructions on the task requirements, including the number of questions, types of questions, and presentation format.
- It includes an example set of questions for a specific goal to guide the model's understanding of the desired output.
- The example covers various question types (rating scales, multiple-choice, and open-ended) to demonstrate the expected diversity in the generated questions.

Testing and Feedback:
After testing the initial prompt design, I found that the generated questions were often repetitive or lacked specificity to the provided goal. The model seemed to rely heavily on the example questions, leading to limited variability in the output.

Iteration 1:
To address this issue, I modified the prompt to encourage more diversity and relevance to the given goal.

```python
GenerateSurveyQuestions = f'''
Task: Generate a set of 8-12 survey questions based on the given goal.

Instructions:
1. The questions should be clear, concise, unbiased, and directly relevant to the provided goal.
2. Include a diverse range of question types such as multiple-choice, rating scales, open-ended, etc.
3. Avoid repeating the same question or concept multiple times.
4. Present the questions in a numbered or bulleted list format.

Goal: {{goal}}

For example, if the goal is "To understand customer satisfaction with our product/service," some relevant survey questions could be:

- On a scale of 1 to 5, how satisfied are you with our overall product/service?
- What specific features or aspects of our product/service do you find most valuable?
- Are there any areas where our product/service could be improved? Please explain.
- How likely are you to recommend our product/service to others? (Scale of 1 to 5)
- Please rate your experience with our customer support team. (Multiple choice: Excellent, Good, Average, Poor, Never used)
- If you have interacted with our customer support, how satisfied were you with their responsiveness and ability to resolve your issue? (Scale of 1 to 5)

Note: These are just examples. Your generated questions should be tailored to the specific goal provided and should not simply repeat the examples verbatim.
'''
```

Changes:
- Added instructions to ensure the generated questions are directly relevant to the provided goal.
- Included a note to avoid repeating the same question or concept multiple times.
- Modified the example questions to be more concise and focused on the given goal.

Testing and Feedback:
The revised prompt produced more relevant and diverse questions. However, some of the generated questions still lacked clarity or were leading/biased.

Iteration 2:
To further improve the prompt, I added instructions to ensure the generated questions are clear, unbiased, and avoid leading or influencing responses.

```python
GenerateSurveyQuestions = f'''
Task: Generate a set of 8-12 survey questions based on the given goal.

Instructions:
1. The questions should be clear, concise, unbiased, and directly relevant to the provided goal.
2. Include a diverse range of question types such as multiple-choice, rating scales, open-ended, etc.
3. Avoid repeating the same question or concept multiple times.
4. Ensure questions are unbiased and do not lead or influence responses in a particular direction.
5. Present the questions in a numbered or bulleted list format.

Goal: {{goal}}

For example, if the goal is "To understand customer satisfaction with our product/service," some relevant survey questions could be:

- On a scale of 1 to 5, how would you rate your overall satisfaction with our product/service?
- What specific features or aspects of our product/service do you find most valuable or helpful?
- Are there any areas or aspects of our product/service that could be improved? If so, please explain.
- How likely are you to recommend our product/service to others on a scale of 1 to 5?
- Which of the following best describes your experience with our customer support team? (Multiple choice: Excellent, Good, Average, Poor, Never used customer support)
- If you have interacted with our customer support, how satisfied were you with their responsiveness and ability to resolve your issue? (Scale of 1 to 5, or "Not applicable")

Note: These are just examples. Your generated questions should be tailored to the specific goal provided and should not simply repeat the examples verbatim.
'''
```

Changes:
- Added an instruction to ensure questions are unbiased and do not lead or influence responses in a particular direction.
- Modified the example questions to be more neutral and avoid potential biases.

Testing and Feedback:
After multiple rounds of testing and refinement, the current prompt design produces high-quality survey questions that are clear, concise, unbiased, and directly relevant to the provided goal. The generated questions cover a diverse range of types, including rating scales, multiple-choice, and open-ended questions.

---

### Final Design Justification:
The final prompt design incorporates best practices for creating effective survey questions, such as:

1. Ensuring clarity and conciseness to avoid confusion or ambiguity.
2. Maintaining neutrality and avoiding biased or leading questions that could influence responses.
3. Encouraging diversity in question types to gather a range of insights and feedback.
4. Promoting relevance to the specific goal or purpose of the survey.
5. Discouraging repetition or redundancy in the generated questions.

### Evaluation:  
- Neutrality and Lack of Bias
- Relevance to the Goal
- Non-redundancy:
- Response Effectiveness
- Best Practices  
The metrics can be evaluated through a combination of expert review (e.g., by experienced survey designers or subject matter experts)