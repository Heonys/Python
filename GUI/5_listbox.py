from tkinter import*

root = Tk()
root.title("My GUI")
root.geometry("640x480") # 가로 x 세로 

listbox = Listbox(root,selectmode="extended", height=0)
listbox.insert(END, '사과')
listbox.insert(END, '딸기')
listbox.insert(END, '바나나')
listbox.insert(END, '수박')
listbox.insert(END, '포도')
listbox.pack()

def btncmd():
    #삭제 
    #listbox.delete(END) #맨뒤에 값 삭제
    
    #개수 확인
    # print("listbox의 사이즈는", listbox.size())

    #항목확인
    print("선택된 항목: ",listbox.curselection())


btn = Button(root ,text="클릭", command=btncmd)
btn.pack()

root.mainloop()

