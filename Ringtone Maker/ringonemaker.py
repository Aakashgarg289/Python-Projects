import os
import random
from pydub import AudioSegment
from gtts import gTTS

# def textToSpeech(text, filename):
#     mytext = str(text)
#     language = 'hi'
#     myobj = gTTS(text=mytext, lang=language, slow=False)
#     myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3("Yaar.mp3")
    start = 1000
    finish = 10000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3.mp3", format="mp3")

def generateAnnouncement():
    audios = ["1.mp3", "3.mp3"]
        # audios = [f"{i}.mp3" for i in range(2, 4)]
    announcement = mergeAudios(audios)
    announcement.export(f"ringtone1.mp3", format="mp3")

if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement()