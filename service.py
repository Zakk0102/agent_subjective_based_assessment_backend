from utilities import *
import google.generativeai as genai
from config import *
import markdown


def gen_model():
    """
    Initializes and configures the GenerativeModel from GenAI.

    Returns:
        genai.GenerativeModel: The configured GenerativeModel instance.
    """

    # Configure GenAI with the provided Google API key
    genai.configure(api_key=GOOGLE_API_KEY)

    # Initialize a GenerativeModel with specified model name, generation configuration, and safety settings
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",  # Specify the model name
        generation_config=config,  # Provide generation configuration (assumed to be defined elsewhere)
        safety_settings=SAFETY_SETTINGS  # Provide safety settings (assumed to be defined elsewhere)
    )

    return model


def generate_exercise():
    prompts = generate_exercise_input()

    responses = []
    for prompt in prompts:
        response = gen_model().generate_content(prompt)
        generated_exercise = response.parts[0].text
        exercise = generated_exercise
        responses.append(exercise)
        resp = "".join(responses)
        res = markdown.markdown(resp)

    return res
