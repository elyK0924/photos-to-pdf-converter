## PhotosToPDF.py
## Kyle Viti
## Select photos from your computer one-by-one to merge and convert into a PDF file!
## Inspiration and idea from https://datatofish.com/images-to-pdf-python/

from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightgreen', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightgreen')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

images = list()

def getFile ():
    global im1
    
    import_file_path = filedialog.askopenfilename()
    image1 = Image.open(import_file_path)
    im1 = image1.convert('RGB')
    images.append(im1)
    print(images)
    MsgBox = tk.messagebox.showinfo('Success', f"File imported successfully from\n{import_file_path}")

browseButton = tk.Button(text="     Select File     ", command=getFile, bg='lightgreen', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton)

def convertToPdf ():
    global im1
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    if(len(images) == 1):
        im1.save(export_file_path)
    else:
        first_image = images[0]
        first_image.save(export_file_path, save_all = True, append_images=images[1:])
    MsgBox = tk.messagebox.showinfo('Success', f'File converted to PDF successfully to:\n{export_file_path}')

saveAsButton = tk.Button(text='Convert to PDF', command=convertToPdf, bg='lightgreen', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit','Are you sure you want to exit the application?',icon = 'warning')
    if MsgBox == 'yes':
        root.destroy()
     
exitButton = tk.Button (root, text='Exit Application',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()
