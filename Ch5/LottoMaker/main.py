import tkinter
from tkinter import *
import random

lotto_num = range(1, 46)
index = 0
def buttonClick():
    global index
    index += 1
    listbox.insert(index, f"{index}회: {','.join(map(str,random.sample(lotto_num, 6)))}")


window = tkinter.Tk()
window.title("로또")
window.geometry("400x200+800+300") # 800, 300은 초기 위치
window.resizable(False, False)

button = tkinter.Button(window, overrelief="solid", text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

bar = Frame(window, padx=20, pady=20)
bar.pack()

scrollbar = Scrollbar(bar, orient="vertical")
scrollbar.pack(side="right", fill="y")

listbox = tkinter.Listbox(bar, selectmode='extended', yscrollcommand=scrollbar.set)
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)

window.mainloop()