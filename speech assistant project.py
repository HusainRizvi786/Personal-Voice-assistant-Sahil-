#!/usr/bin/env python
# coding: utf-8

# In[54]:


import speech_recognition as sr
import time
from time import ctime
import playsound
import os
from gtts import gTTS


# In[55]:


r = sr.Recognizer()


# In[56]:


def record_audio():
    with sr.Microphone() as source:
        if ask:
            Sahil_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
      
        except sr.UnknownValueError:
            Sahil_speak('Sorry,I did not get that')
        except sr.RequestError:
            Sahil_speak('Sorry, my speech service is down')
        return voice_data
    
    
    


# In[57]:


def Sahil_speak(audio_string):
   tts = gTTS(text=audio_string, lang='en')
   r = random.randint(1, 10000000)
   audio_file = 'audio-' + str(r) + '.mp3'
   tts.save(audio_file)
   playsound.playsound(audio_file)
   print(audio_string)
   os.remove(audio_file)


# In[58]:


def respond(voice_data):
    if'what is your name' in voice_data:
       print('My name is Sahil')
    if 'what time is it' in voice_data:
       print(ctime())
    if 'search' in voice_data:
       search = record_audio('What do you want to search for?')
       url = 'https://google.com/search?q=' + search
       webbrowser.get().open(url)
       print('Here is what i found ' +search)
    if 'find location' in voice_data:
        location = record_audio('What is the Location?')
        url ='https://google.nl/maps/place' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location' + location)
    if 'exit' in voice_data:
        exit()


# In[59]:


time.sleep(1)
print('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)


# In[ ]:




