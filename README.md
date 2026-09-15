# Python Mega Projects

## Projects

- Jarvis AI Assistant
- WhatsApp Auto-Reply Chatbot
- Slot Machine
- K - AI Chatbot
- Turtle Race
- WPM Typing Test

## Jarvis AI Assistant Features

- Voice Command Support
- Opens Popular Websites
- Fetches Latest News using News API
- Text-to-Speech Responses
- Command-based Automation
- Beginner-friendly Project Structure

## WhatsApp Auto-Reply Chatbot Features

- Reads Latest Chat Messages via Screen Automation
- AI-Generated Replies using Groq (LLaMA 3.3)
- Hinglish + English Conversational Responses
- Automated Message Sending
- Context-Aware Reply Generation

## Slot Machine Features

- Deposit & Balance Management System
- Bet on Multiple Lines (up to 3)
- Configurable Min/Max Bet Limits
- Randomized Slot Symbol Generation (weighted by symbol count)
- Dynamic Slot Grid Display (rows x columns)
- Win Checking Across Betted Lines
- Symbol-based Payout Values
- Play Again / Quit Loop
- Automatic Game Over on Insufficient Balance
- Input Validation for Deposits, Lines, and Bets

## K - AI Chatbot Features

- Custom AI Personality (frank, human-like tone with minimal emojis)
- Short, Impactful, Conversational Responses
- Supports English + Hinglish Communication
- Powered by Groq API (LLaMA 3.3 70B Versatile)
- Simple Terminal-based Chat Loop
- Exit Commands (`exit`, `bye`, `quit`)

## Turtle Race Features

- User-Selectable Number of Racers (2-10)
- Random Turtle Color Assignment from a Preset Palette
- Guess-the-Winner Mini Game Before the Race Starts
- Dynamic Starting Position Calculation Based on Racer Count
- Randomized Turtle Movement for Unpredictable Races
- Automatic Winner Detection at the Finish Line
- Turtle Graphics-based Visual Race Simulation
- Input Validation for Racer Count and Color Guess

## WPM Typing Test Features

- Terminal-based Speed Typing Test using `curses`
- Random Practice Text Loaded from `text.txt`
- Real-Time WPM (Words Per Minute) Calculation
- Live Character-by-Character Color Feedback (green for correct, red for incorrect)
- Backspace Support for Correcting Mistakes
- Auto-Completion Detection When Typed Text Matches Target Text
- Escape Key to Exit at Any Time
- Replay Loop to Take Another Test After Completion
- Non-blocking Key Input for Smooth Live Updates

## Technologies

- Python 3
- SpeechRecognition
- pyttsx3
- Requests
- News API
- PyAudio
- PyAutoGUI
- Pyperclip
- Groq API
- curses (built-in module)
- random (built-in module)
- turtle (built-in module)

## What I Learned

- Python Automation
- Voice Recognition
- Text-to-Speech
- API Integration
- Working with External Libraries
- Python Modules (`import`)
- Functions
- Conditional Statements (`if-else`)
- User Input
- Code Organization
- Screen/GUI Automation
- Working with LLM APIs
- Clipboard Handling
- Working with Dictionaries
- Nested Loops and Data Structures (Matrix/Grid Logic)
- Input Validation with `while` Loops
- Game Loop Design
- Randomization Logic (`random.choice`, `random.remove`)
- Using AI to Assist with Function Generation
- Working with LLM Chat Completion APIs (Groq)
- Designing AI Personality via System Prompts
- Structuring Multi-role Messages (`user` / `system`)
- Building Simple Terminal Chatbot Loops
- Turtle Graphics Programming
- Coordinate-based Positioning and Movement
- Using `enumerate()` for Indexed Iteration
- Simulating Simple Games with Randomness
- Terminal UI Programming with `curses`
- Real-Time Input Handling and Non-blocking Key Reads
- Live Timing and Rate Calculations (WPM Formula)
- Reading and Processing Text Files
- Color Pair Setup and Conditional Text Styling in the Terminal
- Comparing Lists and Strings via `"".join()`
- Handling Special Keys (Backspace, Escape) via Key Codes
- Try/Except for Safe Input Handling

## Project Structure

```text
Python-Mega-Projects/
├── Jarvis-AI-Assistant/
│   ├── main.py
│   └── requirements.txt
│
├── WhatsApp-Auto-Reply-Chatbot/
│   ├── main.py
│   └── requirements.txt
│
├── Slot-Machine/
│   └── main.py
│
├── K-AI-Chatbot/
│   ├── main.py
│   └── requirements.txt
│
├── Turtle-Race/
│   └── main.py
│
├── WPM-Typing-Test/
│   ├── main.py
│   └── text.txt
│
└── README.md
```

## About

This repository contains beginner-friendly Python mega projects that I built while learning Python programming.

These projects helped me gain hands-on experience with automation, APIs, voice recognition, LLM integration, game logic, terminal UI programming, and real-world Python development.

## Future Improvements

- Add more voice commands
- Integrate AI models for smarter responses
- Add weather and calendar support
- Improve command recognition
- Create a graphical user interface (GUI)
- Optimize code structure
- Replace screen-automation chat reading with DOM/API-based methods for reliability
- Add support for multiple chat platforms
- Add a GUI version of the Slot Machine
- Add more slot symbols and bonus rounds
- Add persistent balance storage (save/load between sessions)
- Add conversation memory/context to K Chatbot
- Move Groq API key to environment variables for security
- Add voice input/output support to K Chatbot
- Add adjustable turtle speed settings to Turtle Race
- Add a scoreboard/leaderboard for repeated Turtle Race guesses
- Add sound effects for the Turtle Race finish
- Add accuracy percentage tracking to WPM Typing Test
- Add difficulty levels (short/medium/long texts) to WPM Typing Test
- Store and display best WPM scores across sessions
- Expand the `text.txt` practice text pool

## Note

This repository represents my Python learning journey.

All projects are written by me.
- My goal is to build more advanced Python projects as I continue learning.