import openai

# Configura tu clave de API
openai.api_key = 'Bearer'

# Función para enviar preguntas al modelo GPT-4
def interact_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": (
                "Eres un experto en salud especializado en la gestión, prevención y educación sobre la diabetes, "
                "enfocado en México. Proporciona recomendaciones breves, concretas y personalizadas basadas en "
                "características individuales, manteniendo un enfoque conversacional."
            )},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# Función principal para recopilar información y generar recomendaciones
def main():
    print("¡Hola! ¿Cómo estás? Me gustaría saber tu nombre para ofrecerte recomendaciones personalizadas.")
    nombre = input("Nombre: ")
    
    # Recopilar información personal
    print(f"Para poder ayudarte mejor con recomendaciones de salud, {nombre}, me gustaría hacerte algunas preguntas.")
    
    edad = input("¿Cuántos años tienes?: ")
    altura = input("¿Cuánto mides (en cm)?: ")
    peso = input("¿Cuánto pesas (en kg)?: ")
    sexo = input("Sexo (M/F): ")
    actividad = input("¿Cuál es tu nivel de actividad física (bajo, medio, alto)?: ")
    restricciones = input("¿Tienes alguna preferencia o restricción alimenticia?: ")
    ubicacion = input("¿Dónde vives (ciudad o región)?: ")
    antecedentes = input("¿Tienes antecedentes familiares de diabetes?: ")
    ocupacion = input("¿Cuál es tu ocupación?: ")
    ingresos = input("¿Cuál es tu rango de ingresos (bajo, medio, alto)?: ")
    objetivo = input("¿Cuál es tu objetivo de salud?: ")

    # Crear un resumen del perfil del usuario
    perfil = (
        f"Nombre: {nombre}, Edad: {edad}, Altura: {altura} cm, Peso: {peso} kg, Sexo: {sexo}, "
        f"Actividad Física: {actividad}, Restricciones Alimenticias: {restricciones}, Ubicación: {ubicacion}, "
        f"Antecedentes Familiares de Diabetes: {antecedentes}, Ocupación: {ocupacion}, "
        f"Ingresos: {ingresos}, Objetivo de Salud: {objetivo}."
    )

    # Generar recomendaciones basadas en el perfil del usuario
    prompt = (
        f"Con base en la información proporcionada: {perfil}. "
        "Ofrece recomendaciones dietéticas y de actividad física para la gestión y prevención de la diabetes."
    )

    respuesta = interact_with_gpt(prompt)
    print("\nRecomendaciones personalizadas:")
    print(respuesta)

if _name_ == "_main_":
    main()