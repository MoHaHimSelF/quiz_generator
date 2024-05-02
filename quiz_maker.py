from langchain.llms import OpenAI
from langchain.chains import Chain  # Assuming Chain is the correct class to use

def generate_quiz(text):
    # Configure your OpenAI model
    llm = OpenAI(model_name="gpt-3.5-turbo")
    chain = Chain(llm)
    questions = chain.generate_questions(text)
    return questions
