from tkinter import *
import tkinter as tk
##################################################################################################################

allList = []
Style = ["AUTO-BHOP   ",
         "Sideways",
         "Half-Sideways",
         "D-Only","A-Only",
         "W-Only",
         "Scroll/Normal",
         "Easy Scroll","Stamina",
         "Slowmotion","Low-Gravity"]

###

MapSearchList = ["Select A Map"]

###
##################################################################################################################

def hide():

    header.grid_remove()
    content.grid_remove()
    Footer.grid_remove()
    allremove()

##################################################################################################################


def addpage():
    root.geometry('250x360')
    hide()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, pad=3)
    root.rowconfigure(1, pad=10)
    root.rowconfigure(2, pad=3)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')

##############################################
    title1 = Label(header, text="Add Time", fg="White", bg="grey", font="Verdana 17 bold", )
    title1.grid(row=0, column=1, padx=(76,0))
    allList.append(title1)
    Label7 = Label(content, text="MAP:", font="Arial 14 bold")
    Label7.grid(row=0, column=0,pady=(10,0), padx=20)
    allList.append(Label7)
    MapAddSearch = StringVar()
    entry1 = Entry(content, textvariable=MapAddSearch, width=16)
    entry1.grid(row=0, column=1,pady=(10,0))
    allList.append(entry1)
    MapList_button = tk.Button(content, text='Map List', command=hide)
    MapList_button.grid(row=1, column=1,padx=(0,78))
    allList.append(MapList_button)
    MapConfirm_button1 = tk.Button(content, text= "Confirm", command=hide)
    MapConfirm_button1.grid(row=1, column=1, padx=(78, 0))
    allList.append(MapConfirm_button1)

    Label8 = Label(content, text="STYLE:", font="Arial 14 bold")
    Label8.grid(row=2, column=0,pady=(10, 0))
    allList.append(Label8)
    Styles = StringVar()
    Styles.set(Style[0])  # default value
    DropdownStyle = OptionMenu(content, Styles, *Style)
    DropdownStyle.grid(row=2, column=1,pady=(10, 0))
    allList.append(DropdownStyle)
    MapConfirm_button2 = tk.Button(content, text= "Confirm", command=hide)
    MapConfirm_button2.grid(row=3, column=1, padx=(78, 0))
    allList.append(MapConfirm_button2)

    TimeAdd = DoubleVar()
    Label9 = Label(content, text="TIME:", font="Arial 14 bold")
    Label9.grid(row=5, column=0,pady=(10, 0))
    allList.append(Label9)
    entry2 = Entry(content, textvariable=TimeAdd, width=16)
    entry2.grid(row=5, column=1,pady=(10,0))
    allList.append(entry2)
    MapConfirm_button3 = tk.Button(content, text= "Confirm", command=hide)
    MapConfirm_button3.grid(row=6, column=1, padx=(78, 0))
    allList.append(MapConfirm_button3)

    Label10 = Label(content, text="TICK", font="Arial 14 bold")
    Label10.grid(row=7, column=0,pady=(10, 0))
    allList.append(Label10)
    Label11 = Label(content, text="RATE:", font="Arial 14 bold")
    Label11.grid(row=8, column=0)
    allList.append(Label11)

    statusSelect = IntVar()
    Tick124 = Radiobutton(content, text="124 Tick Rate", variable=statusSelect, value="124")
    Tick124.grid(row=7, column=1,padx=(0,10))
    allList.append(Tick124)
    Tick100 = Radiobutton(content, text="100 Tick Rate", variable=statusSelect, value="100")
    Tick100.grid(row=8, column=1,padx=(0,10))
    allList.append(Tick100)
    Tick64 = Radiobutton(content, text=" 64 Tick Rate", variable=statusSelect, value="64")
    Tick64.grid(row=9, column=1, padx=(0,14))
    allList.append(Tick64)

    MapConfirm_button4 = tk.Button(Footer, text= "Add Time", command=hide, width=10)
    MapConfirm_button4.grid(row=10, column=1, pady=(0,10), padx=(5,0))
    allList.append(MapConfirm_button4)

    Home_button1 = tk.Button(Footer, text= "Home", command=home, width=10)
    Home_button1.grid(row=10, column=0, pady=(0,10), padx=(0,5))
    allList.append(Home_button1)


##################################################################################################################

root = tk.Tk()
root.title("BHOP Time Recorder")
header = tk.Frame(root, bg='grey')
content = tk.Frame(root, bg='white')
Footer = tk.Frame(root, bg='white')
gider = tk.Frame(root, bg="white")


##################################################################################################################


def MainPage():
    title = Label(header, text="BHOP Time Recorder", fg="White", bg="grey", font="Verdana 17 bold", )
    title.grid(row=0, column=1, padx=30)
    allList.append(title)
    packer = Label(content, text="                   ")
    packer.grid(row=0, column=0)
    allList.append(packer)
    packer1 = Label(content, text="                   ")
    packer1.grid(row=0, column=2)
    allList.append(packer1)
    Label1 = Label(content, text="Welcome User")
    Label1.grid(row=0, column=1)
    allList.append(Label1)
    Label2 = Label(content, text="Previous Time:")
    Label2.grid(row=1, column=1)
    allList.append(Label2)
    PrevTime = DoubleVar()
    PrevTime.set(0.0)
    Label3 = Label(content, textvariable=PrevTime)
    Label3.grid(row=2, column=1)
    allList.append(Label3)
    Label4 = Label(content, text="Previous Map:")
    Label4.grid(row=3, column=1)
    allList.append(Label4)
    PrevMap = StringVar()
    PrevMap.set("")
    Label5 = Label(content, textvariable=PrevMap)
    Label5.grid(row=4, column = 1)
    allList.append(Label5)

    Label6 = Label(Footer, text="_________________________________________")
    Label6.grid(row=0, column=0)
    allList.append(Label6)

    add_button = tk.Button(Footer, text='Add Time', width=15, command=addpage)
    add_button.grid(row=1, column=0)
    allList.append(add_button)

    view_button = tk.Button(Footer, text='View', width=15, command=view)
    view_button.grid(row=2, column=0)
    allList.append(view_button)

    delete_button = tk.Button(Footer, text='Delete', width=15, command=delete)
    delete_button.grid(row=3, column=0)
    allList.append(delete_button)

    settings_button = tk.Button(Footer, text='Settings', width=15, command=settings)
    settings_button.grid(row=4, column=0)
    allList.append(settings_button)

##################################################################################################################


def view():
    root.geometry('250x240')
    hide()
    root.rowconfigure(0, pad=2)
    root.rowconfigure(1, pad=3)
    root.rowconfigure(2, pad=3)
    root.rowconfigure(3, pad=3)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')
    gider.grid(row=3, sticky='news')

##############################################

    title2 = Label(header, text="View", fg="White", bg="grey", font="Verdana 17 bold", )
    title2.grid(row=0, column=0, padx=(100, 0))
    allList.append(title2)

    Label12 = Label(content, text="Search for Map", font="Arial 15 bold")
    Label12.grid(row=0, column=0,pady=(10,0), padx=(34, 0))
    allList.append(Label12)


    SearchMap = StringVar()
    entry3 = Entry(content, textvariable=SearchMap, width=20)
    entry3.grid(row=1, column=0, padx=(28, 0))
    allList.append(entry3)

    MapList_button1 = tk.Button(Footer, text='Map List', command=hide)
    MapList_button1.grid(row=2, column=0,padx=(40,0))
    allList.append(MapList_button1)
    MapConfirm_button5 = tk.Button(Footer, text= "Confirm", command=hide)
    MapConfirm_button5.grid(row=2, column=1,padx=(10,0))
    allList.append(MapConfirm_button5)

    Label13 = Label(gider, text="Map Select", font="Arial 15 bold")
    Label13.grid(row=0, column=0,pady=(10,0), padx=(55, 0))
    allList.append(Label13)

    Mapselect = StringVar()
    Mapselect.set(MapSearchList[0])  # default value
    DropdownMapSelect = OptionMenu(gider, Mapselect, *MapSearchList)
    DropdownMapSelect.grid(row=1, column=0,padx=(55, 0))
    allList.append(DropdownMapSelect)

    view_button1 = tk.Button(gider, text= "View", command=hide)
    view_button1.grid(row=2, column=0,padx=(55,0))
    allList.append(view_button1)

    Home_button2 = tk.Button(gider, text= "Home", command=home,width=5)
    Home_button2.grid(row=3, column=0, padx=(0,120))
    allList.append(Home_button2)
##################################################################################################################


def settings():
    root.geometry('250x187')
    hide()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, pad=1)
    root.rowconfigure(1, pad=2)
    root.rowconfigure(2, pad=1)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')


##############################################

    title3 = Label(header, text="Settings", fg="White", bg="grey", font="Verdana 17 bold", )
    title3.grid(row=0, column=0, padx=(86, 0))
    allList.append(title3)

    Label14 = Label(content, text="Clear Wipe", font="Arial 18 bold", bg="#FFF8DC")
    Label14.grid(row=0, column=0,pady=(10,0), padx=(80, 0))
    allList.append(Label14)

    Label15 = Label(Footer, text="Are you sure?", font="Arial 14 bold")
    Label15.grid(row=1, column=0, pady=(10, 0), padx=(71, 0))
    allList.append(Label15)

    ClearWipeQuerry = StringVar()
    wipeyes = Radiobutton(Footer, text="Yes", variable=ClearWipeQuerry, value="yes")
    wipeyes.grid(row=2, column=0,padx=(65,0))
    allList.append(wipeyes)

    confirmwipe_button = tk.Button(Footer, text="WIPE", command=home, width=5)
    confirmwipe_button.grid(row=4, column=0, padx=(65,0))
    allList.append(confirmwipe_button)

    Home_button3 = tk.Button(Footer, text="Home", command=home, width=5)
    Home_button3.grid(row=5, column=0,pady=(10,0),padx=(0, 120))
    allList.append(Home_button3)

##################################################################################################################


def allremove():
    for i in allList:
        i.grid_remove()


##################################################################################################################

def delete():
    root.geometry('250x340')
    hide()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, pad=1)
    root.rowconfigure(1, pad=2)
    root.rowconfigure(2, pad=1)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')

##############################################


    title4 = Label(header, text="Delete", fg="White", bg="grey", font="Verdana 17 bold", )
    title4.grid(row=0, column=0, padx=(92, 0))
    allList.append(title4)

    Label16 = Label(content, text="Search Map", font="Arial 15 bold")
    Label16.grid(row=0, column=0, pady=(10, 0), padx=(40, 0))
    allList.append(Label16)

    MapDeleteSearch = StringVar()
    entry4 = Entry(content, textvariable=MapDeleteSearch, width=18)
    entry4.grid(row=1, column=0, padx=(37,0))
    allList.append(entry4)




##################################################################################################################

def home():
    hide()
    MainWindowLayout()
    MainPage()

##################################################################################################################

def MainWindowLayout():
    root.geometry('250x300')
    root.columnconfigure(0, weight=1) # 100%

    root.rowconfigure(0, pad=3) # 10%
    root.rowconfigure(1, pad=13) # 30%
    root.rowconfigure(2, pad=13) # 60%

    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')
##################################################################################################################


MainWindowLayout()
MainPage()
root.mainloop()