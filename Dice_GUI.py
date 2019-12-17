#Sorry about it not scaling well, was originally made on a school 17" panel

import tkinter
import random
import sqlite3
running_score = 0
new_window = tkinter.Tk()
new_window.configure(background="darkcyan")
new_window.title("Login-screen")
new_window.geometry("1080x1280")
new_window.wm_iconbitmap("Dice.ico")

#Setting up SQL
connect = sqlite3.connect('dice_game.db')
c = connect.cursor()

#Create a new login
def create():
    if username_entry.get() == "" or password_entry.get() =="":
        help_display.configure(text="  No Username or   \n   Password entered    ")
    else:
        c.execute("INSERT INTO logins VALUES(?,?)",(username_entry.get(),password_entry.get()))
        connect.commit()
        help_display.configure(text="   New login added!   ")
        
# Login Interface
def onclick():
    if username_entry.get() == "" or password_entry.get() =="":
        help_display.configure(text="  No Username or   \n   Password entered    ")
    c.execute("SELECT COUNT(Username)FROM logins")
    loop_count = c.fetchall()
    loop_count = loop_count[0][0]
    c.execute("SELECT * FROM logins")
    data = c.fetchall()
    for x in range(loop_count):
        if username_entry.get() == data[x][0] and password_entry.get() == data[x][1]:
            
            #Creation of game interface
            global window_2
            global intro_label
            window_2 = tkinter.Toplevel()
            window_2.wm_iconbitmap("Dice.ico")
            window_2.title("Dice game")
            window_2.geometry('1080x1280')
            window_2.configure(bg="ivory")
            intro_label = tkinter.Label(window_2, text="Press the button to play.",fg="white", bg="darkcyan",width = 20,relief="sunken")
            new_button = tkinter.Button(window_2, text="Roll Dice", bg="darkcyan",command=second_click,fg="white",width = 20)    
            # Packed text
            new_window.wm_state('iconic')
            new_window.iconify()
            new_button.place(x=449,y=170)
            intro_label.place(x=450,y=150)
            window_2.mainloop()
    else:
        help_display.configure(text=" Inputs are incorrect! ")
    

# dice roll
def second_click():
    global running_score
    global score_counter
    if running_score == 0:
        score_counter = tkinter.Label(window_2,bg="darkcyan", fg="white",text="Score:",relief="sunken",width = 20)
        score_counter.place(x=449,y=130)
        update()
    else:
        update()

def update():
    global running_score        
    dice_score1 = random.randint(1, 6)
    dice_score2 = random.randint(1, 6)
    d_total = dice_score1 + dice_score2
    image_display = tkinter.Label(window_2)
    image_display.place(x=550,y=204)
    image_display2 = tkinter.Label(window_2)
    image_display2.place(x=300,y=200)
    running_score += d_total
    if d_total == 2:
        intro_label.configure(text="That's awful you rolled " + str(d_total))
    elif d_total >= 3 and d_total <= 5:
        intro_label.configure(text="Unlucky you rolled " + str(d_total))
    elif d_total >= 6 and d_total <= 9:
        intro_label.configure(text="Well done you rolled " + str(d_total))
    else:
        intro_label.configure(text="Amazing you rolled " + str(d_total))
    score_counter.configure(text="The total score is now: "+str(running_score))
    # Dice Image Code
    for x in range(1,7):
        if dice_score1 == x:
            image_display.configure(image = image_list[x])
    for x in range(1,7):
        if dice_score2 == x:
            image_display2.configure(image = image_list[x])
python_banner = tkinter.PhotoImage(file="banner_2.gif")   
d_image1 = tkinter.PhotoImage(file="one_side.gif")
d_image2 = tkinter.PhotoImage(file="two_side.gif")
d_image3 = tkinter.PhotoImage(file="three_side.gif")
d_image4 = tkinter.PhotoImage(file="four_side.gif")
d_image5 = tkinter.PhotoImage(file="five_side.gif")
d_image6 = tkinter.PhotoImage(file="six_side.gif")

image_list = ["place_holder",d_image1,d_image2,d_image3,d_image4,d_image5,d_image6]    
    
#Packed text

python_display = tkinter.Label(new_window,image=python_banner)
large_label = tkinter.Label(new_window,text="",relief="sunken",width=50,height=20,bg="darkcyan")
username_entry = tkinter.Entry(new_window)
u_label = tkinter.Label(new_window, text="Enter your username", bg="darkcyan",relief="groove",width=17)
password_entry = tkinter.Entry(new_window)
p_label = tkinter.Label(new_window, text="Enter your password", bg="darkcyan",relief="groove",width=17)
login = tkinter.Button(new_window, text="Login",fg="darkcyan", bg="black",command=onclick,width=7)
create = tkinter.Button(new_window, text="Create",fg="darkcyan", bg="black",command=create,width=7)
help_display = tkinter.Label(new_window, text="Default login is set to \n admin and password",fg="darkcyan", bg="black",pady=4,padx=4)

large_label.place(x=330,y=150)
u_label.place(x=450,y=250)
username_entry.place(x=450,y=270)
p_label.place(x=450,y=290)
password_entry.place(x=450,y=310)
login.place(x=450,y=335)
create.place(x=518,y=335)
help_display.place(x=453,y=375)
python_display.place(x=362,y=480)

new_window.mainloop()
