#done
from groq import Groq
from json import load, dump
import datetime
import os
from dotenv import load_dotenv

# -------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# -------------------------------------------------
# Force load .env from current directory
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

GroqAPIkey = os.getenv("GroqAPIkey")
Username = os.getenv("Username", "User")
Assistantname = os.getenv("Assistantname", "IRIS")

if GroqAPIkey is None:
    raise ValueError("❌ GroqAPIkey not found. Check .env file location and name.")

client = Groq(api_key=GroqAPIkey)

# -------------------------------------------------
# SYSTEM PROMPT
# -------------------------------------------------
System = f"""
Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} 
which also has real-time up-to-date information from the internet.

*** Do not tell time until I ask, do not talk too much, just answer the question. ***
*** Reply in only English, even if the question is in Hindi, reply in English. ***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

SystemChatBot = [{"role": "system", "content": System}]

# -------------------------------------------------
# CREATE CHAT HISTORY FILE IF NOT EXISTS
# -------------------------------------------------
if not os.path.exists("./data"):
    os.makedirs("./data")

if not os.path.exists("./data/ChatLot.json"):
    with open("./data/ChatLot.json", "w") as f:
        dump([], f)

# -------------------------------------------------
# REAL-TIME INFORMATION
# -------------------------------------------------
def RealtimeInformation():
    now = datetime.datetime.now()

    return (
        "please use this real-time information if needed,\n"
        f"Day: {now.strftime('%A')}\n"
        f"Date: {now.strftime('%d')}\n"
        f"Month: {now.strftime('%B')}\n"
        f"Year: {now.strftime('%Y')}\n"
        f"Time: {now.strftime('%H')} Hours :{now.strftime('%M')} :{now.strftime('%S')} Second.\n"
    )

# -------------------------------------------------
# CLEAN ANSWER FORMAT
# -------------------------------------------------
def AnswerModifier(text):
    lines = text.split('\n')
    clean = [l for l in lines if l.strip()]
    return "\n".join(clean)

# -------------------------------------------------
# MAIN CHATBOT FUNCTION
# -------------------------------------------------
def ChatBot(Query):

    # Load previous chat
    try:
        with open("./data/ChatLot.json", "r") as f:
            messages = load(f)
    except:
        messages = []

    # Add user message
    messages.append({"role": "user", "content": Query})

    try:
        # Send request
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=(
                SystemChatBot +
                [{"role": "system", "content": RealtimeInformation()}] +
                messages
            ),
            max_tokens=1024,
            stream=True
        )

        Answer = ""

        # Stream output
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s>", "")

        # Save assistant reply to history
        messages.append({"role": "assistant", "content": Answer})
        with open("./data/ChatLot.json", "w") as f:
            dump(messages, f, indent=4)

        return AnswerModifier(Answer)

    except Exception as e:
        print(f"ERROR: {e}")
        return "An error occurred, please try again."

# -------------------------------------------------
# CHAT LOOP
# -------------------------------------------------
if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question: ").strip()

        if user_input.lower() in ["exit", "quit", "stop", "bye"]:
            print(ChatBot("Goodbye"))
            break

        print(ChatBot(user_input))
