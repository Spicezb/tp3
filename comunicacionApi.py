import google.generativeai as genai
# Se necesita instalar la libreria google-generativeai

# Se configura la clave para poder tener comunicacion mediante la Api que se creo.
genai.configure(api_key="AIzaSyAL__x8-xUgNLlqGoy9RL_Dju5JBHFCkjM")

def comunicacionGemini(prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    respuesta=model.generate_content(prompt)
    return respuesta.text
