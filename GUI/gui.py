# import time
from tkinter import *

# WIDGETS = GUI elements: buttons, text boxes, labels, images
# WINDOWS = serves as a container to hold or contain these widgets
# LABEL = an area widget that holds text and/or an image with in a window
# BUTTON = you click it, then it does stuff
# ENTRY WIDGET = textbox that accepts a single line of user input
# RADIO BUTTON = similar to checkbox, but you can select one from a group
# LISTBOX = a listing of selectable text items within its own container
# TEXT WIDGET= functions like a text area, you can enter multiple lines of text
# FRAME = a rectangular container to group and hold widgets
# GRID, grid()= geometry manager that organizes widgets in a table like structure in a parent
# CANVAS = widget that is used to draw plots, graphs, images in a window

# ''' window , image code '''
# window = Tk() #instantiate an instance of window
# window.geometry('500x500') # resolution order
# window.title('GUI') #title bar
# img = PhotoImage(file = 'kg.png')
# window.iconphoto(True,img) # to replace icon of your window
# label = Label(window, text= 'Conspiracies', font= ('arial', 40, 'bold'),bg= 'cyan',
# fg= 'brown', bd= 10, relief= RAISED, padx= 9, pady= 9, image= img, compound= 'bottom')
# label.place(x=9, y=9) # to place position of your text in the window
# label.pack()

# ''' button code'''
# count=0
# def button():
#     global count
#     count += 1
#     print(f 'you touched the imposter!\n Total number of counts: {count}')
#
# window = Tk()
# img = PhotoImage(file ='among us.png')
# b = Button(window, text= 'CLICK !!!', command= button, fg= 'purple', bg= 'cyan',
#            font= 'bold', activebackground='red', activeforeground='brown',
#            image= img, compound= 'bottom', )
# b.pack()
#
#
# window.mainloop() # place window on computer screen, listen for events

# ''' if user want to input something, delete, backspace: code'''

# def submit(): # function for submit button
#     user = entry.get()
#     print('you wrote:', user)
#     entry.config(state=DISABLED)# after pressing submit button you can't write anymore
#
#
# def delete(): # function for delete button
#     entry.delete(0, END)
#
#
# def backspace(): # function for backspace button
#     entry.delete(len(entry.get())-1, END)
#
#
# window = Tk()
# entry = Entry(window, font = ( 'arial', 50, 'bold')) # user input
# entry.pack(side= LEFT)
#
# submit_button = Button(window, text='submit', command=submit, fg='brown', bg='yellow',font=('bold',15))
# submit_button.pack(side= RIGHT)
#
# delete_button = Button(window, text='delete', command=delete, fg='brown', bg='#bfad86', font=('bold',15))
# delete_button.pack(side= RIGHT)
#
# backspace_button = Button(window, text='backspace', command=backspace, fg='brown', bg='#869cbf', font=('bold',15))
# backspace_button.pack(side= RIGHT)
#
# window.mainloop()

# ''' check button '''
# def check_button():
    # if (x.get()): for boolean
    # if (x.get() == 'yes'): for string
    # if (x.get() == 1):
    #     print('you agree :)')
    # else:
    #     print("you don't agree :(")
#
# window = Tk()
# x= BooleanVar() , onvalue=True , offvalue=False
# x=StringVar() , onvalue='yes' , offvalue='no'
# x = IntVar()
# photo = PhotoImage(file='python logo.png')
# check_button = Checkbutton(window, text='do you agree',variable=x,
#              onvalue=1, offvalue=0, command=check_button,
#              fg= 'brown', bg='green', activeforeground='brown',
#              activebackground='green',padx=9, pady=15, image=photo,
#              compound=RIGHT)
# check_button.pack()
# window.mainloop()

# ''' radio button '''
# def order():
#     if x.get() == 0:
#         print('you ordered fries :)')
#     elif x.get() == 1:
#         print('you ordered burger :)')
#     elif x.get() == 2:
#         print('you ordered pizza :)')
#     elif x.get() == 3:
#         print('you ordered soda :)')
#     elif x.get() == 4:
#         print('you ordered juice :)')
#     else:
#         print('huh...? :|')
#
# window = Tk()
# fries_img=PhotoImage(file='fries.png')
# burger_img=PhotoImage(file='burger.png')
# pizza_img=PhotoImage(file='pizza.png')
# soda_img=PhotoImage(file='soda.png')
# juice_img=PhotoImage(file='juice.png')
#
# Food_images=[fries_img , burger_img , pizza_img , soda_img , juice_img]
# Food=['fries' , 'burger' , 'pizza' , 'soda' , 'juice']
#
# x=IntVar()
#
# for index in range(len(Food)):
#     radio_button=Radiobutton(window, text=Food[index] , font= ('arial', 15, 'bold'),
#                  variable=x, value= index, fg= 'brown', bg='#9dbfb7', pady=15,padx=9,
#                  image=Food_images[index] ,
                 #compound= LEFT, indicatoron=0, # elimate circle indicators
#                  width=199, command=order)
#     radio_button.pack(anchor=W)
# window.mainloop()

# ''' scale'''
# def submit():
#     print('the temperature is '+str(scale.get()) +' celsius')
#
# window = Tk()
# hotImage = PhotoImage(file='hotflame.png')
# h_label=Label(image=hotImage)
# h_label.pack()
#
# button=Button(text='submit', command=submit)
# button.pack(side= RIGHT)
#
# scale = Scale(window, from_= 500, to= 0, orient= VERTICAL,
#               length=300, font=('console', 25),
#               tickinterval=10, # adds numeric indicators for value ,
#               resolution=5, #increment of slider
#               troughcolor= 'cyan', # scale color
#               fg='red', bg='black')
# scale.set(0)
# scale.pack()
#
# coldImage = PhotoImage(file='snowflake.png')
# c_label=Label(image=coldImage)
# c_label.pack()
#
# window.mainloop()

# ''' listbox '''
# def submit():
    # print("you have ordered:")
    # print(listbox.get(listbox.curselection())) # only for one selection
    # to submit multiple items
    # food = []
    # for item in listbox.curselection():
    #     food.insert(item, listbox.get(item))
    # for item in food:
    #     print(item)
#
# def delete():
#     to delete multiple items
    # food=[]
    # for item in reversed(listbox.curselection()):
    #     listbox.delete(item)
    # listbox.delete(listbox.curselection()) # only for one selection
    # listbox.config(height=listbox.size())

# def add():
#     listbox.insert(listbox.size(),entry_box.get())
#     listbox.config(height=listbox.size())

# window=Tk()
#
# listbox=Listbox(window,font=('constantia', 35), width=11,
#                 selectmode=MULTIPLE)
# listbox.pack()
#
# listbox.insert(1,'pizza')
# listbox.insert(2,'burger')
# listbox.insert(3,'ramen')
# listbox.insert(4,'sushi')
# listbox.insert(5,'soup')
#
# listbox.config(height=listbox.size()) #automatically adjust window with listbox size
#
# submit_button=Button(window, text='submit', command=submit)
# submit_button.pack()
#
# entry_box= Entry(window)
# entry_box.pack()
#
# delete_button=Button(window, text='delete', command=delete)
# delete_button.pack()
#
# add_button=Button(window, text='add', command=add)
# add_button.pack()
#
# window.mainloop()

# ''' message box '''
# we can also change the icon of message box: "icon = error/warning/info"
# from tkinter import messagebox # import message library
# window = Tk()
# def click():
    # messagebox.showinfo(title='show info', message='you are a human :|')
    # messagebox.showwarning(title='show warning', message='this PC has a VIRUS!')
    # messagebox.showerror(title='show error', message='ERROR ! :|')

    # if messagebox.askokcancel(title='ask ok/cancel', message='Do you want to do this?'):
    #     print('you did this :) ')
    # else:
    #     print('you canceled :(')

    # if messagebox.askretrycancel(title='ask retry/cancel', message='Do you want to retry?'):
    #     print('you did retried :)')
    # else:
    #     print('you canceled :(')

    # if messagebox.askyesno(title='ask yes/no', message='Do you like programming?'):
    #     print('me too :) ')
    # else:
    #     print("you don't like :(")

    # answer= messagebox.askquestion(title='ask question', message=' are you a programmer?')
    # if answer == 'yes':
    #     print(' :) ')
    # else:
    #     print(' :( ')

    # var=messagebox.askyesnocancel(title='ask yes/no/cancel', message='Do '
    # 'you want to continue?') # returns true/false/none
    # if var == True:
    #     print(' GOOD :) ')
    # elif var == False:
    #     print('WHY? :(')
    # else:
    #     print('You canceled :|')


# b= Button(window, text='click me!', command=click)
# b.pack()
# window.mainloop()

# ''' color chooser or picker '''
# from tkinter import colorchooser  # SUB MODULE
# def click():
#     color=colorchooser.askcolor() # assign colo to a variable
#     color_hex= color[1] # assigning element at index 1 to a variable
#     window.config(bg=color_hex)
#     print('window color has been changed.')
#
# window=Tk()
# window.geometry('420x420')
# b=Button(text='click !!!', command=click)
# b.pack()
# window.mainloop()

# ''' text widget/button '''
# window = Tk()
# def submit():
#     input=(text.get('1.0',END))
#     print(input)
#
# text=Text(window,bg='light yellow', fg='purple', font=('Ink free', 25), height=9,
#           width=25, pady=7, padx=7)
# text.pack()
#
# button=Button(text='submit', command=submit)
# button.pack()
#
# window.mainloop()

# ''' to open a file using filedialog '''
# from tkinter import filedialog


# def open_file():
    # to open file anywhere from pc:
    # file_path = filedialog.askopenfilename()
    # print(file_path)
    # to open file while using directory:
    # file_path = filedialog.askopenfilename(title='want to open file?', # tiltle of window
    # initialdir = 'D:\\pycharm files\\pythonProject1', # copy absolute path
    # filetypes = ([('text files', '*.txt'), ('all files', '*.*')]))
    # file = open(file_path, 'r')
    # print(file.read())
    # file.close()
# window = Tk()

# button = Button(text='open file', command=open_file)
# button.pack()

# window.mainloop()
#
# ''' to save a file using filedialog '''
# from tkinter import filedialog
# def save_file():
#     file = filedialog.asksaveasfile(title='want to save file?',
#            initialdir='D:\\pycharm files\\pythonProject',
#            defaultextension='.txt',
#            filetypes=[('all files','*.*'),('HTML files','*.html')])
#     if file is None:
#           return
#     file_text = str(text.get(1.0, END))
#     #for python console:
#     #file_text= input('enter some text :)')
    # file.write(file_text)
    # file.close()
#
# window = Tk()
# button = Button(text='save', command=save_file)
# button.pack()
# text=Text(window)
# text.pack()
# window.mainloop()

# ''' menu bar '''
# def open_file():
#     print('File opened !')
# def save_file():
#     print('File saved !')
# def cut():
#     print('File cut !')
# def copy():
#     print('File copied !')
# def paste():
#     print('File pasted !')
# window = Tk()
#
# menubar = Menu(window) # adding menubar in the window
# window.config(menu=menubar) # setting menu of the window to menu bar
#
# # creating separate file menu in the menubar
# fileMenu= Menu(menubar, tearoff=0 # tearoff removes --- part from drop down
#                ) # adding file menu in menubar
# menubar.add_cascade(label='File', menu=fileMenu) # drop down effect for file menu
# # creating options in file menu
# fileMenu.add_command(label='Open', command=open_file)
# fileMenu.add_command(label='Save',command=save_file)
# # to separate exit option from save and open options by adding a horizontal line
# fileMenu.add_separator()
# fileMenu.add_command(label='Exit', command=quit)
#
# # creating separate edit menu in the menubar
# editMenu= Menu(menubar, tearoff=0 # tearoff removes --- part from drop down
#                ) # adding edit menu in menubar
# menubar.add_cascade(label='Edit', menu=editMenu) # drop down effect for edit menu
# # creating options in edit menu
# editMenu.add_cascade(label='Cut', command=cut)
# editMenu.add_cascade(label='Copy', command=copy)
# editMenu.add_cascade(label='Paste', command=paste)
# window.mainloop()

# ''' frames '''
# window = Tk()
# frame = Frame(window, bg='pink', bd=5, relief=SUNKEN)# creating frame
# frame.pack(side='bottom')
# # creating buttons
# Button(frame,text='W', font=('Consolas', 25), width=3).pack(side=TOP)
# Button(frame,text='A', font=('consolas', 25), width=3).pack(side=LEFT)
# Button(frame,text='S', font=('consolas', 25), width=3).pack(side=LEFT)
# Button(frame,text='D', font=('consolas', 25), width=3).pack(side=LEFT)

# window.mainloop()

# ''' opening new window'''
# def create_window():
    # new_window = Toplevel() # new window 'on top' of other windows linked to a 'bottom' window.
    # new_window= Tk() # independent from bottom window
    # old_window.destroy() # close out of old window

# old_window = Tk() # new independent window
# creating new window by using button in main window
# Button(old_window, text='create new window', command=create_window).pack()
# old_window.mainloop()

# ''' window tabs '''
# from tkinter import ttk
# window = Tk()
#
# notebook = ttk.Notebook(window) # widget that manages a collection of windows/displays
#
# tab1 = Frame(notebook) # new frame for tab1
# tab2 = Frame(notebook) # new frame for tab2
#
# notebook.add(tab1, text='tab1')
# notebook.add(tab2, text='tab2')
# notebook.pack(expand=True, fill='both')# expand: to fill any space not otherwise used(notebook will be on centre)
#                                        # fill: space on x-axis and y-axis(tabs will be on left side of window)
# # adding something related to these tabs
# Label(tab1, text='this is tab1 : )', width=50, height=25).pack()
# Label(tab2, text='this is tab2 : )', width=50, height=25).pack()
#
# window.mainloop()

# ''' grid '''
# def submit():
#    # not working
#     print(f'{first_name_entry}\n{last_name_entry}\n{gender_entry}')
#
# window = Tk()
# window.title('My Info')
#
# title_label = Label(window, text='enter you info :)(:', font=('Arial',9)).grid(row=0,column=0,columnspan=2)
#
# # creating labels and entry boxes
# first_name_label= Label(window, text='First Name:', bg='yellow', width=15).grid(row=1, column=0)
# first_name_entry = Entry(window, bg='grey').grid(row=1, column=1)
#
# last_name_label= Label(window, text='Last Name:', bg='orange', width=15).grid(row=2, column=0)
# last_name_entry = Entry(window, bg='grey').grid(row=2, column=1)
#
# gender_label= Label(window, text='gender:', bg='cyan', width=15).grid(row=3, column=0)
# gender_entry = Entry(window, bg='grey').grid(row=3, column=1)
#
# # creating  submit button
# submit_button = Button(window, text='submit', command=submit).grid(row=4, column=0, columnspan=2)
#
# window.mainloop()

# ''' bar/loading '''
# def start():
#     GB = 10
#     download = 0
#     speed = 1
#     while(download < GB):
#         time.sleep(0.05)
#         bar['value'] += 10 # value of bar to be increased
#         download += speed
#         percent.set(str(int((download/GB)*100))+'%') # displaying % below bar
#         text.set(str(download)+'/'+str(GB)) # displaying value of download divides by no. of tasks
#         window.update_idletasks() # to refresh our bar
#
# from tkinter.ttk import *
# window = Tk()
# percent = StringVar()
# text = StringVar()
#
# bar= Progressbar(window, orient=HORIZONTAL, length=300)
# bar.pack(pady= 10) # adding a bar
#
# # creating a labels after bar and before download button, to display % and tasks downloading
# percent_label = Label(window, textvariable=percent).pack()
# text_label = Label(window, textvariable=text).pack()
#
# button= Button(window,text='download', command=start).pack()
#
# window.mainloop()

# ''' canvas : creating geometrical objects '''
# window = Tk()
#
# canvas = Canvas(window, width=500, height=500)
# canvas.create_line(0,0,500,500, fill='blue', width=5) # blue line
# canvas.create_line(0,500,500,0, fill='red', width=5) # red line
# canvas.create_rectangle(50,50,250,250, fill='purple') # rectangle
# polygon
# point = [250,0,500,500,0,500]
# canvas.create_polygon(point, fill='yellow', outline='black', width=5)
# canvas.create_arc(0,0,500,500,style=PIESLICE, fill='green',
#                   start=180)# style can be chord & start can be 90/270
#
# # creating pokeball
# canvas.create_arc(0,0,500,500, fill='red', extent=180, width=9)
# canvas.create_arc(0,0,500,500, fill='white', extent=180, start=180, width=9)
# canvas.create_oval(190,190,310,310, fill='white', width=9)
#
# canvas.pack()
#
# window.mainloop()

# ''' key events '''
# def do_something(event):
#     print('you pressed:' + event.keysym) # whatever key will press, will be appeared on python console
#     label.config(text=event.keysym) # whatever we press in keyboard that will appear on window
#
# window = Tk()
# window.bind("<Key>",do_something)# bind(event='<key>', function= do_something)
#
# label= Label(window, font=('helvetica', 100))
# label.pack()
#
# window.mainloop()

# ''' mouse events '''
# def do_something(event):
#     print('mouse coordinates:'+ str(event.x)+ ',' + str(event.y))
#
# window = Tk() # left mouse click
#
# window.bind("<Button-1>", do_something) # left mouse click
# window.bind("<Button-2>", do_something) # scroll mouse click
# window.bind("<Button-3>", do_something) # right mouse click
# window.bind("<ButtonRelease>", do_something) # release mouse click
# window.bind("<<Enter>", do_something) # enter the window
# window.bind(">Leave>", do_something) # leave the window
# window.bind("<Motion>", do_something) # where the mouse moved
#
# window.mainloop()

# ''' writing contents of file in tkinter window. '''
# we can also save by writing contents on the window
# w = Tk()
#
#
# def open_():
#     file = open('filer.txt', 'r+')
#     f = file.read()
#     file_text.insert(END, f)
#     file.close()
#
#
# def save_():
#     file = open('filer.txt', 'w')
#     f = file.write(file_text.get(1.0, END))
#     file.close()
#
#
# file_text = Text(w, width=50, height=10, font=('arial', 12))
# file_text.pack(pady=19)
#
# open_button = Button(w, text='open file', command=open_)
# open_button.pack(pady=19)
#
# save_button = Button(w, text='save file', command=save_)
# save_button.pack(pady=19)
#
# w.mainloop()


# def string_processing(string_list):
#     for ch in string_list:
#         for i in range(len(ch)):
#             if 'a' <= ch[i] <= 'z' or 'A' <= ch[i] <= 'Z':
#                 print(ch[i], end='')
#         print(end=' ')
#     print()
#
#
# string_processing(['Hello,','World!'])
# string_processing(['Test...','me...','please'])
#
