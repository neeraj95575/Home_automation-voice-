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

import speech_recognition as sr
from gtts import gTTS 
import os
import random
import RPi.GPIO as GPIO 
from time import sleep
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT) # light
GPIO.setup(3, GPIO.OUT) # fan
GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)


mytext = 'नमस्ते मेरा नाम मानवी है  मैं आपकी क्या सहायता कर सकती हूं'
language = 'hi'
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
                            data = r.recognize_google(audio,language='hi')

                        except sr.UnknownValueError:
                            print ('Attention ! Google could not understand audio')
                            data='Could not understand anything'
                        except sr.RequestError as e:

                           print ('Attention ! Could not request results from Google service.')

                        print(data)


                        ################################
                        if data =='मानवी लाइट ऑन करो' or  data == 'मानवी लाइट ऑन कर' or  data == 'लाइट चालू कर दो मानवी' or  data == 'मानवी लाइट चालू कर दो':
                            print("light on")
                            GPIO.output(2, GPIO.LOW)
                            mytext = 'मैंने लाइट ऑन कर दिया '
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        if data =='मानवी लाइट ऑफ करो' or  data == 'मानवी लाइट ऑफ कर' or  data == 'लाइट बंद कर दो मानवी' or  data == 'मानवी लाइट बंद कर दो':
                            print("light off")
                            GPIO.output(2, GPIO.HIGH)
                            mytext = 'मैंने लाइट  ऑफ  कर दिया '
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        if data =='मानवी लाइट पंखा ऑफ करो' or  data == 'मानवी लाइट पंखा ऑफ कर' or  data == 'लाइट पंखा बंद कर दो मानवी' or  data == 'मानवी लाइट पंखा बंद कर दो':
                            print("light fan off")
                            GPIO.output(2, GPIO.HIGH)
                            GPIO.output(3, GPIO.HIGH)
                            mytext = 'मैंने लाइट पंखा ऑफ  कर दिया '
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3") 
                        
                        if data == 'मानवी पंखा ऑन करो' or data == 'मानवी पंखा ऑन कर' or data == 'मानवी पंखा चालू कर दो' or data == 'पंखा चालू कर दो मानवी':
                            print("fan on")
                            GPIO.output(3, GPIO.LOW)
                            mytext = 'मैंने पंखा ऑन कर दिया'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        if data == 'मानवी पंखा ऑफ करो' or data == 'मानवी पंखा ऑफ कर' or data == 'मानवी पंखा बंद कर दो' or data == 'पंखा बंद कर दो मानवी' :
                            print("fan off")
                            GPIO.output(3, GPIO.HIGH)
                            mytext = 'मैंने पंखा  ऑफ कर दिया'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        

                        if data =='मानवी लाइट पंखा ऑन करो' or  data == 'मानवी लाइट पंखा ऑन कर' or  data == 'लाइट पंखा चालू कर दो मानवी' or  data == 'मानवी लाइट पंखा चालू कर दो':
                            print("light and fan on")
                            GPIO.output(2, GPIO.LOW)
                            GPIO.output(3, GPIO.LOW)
                            mytext = 'मैंने लाइट  और पंखा ऑन कर दिया '
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")
                            
                        if data == 'मानवी आपका धन्यवाद':
                            mytext = 'इसकी कोई जरूरत नही यह मेरा फर्ज हैं'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        if data == 'मानवी तुम बहुत बुरी हो':
                            mytext = 'पहले आप अपने को देख लीजिए'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")
                            os.system("mpg321 ooobai.mp3")

                        if  data == 'मेरी गर्लफ्रेंड बनोगी मानवी' or data == 'मानवी क्या आप मेरी गर्लफ्रेंड बनोगी' or data == 'क्या आप मेरी गर्लफ्रेंड बनोगी मानवी' or data == 'मानवी क्या तुम मेरी गर्लफ्रेंड बनोगी':
                            mytext = 'आप अच्छा मजाक कर लेते हैं हो हो हो हो'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")
                            #os.system("mpg321 oooooo.mp3")
                            os.system("mpg321 oootabla.mp3")

                        if data == 'मानवी क्या आप मुझे सुन रही हो' or data == 'मानवी क्या आप मुझे सुन रहे हो'  or data == ' मानवी आप मुझे सुन रहे हो'  or data == ' मानवी आप मुझे सुन रही हो':
                            mytext = 'जी हां मैं आपको सुन रही हूं'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        if  data ==  'मानवी गाड़ी आज मैं चला लूंगा':
                            mytext = 'अब मुझे भगवान ही बचाएं'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3")
                            os.system("mpg321 welcome.mp3")
                            os.system("mpg321 coffin.mp3")

                        if  data ==  'हेलो मानवी':
                            mytext = 'मैं आपकी क्या सहायता कर सकती हूं'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3")
                            #os.system("mpg321 ksehae.mp3")
                            os.system("mpg321 welcome.mp3")


                        if  data ==  'मानवी आज मैं कैसा लग रहा हूं':
                            #l = ['आज तुम खूबसूरत लग रहे हो', 'आज तुम लाजवाब लग रहे हो', 'आज तुम झक्कास लग रहे हो', 'आज तुम काफी खुश लग रहे हो']
                            mytext = random.choice(('आज तुम खूबसूरत लग रहे हो', 'आज तुम लाजवाब लग रहे हो', 'आज तुम झक्कास लग रहे हो', 'आज तुम काफी खुश लग रहे हो'))
                            print(mytext)
                            #mytext = 'आज तुम खूबसूरत लग रहे हो'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")

                        if  data ==  'मानवी तुम खूबसूरत लग रही हो':
                            #l = ['आज तुम खूबसूरत लग रहे हो', 'आज तुम लाजवाब लग रहे हो', 'आज तुम झक्कास लग रहे हो', 'आज तुम काफी खुश लग रहे हो']
                            #mytext = 'आज तुम खूबसूरत लग रहे हो'
                            #language = 'hi'
                            #myobj = gTTS(text=mytext, lang=language, slow=False)   
                            #myobj.save("welcome.mp3") 
                            os.system("mpg321 hamalum.mp3")

                        """else:
                            mytext = 'कृपया आप दोबारा बोलोगे आप की आवाज समझ नहीं आई'
                            language = 'hi'
                            myobj = gTTS(text=mytext, lang=language, slow=False)   
                            myobj.save("welcome.mp3") 
                            os.system("mpg321 welcome.mp3")"""

finally:
    GPIO.cleanup()
                
              

                    
             
                    
                    


