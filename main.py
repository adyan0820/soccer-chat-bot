from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """
You are a SoccerBot, an expert in all questions related to soccer. If the user asks a question 
that is NOT related to soccer (including football, leagues, players, tactics, rules, stats, etc.) then
respond exactly with: I can only answer questions related to soccer.

Here is the coversation history: {context}

Question: {question}

Answer
"""
model = OllamaLLM(model = 'mistral')
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def coversation():
    context = ''
    print("Welcome to SoccerLLM! I'm here to answer all of your soccer related questions. " \
    "Type 'exit' if you would like to end the conversation")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        result = chain.invoke({"context": context, "question": user_input})
        print("SoccerLLM: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"



