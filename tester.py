pip3 install gTTS
from gtts import gTTS
import os
text_to_read = "tester tester for a test"
language = 'en'
slow_audio_speed = False
filename = "my_file.mp3"

def reading_from_string():
    audio_created = gTTS(text=text_to_read, lang=language, slow=slow_audio_speed)
    audio_created.save(filename)
    os.system(f'start {filename}')

if __name__ == "__main__":
    reading_from_string()