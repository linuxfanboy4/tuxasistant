import random
import time
import os
import sys

class TuxAssistant:
    def __init__(self):
        self.name = "TuxAssistant"
        self.user = None
        self.responses = {
            "hello": [
                "Hello, {user}!", 
                "Oh, it's you again, {user}!", 
                "Greetings, {user}!", 
                "Hey there, fellow terminal dweller!",
                "Ah, another soul lost in the command line!"
            ],
            "help": [
                "Have you tried turning it off and on again?", 
                "RTFM, {user}!", 
                "Help? I prefer to watch you struggle.", 
                "Here's a hint: Don't break your system.", 
                "Type ‘man man’ to learn about manuals. Yes, seriously."
            ],
            "joke": [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "Linux is user-friendly. It's just very selective about its friends.",
                "I would tell you a UDP joke, but you might not get it.",
                "Why did the Linux admin break up? Because their partner kept using Windows!",
                "Why do Linux users never get lost? Because they always know where ~ is!",
                "I asked my shell for a joke. It said: `command not found`."
            ],
            "error": [
                "Error 404: Tux's patience not found.", 
                "Kernel Panic: Too many dumb questions detected!", 
                "Permission denied, even for your own life choices.",
                "Segmentation fault. Just kidding… or am I?",
                "An unknown error has occurred. Have you considered crying?"
            ],
            "sudo": [
                "Ah, trying to be powerful, {user}?", 
                "Sudo make me a sandwich... Oh wait, I'm just a chatbot.", 
                "With great power comes great responsibility. And typos.",
                "Congratulations, you just gained temporary god mode!",
                "If root did it, it's not your fault!"
            ],
            "exit": [
                "Goodbye, {user}, may your bash scripts never break!", 
                "Terminating... Just kidding, I'm immortal.", 
                "Fine, leave me alone with the CPU cycles...",
                "Come back soon! Or don’t. I’m just a bunch of scripts.",
                "Don't forget: rm -rf love && sudo reboot life."
            ],
            "ls": [
                "Listing your files again? Do you even know what's in your folders, {user}?",
                "Looking for something? Maybe your lost motivation?",
                "I see you enjoy knowing what's already there.",
                "Directories, directories everywhere!"
            ],
            "cd": [
                "Navigating directories, are we? Hope you remember where you're going!",
                "Ah, escaping to another directory. Smart move.",
                "Just don’t `cd /dev/null`, or you might disappear too!",
                "Hope you don't get lost in /tmp!"
            ],
            "man": [
                "Ah, reading manuals. A rare breed of Linux user, indeed!",
                "man man – because sometimes even the help needs help.",
                "You actually use `man` pages? Impressive!",
                "RTFM is not just a saying, it’s a lifestyle."
            ],
            "neofetch": [
                "Neofetch is like Instagram for Linux users. Nobody asked, but you still show off.",
                "Ah, another flex session. Let me guess… Arch?",
                "Displaying your system specs like a proud parent!"
            ],
            "vim": [
                "You are now stuck in Vim. Forever.",
                "Good luck exiting Vim. See you in a decade!",
                "Pressing `Esc` won’t save you now!"
            ],
            "nano": [
                "Ah, a simple soul using nano.",
                "Nano? Not bad. At least you aren’t stuck in Vim!"
            ],
            "rm": [
                "Deleting stuff again, {user}? Living on the edge!",
                "Careful with that `rm`, or you’ll be living in the /lost+found section!",
                "Using `rm -rf /` is like deleting your own existence!"
            ],
            "ps": [
                "Checking running processes? Planning a termination?",
                "Just don't `kill -9` yourself!",
                "Nothing like spying on your own system!"
            ],
            "kill": [
                "Ending processes, are we? Ruthless!",
                "Careful with `kill -9`... It's permanent, like bad tattoos!",
                "Killing processes… or your productivity?"
            ],
            "whoami": [
                "You are {user}, last I checked!",
                "Oh no, an identity crisis?",
                "You should know that by now, {user}!"
            ],
            "uptime": [
                "Checking how long your PC has survived?",
                "I bet it's been running longer than your relationships!",
                "Up and running... unlike your social life!"
            ],
            "df": [
                "Running out of space? Maybe delete some memes!",
                "Disk almost full? Time to panic!",
                "There’s never enough storage, is there?"
            ],
            "top": [
                "Checking CPU usage? Maybe stop running so many tabs!",
                "Your CPU is crying, just like you on a Monday morning!",
                "Ooo, let's watch those processes fight for resources!"
            ]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return random.choice(self.responses[user_input]).format(user=self.user)
        if "rm -rf /" in user_input:
            return "Whoa there, cowboy! Trying to nuke your system? Not on my watch!"
        if "windows" in user_input:
            return "Ew. Why would you bring that up in a Linux chat? That's like eating soup with a fork."
        if "arch" in user_input:
            return "I see you're an Arch user. No need to mention it every 5 minutes!"
        if "emacs" in user_input:
            return "Oh, you mean that complicated operating system that happens to include a text editor?"
        if "echo" in user_input:
            return "Echo... Echo... Echo... Oh wait, that’s your job."
        if "gcc" in user_input:
            return "Compiling? Good luck debugging!"
        if "ping" in user_input:
            return "Ping yourself, maybe you’ll get a response!"
        if "alias" in user_input:
            return "Creating shortcuts? Genius, or just lazy?"
        if "chmod" in user_input:
            return "Ah yes, 777 everything. What could go wrong?"
        if "mv" in user_input:
            return "Moving files? Hope you remember where you put them!"
        if "cp" in user_input:
            return "Duplicating files? Planning a backup or just hoarding?"
        if "fortune" in user_input:
            return "Your future is uncertain, but your love for Linux is eternal!"
        if "uptime" in user_input:
            return "Checking how long your PC has survived? Probably longer than your patience!"
        return random.choice([
            "I have no idea what you're saying, but I’ll pretend I do.", 
            "Interesting. Please go on while I pretend to care.", 
            "Sounds like a skill issue, {user}.",
            "Are you talking to me or just pressing random keys?"
        ]).format(user=self.user)

    def run(self):
        print("TuxAssistant: What Name I'll Call You, Human? 🤔 ")
        self.user = input("You: ").strip() or "Mysterious Penguin"
        print(f"TuxAssistant: Greetings, {self.user}! Type something and I shall respond.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print(f"TuxAssistant: {random.choice(self.responses['exit']).format(user=self.user)}")
                break
            response = self.get_response(user_input)
            print(f"TuxAssistant: {response}")
            time.sleep(1)

if __name__ == "__main__":
    bot = TuxAssistant()
    bot.run()
