import os
from gtts import gTTS

mytext = 'Todays news is : !'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("Voices/news.mp3")





