import tkinter as tk
import os
import fnmatch
from pygame import mixer

canvas = tk.Tk()
canvas.title("My playlist")
canvas.geometry("550x550")
canvas.config(bg='beige')

rootpath = "C:\\Users\\diall\\Music\\my music"
pattern = "*.mp3"

mixer.init()

prec_img = tk.PhotoImage(file="music-prec-button_1.png")
stop_img = tk.PhotoImage(file="music-stop-button_1.png")
play_img = tk.PhotoImage(file="music-play-button_1.png")
pause_img = tk.PhotoImage(file="music-pause-button_1.png")
suiv_img = tk.PhotoImage(file="music-suiv-button_1.png")

def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear(0, 'end')

def suiv():
    suiv_song = listbox.curselection()
    suiv_song = suiv_song[0] + 1
    suiv_song_name = listbox.get(suiv_song)
    label.config(text=suiv_song_name)
    mixer.music.load(rootpath + "\\" + suiv_song_name)
    mixer.music.play()
    listbox.select_clear(0, 'end')
    listbox.activate(suiv_song)
    listbox.select_set(suiv_song)

def prec():
    prec_song = listbox.curselection()
    prec_song = prec_song[0] - 1
    prec_song_name = listbox.get(prec_song)
    label.config(text=prec_song_name)
    mixer.music.load(rootpath + "\\" + prec_song_name)
    mixer.music.play()
    listbox.select_clear(0, 'end')
    listbox.activate(prec_song)
    listbox.select_set(prec_song)


def pause():
	if pauseButton["text"]== "pause":
		 mixer.music.pause()
		 pauseButton["text"]= "play"

	else:
		mixer.music.unpause()
		pauseButton["text"]= "pause"



listbox = tk.Listbox(canvas, fg="black", bg="cyan", width=100, font=('poppin', 14))
listbox.pack(padx=20, pady=20)

label = tk.Label(canvas, text="", bg='white', fg='black', font=('poppin', 19))
label.pack(pady=14)

top = tk.Frame(canvas, bg='black')
top.pack(padx=16, pady=6, anchor='center')

precButton = tk.Button(canvas, text='prec', image=prec_img, bg='cyan', width=250, height=250, command=prec)
precButton.pack(pady=15, in_=top, side="left")
stopButton = tk.Button(canvas, text='stop', image=stop_img, bg='cyan', width=250, height=250, command=stop)
stopButton.pack(pady=15, in_=top, side="left")
playButton = tk.Button(canvas, text='play', image=play_img, bg='cyan', width=250, height=250, command=select)
playButton.pack(pady=15, in_=top, side="left")
pauseButton = tk.Button(canvas, text='pause', image=pause_img, bg='cyan', width=250, height=250, command=pause)
pauseButton.pack(pady=15, in_=top, side="left")
suivButton = tk.Button(canvas, text='suiv', image=suiv_img, bg='cyan', width=250, height=250, command=suiv)
suivButton.pack(pady=15, in_=top, side="left")

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert('end', filename)

canvas.mainloop()
