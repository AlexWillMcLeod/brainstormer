from tkinter import*
from tkinter import filedialog
import os

green_pastel = '#CFFFB8'
red_pastel = '#FF9A9C'
orange_pastel = '#F7D9B1'
light_green_pastel = '#E4FFD6'
blue_pastel = '#B8E7FF'
yellow_pastel = '#FCF7DE'
brown_pastel = '#CFAF91'
pink_pastel = '#E8A8BE'
dark_grey_pastel = 'gray19'
light_grey_pastel = 'gray81'
purple_pastel = "#B7B7DE"
white_pastel = "gray87"
grey_pastel = "gray60"



def create_title_screen():
    
    global new_button
    global open_button
    global del_button
    global title_label
    global fullscreen_button
    global exit_button
    global help_button
    

    new_button = Button(root, height = 1, bg=dark_grey_pastel, fg=green_pastel, bd=0, takefocus=False, relief='flat', width = 2, font=("Product Sans", 100), activebackground=dark_grey_pastel, activeforeground=green_pastel)
    new_button.place(x=960, y=590, anchor = CENTER)
    new_button.bind("<Button-1>", new_folder)
    new_button.config(text="+")

    open_button = Button(root, bg=dark_grey_pastel, height = 1, text="O", fg=blue_pastel, bd=0, takefocus=False, relief='flat', width = 2,font=("Product Sans", 60), activebackground=dark_grey_pastel, activeforeground=blue_pastel)
    open_button.place(x=860, y=600, anchor = CENTER)
    open_button.bind("<Button-1>", open_folder)

    del_button = Button(root, bg=dark_grey_pastel, fg=red_pastel, bd=0, takefocus=False, relief='flat', width = 2,font=("Product Sans", 60), activebackground=dark_grey_pastel, activeforeground=red_pastel, height=1)
    del_button.place(x=1060, y=600, anchor = CENTER)
    del_button.bind("<Button-1>", del_folder)
    del_button.config(text="✕")

    exit_button = Button(root, text="✕", font=("Product Sans", 25), bg=dark_grey_pastel, fg=light_grey_pastel, relief = 'flat', bd=0, command = lambda: os._exit(0), width =1, takefocus=False, activeforeground=light_grey_pastel, activebackground=dark_grey_pastel) # Closes the application once clicked
    exit_button.place(relx=0.985, rely=0.043, anchor = E)

    fullscreen_button = Button(root, text = "□", font=("Product Sans", 35), bg=dark_grey_pastel, fg=light_grey_pastel, relief = 'flat', bd=0, command = lambda: fullscreen_toggle("event"), width =2, takefocus=False, activeforeground=light_grey_pastel, activebackground=dark_grey_pastel) # Fullscreens the window
    fullscreen_button.place(relx=0.97, rely=0.04, anchor = E)

    title_label = Label(root, text="Veloce", font=("Product Sans", 70), bg=dark_grey_pastel, fg=white_pastel)
    title_label.place(x=960, y=480, anchor = CENTER)

    help_button = Button(root, text = "(?)", font=("Product Sans", 35), bg=dark_grey_pastel, fg=light_grey_pastel, relief = 'flat', bd=0, command = lambda: help_menu("event"), width =2, takefocus=False, activeforeground=light_grey_pastel, activebackground=dark_grey_pastel) # Fullscreens the window
    help_button.place(relx=0.01, rely=0.95, anchor = W)



# Button choices

def open_folder(event):
    create_appdata_folder()
    global filename

    filename = filedialog.askopenfilename(initialdir = "C:\\Users\{}\AppData\Roaming\Veloce\\".format(os.getlogin()), title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) 
    if filename != "":
        cleartitlepage()
        global drawing_list
        global ideas_list
        f = open(filename, "r+")
        text = f.read()
        ideas_list = list(eval(text.split("&*(^$%^%&^*%&*%&%*^&(")[0]))
        drawing_list = list(eval(text.split("&*(^$%^%&^*%&*%&%*^&(")[1]))
        for i in range(len(ideas_list)):
            ideas_list[i] = (ideas_list[i]).replace("--++==__**","○")        
        f.close
        create_open_page()


def new_folder(event):
    global filename
    create_appdata_folder()
    filename = filedialog.asksaveasfilename(initialdir = "C:\\Users\{}\AppData\Roaming\Veloce\\".format(os.getlogin()), title = "Create a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) 
    f = open(filename + ".txt", "w+")
    f.write("[]")
    f.close
    filename += ".txt"
    if filename != "":
        cleartitlepage()
        global ideas_list
        global drawing_list
        ideas_list = []
        drawing_list = []
        create_open_page()

def del_folder(event):
    create_appdata_folder()
    filename = filedialog.askopenfilename(initialdir = "C:\\Users\{}\AppData\Roaming\Veloce\\".format(os.getlogin()), title = "Create a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) 
    os.remove(filename)

def fullscreen_toggle(event):
    
    global fullstate
    fullstate = not fullstate  # Just toggling the boolean
    root.attributes("-fullscreen", fullstate)


def create_appdata_folder():
    try:
        os.mkdir("C:\\Users\{}\AppData\Roaming\Veloce\\".format(os.getlogin()))
    except:
        pass


def help_menu(event):

    global menu_button
    global new_idea_label
    global middle_mouse_button
    global delete_idea_label
    global delete_button
    global main_menu_label
    global escape_button
    global fullscreen_label
    global f11_button
    
    cleartitlepage()
    
    menu_button = Button(root, font=("Product Sans", 35), bg=dark_grey_pastel, fg=light_grey_pastel, activebackground=dark_grey_pastel, activeforeground=light_grey_pastel, takefocus=False, bd=0, relief='flat')
    menu_button.config(text="≡")
    menu_button.place(relx=0.03, rely=0.04, anchor =  CENTER)
    menu_button.bind("<Button-1>", return_to_menu_from_help)

    new_idea_label = Label(root, text="New Idea", font=("Product Sans", 20), bg=dark_grey_pastel, fg=blue_pastel, activebackground=dark_grey_pastel, activeforeground=blue_pastel, justify=LEFT)
    new_idea_label.place(relx=0.02, rely=0.1, anchor = W)

    middle_mouse_button = Label(root, text="Middle Mouse Button", font=("Product Sans", 20), bg=dark_grey_pastel, fg=blue_pastel, activebackground=dark_grey_pastel, activeforeground=blue_pastel, justify=LEFT)
    middle_mouse_button.place(relx=0.02, rely=0.13, anchor =W)

    delete_idea_label = Label(root, text="Delete Idea", font=("Product Sans", 20), bg=dark_grey_pastel, fg=red_pastel, activebackground=dark_grey_pastel, activeforeground=blue_pastel, justify=LEFT)
    delete_idea_label.place(relx=0.02, rely=0.18, anchor = W)

    delete_button = Label(root, text="Delete Key", font=("Product Sans", 20), bg=dark_grey_pastel, fg=red_pastel, activebackground=dark_grey_pastel, activeforeground=red_pastel, justify=LEFT)
    delete_button.place(relx=0.02, rely=0.21, anchor =W)

    main_menu_label = Label(root, text="Main Menu", font=("Product Sans", 20), bg=dark_grey_pastel, fg=blue_pastel, activebackground=dark_grey_pastel, activeforeground=blue_pastel, justify=LEFT)
    main_menu_label.place(relx=0.02, rely=0.26, anchor = W)

    escape_button = Label(root, text="Escape Key", font=("Product Sans", 20), bg=dark_grey_pastel, fg=blue_pastel, activebackground=dark_grey_pastel, activeforeground=red_pastel, justify=LEFT)
    escape_button.place(relx=0.02, rely=0.29, anchor =W)

    fullscreen_label = Label(root, text="Fullscreen", font=("Product Sans", 20), bg=dark_grey_pastel, fg=red_pastel, activebackground=dark_grey_pastel, activeforeground=red_pastel, justify=LEFT)
    fullscreen_label.place(relx=0.02, rely=0.34, anchor = W)

    f11_button = Label(root, text="F11", font=("Product Sans", 20), bg=dark_grey_pastel, fg=red_pastel, activebackground=dark_grey_pastel, activeforeground=red_pastel, justify=LEFT)
    f11_button.place(relx=0.02, rely=0.37, anchor =W)

    root.bind("<Escape>", return_to_menu_from_help)


def return_to_menu_from_help(event):

    clear_help_menu()
    create_title_screen()


def clear_help_menu():

    menu_button.destroy()
    new_idea_label.destroy()
    middle_mouse_button.destroy()
    delete_idea_label.destroy()
    delete_button.destroy()
    main_menu_label.destroy()
    escape_button.destroy()
    fullscreen_label.destroy()
    f11_button.destroy()
    

# Opened Idea Page

def cleartitlepage():

    new_button.destroy()
    open_button.destroy()
    del_button.destroy()
    title_label.destroy()
    help_button.destroy()
    fullscreen_button.destroy()
    exit_button.destroy()


def create_open_page():

    global DrawingBoard

    DrawingBoard = Canvas(master = root, width = 1920, height = 1080, bg=dark_grey_pastel, bd=0, highlightthickness=0)
    DrawingBoard.place(x=960, y=540, anchor = CENTER)


    global menu_button
    global eraser_button
    global pencil_button
    global text_button
    global exit_button
    global fullscreen_button

    root.bind("<Button-2>", create_idea)
    root.bind("<Key>", typing)
    root.bind("<Delete>", lambda event: delete_idea())
    root.bind("<Escape>", return_to_menu)
    global idea_count
    idea_count = 0
    
    exit_button = Button(root, text="✕", font=("Product Sans", 25), bg=dark_grey_pastel, fg=light_grey_pastel, relief = 'flat', bd=0, command = lambda: os._exit(0), width =1, takefocus=False, activeforeground=light_grey_pastel, activebackground=dark_grey_pastel) # Closes the application once clicked
    exit_button.place(relx=0.985, rely=0.043, anchor = E)

    fullscreen_button = Button(root, text = "□", font=("Product Sans", 35), bg=dark_grey_pastel, fg=light_grey_pastel, relief = 'flat', bd=0, command = lambda: fullscreen_toggle("event"), width =2, takefocus=False, activeforeground=light_grey_pastel, activebackground=dark_grey_pastel) # Fullscreens the window
    fullscreen_button.place(relx=0.97, rely=0.04, anchor = E)

    menu_button = Button(root, font=("Product Sans", 35), bg=dark_grey_pastel, fg=light_grey_pastel, activebackground=dark_grey_pastel, activeforeground=light_grey_pastel, takefocus=False, bd=0, relief='flat')
    menu_button.config(text="≡")
    menu_button.place(relx=0.03, rely=0.04, anchor =  CENTER)
    menu_button.bind("<Button-1>", return_to_menu)

    eraser_button = Button(root, font=("Product Sans", 14), bg=red_pastel, fg=dark_grey_pastel, activebackground=red_pastel, activeforeground=dark_grey_pastel, takefocus=False, bd=0, relief='flat')
    eraser_button.config(text="Eraser")
    eraser_button.place(relx=0.95, rely=0.91, anchor =  E)
    eraser_button.bind("<Button-1>", eraser_mode)

    pencil_button = Button(root, font=("Product Sans", 14), bg=green_pastel, fg=dark_grey_pastel, activebackground=green_pastel, activeforeground=dark_grey_pastel, takefocus=False, bd=0, relief='flat')
    pencil_button.config(text="Pencil")
    pencil_button.place(relx=0.9, rely=0.91, anchor =  E)
    pencil_button.bind("<Button-1>", pencil_mode)

    text_button = Button(root, font=("Product Sans", 14), bg=blue_pastel, fg=dark_grey_pastel, activebackground=blue_pastel, activeforeground=dark_grey_pastel, takefocus=False, bd=0, relief='flat')
    text_button.config(text="Post-It")
    text_button.place(relx=0.85, rely=0.91, anchor =  E)
    text_button.bind("<Button-1>", idea_mode)


    root.bind("<Left>", lambda event: dec_cursor())
    root.bind("<Right>", lambda event: inc_cursor_bind())    

    for i in range(len(ideas_list)):
        create_idea_button(i)

    for i in range(len(drawing_list)):
        x = drawing_list[i].split("(*)")
        try:
            DrawingBoard.create_line(int(x[1]), int(x[2]), int(x[3]), int(x[4]), width = int(x[5]), fill=x[6], smooth = FALSE, splinesteps = 1, capstyle=ROUND)
        except:
            pass


def pencil_mode(event):

    root.bind("<B1-Motion>", pencil_down)
    root.bind("<ButtonRelease-1>", pencil_up)
    root.unbind("<Button-2>")
    unselect_idea()
    try:
        for i in range(len(ideas_list)):
            globals()["idea_button" + str(i)].unbind("<Button-1>")
    except:
        pass
    
def pencil_up(event):

    global old_x
    global old_y

    old_x, old_y = None, None

    save_file()


def pencil_down(event):

    global old_x
    global old_y

    root.unbind("<B1-Motion>")

    try:
        if old_x != None:
            v = ("line" + str(len(drawing_list) - 1) + "(*)" + str(old_x) + "(*)" +  str(old_y) + "(*)" + str(event.x) + "(*)" + str(event.y) + "(*)" + str(2) + "(*)" + white_pastel)
            drawing_list.append(v)
            globals()["line" + (str(len(drawing_list) - 1))] = DrawingBoard.create_line(old_x, old_y, event.x, event.y, width = 2, fill=white_pastel, smooth = FALSE, splinesteps = 1, capstyle=ROUND)
    except:
        pass

    old_x = event.x
    old_y = event.y

    root.bind("<B1-Motion>", pencil_down)

    

def idea_mode(event):

    root.unbind("<B1-Motion>")
    root.unbind("<ButtonRelease-1>")
    root.bind("<Button-2>", create_idea)

    for i in range(len(ideas_list)):
        try:
            globals()["idea_button" + str(i)].destroy()
        except:
            pass
    
    for i in range(len(ideas_list)):
        create_idea_button(i)

    

def eraser_mode(event):

    root.bind("<B1-Motion>", eraser_down)
    root.bind("<ButtonRelease-1>", pencil_up)
    root.unbind("<Button-2>")
    unselect_idea()
    try:
        for i in range(len(ideas_list)):
            globals()["idea_button" + str(i)].unbind("<Button-1>")
    except:
        pass

def eraser_down(event):

    global old_x
    global old_y

    root.unbind("<B1-Motion>")


    try:
        if old_x != None:
            v = ("line" + str(len(drawing_list) - 1) + "(*)" + str(old_x) + "(*)" +  str(old_y) + "(*)" + str(event.x) + "(*)" + str(event.y) + "(*)" + str(75) + "(*)" + dark_grey_pastel)
            globals()["line" + (str(len(drawing_list) - 1))] = DrawingBoard.create_line(old_x, old_y, event.x, event.y, width = 75, fill=dark_grey_pastel , smooth = FALSE, splinesteps = 1, capstyle=ROUND)
    except:
        pass

    old_x = event.x
    old_y = event.y
    drawing_list.append("line" + str(len(drawing_list) - 1) + "(*)" + str(old_x) + "(*)" +  str(old_y) + "(*)" + str(event.x) + "(*)" + str(event.y) + "(*)" + str(75) + "(*)" + dark_grey_pastel)

    root.bind("<B1-Motion>", eraser_mode)




def dec_cursor():

    global cursor_slot

    x = (ideas_list[selected_idea].split("*%$!$%*")[0])

    try:

        if cursor_slot != 0:
            cursor_slot -= 1

        flash_once()

    except:
        pass



def inc_cursor_bind():

    global cursor_slot

    x = (ideas_list[selected_idea].split("*%$!$%*")[0])

    try:

        if cursor_slot != len((ideas_list[selected_idea].split("*%$!$%*")[0])):
            cursor_slot += 1

        flash_once()

    except:
        pass

def inc_cursor():

    global cursor_slot

    x = (ideas_list[selected_idea].split("*%$!$%*")[0])

    try:

        cursor_slot += 1

        flash_once()

    except:
        pass

def return_to_menu(event):
    
    clear_open_page()
    create_title_screen()


def clear_open_page():

    global cursor_slot
    global hide_cursor

    save_file()

    menu_button.destroy()
    eraser_button.destroy()
    text_button.destroy()
    pencil_button.destroy()
    fullscreen_button.destroy()
    exit_button.destroy()
    
    for i in range(len(ideas_list)):
        try:
            globals()["idea_button" + str(i)].destroy()
        except:
            pass

    root.unbind("<Key>")
    root.unbind("<Delete>")
    root.unbind("<Escape>")
    root.unbind("<Button-2>")
    root.unbind("<Left>")
    root.unbind("<Right>")

    try:
        del cursor_slot
    except:
        pass

    try:
        del selected_idea
    except:
        pass
    hide_cursor = True

    DrawingBoard.destroy()

def save_file():

    global filename
    global ideas_list
    global drawing_list

    f = open(filename, "w+")
    f.write(str(str(ideas_list).replace("○","--++==__**")) + "&*(^$%^%&^*%&*%&%*^&(" + str(drawing_list))
    f.close

def create_idea(event):

    ideas_list.append(" " + "*%$!$%*" + str(event.x) + "*%$!$%*" + str(event.y) + "*%$!$%*" + "Enabled")
    i = len(ideas_list) - 1
    create_idea_button(i)
    select_idea(i, event)

    save_file()

def create_idea_button(i):

    global idea_count

    if ideas_list[i].split("*%$!$%*")[3] == "Disabled":
        return
    
    info = ideas_list[i].split("*%$!$%*")
    globals()["idea_button" + str(i)] = Button(root, text=info[0].replace("○","\n") + " ", font=("Product Sans", 14), bg=grey_pastel, relief='flat', bd=0, takefocus=False)
    globals()["idea_button" + str(i)].place(x=info[1], y=info[2], anchor = CENTER)
    globals()["idea_button" + str(i)].bind("<Button-1>", lambda event: select_idea(i, event))
    if len(info[0]) < 13:
        globals()["idea_button" + str(i)].config(width=13, height = 1)
    else:
        globals()["idea_button" + str(i)].config(width=0, height = 0)

    idea_count += 1
    

def select_idea(i, event):

    global selected_idea
    global hide_cursor
    global cursor_slot
    global showing_cursor

    
    unselect_idea()
    
    selected_idea = i
    globals()["idea_button" + str(selected_idea)].config(bg=yellow_pastel, activebackground=yellow_pastel, bd=0, relief='flat')
    cursor_slot = len((ideas_list[selected_idea].split("*%$!$%*")[0]))

    save_file()

    global currentxy

    try:
        del currentxy
    except:
        pass

    

    find_xy(event)

    move_idea(event)

def unselect_idea():
    
    global selected_idea
    global hide_cursor
    global cursor_slot
    global showing_cursor

    hide_cursor = False

    try:
        globals()["idea_button" + str(selected_idea)].config(bg=grey_pastel, activebackground=grey_pastel, bd=0, relief='flat')
        showing_cursor = True
        flash_once()
        del selected_idea

    except:
        pass

    



def find_xy(event):

    global currentxy
    currentxy = (str(int(ideas_list[selected_idea].split("*%$!$%*")[1]) - event.x_root) + " " + str(int(ideas_list[selected_idea].split("*%$!$%*")[2]) - event.y_root))

def move_idea(event):


    globals()["idea_button" + str(selected_idea)].bind("<B1-Motion>", drag)
    globals()["idea_button" + str(selected_idea)].bind("<ButtonRelease-1>", release)

def drag(event):

    global currentxy

    new_x = event.x_root + int(currentxy.split()[0]) 
    new_y = event.y_root + int(currentxy.split()[1]) 
    globals()["idea_button" + str(selected_idea)].place(x=new_x, y=new_y, anchor = CENTER)
    ideas_list[selected_idea] = ((ideas_list[selected_idea].split("*%$!$%*")[0]) + "*%$!$%*" + str(new_x) + "*%$!$%*" + str(new_y) + "*%$!$%*" + "Enabled")

    
def release(event):

    global currentxy

    globals()["idea_button" + str(selected_idea)].unbind("<B1-Motion>")
    globals()["idea_button" + str(selected_idea)].unbind("<ButtonRelease-1>")
    save_file()
    try:
        del currentxy
    except:
        pass

def delete_idea():

    global selected_idea
    global idea_count

    try:
        selected_idea
    except:
        return

    ideas_list[selected_idea] = ((ideas_list[selected_idea].split("*%$!$%*")[0]) + "*%$!$%*" + (ideas_list[selected_idea].split("*%$!$%*")[1]) + "*%$!$%*" + (ideas_list[selected_idea].split("*%$!$%*")[2]) + "*%$!$%*" + "Disabled")
    globals()["idea_button" + str(selected_idea)].destroy()
    idea_count -= 1

    save_file()

def typing(event):


    global selected_idea
    global cursor_slot

    try:
        selected_idea
    except:
        return

    if ideas_list[selected_idea].split("*%$!$%*")[3] == "Disabled":
        return

    text_item = (ideas_list[selected_idea].split("*%$!$%*")[0])


    if str(event.keysym) == "space" and len(text_item.split(" ")) % 4 == 0:
        inc_cursor()
        x = text_item = text_item[: cursor_slot -1] + "○" + text_item[cursor_slot -1:]
        ideas_list[selected_idea] = (x + "*%$!$%*" + (ideas_list[selected_idea].split("*%$!$%*")[1]) + "*%$!$%*" + (ideas_list[selected_idea].split("*%$!$%*")[2]) + "*%$!$%*" + "Enabled")
    if str(event.keysym) != "BackSpace" and str(event.keysym) != "Return":
        inc_cursor()
        x = text_item = text_item[: cursor_slot -1] + str(event.char) + text_item[cursor_slot -1:]
        ideas_list[selected_idea] = (x + "*%$!$%*" + (ideas_list[selected_idea].split("*%$!$%*")[1]) + "*%$!$%*" + (ideas_list[selected_idea].split("*%$!$%*")[2]) + "*%$!$%*" + "Enabled")
    if str(event.keysym) == "BackSpace":
        if cursor_slot != 0:
            dec_cursor()
            text_item = text_item[:cursor_slot] + text_item[(cursor_slot + 1):]
            ideas_list[selected_idea] = (text_item + "*%$!$%*" + (ideas_list[selected_idea].split("*%$!$%*")[1]) + "*%$!$%*" + (ideas_list[selected_idea].split("*%$!$%*")[2]) + "*%$!$%*" + "Enabled")
    if str(event.keysym) == "Return":
        inc_cursor()
        x = text_item = text_item[: cursor_slot] + " " + text_item[cursor_slot:]
        ideas_list[selected_idea] = (x + "*%$!$%*" + (ideas_list[selected_idea].split("*%$!$%*")[1]) + "*%$!$%*" + (ideas_list[selected_idea].split("*%$!$%*")[2]) + "*%$!$%*" + "Enabled")

    if len(text_item) < 13:
        globals()["idea_button" + str(selected_idea)].config(width=13, height = 1)
    else:
        globals()["idea_button" + str(selected_idea)].config(width=0, height = 0) 

    flash_once()

def flash_once():

    global showing_cursor
    global hide_cursor
    global cursor_slot

        

    try:

        x = (ideas_list[selected_idea].split("*%$!$%*")[0]).replace("○", "\n")

        if showing_cursor == False and hide_cursor == False:
            x = x[: cursor_slot] + '|' + x[cursor_slot:]
            globals()["idea_button" + str(selected_idea)].config(text = str(x))
        else:
            x = x[: cursor_slot] + ' ' + x[cursor_slot:]
            globals()["idea_button" + str(selected_idea)].config(text = str(x))           
    except:
        pass

        
def flash_cursor():

    global showing_cursor

    flash_once()

    showing_cursor = not showing_cursor
    
    root.after(750, flash_cursor)




def __init__():

    global root
    global fullstate
    global showing_cursor
    global hide_cursor

    showing_cursor = False

    create_root()
    
    fullstate = False

    root.bind("<F11>", fullscreen_toggle)

    flash_cursor()



def create_root():

    global root

    root = Tk()
    root.state('zoomed')
    root.title('Veloce')
    root.config(bg=dark_grey_pastel)



__init__()
create_title_screen()
root.mainloop()

