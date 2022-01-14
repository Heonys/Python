from cgitb import text
from email.mime import image
from tkinter import*

root = Tk()
root.title("My GUI")
root.geometry("640x480") # 가로 x 세로 

# 레이블 >> 글자나 이미지만 단순히 보여주는 용도
label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="GUI/img.png")
label2 = Label(root, image=photo )
label2.pack()

def change():
    label1.config(text="또만나요")
    global photo2
    photo2 = PhotoImage(file="GUI/img2.png")
    label2.config(image=photo2)

    
btn1 = Button(root, text="버튼", command=change)
btn1.pack()


root.mainloop()
