import os
import openai
from dotenv import load_dotenv
import whisper

# Configura tu clave de API
openai.api_key = "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"

import whisper

# Cargar el modelo
model = whisper.load_model("base")

# Utiliza la ruta completa del archivo de audio
audio_path = "C:\\Users\\josel\\OneDrive\\Escritorio\\Cursos\\Python\\Estadistica\\Asistente de voz\\audio.mp3"

# Transcribir el archivo de audio
transcribed = model.transcribe(audio_path, language='es')

# Imprimir el resultado
print("Texto transcrito:", transcribed['text'])
