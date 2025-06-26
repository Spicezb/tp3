import google.generativeai as genai
# Realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado
# Fecha de inicio 15/05/2025 a las 18:00
# Última modificación 26/06/2025 02:30
# Versión de Python 3.13.2
# Importaciones de Librerías
# Se necesita instalar la libreria google-generativeai

# Se configura la clave para poder tener comunicacion mediante la Api que se creo.
genai.configure(api_key="AIzaSyAL__x8-xUgNLlqGoy9RL_Dju5JBHFCkjM")

def comunicacionGemini(prompt):
    """
    Funcionamiento:
    - Utiliza el modelo generativo "gemini-1.5-flash" para generar contenido basado en un texto de entrada.
    - Envía el prompt al modelo y recibe una respuesta generada.
    - Retorna el texto generado por el modelo.
    Entradas:
    - prompt (str): Texto con la instrucción o consulta que se desea enviar al modelo generativo.
    Salidas:
    - str: Texto generado por el modelo como respuesta al prompt.
    """
    model=genai.GenerativeModel("gemini-1.5-flash")
    respuesta=model.generate_content(prompt)
    return respuesta.text
