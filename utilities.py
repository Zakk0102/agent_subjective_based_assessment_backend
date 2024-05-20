from flask import request


def generate_exercise_input():
    data = request.get_json()
    role = data.get('role')
    levels = data.get('levels')
    tools = data.get('tools')
    hints = data.get('hints', False)

    if not role or not levels:
        raise ValueError("Role and levels fields are required")

    for level_info in levels:
        level = level_info.get('level')
        noOfQuestions = level_info.get('noOfQuestions')
        keywords = level_info.get('keywords')

        if not level or not noOfQuestions or not keywords:
            raise ValueError("Each level must have level, noOfQuestions, and keywords fields")

        level_lower = level.lower()
        if level_lower not in ['low', 'medium', 'high']:
            raise ValueError("Level must be 'Low', 'Medium' or 'High'")

        if not (1 <= int(noOfQuestions) <= 20):
            raise ValueError("Number of questions should be between 1 and 20")

        # if not isinstance(keywords, str):
        #     raise ValueError("Keywords should be a string")

    prompts = []

    for level_info in levels:
        level = level_info['level']
        noOfQuestions = level_info['noOfQuestions']
        keywords = level_info['keywords']

        prompt1 = f"""I want {noOfQuestions} practice exercise questions of {level} complexity for the 
               {role} role on the {keywords}.
           For the exercises use the {tools} software tools/technologies/platform."""

        prompt2 = f"""Provide hints if applicable to guide the participant to complete the exercise.
           Provide a list of detailed steps in numbered list format that participant will need to implement 
           the practice exercise. """

        prompt3 = """Give the output in the following format:

           ### Practice Exercise on ______ (mentioned keyword)

           Question 1 (Duration)

           Question 2 (Duration), and so on.

           Do not include information on complexity level.

           For each practice exercise, suggest the duration in hours and minutes 
           the participant will take to complete the practice exercise.

           Besides these questions, do not include any notes or conclusions."""""

        prompt4 = """Give the output in the following format:

           ### Practice Exercise on ______ (mentioned keyword)

           Question 1 (Duration)

           Hints: (if provided)
           Steps: (If provided)

           Question 2 (Duration), and so on.

           Do not include information on complexity level.

           For each practice exercise, suggest the duration in hours and minutes 
           the participant will take to complete the practice exercise.

           Besides these questions, do not include any notes or conclusions."""

        if hints:
            prompt = prompt1 + prompt2 + prompt4
        else:
            prompt = prompt1 + prompt3

        prompts.append(prompt)

    return prompts
