from tkinter import*

root = Tk()
root.title("My GUI")
root.geometry("640x480") # 가로 x 세로 
# root.geometry("640x480+100+300") # 가로 x 세로 + x좌표 + y좌표

root.resizable(False,False) # (너비, 높이)의 값(=창) 크기 변경 불가 


root.mainloop()

