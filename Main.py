import whisper
from pytube import YouTube
import os
import ctypes

def create_and_open_txt(text, filename):
    # create and write the text to a .txt file
    with open(filename, "w") as file:
        file.write(text)
    os.startfile(filename)

url = input("Enter the YouTube video URL: ")

yt = YouTube(url)
audio_stream = yt.streams.filter(only_audio=True).first()

output_path = "Youtubeaudios"
filename = "audio.mp3"
audio_stream.download(output_path=output_path, filename=filename)

print(f"Audio downloaded to {output_path}/{filename}")

try:
    model = whisper.load_model("base")
    if model is not None:
        result = model.transcribe(os.path.join(output_path, filename))
        print(result["text"])

        create_and_open_txt(result["text"], 'output.txt')
    else:
        print("Error: Model loading failed.")
except Exception as e:
    print(f"An error occurred: {e}")
