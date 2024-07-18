from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
  try:
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension="mp4")
    highest_res_streams = streams.get_highest_resolution()
    highest_res_streams.download(output_path=save_path)
    print("Video download succesfully!")
  except Exception as e:
    print(e)
    
def open_file_dialog():
  folder = filedialog.askdirectory()
  if folder:
    print(f"selected folder: {folder}")
return folder


if __name__ == "__main__":
root = tk.TK()
root.withdraw()

video_url = input("please enter a Youtube url: ")

save_dir = open_file_dialog()

if  save_dir:
  download_video(video_url, save_dir)
else:
  print("Invalid save location.")