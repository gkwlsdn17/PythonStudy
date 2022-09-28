
from gtts import gTTS
import os

from playsound import playsound

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "어서오세요."

tts = gTTS(text=text , lang='ko')
tts.save(" hi.mp3 ")

playsound(" hi.mp3 ")