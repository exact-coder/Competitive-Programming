import pyttsx3
import wikipedia

bhai = pyttsx3.init()

In =input("Search Wikipedia/Google: ")

result = wikipedia.summary(In, sentences = 5)

print(result)
bhai.say(result)
bhai.runAndWait()
