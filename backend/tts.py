import wave
import os
from piper.voice import PiperVoice

model_path = "en_US-libritts_r-medium.onnx"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

voice = PiperVoice.load(model_path)

output_path = "tts_output.wav"


def gen_speech(text):
    
    text = str(text)

    with wave.open(output_path, "wb") as wav_file:
        voice.synthesize_wav(text,wav_file)

    return output_path
