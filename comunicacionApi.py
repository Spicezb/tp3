import google.generativeai as genai
# Se necesita instalar la libreria google-generativeai

# Se configura la clave para poder tener comunicacion mediante la Api que se creo.
genai.configure(api_key="AIzaSyAL__x8-xUgNLlqGoy9RL_Dju5JBHFCkjM")

def comucacionGemini(prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    respuesta=model.generate_content(prompt)
    return respuesta.text

# Prueba
print(comucacionGemini("Dame el nombre científico, hábitat y dieta del animal llamado Oso Panda,Debe de sacar la informacion de Wikipedia.com. Respondé de forma resumida y clara."))