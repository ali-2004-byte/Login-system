from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title("Login")
root.geometry('1920x1000+0+0')
root.configure(bg = '#38b6ff')
root.resizable(True,True)

def signin():
    username = user.get()
    password = pas.get()

    file = open('datasheet.txt', 'r')
    d = file.read()
    r=ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('1920x1000+0+0')
        screen.config(bg='#38b6ff')
        img = PhotoImage(file = 'pep.png')
        Label(screen, text='Hello Master!', image = img, bg='#38b6ff', fg = 'yellow', font=('Calibri(Body)', 50, 'bold'),compound='right', pady=100).pack(expand=True)

        screen.mainloop()

    else:
        messagebox.showerror("Invalid", "Invalid username or password")
    
########################################################################################
def signup_command():
    window=Toplevel(root)
    window.title("Sign up")
    window.geometry('925x500+300+200')
    window.configure(bg = '#38b6ff')
    window.resizable(True, True)

    def signup():
        username = user2.get()
        password = pas2.get()
        confirm = conf.get()

        if password == confirm:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r=ast.literal_eval(d)
                dict2 = {username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt', 'w')
                w = file.write(str(r))
                messagebox.showinfo('Signup','Successfully signed up')
                file = open('datasheet.txt', 'r+')
                window.destroy()
            except:
                file=open('datasheet.txt','w')
                pp = str({'Username':'Password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid', 'Both passwords should match')

    def sign():
        window.destroy()
    
    img = PhotoImage(file = 'sin.png')
    Label(window, image = img, bg = '#38b6ff').place(x=50,y=90) 
    frame2 = Frame(window, width=350, height=390, bg='#38b6ff')
    frame2.place(x=480, y=50)

    heading2 = Label(frame2, text='Sign Up', fg='white', bg='#38b6ff', font=('Baskerville',23,'bold'))
    heading2.place(x=100,y=5)

    def on_enter(e):
        user2.delete(0,"end")
    def on_leave(e):
        name=user2.get()
        if name=='':
            user2.insert(0,'Username')

    user2 =Entry(frame2, width=25, fg='white', border=0, bg='#38b6ff',font=('Baskerville',11))
    user2.place(x=30,y=80)
    user2.insert(0,'Username')
    user2.bind('<FocusIn>',on_enter)
    user2.bind('<FocusOut>',on_leave)

    Frame(frame2,width=295,height=2,bg='white').place(x=25,y=107)

    def on_enter(e):
        pas2.delete(0,"end")
    def on_leave(e):
        name=pas2.get()
        if name=='':
            pas2.insert(0,'Password')
    pas2 =Entry(frame2, width=25, fg='white', border=0, bg='#38b6ff',font=('Baskerville',11))
    pas2.place(x=30,y=130)
    pas2.insert(0,'Password')
    pas2.bind('<FocusIn>',on_enter)
    pas2.bind('<FocusOut>',on_leave)  

    Frame(frame2,width=295,height=2,bg='white').place(x=25,y=157)

    def on_enter(e):
        conf.delete(0,"end")
    def on_leave(e):
        name = conf.get()
        if name =='':
            conf.insert(0,'Confirm Password')
    conf=Entry(frame2, width=25,fg='white',border=0,bg='#38b6ff', font=('Baskerville',11))
    conf.place(x=30,y=180)
    conf.insert(0,'Confirm Password')
    conf.bind('<FocusIn>',on_enter)
    conf.bind('<FocusOut>',on_leave)  
    Frame(frame2,width=295,height=2,bg='white').place(x=25,y=207)

    Button(frame2, width=39,pady=7,text='Sign Up', bg='white',fg='#38b6ff',border=0, command=signup ).place(x=35,y=280)
    label2=Label(frame2, text="I have an account?", fg='white',bg='#38b6ff',font=('Baskerville',9))
    label2.place(x=90,y=340)

    signin=Button(frame2, width=6,text='Sign in', border=0, bg='#38b6ff',cursor='hand2', fg='black', command=sign)
    signin.place(x=200,y=340)
    window.mainloop()

#######################################################################################
img = PhotoImage(file = 'log.png')
Label(root, image = img, bg = 'white').place(x=0,y=0)

frame = Frame(root, width=450, height=700, bg='#38b6ff')
frame.place(x=1400, y=200)

heading = Label(frame, text='Sign in', fg='white', bg='#38b6ff', font=('Baskerville',75,'bold'))
heading.place(x=50,y=5)
def on_enter(e):
    user.delete(0,"end")
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user =Entry(frame, width=25, fg='white', border=0, bg='#38b6ff',font=('Baskerville',25))
user.place(x=30,y=250)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=195,height=2,bg='white').place(x=25,y=290)

def on_enter(e):
    pas.delete(0,"end")
def on_leave(e):
    name=pas.get()
    if name=='':
        pas.insert(0,'Password')
pas =Entry(frame, width=25, fg='white', border=0, bg='#38b6ff',font=('Baskerville',25))
pas.place(x=30,y=300)
pas.insert(0,'Password')
pas.bind('<FocusIn>',on_enter)
pas.bind('<FocusOut>',on_leave)  

Frame(frame,width=195,height=2,bg='white').place(x=25,y=340)

Button(frame, width=30,pady=7,text='Sign in', bg='white',fg='#38b6ff',border=0, font=('Baskerville',15), command=signin).place(x=50,y=400)
label=Label(frame, text="Don't have an account?", fg='white',bg='#38b6ff',font=('Baskerville',10))
label.place(x=90,y=450)

sign_up=Button(frame, width=6,text='Sign up', border=0, bg='#38b6ff',cursor='hand2', fg='black', command=signup_command)
sign_up.place(x=235,y=450)
root.mainloop()