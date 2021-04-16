import speech_recognition as sr
from datetime import date
from gpiozero import LED
from time import sleep

red = LED(17)
relay1 = LED(14)
relay2 = LED(15)

r = sr.Recognizer()
mic = sr.Microphone()

print("hello")

while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)

    if words == "today":
        print(date.today())

    if words == "LED on":
        red.on()

    if words == "LED off":
        red.off()

    if words == "relay one on":
        relay1.on()

    if words == "relay one off":
        relay1.off()

    if words == "relay two on":
        relay2.on()

    if words == "relay two off":
        relay2.off()

    if words == "exit":
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("Goodbye")
        break

