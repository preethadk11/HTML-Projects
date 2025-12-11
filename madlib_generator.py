def story1(win):
     def final(t1:Toplevel, Hero,Villian,Location,Power,Food):
               text = f'''
           Once upon a time in a land called {Location}, there lived a hero named {Hero}.
           {Hero} possessed the incredible power of {Power}, which made them a formidable force against evil.
           One day, a notorious villian named {Villian} threatened the peace of {Location}.
           With courage and determination, {Hero} confronted {Villian} and defeated them using their power.
           To celebrate the victory, the people of {Location} feasted on delicious {Food}.
           And so, peace was restored, and {Hero} became a legend in the land.'''
               t1.geometry('450x450')
               Label(t1,text='Story:',wraplength=t1.winfo_width()).place(x=155,y=230)
               Label(t1,text=text,wraplength=t1.winfo_width()).place(x=0,y=250)
               def clicked():
                     Label(t1,text="Hope you liked this story😊",fg='black',bg='pink').place(x=200,y=400)
               Button(t1,text='Click Here',fg='red',command=clicked).place(x=360,y=400)
               def comment():
                     Label(t1,text="Comment your thoughts here",fg='black').place(x=360,y=420)
               entrybox=Entry(t1,width=30,command=comment).place(x=360,y=420)
     Newscreen=Toplevel(win,bg='lightblue')
     Newscreen.geometry('450x450')
     Label(Newscreen,text='FANTASY STORY').place(x=150,y=0)
     Label(Newscreen,text='Enter the Hero name: ').place(x=0,y=30)
     Label(Newscreen,text='Enter the villian name: ').place(x=0,y=60)
     Label(Newscreen,text='Location: ').place(x=0,y=90)
     Label(Newscreen,text='Power: ').place(x=0,y=120)
     Label(Newscreen,text='Food: ').place(x=0,y=150)
     Hero=Entry(Newscreen,width=20)
     Hero.place(x=150,y=30)
     Villian=Entry(Newscreen,width=20)
     Villian.place(x=150,y=60)
     Location=Entry(Newscreen,width=20)
     Location.place(x=150,y=90)
     Power=Entry(Newscreen,width=20)
     Power.place(x=150,y=120)
     Food=Entry(Newscreen,width=20)
     Food.place(x=150,y=150)
     SubmitButton=Button(Newscreen,text='Submit',fg='pink',bg='blue',command=lambda:final(Newscreen,Hero.get(),Villian.get(),Location.get(),Power.get(),Food.get()))
     SubmitButton.place(x=150,y=200)
def story2(win):
      def final(t2:Toplevel,Name,Friend,Location,Twists,Weapon):
            text='''
                  #to be written
'''
            t2.geomentry("450x450")
            Label(t2,text="Story",fg='White',wraplength=t2.winfo_width()).place(x=,y=)
            Label(t2,text=text,wraplength=t2.winfo_width()).place(x=,y=)
      Newscreen=Toplevel(win,bg="black")
      Newscreen.geomentry("450x450")
      Label(Newscreen,text="Crime Story").place(x=,y=)
      Label(Newscreen,text="Name").place(x=,y=)
      Label(Newscreen,text="Friend Name").place(x=,y=)
      Label(Newscreen,text="Location").place(x=,y=)
      Label(Newscreen,text="Twists").place(x=,y=)
      Label(Newscreen,text="Weapon").place(x=,y=)
      Name=Entry(Newscreen,width=20)
      Name.place(x=,y=)
      Friend=Entry(Newscreen,width=20)
      Friend.place(x=,y=)
      Location=Entry(Newscreen,width=20)
      Location.place(x=,y=)
      Twists=Entry(Newscreen,width=20)
      Twists.place(x=,y=)
      Weapon=Entry(Newscreen,width=20)
      Weapon.place(x=,y=)
      SubmitButton=Button(Newscreen,text="Submit",fg="Yellow",bg="white",command=lambda:final(Newscreen,Name.get(),Friend.get(),Location.get(),Twists.get(),Weapon.get()))
      SubmitButton.place(x=y=)

     
     
     
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

