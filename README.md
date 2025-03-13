# TuxAssistant - Your Linux Terminal Companion

TuxAssistant is a fun and interactive terminal-based assistant inspired by the nostalgic Microsoft Clippy, but with a Linux twist. Designed to bring humor and personality to your command-line experience, TuxAssistant responds to common Linux commands and user inputs with witty, sarcastic, and sometimes helpful remarks. Whether you're navigating directories, compiling code, or just looking for a laugh, TuxAssistant is here to keep you company.

## Features

- **Interactive Responses**: TuxAssistant responds to a variety of Linux commands and user inputs with humorous and context-aware replies.
- **Customizable User Name**: Personalize your experience by setting a custom name for yourself.
- **Wide Range of Commands Supported**: From `ls` and `cd` to `sudo` and `rm`, TuxAssistant has a response for almost every common Linux command.
- **Error Handling**: Even when things go wrong, TuxAssistant has a sarcastic remark ready to lighten the mood.
- **Exit with Style**: Say goodbye with a memorable exit message tailored to your session.

---

## Installation

To get started with TuxAssistant, simply follow these steps:

1. **Download the Script**:
   Use `wget` to download the script directly to your machine:
   ```bash
   wget https://raw.githubusercontent.com/linuxfanboy4/tuxasistant/refs/heads/main/tux.py
   ```

2. **Run the Script**:
   Execute the script using Python 3:
   ```bash
   python3 tux.py
   ```

3. **Enjoy**:
   Follow the on-screen prompts to start interacting with TuxAssistant.

## Usage

Once the script is running, TuxAssistant will greet you and ask for your name. After setting your name, you can start typing commands or phrases, and TuxAssistant will respond accordingly. Here are some examples of what you can try:

- **Basic Commands**:
  - `ls`: "Listing your files again? Do you even know what's in your folders?"
  - `cd`: "Navigating directories, are we? Hope you remember where you're going!"
  - `sudo`: "Ah, trying to be powerful, are we?"

- **Fun Interactions**:
  - `joke`: "Why do programmers prefer dark mode? Because light attracts bugs!"
  - `help`: "Have you tried turning it off and on again?"
  - `exit`: "Goodbye, may your bash scripts never break!"

- **Error Handling**:
  - `rm -rf /`: "Whoa there, cowboy! Trying to nuke your system? Not on my watch!"
  - `windows`: "Ew. Why would you bring that up in a Linux chat?"

## Supported Commands and Keywords

TuxAssistant recognizes a wide range of commands and keywords, including but not limited to:

- `hello`, `help`, `joke`, `error`, `sudo`, `exit`
- `ls`, `cd`, `man`, `neofetch`, `vim`, `nano`
- `rm`, `ps`, `kill`, `whoami`, `uptime`, `df`, `top`
- `windows`, `arch`, `emacs`, `echo`, `gcc`, `ping`, `alias`, `chmod`, `mv`, `cp`, `fortune`

For unsupported inputs, TuxAssistant will respond with a generic, humorous remark.

## Customization

TuxAssistant is designed to be simple and straightforward, but you can easily customize the responses by modifying the `responses` dictionary in the script. Add your own commands, jokes, or sarcastic remarks to make TuxAssistant truly your own.

## Inspiration

TuxAssistant is inspired by the iconic Microsoft Clippy, but with a focus on the Linux community. It aims to bring a touch of humor and personality to the terminal, making your command-line experience more enjoyable.

## Contributing

Contributions are welcome! If you have ideas for new features, commands, or responses, feel free to fork the repository and submit a pull request. Let's make TuxAssistant even better together.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as you see fit.

## Feedback

If you have any feedback, suggestions, or just want to share a funny interaction with TuxAssistant, feel free to open an issue on the GitHub repository. Your input is greatly appreciated!
