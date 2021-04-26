import sys
import speech_recognition as sr
from playsound import playsound
import time
import pyttsx3 as pyttsx

def get_morse_letter(letter):
    switcher = {
        "a": ".- ",
        "b": "-... ",
        "c": "-.-. ",
        "d": "-.. ",
        "e": ". ",
        "f": "..-. ",
        "g": "--. ",
        "h": ".... ",
        "i": ".. ",
        "j": ".--- ",
        "k": "-.- ",
        "l": ".-.. ",
        "m": "-- ",
        "n": "-. ",
        "o": "--- ",
        "p": ".--. ",
        "q": "--.- ",
        "r": ".-. ",
        "s": "... ",
        "t": "- ",
        "u": "..- ",
        "v": "...- ",
        "w": ".-- ",
        "x": "-..- ",
        "y": "-.-- ",
        "z": "--.. ",
        "0": "---- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        " ": "/ ",
        ",": "--..-- ",
        ".": ".-.-.- ",
        "?": "..--.. ",
        "/": "-..-. ",
        "-": "-....- ",
        "(": "-.--. ",
        ")": "-.--.- ",
    }
    return switcher.get(letter, "  ")

def make_new_string(raw_string):
    new_string = ""

    for i in raw_string :
        new_string += get_morse_letter(i)

    new_string = new_string[:-1]

    return new_string

def MainFunction(raw_string) :
    new_string = make_new_string(raw_string)

    print("----INPUT----\n")
    print(raw_string)
    print("\n----OUTPUT----\n")
    print(new_string)
    print("\n--------------\n")

    for i in new_string :
        if i == ".":
            playsound("sounds/dit.wav")
        elif i == "-" :
            playsound("sounds/dah.wav")
        else :
            time.sleep(0.5)

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source :
        while True :
            audio = r.listen(source)
            text = r.recognize_google(audio, language='fr_FR')
            text = text.lower()
            MainFunction(text)