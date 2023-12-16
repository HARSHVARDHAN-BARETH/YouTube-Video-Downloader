from tkinter import *
from pytube import YouTube
root = Tk()

root.geometry("500x300")
root.title("Youtube Downloader")

root.config(bg="#f0f8ff")

def getvid():
    linx = YtLink.get()
    video = YouTube(linx)
    strm = video.streams.get_highest_resolution()
    strm.download("C:\\Users\\HARSHVARDHAN\\Desktop\\python")

mylab = Label(root, text="Enter your video link", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#1e90ff", pady=20)
mylab.pack(pady=10)

YtLink = Entry(root, width=40)
YtLink.pack(pady=40, ipady=10)  

clickBtn = Button(root, text="Download", command=getvid, pady=10, padx=10)
clickBtn.pack()

root.mainloop()