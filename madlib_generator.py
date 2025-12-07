from tkinter import *
screen =Tk()
screen.geometry("430x430")
screen.config(bg='purple')
screen.title("Story Maker")
Label(screen,text="CHOOSE YOUR FAV GENRE",fg='black').place(x=130,y=20)
def clicked():
     Label(text="BY:PREETHA CATHERIN",fg='black').place(x=200,y=350)
btn=Button(screen,text="CLICK ME",fg='red',command=clicked).place(x=350,y=350)
     
Storybutton1=Button(screen,text='FANTASY💕',bg='pink',fg='black',command=lambda: story1(screen)).place(x=170,y=100)
Storybutton2=Button(screen,text='CRIME🌃',bg='black',fg='white',command=lambda: story2(screen)).place(x=170,y=150)
Storybutton3=Button(screen,text='SCI-FI👽',bg='blue',fg='white',command=lambda: story3(screen)).place(x=170,y=200)
screen.update()
screen.mainloop()
