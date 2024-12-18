import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video(quality):
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "!Please enter your video")
        return
   
    try:
        yt = YouTube(url)
        if quality == "high":
            stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        elif quality == "low":
            stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").asc().first()
        elif quality == "audio":
            stream = yt.streams.filter(only_audio=True).first()
        else:
            messagebox.showerror("Error", "Incorrect choice")
            return
       
        stream.download()
        messagebox.showinfo("success", f"the video has been unploaded in high quality     {quality}!")
    except Exception as e:
        messagebox.showerror("error", f"Ab error occurred : {str(e)}")

root = tk.Tk()
root.title("Youtube Downloader")
root.geometry("500x400")
root.configure(bg="#F9BBFF")  
url_label = tk.Label(root, text=" Enter the video link :", bg="#CF8AB5", font=("Arial", 12))
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=10)
button_frame = tk.Frame(root, bg="#CF8AB5")
button_frame.pack(pady=20)
button_high = tk.Button(button_frame, text="High resolution ", command=lambda: download_video("high"),bg="#FFFAB1" ,font=("Arial", 10), width=14, height=2)
button_high.grid(row=0, column=0, padx=10, pady=10)
button_low = tk.Button(button_frame, text=" Low resolution ", command=lambda: download_video("low"),bg="#FFFAB1", font=("Arial", 10), width=14, height=2)
button_low.grid(row=0, column=1, padx=10, pady=10)
button_audio = tk.Button(button_frame, text="Audio only ", command=lambda: download_video("audio"), bg="#FFFAB1" ,font=("Arial", 10), width=14, height=2)
button_audio.grid(row=0, column=2, padx=10, pady=10)
root.mainloop()