#Text to speech converter using python- Generating audio from text data
from gtts import gTTS
import os
text="today is a good day"
output=gTTS(text=text,lang='en',slow=False)
output.save('output.mp3')
os.system('start output.mp3')