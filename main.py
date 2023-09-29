import speech_recognition as sr
import os
import win32com.client
import webbrowser
import pywhatkit as kit
import datetime
import openai
import random

def say(text):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(text)

def ai(prompt):
        openai.api_key = "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"
        text = f"AI response for Prompt:{prompt}\n"
        response = openai.Completion.create(
                model="text-davinci-003",
                # prompt="Write an email to my boss for resignation\n\nSubject: Resignation - [Your Name]\n\nDear [Your Boss's Name],\n\nI am writing to inform you of my resignation from my position at [Company Name]. My last day will be [Date], as per my contract. It has been an honor and a pleasure to work with you and the team at [Company Name].\n\nI am grateful for the opportunity and experience I have gained at [Company Name] and wish the team all the best in 2020.\n\nPlease let me know if there is anything I can do to assist in the transition of my role.\n\nThank you for your support throughout my time with [Company Name].\n\nSincerely,\n[Your Name]",
                prompt = prompt,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
        )
        try:
                print(response["choices"][0]["text"])
                text += response["choices"][0]["text"]
                if not os.path.exists("Openai"):
                        os.mkdir("Openai")
                with open(f"Openai/{''.join(prompt.split('to')[1:]).strip()}", "w") as f:
                        f.write(text)
        except:
                print("Sorry")


chatStr = ""
def chat(query):
        global chatStr
        # print(chatStr)
        openai.api_key = "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"
        chatStr +=f"Me: {query}\n Jarvis:"
        text = f"AI response for Prompt:{query}\n"
        response = openai.Completion.create(
                model="text-davinci-003",
                # prompt="Write an email to my boss for resignation\n\nSubject: Resignation - [Your Name]\n\nDear [Your Boss's Name],\n\nI am writing to inform you of my resignation from my position at [Company Name]. My last day will be [Date], as per my contract. It has been an honor and a pleasure to work with you and the team at [Company Name].\n\nI am grateful for the opportunity and experience I have gained at [Company Name] and wish the team all the best in 2020.\n\nPlease let me know if there is anything I can do to assist in the transition of my role.\n\nThank you for your support throughout my time with [Company Name].\n\nSincerely,\n[Your Name]",
                prompt=chatStr,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
        )
        try:
                say(response["choices"][0]["text"])
                # print(response["choices"][0]["text"])
                chatStr += f"{response['choices'][0]['text']}\n"
                print(chatStr)
                return response["choices"][0]["text"]
                # if not os.path.exists("Openai"):
                #         os.mkdir("Openai")
                # with open(f"Openai/{''.join(query.split('to')[1:]).strip()}", "w") as f:
                #         f.write(text)
        except:
                print("Sorry")

def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                r.pause_threshold = 1
                audio = r.listen(source)
                try:
                        query = r.recognize_google(audio, language="en-in")
                        print(query)
                        return query
                except Exception as e:
                        return "JARVIS cannot get you. Sorry!"


if __name__ == '__main__':
        print("Hello I am JARVIS ")
        say("Hello I am JARVIS")
        hours = int(datetime.datetime.now().strftime("%H"))
        if 4 <= hours < 12:
                say("Good Morning")
                print("Good Morning")
        if 12 <= hours < 18:
                say("Good Afternoon")
                print("Good Afternoon")
        if 18 <= hours < 20:
                say("Good Evening")
                print("Good Evening")
        if 20 <= hours < 24 or 0 <= hours < 4 :
                say("Good Night")
                print("Good Night")

        while True:
                print("Listening...")
                query = takeCommand()
                sites = [["YouTube", "https://www.youtube.com/"],
                         ["Wikipedia", "https://www.wikipedia.org/"],
                         ["Instagram", "https://www.instagram.com/"],
                         ["FaceBook", "https://www.facebook.com/"],
                         ["Google", "https://www.google.com/"]]
                application = [["obs", ""],
                               ["obs", ""],
                               ["obs", ""],
                               ["obs", ""],
                               ["obs", ""],
                               ["obs", ""],
                               ["obs", ""]]

                if "Open".lower() in query.lower():
                        siteUrl = None
                        sitename = None
                        for site in sites:
                                if f"Open {site[0]}".lower() in query.lower():
                                        siteUrl = site[1]
                                        sitename = site[0]

                        webbrowser.open(siteUrl)
                        say(f"Opening {sitename}")
                ytPlayLink = "http://www.youtube.com/results?search_query="
                if "Play".lower() in query.lower():
                        word = query.split()
                        # print(word)
                        for index,i in enumerate(word):
                                ytPlayLink+=i+"+"
                        kit.playonyt(ytPlayLink)

                if "the time".lower() in query.lower():
                        strftime = datetime.datetime.now().strftime("%H:%M:%S")
                        say(f"The time is {strftime}")
                if "use your mind to ".lower() in query.lower():
                        ai(prompt=query)

                if "Jarvis".lower() in query.lower():
                        chat(query)
                # print(query)
                # say(query)


