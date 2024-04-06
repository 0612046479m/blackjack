import os
from tkinter import *
from cards import *
from player import *


txtColor = "#353535"
hoverColor = "#bdbbb0"
baseColor = "#8a897c"
background = "#91ADC2"

root = Tk()
root.title("Jackle Jack")
root.configure(background=background)
root.geometry("800x800")

def onHover(e):
    e.widget["background"] = hoverColor
    e.widget["foreground"] = txtColor


def offHover(e):
    e.widget["background"] = hoverColor
    e.widget["foreground"] = txtColor


uninstallProgram = Button(
    root,
    text="Uninstall Programs",
    background=background,
    foreground=txtColor,
    activebackground=hoverColor,
    activeforeground=txtColor,
    border=0,
    highlightthickness=2,
    cursor="hand2",
)

root.mainloop() 