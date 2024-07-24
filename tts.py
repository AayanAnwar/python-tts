import pyttsx3
text = ("What should I say?")
while text != 'q':
    friend = pyttsx3.init()
    text = input("What should I say?: ")
    friend.say(text)
    friend.runAndWait()
    friend.stop()


    
