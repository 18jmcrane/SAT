from tkinter import *
import tkinter as tk
from operator import itemgetter
##################################################################################################################
maplist_list = []
back_list = []
WRstyle_list = []
WRtime_list = []
WRtickrate_list = []


f = open("maplist", "r")
for line in f:
    line = line.strip('\n')
    line = line.split(",")
    maplist_list.append(line[0])

maplist_list.sort()
print(maplist_list)
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

StyleSelect_list = ["Choose a Style"]
TimeSelect_list = ["Select Time"]

MapSearchList = ["Select A Map"]
MapSearchList1 = ["Select A Map"]


###
##################################################################################################################

def hide():

    header.grid_remove()
    content.grid_remove()
    Footer.grid_remove()
    allremove()
##################################################################################################################

def mapdisplay(AUTOBHOP_list1,Sideways_list1,HalfSideways_list1,Donly_list1,AOnly_list1,WOnly_list1,ScrollNormal_list1,EasyScroll_list1,Stamina_list1,Slowmotion_list1,LowGravity_list1,searchresult):

    root.geometry('270x400')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, pad=3)
    root.rowconfigure(1, pad=10)
    root.rowconfigure(2, pad=3)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')

    title6 = Label(header, text=searchresult, fg="White", bg="grey", font="Verdana 17 bold", )
    title6.grid(row=0, column=1, padx=(78, 0))
    allList.append(title6)

    laabel1 = Label(content, text="Personal Best Time", font="Arial 15 bold")
    laabel1.grid(row=0, column=1, padx=(10, 0), pady=(5, 0))
    allList.append(laabel1)

    laabel8 = Label(content, text="________________________________", font="Arial 15 bold")
    laabel8.grid(row=1, column=1, padx=(0, 10), pady=(0, 0))
    allList.append(laabel1)

    Styles1 = StringVar()
    Styles1.set(Style[0])  # default value
    DropdownStyle1 = OptionMenu(Footer, Styles1, *Style)
    DropdownStyle1.grid(row=1, column=0, pady=(0, 0))
    allList.append(DropdownStyle1)

    PersonalBest(Styles1, AUTOBHOP_list1, Sideways_list1, HalfSideways_list1, Donly_list1, AOnly_list1, WOnly_list1,ScrollNormal_list1, EasyScroll_list1, Stamina_list1, Slowmotion_list1, LowGravity_list1)

    MapList_button = tk.Button(Footer, text='Display', command=lambda: PersonalBest(Styles1, AUTOBHOP_list1, Sideways_list1, HalfSideways_list1, Donly_list1, AOnly_list1, WOnly_list1,ScrollNormal_list1, EasyScroll_list1, Stamina_list1, Slowmotion_list1, LowGravity_list1))
    MapList_button.grid(row=1, column=1, padx=(7, 0),pady=(0, 0))
    allList.append(MapList_button)

    laabel2 = Label(Footer, text="Style:", font="Arial 15 bold")
    laabel2.grid(row=2, column=0, padx=(6, 0), pady=(10, 0))
    allList.append(laabel2)

    laabel3 = Label(Footer, text="Time:", font="Arial 15 bold")
    laabel3.grid(row=3, column=0, padx=(6, 0), pady=(10, 0))
    allList.append(laabel3)

    laabel4 = Label(Footer, text="Tick Rate:", font="Arial 15 bold")
    laabel4.grid(row=4, column=0, padx=(0, 20), pady=(10, 0))
    allList.append(laabel4)

    WRupdate(WRstyle_list,WRtime_list,WRtickrate_list)


def WRupdate(WRstyle_list,WRtime_list,WRtickrate_list):
    print("test",WRstyle_list)
    print("test",WRtime_list)
    print("test",WRtickrate_list)

    w = len(WRstyle_list)
    w = w-1
    print(w)

    q = len(WRtime_list)
    q = q - 1
    print(q)

    e = len(WRtickrate_list)
    e = e - 1
    print(e)

    print(WRstyle_list)
    print(WRtime_list)
    print(WRtickrate_list)


    WRstyle = WRstyle_list[w]
    WRtime = WRtime_list[q]
    WRtickrate = WRtickrate_list[e]


    laabel5 = Label(Footer, text=WRstyle, font="Arial 15 bold")
    laabel5.grid(row=2, column=1, padx=(5, 0), pady=(10, 0))
    allList.append(laabel5)

    laabel6= Label(Footer, text=WRtime, font="Arial 15 bold")
    laabel6.grid(row=3, column=1, padx=(5, 0), pady=(10, 0))
    allList.append(laabel6)

    laabel7 = Label(Footer, text=WRtickrate, font="Arial 15 bold")
    laabel7.grid(row=4, column=1, padx=(5, 0), pady=(10, 0))
    allList.append(laabel7)


def PersonalBest(Styles1,AUTOBHOP_list1,Sideways_list1,HalfSideways_list1,Donly_list1,AOnly_list1,WOnly_list1,ScrollNormal_list1,EasyScroll_list1,Stamina_list1,Slowmotion_list1,LowGravity_list1):

    Style1 = Styles1.get()
    print(Style1)

    if Style1 == "AUTO-BHOP   ":
        WRstyle = AUTOBHOP_list1[0][0]
        WRtime =  AUTOBHOP_list1[0][1]
        WRtickrate = AUTOBHOP_list1[0][2]

    elif Style1 == "Sideways":
        WRstyle = Sideways_list1[0][0]
        WRtime =  Sideways_list1[0][1]
        WRtickrate = Sideways_list1[0][2]

    elif Style1 == "Half-Sideways":
        WRstyle = HalfSideways_list1[0][0]
        WRtime = HalfSideways_list1[0][1]
        WRtickrate = HalfSideways_list1[0][2]

    elif Style1 == "D-Only":
        WRstyle = Donly_list1[0][0]
        WRtime = Donly_list1[0][1]
        WRtickrate = Donly_list1[0][2]


    elif Style1 == "A-Only":
        WRstyle = AOnly_list1[0][0]
        WRtime = AOnly_list1[0][1]
        WRtickrate = AOnly_list1[0][2]

    elif Style1 == "W-Only":
        WRstyle = WOnly_list1[0][0]
        WRtime = WOnly_list1[0][1]
        WRtickrate = WOnly_list1[0][2]

    elif Style1 == "Scroll/Normal":
        WRstyle = ScrollNormal_list1[0][0]
        WRtime = ScrollNormal_list1[0][1]
        WRtickrate = ScrollNormal_list1[0][2]

    elif Style1 == "Easy Scroll":
        WRstyle = EasyScroll_list1[0][0]
        WRtime = EasyScroll_list1[0][1]
        WRtickrate = EasyScroll_list1[0][2]

    elif Style1 == "Stamina":
        WRstyle = Stamina_list1[0][0]
        WRtime = Stamina_list1[0][1]
        WRtickrate = Stamina_list1[0][2]

    elif Style1 == "Slowmotion":
        WRstyle = Slowmotion_list1[0][0]
        WRtime = Slowmotion_list1[0][1]
        WRtickrate = Slowmotion_list1[0][2]

    elif Style1 == "Low-Gravity":
        WRstyle = LowGravity_list1[0][0]
        WRtime = LowGravity_list1[0][1]
        WRtickrate = LowGravity_list1[0][2]

    print(WRstyle)
    print(WRtime)
    print(WRtickrate)

    WRstyle_list.append(WRstyle)
    WRtime_list.append(WRtime)
    WRtickrate_list.append(WRtickrate)

    print(WRstyle_list)
    print(WRtime_list)
    print(WRtickrate_list)

    WRupdate(WRstyle_list, WRtime_list, WRtickrate_list)






def view_func(SearchMap):
    mapquery = SearchMap.get()
    searchresult = ("test")
    hide()

    for i in maplist_list:
        if i == mapquery:
            searchresult = i
            print(searchresult)
        else:
            print("nothing found")

    if searchresult != ("test"):
        file = open('./maps/'+searchresult, "r")
        viewmapall_list = []

        for line in file:
            line = line.strip('\n')
            line = line.split(",")
            viewmapall_list.append(line)

        print(viewmapall_list)
        new_list = sorted(viewmapall_list, key=lambda x: x[1])

        stylelist_list = viewmapall_list

        AUTOBHOP_list = []
        Sideways_list = []
        HalfSideways_list = []
        Donly_list = []
        AOnly_list = []
        WOnly_list = []
        ScrollNormal_list = []
        EasyScroll_list = []
        Stamina_list = []
        Slowmotion_list = []
        LowGravity_list = []

        for i in stylelist_list:

            if i[0] == "AUTO-BHOP   ":
                AUTOBHOP_list.append(i)

            if i[0] == "Sideways":
                Sideways_list.append(i)

            if i[0] == "Half-Sideways":
                HalfSideways_list.append(i)

            if i[0] == "D-Only":
                Donly_list.append(i)

            if i[0] == "A-Only":
                AOnly_list.append(i)

            if i[0] == "W-Only":
                WOnly_list.append(i)

            if i[0] == "Scroll/Normal":
                ScrollNormal_list.append(i)

            if i[0] == "Easy Scroll":
                EasyScroll_list.append(i)

            if i[0] == "Stamina":
                Stamina_list.append(i)

            if i[0] == "Slowmotion":
                Slowmotion_list.append(i)

            if i[0] == "Low-Gravity":
                LowGravity_list.append(i)

        AUTOBHOP_list1 = sorted(AUTOBHOP_list, key=lambda x: x[1])
        Sideways_list1 = sorted(Sideways_list, key=lambda x: x[1])
        HalfSideways_list1 = sorted(HalfSideways_list, key=lambda x: x[1])
        Donly_list1 = sorted(Donly_list, key=lambda x: x[1])
        AOnly_list1 = sorted(AOnly_list, key=lambda x: x[1])
        WOnly_list1 = sorted(WOnly_list, key=lambda x: x[1])
        ScrollNormal_list1 = sorted(ScrollNormal_list, key=lambda x: x[1])
        EasyScroll_list1 = sorted(EasyScroll_list, key=lambda x: x[1])
        Stamina_list1 = sorted(Stamina_list, key=lambda x: x[1])
        Slowmotion_list1 = sorted(Slowmotion_list, key=lambda x: x[1])
        LowGravity_list1  = sorted(LowGravity_list, key=lambda x: x[1])



        mapdisplay(AUTOBHOP_list1,Sideways_list1,HalfSideways_list1,Donly_list1,AOnly_list1,WOnly_list1,ScrollNormal_list1,EasyScroll_list1,Stamina_list1,Slowmotion_list1,LowGravity_list1,searchresult)

        #print(searchresult)
        #for i in viewmapall_list:
        #    print("Line",counter)
        #    print(i[0])
        #    print(i[1])
        #    print(i[2])
        #    counter+=1

    else:
        print("Entered Invalid")



def select_item(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    SearchMap.set(value)

    x = len(back_list)
    y = 0
    if x > 1:
        y = (x - 1)

    page = back_list[y]

    if page == "Delete":
        MapDeleteSearch.set(value)

    elif page == "AddPage":
        MapAddSearch.set(value)

    elif page == "View":
        SearchMap.set(value)

def backbutton():
    x = len(back_list)
    y = 0
    if x > 1:
       y = (x-1)

    page = back_list.pop(y)

    if page == "Delete":
        hide()
        delete()

    elif page == "AddPage":
        hide()
        addpage()

    elif page == "View":
        hide()
        view()

def AddFile(mapinput, styles, TimeAdd, statusSelect):
    map = mapinput.get()
    style = styles.get()
    time = TimeAdd.get()
    tickrate = statusSelect.get()
    k=True
    print(map)

    for i in maplist_list:
        if i == map:
            k = False

    if k == True:
        file = open("maplist", "a")
        file.write(map+",\n")
        file.close()

    fi = open('./maps/'+map, "a")
    fi.write(style)
    fi.write(","+time)
    fi.write(","+tickrate+"\n")
    fi.close()
    return

##################################################################################################################

def addpage():
    root.geometry('250x300')
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

    entry1 = Entry(content, textvariable=MapAddSearch, width=16)
    entry1.grid(row=0, column=1,pady=(10,0))
    allList.append(entry1)
    MapList_button = tk.Button(content, text='Map List', command=maplist)
    MapList_button.grid(row=1, column=1,padx=(76,0))
    allList.append(MapList_button)

    ###################
    ##################


    Label8 = Label(content, text="STYLE:", font="Arial 14 bold")
    Label8.grid(row=2, column=0,pady=(10, 0))
    allList.append(Label8)
    Styles = StringVar()
    Styles.set(Style[0])  # default value
    DropdownStyle = OptionMenu(content, Styles, *Style)
    DropdownStyle.grid(row=2, column=1,pady=(10, 0))
    allList.append(DropdownStyle)

    TimeAdd = StringVar()
    Label9 = Label(content, text="TIME:", font="Arial 14 bold")
    Label9.grid(row=5, column=0,pady=(10, 0))
    allList.append(Label9)
    entry2 = Entry(content, textvariable=TimeAdd, width=16)
    entry2.grid(row=5, column=1,pady=(10,0))
    allList.append(entry2)

    Label10 = Label(content, text="TICK", font="Arial 14 bold")
    Label10.grid(row=7, column=0,pady=(10, 0))
    allList.append(Label10)
    Label11 = Label(content, text="RATE:", font="Arial 14 bold")
    Label11.grid(row=8, column=0)
    allList.append(Label11)

    statusSelect = StringVar()
    Tick128 = Radiobutton(content, text="128 Tick Rate", variable=statusSelect, value="128")
    Tick128.grid(row=7, column=1,padx=(0,10))
    allList.append(Tick128)
    Tick100 = Radiobutton(content, text="100 Tick Rate", variable=statusSelect, value="100")
    Tick100.grid(row=8, column=1,padx=(0,10))
    allList.append(Tick100)
    Tick64 = Radiobutton(content, text=" 64 Tick Rate", variable=statusSelect, value="64")
    Tick64.grid(row=9, column=1, padx=(0,14))
    allList.append(Tick64)

    MapConfirm_button4 = tk.Button(Footer, text= "Add Time", width=10, command=lambda: AddFile(MapAddSearch, Styles, TimeAdd, statusSelect))
    MapConfirm_button4.grid(row=10, column=1, pady=(0,10), padx=(5,0))
    allList.append(MapConfirm_button4)

    Home_button1 = tk.Button(Footer, text= "Home", command=home, width=10)
    Home_button1.grid(row=10, column=0, pady=(0,10), padx=(0,5))
    allList.append(Home_button1)

    back_list.append("AddPage")



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
    title.grid(row=0, column=0, padx=(25,30))
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

    quit_button = tk.Button(Footer, text='Quit', width=15, command=root.destroy)
    quit_button.grid(row=5, column=0)
    allList.append(quit_button)
##################################################################################################################


def view():
    root.geometry('250x305')
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

    entry3 = Entry(content, textvariable=SearchMap, width=20)
    entry3.grid(row=1, column=0, padx=(28, 0))
    allList.append(entry3)

    listbox1 = tk.Listbox(Footer, width=20, height=10)
    listbox1.grid(row=3, column=0, padx=(28, 0))
    # create a vertical scrollbar to the right of the listbox
    yscroll1 = tk.Scrollbar(Footer, command=listbox1.yview, orient=tk.VERTICAL)
    yscroll1.grid(row=3, column=1, sticky='ns')
    listbox1.configure(yscrollcommand=yscroll1.set)
    listbox1.bind('<<ListboxSelect>>', select_item)
    # now load the listbox with data
    for item in maplist_list:
        # insert each new item to the end of the listbox
        listbox1.insert('end', item)

    allList.append(listbox1)
    allList.append(yscroll1)

    Home_button2 = tk.Button(gider, text="Home", command=home, width=5)
    Home_button2.grid(row=0, column=0, padx=(32,0))
    allList.append(Home_button2)

    view_button1 = tk.Button(gider, text= "View", command=lambda: view_func(SearchMap),width=5)
    view_button1.grid(row=0, column=1,padx=(30,0))
    allList.append(view_button1)


    back_list.append("View")
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
    root.geometry('250x385')
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

    entry4 = Entry(content, textvariable=MapDeleteSearch, width=18)
    entry4.grid(row=1, column=0, padx=(37,0))
    allList.append(entry4)

    MapList_button2 = tk.Button(content, text='Map List', command=maplist)
    MapList_button2.grid(row=2, column=0, padx=(40, 80))
    allList.append(MapList_button2)
    MapConfirm_button6 = tk.Button(content, text="Confirm", command=maplist)
    MapConfirm_button6.grid(row=2, column=0, padx=(116, 0))
    allList.append(MapConfirm_button6)

    Label17 = Label(content, text="Map Select", font="Arial 15 bold")
    Label17.grid(row=3, column=0, pady=(10, 0), padx=(40, 0))
    allList.append(Label17)

    Mapselect = StringVar()
    Mapselect.set(MapSearchList1[0])  # default value
    DropdownMapSelect = OptionMenu(content, Mapselect, *MapSearchList1)
    DropdownMapSelect.grid(row=4, column=0, padx=(40,0))
    allList.append(DropdownMapSelect)

    delete1_button = tk.Button(content, text='Delete Map', command=home)
    delete1_button.grid(row=5, column=0, padx=(40, 80))
    allList.append(delete1_button)
    select_button = tk.Button(content, text="Select", command=home)
    select_button.grid(row=5, column=0, padx=(130, 0))
    allList.append(select_button)

    Label18 = Label(content, text="Style Select", font="Arial 15 bold")
    Label18.grid(row=6, column=0, pady=(10, 0), padx=(40, 0))
    allList.append(Label18)

    StyleSelect = StringVar()
    StyleSelect.set(StyleSelect_list[0])  # default value
    DropdownStyleSelect = OptionMenu(content, StyleSelect, *StyleSelect_list)
    DropdownStyleSelect.grid(row=7, column=0, padx=(35, 0))
    allList.append(DropdownStyleSelect)

    Label19 = Label(content, text="Time Select", font="Arial 15 bold")
    Label19.grid(row=8, column=0, pady=(10, 0), padx=(40, 0))
    allList.append(Label19)

    TimeSelect = StringVar()
    TimeSelect.set(TimeSelect_list[0])  # default value
    DropdownTimeSelect = OptionMenu(content, TimeSelect, *TimeSelect_list)
    DropdownTimeSelect.grid(row=9, column=0, padx=(35, 0))
    allList.append(DropdownTimeSelect)

    delete2_button = tk.Button(content, text="Delete", command=home)
    delete2_button.grid(row=10, column=0, padx=(30, 0))
    allList.append(delete2_button)
    Home_button4 = tk.Button(content, text='Home', command=home)
    Home_button4.grid(row=11, column=0, padx=(0, 140), pady=(0, 10))
    allList.append(Home_button4)

    back_list.append("Delete")
##################################################################################################################


def maplist():
    root.geometry('250x300')
    hide()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, pad=1)
    root.rowconfigure(1, pad=2)
    root.rowconfigure(2, pad=1)
    root.rowconfigure(3, pad=1)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')
    gider.grid(row=3, sticky='news')

##############################################

    title5 = Label(header, text="Map List", fg="White", bg="grey", font="Verdana 17 bold", )
    title5.grid(row=0, column=0, padx=(86, 0))
    allList.append(title5)

    Label20 = Label(content, text="Maps", font="Arial 15 bold")
    Label20.grid(row=0, column=0, padx=(110, 0))
    allList.append(Label20)


    listbox = tk.Listbox(Footer, width=20, height=12)
    listbox.grid(row=0, column=0, padx=(28,0))
    # create a vertical scrollbar to the right of the listbox
    yscroll = tk.Scrollbar(Footer,command=listbox.yview, orient=tk.VERTICAL)
    yscroll.grid(row=0, column=1, sticky='ns')
    listbox.configure(yscrollcommand=yscroll.set)
    listbox.bind('<<ListboxSelect>>', select_item)
    # now load the listbox with data
    for item in maplist_list:
    # insert each new item to the end of the listbox
        listbox.insert('end', item)

    allList.append(listbox)
    allList.append(yscroll)

    back_button = tk.Button(gider, text="Back", command=backbutton, width=6)
    back_button.grid(row=0, column=0, padx=(24, 0), pady=(10,0))
    allList.append(back_button)

    home2_button = tk.Button(gider, text="Home", command=home, width=6)
    home2_button.grid(row=0, column=1, padx=(25,0), pady=(10,0))
    allList.append(home2_button)

##################################################################################################################


def home():
    hide()
    MainWindowLayout()
    MainPage()

##################################################################################################################


def MainWindowLayout():
    root.geometry('250x320')
    root.columnconfigure(0, weight=1) # 100%

    root.rowconfigure(0, pad=3) # 10%
    root.rowconfigure(1, pad=13) # 30%
    root.rowconfigure(2, pad=13) # 60%

    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')
###################################################################################################################

MapDeleteSearch = StringVar(root, value="")
SearchMap = StringVar(root, value="")
MapAddSearch = StringVar(root, value="")
MainWindowLayout()
MainPage()
root.mainloop()