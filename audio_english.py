''' languages

{'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan',
 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian',
 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'hi': 'Hindi',
 'hu': 'Hungarian', 'is': 'Icelandic', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese',
 'kn': 'Kannada', 'km': 'Khmer', 'ko': 'Korean', 'la': 'Latin', 'lv': 'Latvian', 'mk': 'Macedonian', 'ml': 'Malayalam',
 'mr': 'Marathi', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese',
 'ro': 'Romanian', 'ru': 'Russian', 'sr': 'Serbian', 'si': 'Sinhala', 'sk': 'Slovak', 'es': 'Spanish', 'su': 'Sundanese',
 'sw': 'Swahili', 'sv': 'Swedish', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu',
 'vi': 'Vietnamese', 'cy': 'Welsh', 'zh-cn': 'Chinese (Mandarin/China)', 'zh-tw': 'Chinese (Mandarin/Taiwan)',
 'en-us': 'English (US)', 'en-ca': 'English (Canada)', 'en-uk': 'English (UK)', 'en-gb': 'English (UK)',
 'en-au': 'English (Australia)', 'en-gh': 'English (Ghana)', 'en-in': 'English (India)', 'en-ie': 'English (Ireland)',
 'en-nz': 'English (New Zealand)', 'en-ng': 'English (Nigeria)', 'en-ph': 'English (Philippines)', 'en-za': 'English (South Africa)',
 'en-tz': 'English (Tanzania)', 'fr-ca': 'French (Canada)', 'fr-fr': 'French (France)', 'pt-br': 'Portuguese (Brazil)',
 'pt-pt': 'Portuguese (Portugal)', 'es-es': 'Spanish (Spain)', 'es-us': 'Spanish (United States)'}
 
'''
import speech_recognition as sr  #  i use Google Speech API
from gtts import gTTS      # Google Text-to-Speech
import os
import random
import RPi.GPIO as GPIO 
from time import sleep
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT) # light
GPIO.setup(3, GPIO.OUT) # fan

mytext = 'my name is Manvi how can i help you'
language = 'en-in'
myobj = gTTS(text=mytext, lang=language, slow=False)   
myobj.save("welcome.mp3") 
os.system("mpg321 welcome.mp3") 

try:
        while(1):      
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print ('Attention! Say something')
                            audio = r.listen(source)
                        try:
                            data='something'
                            data = r.recognize_google(audio,language='en-in')
                        except sr.UnknownValueError:
                            print ('Attention ! Google could not understand audio')
                            data='Could not understand anything'
                        except sr.RequestError as e:
                           print ('Attention ! Could not request results from Google service.')
                        print(data)
                        GPIO.output(2, GPIO.HIGH)
                        GPIO.output(3, GPIO.HIGH)

                        
                        
                        if data =='Manvi can you turn on light' or  data == 'turn on light Manvi' or  data == 'Light turned on manvi':
                            print("light on")
                            GPIO.output(2, GPIO.LOW)
                            mytext = 'I turned on light '
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        if data =='Manvi can you turn off light' or  data == 'turn off light Manvi' or  data == 'Light turned off manvi':
                            print("light off")
                            GPIO.output(2, GPIO.HIGH)
                            mytext = 'I turned off light'
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3") 

                        if data == 'Manvi can you turn on fan' or data == 'turn on fan Manvi' or data == 'Fan turned on manvi':
                            print("fan on")
                            GPIO.output(3, GPIO.LOW)
                            mytext = 'I turned on fan'
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        if data == 'Manvi can you turn off fan' or data == 'turn off fan Manvi' or data == 'Fan turned off manvi':
                            print("fan off")
                            GPIO.output(3, GPIO.HIGH)
                            mytext = 'I turned off  fan'
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")
                        
                        if data == 'Manvi can you turn on both light and fan' or data == 'Turn on light and Fan Manvi' or data == 'Light and fan turned on manvi':
                            print("ligh and fan on")
                            GPIO.output(2, GPIO.LOW)
                            GPIO.output(3, GPIO.LOW)
                            mytext = 'I turned on the light and fan'
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        if data =='Manvi can you turn off both light and fan' or  data == 'Turn off light and Fan Manvi'or data == 'Light and fan turned off manvi':
                            print("light and fan off")
                            GPIO.output(2, GPIO.HIGH)
                            GPIO.output(3, GPIO.HIGH)
                            mytext = 'I turned off the light and fan '
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")
 
                        if data == 'thankyou Manvi' or data == 'thank you very much Manvi':
                            mytext = 'There is no need for it, it is my dutyं'
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        if data == 'Manvi you will be my girlfriend'  or  data == 'Manvi will you date with me' or  data == 'My girlfriend will be you manvi':
                            mytext = 'You make a good joke ho ho ho ho'
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")
                            os.system("mpg321 oootabla.mp3")

                        if data == 'Manvi are you listening to me' or data == 'are you listening to me Manvi':
                            mytext = 'Yes, I am listening to you. What can I help you?'
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        
                        if  data ==  'today how am I looking Manvi':
                            mytext = random.choice(('Today you look beautiful', 'Today you look fantastic', 'Today you seem to be shocked', 'Today you seem quite happy'))
                            print(mytext)
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")
                            os.system("mpg321 hoho.mp3")

                            
                        if data == 'you are very bad Manvi':
                            mytext = 'First you see yourself'
                            language = 'en-in'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3")
                            os.system("mpg321 lookathis.mp3")
                            os.system("mpg321 welcome.mp3")
                            os.system("mpg321 lookatthisooooo.mp3")
                            
                        if  data ==  'today I will drive the car Manvi':
                            mytext = 'Now god will save me'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3")
                            os.system("mpg321 welcome.mp3")
                            os.system("mpg321 coffin.mp3")

finally:
    GPIO.cleanup()
                
              

                    
             
                    
                    


