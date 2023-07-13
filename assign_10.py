from tkinter import *
import webbrowser as wb

def navigate():
    site = entry.get()
    print("Navigating to", site)
    wb.open(site)

window = Tk()
window.title("Website Navigation")

label = Label(window, text="Enter Website URL:")
label.grid()
entry = Entry(window)
entry.grid()

button = Button(window, text="Open", command=navigate)
button.grid()
window.mainloop()