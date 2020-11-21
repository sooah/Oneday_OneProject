import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width=-300, height=250, bg='azure3', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_widnow(150, 60, window=label1)

def getPNG():
    global im1
    
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browseButton_PNG = tk.Button(text="    Import PNG File    ", bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.creat_window(150, 100, window=saveAsButton_JPG)

root.mainloop()
