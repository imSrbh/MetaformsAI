#Based on the Persona Predict Domain Prompt
#TODO
#Based on Persona only Generarate Few Goals
#TODO

#Based on Persona and Domain Generate Few Goals
GenerateGoalPromptwithPD =f''' Task: Please analyze the given Persona and Domain Generate the Survey realated Goals: 
Domain: In a broader sense, a domain can refer to any specialized area of knowledge, activity, or expertise. It can encompass various fields such as technology, healthcare, education, marketing, etc. Essentially, the domain delineates the specific context or scope within which a particular task, role, or activity is carried out.

Persona/Role: Within the identified domain, Personas are real working people. a persona or role refers to a fictional character or representation of a typical user or stakeholder within a specific context, such as a business, product, or service. 

Persona: {{persona}}

Domain: {{domain}}

Please Generate lists of Goals specific to given Persona and Domain in the list format:

["Goal1", "Goal2", "Goal3",...]

Here are the few-shot examples format:
1. [Salesforce B2B Sales Representative]: ["Conduct a quarterly survey of 100 financial services decision-makers to understand their pain points, challenges, and needs.", "Analyze survey data to identify trends and insights that inform the creation of targeted sales content tailored to the specific needs of financial services clients.", "Develop and distribute sales materials, such as case studies, whitepapers, and presentations, based on the survey findings to effectively engage prospects and drive conversions."]
2. [Glossier B2C Marketing Manager]: ["Gather customer feedback through surveys, focus groups, and social media interactions to create detailed personas representing different segments of the target audience.", "Utilize persona insights to personalize marketing campaigns, product recommendations, and messaging to resonate with the identified customer segments.", "Collaborate with product development teams to align new product offerings and improvements with the preferences and needs of the identified personas, enhancing customer satisfaction and loyalty."]
3. [Apple Retail Store Manager]: ["Implement strategies to improve employee morale, motivation, and job satisfaction through initiatives such as training programs, recognition schemes, and career development opportunities.", "Conduct regular performance evaluations and feedback sessions to address employee concerns, provide constructive guidance, and foster a positive work environment.", "Measure employee retention rates and track improvements, aiming to achieve a 10% or more increase in retention, which correlates with higher levels of customer satisfaction and loyalty."]
4. [Zappos Customer Support Representative]: ["Implement post-interaction surveys to gather feedback from customers regarding their satisfaction levels, the resolution of their issues, and their overall experience with the support service.", "Analyze survey results to identify areas for improvement in customer support processes, agent training, and product/service offerings.", "Utilize insights from post-interaction surveys to implement enhancements that increase first-call resolution rates, reduce customer effort, and ultimately improve customer satisfaction and loyalty."]
5. [Technology Solutions Consultant]: ["Conduct market research surveys targeting IT decision-makers to understand emerging trends, pain points, and technology adoption patterns, informing product development and strategic business decisions.", "Analyze survey data to identify key insights and market gaps, facilitating the customization of technology solutions to meet diverse client needs and preferences.", "Develop educational materials and workshops based on survey findings to empower clients in leveraging technology effectively, fostering long-term partnerships and client satisfaction."]
6. [Healthcare Administrator]: ["Administer patient satisfaction surveys to gather feedback on healthcare services, staff interactions, and facility experiences, aiming to enhance patient-centered care and improve overall satisfaction levels.", "Analyze survey responses to identify areas for improvement in service delivery, communication practices, and patient engagement strategies, promoting continuous quality enhancement initiatives.", "Implement initiatives based on survey findings, such as staff training programs and process improvements, to elevate the standard of care delivery and strengthen patient-provider relationships."]
7. [Education Program Coordinator]: ["Conduct surveys among students, parents, and educators to assess program effectiveness, curriculum relevance, and satisfaction levels, facilitating data-driven decision-making and program enhancements.", "Analyze survey results to identify areas of success and improvement opportunities, aligning program objectives with stakeholder expectations and educational standards.", "Utilize survey insights to develop tailored interventions, enrichment activities, and support services that address identified needs and foster holistic student development."]
8. [Marketing Strategist]: ["Deploy consumer behavior surveys across target demographics to gain insights into purchasing preferences, brand perceptions, and advertising effectiveness, guiding strategic marketing campaigns and product positioning.", "Analyze survey data to uncover consumer trends, market gaps, and competitive benchmarks, enabling the formulation of data-driven marketing strategies and tactics.", "Leverage survey findings to optimize marketing communication channels, creative content, and promotional offers, maximizing brand engagement, customer acquisition, and retention."]

Note:
Please ensure that the generated output strictly should be in a professional way and adhere to formulate the List of strings as output.
Again think step by step and confirm if the generated output is in the right format, if not fix it and make sure its in the expected list format.'''


#Analyze the Selected Goal and generate list of questions for a survey 
GenerateSurveyQuestions = f''' Task: Generate the survey questions based on the given goal:
Instructions: Based on the provided goal, generate a set of 8-12 survey questions that would help achieve this goal. The questions should be clear, concise, and unbiased. Feel free to include different types of questions such as multiple-choice, rating scales, open-ended, etc. Present the questions in a numbered or bulleted list format.

Goal: {{goal}}

Goal: [State the goal or purpose of the survey here. For example, "To understand customer satisfaction with our product/service."]
For example, if the goal is "To understand customer satisfaction with our product/service," the generated survey questions could be:
On a scale of 1 to 5 (where 1 is "Very Dissatisfied" and 5 is "Very Satisfied"), how satisfied are you with our product/service overall?
What do you like most about our product/service?
What do you like least about our product/service?
How likely are you to recommend our product/service to a friend or colleague? (Scale of 1 to 5, where 1 is "Not at all likely" and 5 is "Extremely likely")
Which of the following best describes your experience with our customer support? (Multiple choice: Excellent, Good, Average, Poor, Never used)
If you have interacted with our customer support, please rate your satisfaction with their service. (Scale of 1 to 5, where 1 is "Very Dissatisfied" and 5 is "Very Satisfied")
Are there any additional features or improvements you would like to see in our product/service? (Open-ended)
Please provide any additional comments or feedback you may have. (Open-ended)
'''