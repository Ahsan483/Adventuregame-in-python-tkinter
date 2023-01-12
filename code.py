from tkinter import *
from functools import partial
from tkinter import messagebox
import random
import time
#global root
ch1 = "pistol"
baglimit = 0
bagi=0;
bag =[]
weapon = ["knife","crossbow","pistol","water","sword"]
pics = ["img1.png","img2.png","img3.png","img4.png","img5.png","img6.png","img7.png","img8.png","img9.png","img10.png","img11.png","img12.png"]
starti = 2
startj = 2
monster = []
matrix = []

qi = random.randint(1,4)
qj = random.randint(1,4)
for i in range(5):          
    a =[]
    b =[]
    for j in range(5):  
        a.append(int(0))
    matrix.append(a)
    monster.append(a)

for i in range(3):
    num = random.randint(1,4)
    monster[i][num] = 1
    num = random.randint(1,4)
    monster[i][num] = 2


def air():
    x = ch1
    print(x)
    if x == "crossbow" or x == "pistol":
        messagebox.showinfo("Congraturlations","\nYou have successfully killed monster move next step to find your queen\n")
        messagebox.showinfo("Infomation", "PLease Move to next Room in order to find Queen\n") 
    else:
        messagebox.showinfo("Oops","\nKnight killed by monster you loose\n")
        exit()


def go():
    check = 0
    print(ch1)
    for i in bag:
        check = 0
        if ch1 == i:
            check = 1
            break
    if check == 1:
        messagebox.showinfo("Congraturlations","\nYou have successfully killed monster move next step to find your queen\n")
        messagebox.showinfo("Infomation", "PLease Move to next Room in order to find Queen\n")    
    else:
        messagebox.showinfo("Oops","\nKnight killed by monster you loose\n")
        exit()

def movedown(root):
    
    img_index = random.randint(1,11)
    root.destroy()
    root = Tk()
    root.geometry("900x700")
    root.title("ADVENTURE GAME")
    left_option = partial(moveleft,root)
    right_option = partial(moveright,root)
    up_option = partial(moveup,root)
    down_option = partial(movedown,root)
    go_option = partial(go)
    air_option = partial(air)    
    bg = PhotoImage(file = pics[img_index])
    img = Label(root,image=bg)
    img.place(x=0,y=0)
    menubar=Menu(root)
    
    menubar.add_command(label="Move Left",activeforeground='red',activebackground="yellow",command=left_option)
    menubar.add_command(label="Move Right",activeforeground='red',activebackground="yellow",command=right_option)
    menubar.add_command(label="Move Up",activeforeground='red',activebackground="yellow",command=up_option)
    menubar.add_command(label="Move Down",activeforeground='red',activebackground="yellow",command=down_option)
    
    # display the menu
    root.config(menu=menubar)
        
    user=StringVar()

    
    global starti
    if starti == 5:
        messagebox.showinfo("showinfo", "No downstair room You can't move downword change your direction !")
    else: 
        messagebox.showinfo("showinfo", "Moving to Downstair Room")
        starti = starti + 1
        messagebox.showinfo("showinfo", "You are in room " + str(startj)  + " at floor " + str(starti))
            
        if startj == qj and starti == qi:
            messagebox.showinfo("showinfo", "Congratulations you Won Your queen is found in this room")
            root.quit()
            exit()
        msg_box = messagebox.askquestion("askquestion", "Do you want to search for items in room : (y/n)?")
        if msg_box == 'yes':
            messagebox.showinfo("showinfo", "Searching Items......!")
            num = random.randint(1,4)
            msg_box2 = messagebox.askquestion("askquestion", "Item found : "+ str(weapon[num])  + "\nDo you want to add in inventory ? ")
            if msg_box2 == 'yes':
                global baglimit
                if baglimit+10 > 30 :
                    messagebox.showinfo("showinfo", "Oops Look like your bag is full!")
                    msg_box3 = messagebox.askquestion("askquestion", "Do you want to remove item from inventory ? ")
            
                    if msg_box3 == 'yes':
                        bag.pop(2)
                        baglimit = baglimit - 10
                        bag.append(weapon[num])
                        messagebox.showinfo("showinfo", "Successfully added in bag " + str(weapon[num]))
                        baglimit = baglimit + 10
                        bag.append(weapon[num])
                        messagebox.showinfo("showinfo","Bag space filled is : " + str(baglimit))
                else:
                    messagebox.showinfo("showinfo", "Successfully added in bag " + str(weapon[num]))
                    baglimit = baglimit + 10
                    bag.append(weapon[num])
                    messagebox.showinfo("showinfo","Bag space filled is : " + str(baglimit))
                    if monster[starti][startj] == 1:
                        messagebox.showinfo("showinfo", "Ground Monster found use inventory item to kill it")
                        choice = Label(root,text = "Select Weapon by name")
                        choice.pack()
                        for i in bag:
                            opt = Label(root,text = i)
                            opt.pack()
                        inp = Label(root,text = "\nWhat you will u use ")
                        inp.pack()
                        ch = Entry(root,textvariable = user, font=('calibre',10,'normal'))
                        ch.pack()
                        ch1 = ch.get()
                        btn = Button(root,text="Attack",command=go)
                        btn.pack()
                        
                    if monster[starti][startj] == 2:
                        messagebox.showinfo("Information","Air Monster found use inventory item to kill it\n")
                        choice = Label(root,text = "Select Weapon by name")
                        choice.pack()
                        for i in bag:
                            opt = Label(root,text = i)
                            opt.pack()
                        inp = Label(root,text = "\nWhat you will u use ")
                        inp.pack()
                        ch = Entry(root,textvariable = user, font=('calibre',10,'normal'))
                        ch.pack()
                        ch1 = ch.get()
                        btn = Button(root,text="Attack",command=air)
                        btn.pack()


def moveup(root):
    
    img_index = random.randint(1,11)
    root.destroy()
    root = Tk()
    root.geometry("900x700")
    root.title("ADVENTURE GAME")
    left_option = partial(moveleft,root)
    right_option = partial(moveright,root)
    up_option = partial(moveup,root)
    down_option = partial(movedown,root)
    go_option = partial(go)
    air_option = partial(air)    
    bg = PhotoImage(file = pics[img_index])
    img = Label(root,image=bg)
    img.place(x=0,y=0)
    menubar=Menu(root)
    
    menubar.add_command(label="Move Left",activeforeground='red',activebackground="yellow",command=left_option)
    menubar.add_command(label="Move Right",activeforeground='red',activebackground="yellow",command=right_option)
    menubar.add_command(label="Move Up",activeforeground='red',activebackground="yellow",command=up_option)
    menubar.add_command(label="Move Down",activeforeground='red',activebackground="yellow",command=down_option)
    
    # display the menu
    root.config(menu=menubar)
        
    user=StringVar()

    
    global starti
    if starti == 0:
        messagebox.showinfo("showinfo", "No upstair room You can't move upword change your direction !")
    else: 
        messagebox.showinfo("showinfo", "Moving to Upstair Room")
        starti = starti - 1
        messagebox.showinfo("showinfo", "You are in room " + str(startj)  + " at floor " + str(starti))
            
        if startj == qj and starti == qi:
            messagebox.showinfo("showinfo", "Congratulations you Won Your queen is found in this room")
            root.quit()
            exit()
       
        msg_box = messagebox.askquestion("askquestion", "Do you want to search for items in room : (y/n)?")
        if msg_box == 'yes':
            messagebox.showinfo("showinfo", "Searching Items......!")
            num = random.randint(1,4)
            msg_box2 = messagebox.askquestion("askquestion", "Item found : "+ str(weapon[num])  + "\nDo you want to add in inventory ? ")
            if msg_box2 == 'yes':
                global baglimit
                if baglimit+10 > 30 :
                    messagebox.showinfo("showinfo", "Oops Look like your bag is full!")
                    msg_box3 = messagebox.askquestion("askquestion", "Do you want to remove item from inventory ? ")
            
                    if msg_box3 == 'yes':
                        bag.pop(2)
                        baglimit = baglimit - 10
                        bag.append(weapon[num])
                        messagebox.showinfo("showinfo", "Successfully added in bag " + str(weapon[num]))
                        baglimit = baglimit + 10
                        bag.append(weapon[num])
                        messagebox.showinfo("showinfo","Bag space filled is : " + str(baglimit))
                else:
                    messagebox.showinfo("showinfo", "Successfully added in bag " + str(weapon[num]))
                    baglimit = baglimit + 10
                    bag.append(weapon[num])
                    messagebox.showinfo("showinfo","Bag space filled is : " + str(baglimit))
                    if monster[starti][startj] == 1:
                        messagebox.showinfo("showinfo", "Ground Monster found use inventory item to kill it")
                        choice = Label(root,text = "Select Weapon by name")
                        choice.pack()
                        for i in bag:
                            opt = Label(root,text = i)
                            opt.pack()
                        inp = Label(root,text = "\nWhat you will u use ")
                        inp.pack()
                        ch = Entry(root,textvariable = user, font=('calibre',10,'normal'))
                        ch.pack()
                        ch1 = ch.get()
                        btn = Button(root,text="Attack",command=go)
                        btn.pack()
                        
                    if monster[starti][startj] == 2:
                        messagebox.showinfo("Information","Air Monster found use inventory item to kill it\n")
                        choice = Label(root,text = "Select Weapon by name")
                        choice.pack()
                        for i in bag:
                            opt = Label(root,text = i)
                            opt.pack()
                        inp = Label(root,text = "\nWhat you will u use ")
                        inp.pack()
                        ch = Entry(root,textvariable = user, font=('calibre',10,'normal'))
                        ch.pack()
                        ch1 = ch.get()
                        btn = Button(root,text="Attack",command=air)
                        btn.pack()



def moveright(root):
    
    img_index = random.randint(1,11)
    root.destroy()
    root = Tk()
    root.geometry("900x700")
    root.title("ADVENTURE GAME")
    left_option = partial(moveleft,root)
    right_option = partial(moveright,root)
    up_option = partial(moveup,root)
    down_option = partial(movedown,root)
    go_option = partial(go)
    air_option = partial(air)    
    bg = PhotoImage(file = pics[img_index])
    img = Label(root,image=bg)
    img.place(x=0,y=0)
    menubar=Menu(root)
    
    menubar.add_command(label="Move Left",activeforeground='red',activebackground="yellow",command=left_option)
    menubar.add_command(label="Move Right",activeforeground='red',activebackground="yellow",command=right_option)
    menubar.add_command(label="Move Up",activeforeground='red',activebackground="yellow",command=up_option)
    menubar.add_command(label="Move Down",activeforeground='red',activebackground="yellow",command=down_option)
    
    # display the menu
    root.config(menu=menubar)
        
    user=StringVar()

    
    global startj
    if startj == 5:
        messagebox.showinfo("showinfo", "No right room You can't move right change your direction !")
    else: 
        messagebox.showinfo("showinfo", "Moving to right Room")
        startj = startj + 1
        messagebox.showinfo("showinfo", "You are in room " + str(startj)  + " at floor " + str(starti))
            
        if startj == qj and starti == qi:
            messagebox.showinfo("showinfo", "Congratulations you Won Your queen is found in this room")
            root.quit()
            exit()
       
        msg_box = messagebox.askquestion("askquestion", "Do you want to search for items in room : (y/n)?")
        if msg_box == 'yes':
            messagebox.showinfo("showinfo", "Searching Items......!")
            num = random.randint(1,4)
            msg_box2 = messagebox.askquestion("askquestion", "Item found : "+ str(weapon[num])  + "\nDo you want to add in inventory ? ")
            if msg_box2 == 'yes':
                global baglimit
                if baglimit+10 > 30 :
                    messagebox.showinfo("showinfo", "Oops Look like your bag is full!")
                    msg_box3 = messagebox.askquestion("askquestion", "Do you want to remove item from inventory ? ")
            
                    if msg_box3 == 'yes':
                        bag.pop(2)
                        baglimit = baglimit - 10
                        bag.append(weapon[num])
                        messagebox.showinfo("showinfo", "Successfully added in bag " + str(weapon[num]))
                        baglimit = baglimit + 10
                        bag.append(weapon[num])
                        messagebox.showinfo("showinfo","Bag space filled is : " + str(baglimit))
                else:
                    messagebox.showinfo("showinfo", "Successfully added in bag " + str(weapon[num]))
                    baglimit = baglimit + 10
                    bag.append(weapon[num])
                    messagebox.showinfo("showinfo","Bag space filled is : " + str(baglimit))
                    if monster[starti][startj] == 1:
                        messagebox.showinfo("showinfo", "Ground Monster found use inventory item to kill it")
                        choice = Label(root,text = "Select Weapon by name")
                        choice.pack()
                        for i in bag:
                            opt = Label(root,text = i)
                            opt.pack()
                        inp = Label(root,text = "\nWhat you will u use ")
                        inp.pack()
                        ch = Entry(root,textvariable = user, font=('calibre',10,'normal'))
                        ch.pack()
                        ch1 = ch.get()
                        btn = Button(root,text="Attack",command=go)
                        btn.pack()
                        
                    if monster[starti][startj] == 2:
                        messagebox.showinfo("Information","Air Monster found use inventory item to kill it\n")
                        choice = Label(root,text = "Select Weapon by name")
                        choice.pack()
                        for i in bag:
                            opt = Label(root,text = i)
                            opt.pack()
                        inp = Label(root,text = "\nWhat you will u use ")
                        inp.pack()
                        ch = Entry(root,textvariable = user, font=('calibre',10,'normal'))
                        ch.pack()
                        ch1 = ch.get()
                        btn = Button(root,text="Attack",command=air)
                        btn.pack()
                        


def moveleft(root):
    
    img_index = random.randint(1,11)
    root.destroy()
    root = Tk()
    root.geometry("900x700")
    root.title("ADVENTURE GAME")
    left_option = partial(moveleft,root)
    right_option = partial(moveright,root)
    up_option = partial(moveup,root)
    down_option = partial(movedown,root)
    go_option = partial(go)
    air_option = partial(air)    
    bg = PhotoImage(file = pics[img_index])
    img = Label(root,image=bg)
    img.place(x=0,y=0)
    menubar=Menu(root)
    
    menubar.add_command(label="Move Left",activeforeground='red',activebackground="yellow",command=left_option)
    menubar.add_command(label="Move Right",activeforeground='red',activebackground="yellow",command=right_option)
    menubar.add_command(label="Move Up",activeforeground='red',activebackground="yellow",command=up_option)
    menubar.add_command(label="Move Down",activeforeground='red',activebackground="yellow",command=down_option)
    
    # display the menu
    root.config(menu=menubar)
        
    user=StringVar()

    
    global startj
    if startj == 0:
        messagebox.showinfo("showinfo", "No left room You can't move left change your direction !")
    else: 
        messagebox.showinfo("showinfo", "Moving to Left Room")
        startj = startj - 1
        messagebox.showinfo("showinfo", "You are in room " + str(startj)  + " at floor " + str(starti))
            
        if startj == qj and starti == qi:
            messagebox.showinfo("showinfo", "Congratulations you Won Your queen is found in this room")
            root.quit()
            exit()
       
        msg_box = messagebox.askquestion("askquestion", "Do you want to search for items in room : (y/n)?")
        if msg_box == 'yes':
            messagebox.showinfo("showinfo", "Searching Items......!")
            num = random.randint(1,4)
            msg_box2 = messagebox.askquestion("askquestion", "Item found : "+ str(weapon[num])  + "\nDo you want to add in inventory ? ")
            if msg_box2 == 'yes':
                global baglimit
                if baglimit+10 > 30 :
                    messagebox.showinfo("showinfo", "Oops Look like your bag is full!")
                    msg_box3 = messagebox.askquestion("askquestion", "Do you want to remove item from inventory ? ")
            
                    if msg_box3 == 'yes':
                        bag.pop(2)
                        baglimit = baglimit - 10
                        bag.append(weapon[num])
                        messagebox.showinfo("showinfo", "Successfully added in bag " + str(weapon[num]))
                        baglimit = baglimit + 10
                        bag.append(weapon[num])
                        messagebox.showinfo("showinfo","Bag space filled is : " + str(baglimit))
                else:
                    messagebox.showinfo("showinfo", "Successfully added in bag " + str(weapon[num]))
                    baglimit = baglimit + 10
                    bag.append(weapon[num])
                    messagebox.showinfo("showinfo","Bag space filled is : " + str(baglimit))
                    if monster[starti][startj] == 1:
                        messagebox.showinfo("showinfo", "Ground Monster found use inventory item to kill it")
                        choice = Label(root,text = "Select Weapon by name")
                        choice.pack()
                        for i in bag:
                            opt = Label(root,text = i)
                            opt.pack()
                        inp = Label(root,text = "\nWhat you will u use ")
                        inp.pack()
                        ch = Entry(root,textvariable = user, font=('calibre',10,'normal'))
                        ch.pack()
                        ch1 = ch.get()
                        btn = Button(root,text="Attack",command=go)
                        btn.pack()
                        
                    if monster[starti][startj] == 2:
                        messagebox.showinfo("Information","Air Monster found use inventory item to kill it\n")
                        choice = Label(root,text = "Select Weapon by name")
                        choice.pack()
                        for i in bag:
                            opt = Label(root,text = i)
                            opt.pack()
                        inp = Label(root,text = "\nWhat you will u use ")
                        inp.pack()
                        ch = Entry(root,textvariable = user, font=('calibre',10,'normal'))
                        ch.pack()
                        ch1 = ch.get()
                        btn = Button(root,text="Attack",command=air)
                        btn.pack()
                        



def play_game(root):
    root.destroy()
    # Create object
    root = Tk()
    
    root.geometry("900x700")
    root.title("ADVENTURE GAME")
    
    # Add image file
    
    left_option = partial(moveleft,root)
    right_option = partial(moveright,root)
    up_option = partial(moveup,root)
    down_option = partial(movedown,root)
    
    
    bg = PhotoImage(file = "img1.png")
    img = Label(root,image=bg)
    img.place(x=0,y=0)
    menubar=Menu(root)
    menubar.add_command(label="Move Left",activeforeground='red',activebackground="yellow",command=left_option)
    menubar.add_command(label="Move Right",activeforeground='red',activebackground="yellow",command=right_option)
    menubar.add_command(label="Move Up",activeforeground='red',activebackground="yellow",command=up_option)
    menubar.add_command(label="Move Down",activeforeground='red',activebackground="yellow",command=down_option)
    # display the menu
    root.config(menu=menubar)
    mainloop()
    
    
def help_game(root):
    root.destroy()
    root = Tk()
    root.geometry("900x700")
    root.config(bg = "skyblue")
    root.title("ADVENTURE GAME")
    back_option = partial(start_menu,root)
    
    # Create text widget and specify size.
    T = Text(root,height=20, foreground="purple",font=("Helvetica", 20),bg="skyblue")
    detail="""\n\nINSTRUCTIONS
    
    1) You can Move your king into rooms
    2) Air or ground monsters can be found in any room
    3) To kill air monster you have to use air weapon
    4) To kill ground monster you have to use ground weapon
    5) If you will use wrong weapon king will get died
    6) In any room there will be queen if you find the exact room you will be winner
    7) In every room you will be able to find some weapons
    8) you can put maximum 3 items in bag pack
    
    GOOD LUCK"""
    T.pack()
    T.insert(END,detail)
    
    # back button
    back_button = Button(root,text="BACK",activeforeground='red',activebackground="yellow",command=back_option, bg="red",fg="yellow",width=10,font=('summer',20),bd=15)
    back_button.pack()
    
def start_menu(root):
    root.destroy()
    root = Tk()
    root.geometry("900x700")
    root.config(bg = "skyblue")
    root.title("ADVENTURE GAME")
    
    l = Label(text = "\nADVENTURE GAME\n" , borderwidth = "10",bg="skyblue", foreground = "black" ,justify="center",font=("Helvetica", 50))
    l.pack()
    help_option = partial(help_game,root)
    play_option = partial(play_game,root)
    
    # play button
    
    play_button = Button(root,text="PLAY",activeforeground='red',activebackground="yellow",command=play_option,  bg="red",fg="yellow",width=10,font=('summer',20),bd=15)
    play_button.pack()
    
    
    # help button
    help_button = Button(root,text="HELP",activeforeground='red',activebackground="yellow",command=help_option, bg="red",fg="yellow",width=10,font=('summer',20),bd=15)
    help_button.pack()

    # exit button
    exit_button = Button(root,text="EXIT", command = root.quit ,activeforeground='red',activebackground="yellow", bg="red",fg="yellow",width=10,font=('summer',20),bd=15)
    
    exit_button.pack()
    
    

def main():
    start_menu(Tk())
    mainloop()

if __name__ == "__main__":
    main()


