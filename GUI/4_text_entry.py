from tkinter import*

root = Tk()
root.title("My GUI")
root.geometry("640x480") # 가로 x 세로 

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e= Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력")

def btncmd():
    #내용 출력
    print(txt.get("1.0", END)) # 1> 라인1의 0번째 부터
    print(e.get())
    # 내용삭제
    txt.delete("1.0", END)
    e.delete(0,END) 
    

btn = Button(root ,text="클릭", command=btncmd)
btn.pack()

root.mainloop()

