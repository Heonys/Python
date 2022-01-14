from tkinter import*

root = Tk()
root.title("My GUI")
root.geometry("640x480") # 가로 x 세로 

chkbar = IntVar() #chkbar에 int형으로 값을 저장한다
chkbox = Checkbutton(root, text="체크박스", variable=chkbar)
chkbox.pack()

chkbar2 = IntVar() #chkbar에 int형으로 값을 저장한다
chkbox2 = Checkbutton(root, text="체크박스2", variable=chkbar2)
chkbox2.pack()

def btncmd():
    print(chkbar.get()) # 0: 체크해제,  1: 체크 
    print(chkbar2.get())
    


btn = Button(root ,text="클릭", command=btncmd)
btn.pack()

root.mainloop()

