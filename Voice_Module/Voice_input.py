import pyttsx3

# Initialization 
engine = pyttsx3.init() 

#### Section For Rate ######

# getting details of current speaking rate
rate = engine.getProperty('rate') 

#printing current voice rate
print (rate)           

# setting up new voice rate
engine.setProperty('rate', 125)     


#### section To Fluctuate  Volume #######

#getting to know current volume level (min=0 and max=1)
volume = engine.getProperty('volume')   

#printing current volume level
print (volume)         

# setting up volume level  between 0 and 1
engine.setProperty('volume',1.0)    

### Voice Section . ######

#getting details of current voice
voices = engine.getProperty('voices')       

#changing index, changes voices. o for male
#engine.setProperty('voice', voices[0].id)  


#changing index, changes voices. 1 for female
engine.setProperty('voice', voices[1].id)   




engine.say("Hello !")
engine.say('speaking rate :' + str(rate))
engine.runAndWait()
engine.stop()
