import tkinter
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from tkinter import font
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600)
canvas.grid(columnspan=3, rowspan=4)

root.title("PDF Text Reader")
#root.iconphoto()

# logo
logo = Image.open('imgserver.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text="Select a PDF file on your computer \n to extract its text", font="Courier")
instructions.grid(columnspan=3, column=0, row=1)

#function to work when button is clicked
def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title = "Choose a file", filetype = [("PDF file","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        #text_box
        text_box = tk.Text(root, height = 10, width=50, padx = 15, pady = 15, font="Courier")
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify = "center")
        text_box.tag_add("center",1.0,"end")
        text_box.grid(column=1, row=4)

        browse_text.set("Browse")
# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text,command = lambda:open_file(),font="Rockwell", bg="#E54320", fg = "white", height=1, width=10)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)
canvas = tk.Canvas(root, width=600, height=150)
canvas.grid(columnspan=3)
root.mainloop()
