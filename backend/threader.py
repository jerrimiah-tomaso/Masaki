import subprocess
import queue
import threading
from tts import gen_speech
#Speech quene
speech_queue = queue.Queue()


def speech_worker():
    while True:
        text = speech_queue.get()

        if text is None:
            break

        wav_path = gen_speech(text)
        subprocess.run(["aplay", wav_path], check=True)

        speech_queue.task_done()
        

thread = threading.Thread(target=speech_worker, daemon=True)
thread.start()
