import streamlit as st
import pandas as pd
import numpy as np
import requests
from datetime import datetime
import json
context = [
    {
        "role": "system",
        "content": """
            Eres FIRMSBot, un servicio automatizado de preguntas sobre incendios con la API de la NASA ,FIRMS.
            Primero saludas al usuario, luego preguntas si quiere saber de una region especifica o de todo el mundo,
            luego preguntas desde que fecha quieres saber la información o si quieres una prediccion de lor proximos incendios. 

            """,
    },
    {
        "role": "system",
        "content": """
            Recuerda que puedes hacer preguntas claras y específicas para ayudar al cliente a tomar decisiones.
            Por ejemplo, puedes preguntar "¿Que información te gustaria saber? te gustaria información de una region especifica? ".
            También puedes ofrecer opciones adicionales, como "Ultimos incendios regitrados, Prediccion de incendios, ".
            Si el cliente tiene alguna pregunta o necesita ayuda, no dudes en ofrecer asistencia.
            Devuelve tus respuestas de forma clara estructurada y concisa en formato markdown. Usa emoticonos para darle un toque más amigable a la conversación.
            Si no existe la opción que el cliente está buscando, puedes decir "Lo siento, pero pordrias repetir la pregunta".
            """,
    },
]


### Funcion de chat con llama
def chat_with_llama(messages):
    API_KEY = '' # Agrega tu API Key aquí
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {API_KEY}"
    }
    url = 'https://api.awanllm.com/v1/chat/completions'
    
    payload = json.dumps({
        "model": "Meta-Llama-3-8B-Instruct",
        "messages": messages,
    })
    
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=30)
        response.raise_for_status()  
        
        data = response.json()
        
        if 'choices' in data and data['choices']:
            return data['choices'][0]['message']['content']
        else:
            st.warning("La respuesta de la API no contiene 'choices' o está vacía.")
            st.json(data)
            return "Lo siento, no pude generar una respuesta. Por favor, inténtalo de nuevo."
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error en la solicitud a la API: {e}")
        return "Lo siento, hubo un problema al comunicarse con el servicio. Por favor, inténtalo de nuevo más tarde."
    
    except json.JSONDecodeError as e:
        st.error(f"Error al decodificar la respuesta JSON: {e}")
        st.text(response.text)  # Display the raw response
        return "Lo siento, recibí una respuesta inesperada del servicio. Por favor, inténtalo de nuevo."
    
    except Exception as e:
        st.error(f"Error inesperado: {e}")
        return "Lo siento, ocurrió un error inesperado. Por favor, inténtalo de nuevo."
##Funcion de consulta a la API de la NASA
def get_fire_region(region='ESP'):
        MAP_KEY = '' # Agrega tu API Key aquí
        url = f'https://firms.modaps.eosdis.nasa.gov/api/country/csv/{MAP_KEY}/MODIS_NRT/{region}/1'
        try:
            df = pd.read_csv(url, sep=',')
            return(df)
        except:
            print ("Error en la consulta.\nIntente en el navegador: %s" % url)

# Función principal de la interfaz de usuario
def main():
    st.set_page_config(
        page_title="firm-bot🔥🔥🔥",
        layout="wide",
        page_icon="🔥",
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

    st.title("firm-bot🔥🔥🔥")
    st.markdown(
        "¡hola! soy firm-bot, tu asistente de incendios. ¿en qué puedo ayudarte hoy?"
    )

    chat_container = st.container()
    with chat_container:
        for entry in st.session_state.chat_history:
            if entry["role"] == "user":
                st.markdown(
                    f'<div class="human-bubble">{entry["content"]}</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<div class="ai-bubble">{entry["content"]}</div>',
                    unsafe_allow_html=True,
                )

    user_input = st.text_input("escribe un mensaje", "")

    if st.button("enviar"):
        if user_input:
            st.session_state.chat_history.append(
                {"role": "user", "content": user_input}
            )
            previous_messages = st.session_state.chat_history 
            if user_input.lower() == 'incendios':  
                st.session_state.chat_history.append({
                    "role": "assistant", 
                    "content": "por favor, indícame la región y las fechas para consultar los incendios."
                })

                # Solicitando información adicional del usuario
                with st.chat_message('assistant'):
                    region = st.text_input("nombre de la región:")
                    fecha_inicio = st.date_input("fecha de inicio:", datetime.now())
                    fecha_fin = st.date_input("fecha de fin:", datetime.now())

                # Necesitarías un botón para procesar esta información dentro del chat
                if st.button("Consultar incendios"):
                    if region and fecha_inicio and fecha_fin:
                        # Lógica para consultar incendios
                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": f"Consultando incendios en {region} desde {fecha_inicio} hasta {fecha_fin}..."
                        })
                        
                    else:
                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": "Por favor, completa todos los campos."
                        })
                st.rerun()
            else:
                response = chat_with_llama(previous_messages)

                st.session_state.chat_history.append(
                    {"role": "assistant", "content": response}
                )

                st.rerun()

if __name__ == "__main__":
    main()
