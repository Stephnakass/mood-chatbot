import time

def type_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()
    
import random

type_text("What is your name? ")
name = input()

while True:
    type_text("How are you feeling today, " + name + "? ")
    mood = input().lower()

    if mood == "tired":
        responses = [
            "You should get some rest (-_-)zｚＺ",
            "Maybe a nap is calling your name (￣o￣)zzZ",
            "Rest mode activated (-_-)zｚＺ"
        ]
        print("Hmm...")
        time.sleep(2)
        type_text(name + ", " + random.choice(responses))
    
    elif mood == "happy":
        responses = [
            "Love that for you (＾▽＾)",
            "Keep that energy going (≧◡≦)",
            "We love a happy moment (＾▽＾)"
        ]
        type_text(name + ", " + random.choice(responses))
    
    elif mood == "stressed":
        responses = [
            "Take a breath, you've got this (•̀ᴗ•)́و",
            "One step at a time (－‸ლ)",
            "You're handling more than you think (•̀ᴗ•́)و"
        ]
        type_text(name + ", " + random.choice(responses))
    
    elif mood == "hungry":
        type_text("Go eat something immediately (¬‿¬)")
        
    elif mood == "bye":
        type_text("uhhh... kay bai")
        break
    
    else:
        type_text("Hmm... interesting mood (・_・)")