import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
from tkinter import *
from tkinter import messagebox as msg
from PIL import ImageTk , Image
import requests

def textToHindi(text, filename):
    mytext = str(text)
    launguage = "hi"
    myobj = gTTS(text = mytext, lang = launguage, slow = False)
    myobj.save(filename)

def textToEnglish(text, filename):
    mytext = str(text)
    launguage = "en"
    myobj = gTTS(text = mytext, lang = launguage, slow = False)
    myobj.save(filename)

def mergeHindi(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    
    return combined

def audioFrame():
    """
    HINDI ANNOUNCEMENT PART
    """
    # No_1 Generate Kripya Dhyan Dijiye
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 167000
    finish = 170500
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format = "mp3")
    
    # No_2 gtts upar wale audio ke baad ye audio bolega train_no

    # No_3 gtts train name bolega

    # No_4

    # No_5 Generate ke rastse
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 131300
    finish = 132000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format = "mp3") 
    # No_6 Destination station
    
    # NO_7 ko jane wali
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 132500
    finish = 133500
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format = "mp3") 

    # No_8 Generate apne Nirdharit samay 
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 178600
    finish = 180100
    audioProcessed = audio[start:finish]
    audioProcessed.export("8_hindi.mp3",format = "mp3") 
    # N0_9 Time

    # No_10 Generate par Platform No
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 182900
    finish = 184800
    audioProcessed = audio[start:finish]
    audioProcessed.export("10_hindi.mp3",format = "mp3") 

    # No_11 Platform no from gTTS
    # No_13 Genrerate Se Jyegi
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 185500
    finish = 186500
    audioProcessed = audio[start:finish]
    audioProcessed.export("12_hindi.mp3",format = "mp3") 

    """
    ENGLISH ANNOUNCEMENT PART
    """
    # No_1 Generate May i Have your Attention Please
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 187200
    finish = 191000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3",format = "mp3") 

    # No_4 Generate to
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 195000
    finish = 195700
    audioProcessed = audio[start:finish]
    audioProcessed.export("4_english.mp3",format = "mp3") 

    # No_5 Destination
    # No_6 Genrate via
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 196300
    finish = 196750
    audioProcessed = audio[start:finish]
    audioProcessed.export("6_english.mp3",format = "mp3")

    # No_8 Will Depart at its scheduled time 
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 198700
    finish = 201300
    audioProcessed = audio[start:finish]
    audioProcessed.export("8_english.mp3",format = "mp3")
    
    # No_10 Generate from Platform Number
    audio = AudioSegment.from_mp3("railway.mp3")
    start = 204500
    finish = 206400
    audioProcessed = audio[start:finish]
    audioProcessed.export("10_english.mp3",format = "mp3")


def generateAnnouncement(filename):
    """
    FOR HINDI ANNOUNCEMENT
    """
    df1 = pd.read_excel(filename)
    print(df1)
    for index, item in df1.iterrows():
    # from city
        textToHindi(item['train_no'],'2_hindi.mp3')
    # Via City
        textToHindi(item['train_name'],'3_hindi.mp3')
    # To City 
        textToHindi(item['to'],'6_hindi.mp3')
    # time
        textToHindi(item['time'],'9_hindi.mp3')
    # Platform No
        textToHindi(item['platform'],'11_hindi.mp3')

    """
    FOR ENGLISH ANNOUNCEMENT
    """
    df2 = pd.read_excel(filename)
    for index, item in df2.iterrows():
    # No2_eng Train Number 
        textToEnglish(item['train_no'],'2_english.mp3')
    # No3_eng Train Name 
        textToEnglish(item['train_name'],'3_english.mp3')
    # No5_eng Destination
        textToEnglish(item['to'],'5_english.mp3')
    # No7_eng Via Station
        textToEnglish(item['via'],'7_english.mp3')
    # No8_eng time
        textToEnglish(item['time'],'9_english.mp3')
    # No_11 platform Number
        textToEnglish(item['platform'],'11_english.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,13)]
        eng = [f"{i}_english.mp3"for i in range(1,12)]
        audios.extend(eng)
        announcement = mergeHindi(audios) 
        announcement.export(f"announce_{index+1}.mp3", format = "mp3")


def final():
    print("Generatig Skeleton..")
    audioFrame()
    print("Now Generating Announcement")
    generateAnnouncement("trainhindi.xlsx")
    generateAnnouncement("trainenglish.xlsx")

def sourceCode():
    url = ""
    requests.get(url=url)

if __name__ == "__main__":
    root = Tk()
    root.geometry("500x500")
    root.title("Ｉｎｄｉａｎ Ｒａｉｌｗａｙｓ Ａｎｎｏｕｍｅｎｔ Ｇｅｎｅｒａｔｏｒ")
    Label(root,text = "Indian Railway Announcement Generetor", bg = "grey", fg = "black", padx = 10, pady = 10,relief = SUNKEN,font = "comicsansms 19 bold ").pack(fill = X)
    photo = ImageTk.PhotoImage(Image.open("railway.jfif"))
    Label(root, image = photo).pack()
    Button(root, text = "Generate Announcement", command = final).pack()
    Button(root,text = "Exit", command = quit).pack(side = RIGHT)
    Button(root,text = "SourceCode", command = sourceCode).pack()
    msg.showinfo("Not--A--Professional--Tool", "We strongly recomend not to use this software for professional development because its just a portfolio project ")
    root.mainloop()




