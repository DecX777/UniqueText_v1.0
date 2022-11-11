from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage, END
from googletrans import Translator
import clipboard


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = (r"assets/frame0")

lngs = ['zh-tw','ja','en'] # Intermediate languages
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def translate(lngs):
    text = entry_2.get(1.0, END)
    translator = Translator()
    for lang in lngs:
        text = translator.translate(text, dest=str(lang)).text
    text = translator.translate(text, dest='ru').text          # Target language
    entry_1.delete(1.0, END)
    entry_1.insert(1.0, text)

def delete_text():
    entry_1.delete(1.0, END)
    entry_2.delete(1.0, END)

def copytext():
    text = entry_1.get(1.0, END)
    clipboard.copy(text)
    

window = Tk()
window.title('UniqueTextPython v1.0')
window.geometry("1128x780")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 780,
    width = 1128,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    564.0,
    390.0,
    image=image_image_1
)

canvas.create_text(
    86.0,
    13.0,
    anchor="nw",
    text="UniqueTextPython",
    fill="#000000",
    font=("Inter SemiBold", 32 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: translate(lngs),
    relief="flat"
)
button_1.place(
    x=1027.0,
    y=225.0,
    width=73.0,
    height=31.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copytext(),
    relief="flat"
)
button_2.place(
    x=1039.0,
    y=182.0,
    width=60.0,
    height=30.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: delete_text(),
    relief="flat"
)
button_3.place(
    x=1039.0,
    y=144.0,
    width=60.0,
    height=30.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    796.0,
    420.5,
    image=entry_image_1
)
entry_1 = Text(
    font=('Arial 16'),
    bd=0,
    bg="#EDEDED",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=567.0,
    y=86.0,
    width=458.0,
    height=667.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    259.5,
    420.5,
    image=entry_image_2
)
entry_2 = Text(
    font=('Arial 16'),
    bd=0,
    bg="#EDEDED",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=30.0,
    y=86.0,
    width=459.0,
    height=667.0
)
window.resizable(False, False)
window.mainloop()
