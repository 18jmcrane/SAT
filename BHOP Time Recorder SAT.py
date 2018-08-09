from tkinter import *
import tkinter as tk
import os
from operator import itemgetter
##################################################################################################################
#All these Lists are used as a way to make it accessable globally, without using GLOBAL command or Classes.
# This allow Data to be stored between multiple funtions
maplist_list = []
back_list = []
WRstyle_list = []
WRtime_list = []
WRtickrate_list = []
allList = []
##################################################################################################################

#These List are used for preset selections, for dropdown boxes. A way to preseleect what the user can choose from.
Style = ["AUTO-BHOP   ",
         "Sideways",
         "Half-Sideways",
         "D-Only","A-Only",
         "W-Only",
         "Scroll/Normal",
         "Easy Scroll","Stamina",
         "Slowmotion","Low-Gravity"]

#This is used in Dropboxes to make it look more appealing, when first seen before being updated with other selections.
TimeSelect_list = ["Select Time"]
MapSearchList = ["Select A Map"]
MapSearchList1 = ["Select A Map"]


#This opens the maplist file and receives all the data inside the file, using ","
# as a way to distinguish which data is which and append the element into a list(maplist_list)
f = open("maplist", "r")
for line in f:
    line = line.strip('\n')
    line = line.split(",")
    maplist_list.append(line[0])

root = tk.Tk()
root.title("BHOP Time Recorder")
header = tk.Frame(root, bg='grey')
content = tk.Frame(root, bg='white')
Footer = tk.Frame(root, bg='white')
gider = tk.Frame(root, bg="white")
Lower = tk.Frame(root, bg="white")
Bottom = tk.Frame(root, bg="white")


##################################################################################################################

##################################################################################################################
#
#                                                    FUNTIONS
#
##################################################################################################################

#This Funtion is used for the multiple page effect, this removes the Layout after each page change,
# so spacings and Frames can be better adjusted giving the effect that its a different page

#Aswell hides all everything displayed on the page,
# so that new content can be displayed instead through the use of the "allremove" funtion
def hide():
    header.grid_remove()
    content.grid_remove()
    Footer.grid_remove()
    allremove()
##################################################################################################################
def WRupdate(WRstyle_list, WRtime_list, WRtickrate_list, WRlabel1, WRlabel2, WRlabel3):

    w = len(WRstyle_list)
    w = w-1

    q = len(WRtime_list)
    q = q - 1

    e = len(WRtickrate_list)
    e = e - 1

    WRstyle = WRstyle_list[w]
    WRtime = WRtime_list[q]
    WRtickrate = WRtickrate_list[e]

    WRlabel1.set(WRstyle)
    WRlabel2.set(WRtime)
    WRlabel3.set(WRtickrate)


def PersonalBest(Styles1,AUTOBHOP_list1,Sideways_list1,HalfSideways_list1,Donly_list1,AOnly_list1,WOnly_list1,ScrollNormal_list1,EasyScroll_list1,Stamina_list1,Slowmotion_list1,LowGravity_list1, WRlabel1, WRlabel2, WRlabel3):

    Style1 = Styles1.get()

    if Style1 == "AUTO-BHOP   ":
        WRstyle = AUTOBHOP_list1[0][0]
        WRtime =  AUTOBHOP_list1[0][1]
        WRtickrate = AUTOBHOP_list1[0][2]
        listvariable = AUTOBHOP_list1

    elif Style1 == "Sideways":
        WRstyle = Sideways_list1[0][0]
        WRtime =  Sideways_list1[0][1]
        WRtickrate = Sideways_list1[0][2]
        listvariable = Sideways_list1

    elif Style1 == "Half-Sideway":
        WRstyle = HalfSideways_list1[0][0]
        WRtime = HalfSideways_list1[0][1]
        WRtickrate = HalfSideways_list1[0][2]
        listvariable = HalfSideways_list1

    elif Style1 == "D-Only":
        WRstyle = Donly_list1[0][0]
        WRtime = Donly_list1[0][1]
        WRtickrate = Donly_list1[0][2]
        listvariable = Donly_list1


    elif Style1 == "A-Only":
        WRstyle = AOnly_list1[0][0]
        WRtime = AOnly_list1[0][1]
        WRtickrate = AOnly_list1[0][2]
        listvariable = AOnly_list1

    elif Style1 == "W-Only":
        WRstyle = WOnly_list1[0][0]
        WRtime = WOnly_list1[0][1]
        WRtickrate = WOnly_list1[0][2]
        listvariable = WOnly_list1

    elif Style1 == "Scroll/Normal":
        WRstyle = ScrollNormal_list1[0][0]
        WRtime = ScrollNormal_list1[0][1]
        WRtickrate = ScrollNormal_list1[0][2]
        listvariable = ScrollNormal_list1

    elif Style1 == "Easy Scroll":
        WRstyle = EasyScroll_list1[0][0]
        WRtime = EasyScroll_list1[0][1]
        WRtickrate = EasyScroll_list1[0][2]
        listvariable = EasyScroll_list1

    elif Style1 == "Stamina":
        WRstyle = Stamina_list1[0][0]
        WRtime = Stamina_list1[0][1]
        WRtickrate = Stamina_list1[0][2]
        listvariable = Stamina_list1

    elif Style1 == "Slowmotion":
        WRstyle = Slowmotion_list1[0][0]
        WRtime = Slowmotion_list1[0][1]
        WRtickrate = Slowmotion_list1[0][2]
        listvariable = Slowmotion_list1

    elif Style1 == "Low-Gravity":
        WRstyle = LowGravity_list1[0][0]
        WRtime = LowGravity_list1[0][1]
        WRtickrate = LowGravity_list1[0][2]
        listvariable = LowGravity_list1


    WRstyle_list.append(WRstyle)
    WRtime_list.append(WRtime)
    WRtickrate_list.append(WRtickrate)

    WRupdate(WRstyle_list, WRtime_list, WRtickrate_list, WRlabel1, WRlabel2, WRlabel3)
    timelist(listvariable)



def view_func(SearchMap):
    mapquery = SearchMap.get()
    searchresult = ("test")
    hide()

    for i in maplist_list:
        if i == mapquery:
            searchresult = i

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


def ClearWipe(ClearWipeQuerry):
    ClearQuerry = ClearWipeQuerry.get()
    if ClearQuerry == "yes":
        for i in maplist_list:
            try:
                os.remove("maps/"+i)
            except OSError as e:  ## if failed, report it back to the user ##
                print("Error: %s - %s." % (e.filename, e.strerror))

        f = open("maplist", "w")
        f.close()


def allremove():
    for i in allList:
        i.grid_remove()

def DeleteLine(TimeSelect, MapStyle, mapquery, TimeList_list):
    MapName = mapquery
    Timechoice = TimeSelect.get()
    print(TimeList_list, "desss")

    for i in TimeList_list:
        if MapStyle == i[0] and Timechoice == i[1]:
            deletetickrate = i[2]
            print(deletetickrate)

    f = open('./maps/' + MapName, "r+")
    d = f.readlines()
    print(d)
    f.seek(0)
    for i in d:
        if i != MapStyle + "," + Timechoice + "," + deletetickrate + "\n":
            f.write(i)
    f.truncate()
    f.close()



def deleteupdate(MapDeleteSearch, StyleSelect1):
    mapquery = MapDeleteSearch.get()
    MapStyle = StyleSelect1.get()
    searchresult = ("test")

    for i in maplist_list:
        if i == mapquery:
            searchresult = i

    if searchresult != ("test"):
        file = open('./maps/' + searchresult, "r")
        viewmapall_list = []

        for line in file:
            line = line.strip('\n')
            line = line.split(",")
            viewmapall_list.append(line)

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

        if MapStyle == "AUTO-BHOP   ":
            AUTOBHOP_list1 = sorted(AUTOBHOP_list, key=lambda x: x[1])
            print(AUTOBHOP_list1)
            TimeList_list = AUTOBHOP_list1

        if MapStyle == "Sideways":
            Sideways_list1 = sorted(Sideways_list, key=lambda x: x[1])
            print(Sideways_list1)
            TimeList_list = Sideways_list1

        if MapStyle == "Half-Sideways":
            HalfSideways_list1 = sorted(HalfSideways_list, key=lambda x: x[1])
            print(HalfSideways_list1)
            TimeList_list = HalfSideways_list1

        if MapStyle == "D-Only":
            Donly_list1 = sorted(Donly_list, key=lambda x: x[1])
            print(Donly_list1)
            TimeList_list = Donly_list1

        if MapStyle == "A-Only":
            AOnly_list1 = sorted(AOnly_list, key=lambda x: x[1])
            print(AOnly_list1)
            TimeList_list = AOnly_list1

        if MapStyle == "W-Only":
            WOnly_list1 = sorted(WOnly_list, key=lambda x: x[1])
            print(WOnly_list1)
            TimeList_list = WOnly_list1

        if MapStyle == "Scroll/Normal":
            ScrollNormal_list1 = sorted(ScrollNormal_list, key=lambda x: x[1])
            print(ScrollNormal_list1)
            TimeList_list = ScrollNormal_list1

        if MapStyle == "Easy Scroll":
            EasyScroll_list1 = sorted(EasyScroll_list, key=lambda x: x[1])
            print(EasyScroll_list1)
            TimeList_list = EasyScroll_list1

        if MapStyle == "Stamina":
            Stamina_list1 = sorted(Stamina_list, key=lambda x: x[1])
            print(Stamina_list1)
            TimeList_list = Stamina_list1

        if MapStyle == "Slowmotion":
            Slowmotion_list1 = sorted(Slowmotion_list, key=lambda x: x[1])
            print(Slowmotion_list1)
            TimeList_list = Slowmotion_list1

        if MapStyle == "Low-Gravity":
            LowGravity_list1 = sorted(LowGravity_list, key=lambda x: x[1])
            print(LowGravity_list1)
            TimeList_list = LowGravity_list1

        for i in TimeList_list:
            TimeSelect_list.append(i[1])

        TimeUpdate(TimeSelect_list, MapStyle, mapquery, TimeList_list)

def DeleteMap(MapDeleteSearch):
    Fileinput = MapDeleteSearch.get()
    FileDelete = "maps/" + Fileinput
    ## Try to delete the file ##
    error = False
    try:
        os.remove(FileDelete)
    except OSError as e:  ## if failed, report it back to the user ##
        error = True
        print("Error: %s - %s." % (e.filename, e.strerror))

    f = open("maplist", "r+")
    d = f.readlines()
    print(d)
    f.seek(0)
    for i in d:
        if i != Fileinput + "," + "\n":
            f.write(i)
    f.truncate()
    f.close()
    return error


def home():
    hide()
    MainWindowLayout()
    MainPage()

##################################################################################################################
##################################################################################################################

##################################################################################################################
#
#                                                    GUI
#
##################################################################################################################

#This Funtion is used to display the Map details through the view funtion, it is the GUI of the page and is called after
# a listbox page where a map is selected.
def mapdisplay(AUTOBHOP_list1,Sideways_list1,HalfSideways_list1,Donly_list1,AOnly_list1,WOnly_list1,ScrollNormal_list1,EasyScroll_list1,Stamina_list1,Slowmotion_list1,LowGravity_list1,searchresult):

    #Below shows the configuration of the size of the Window and each of the frames(header,content,Footer,gider,Lower,Bottom)
    # and determined order through the rowconfigure, size through the "pad" command.
    #This is the "Window configuration block"
    root.geometry('270x420')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, pad=3)
    root.rowconfigure(1, pad=10)
    root.rowconfigure(2, pad=3)
    root.rowconfigure(3, pad=3)
    root.rowconfigure(4, pad=3)
    root.rowconfigure(5, pad=3)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')
    gider.grid(row=3, sticky='news')
    Lower.grid(row=4, sticky='news')
    Bottom.grid(row=5, sticky='news')

    #Creates the Title or header at the top of the page. With a grey background and a font of "Verdana 17 bold".
    #This has uses a variable to find the map name selected then display it.
    title6 = Label(header, text=searchresult, fg="White", bg="grey", font="Verdana 17 bold", )
    #Actually displays the label in a designated position through the use of grid
    title6.grid(row=0, column=1, padx=(78, 0))
    #Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(title6)

    #Creates the "Person Best Time" subheading, displayed when mapdisplay() is activated
    laabel1 = Label(content, text="Personal Best Time", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel1.grid(row=0, column=1, padx=(10, 0), pady=(5, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel1)

    laabel8 = Label(content, text="________________________________", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel8.grid(row=1, column=1, padx=(0, 10), pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel8)

    Styles1 = StringVar()
    Styles1.set(Style[0])  # default value
    DropdownStyle1 = OptionMenu(Footer, Styles1, *Style)
    # displays the dropdown box in a designated position through the use of grid
    DropdownStyle1.grid(row=1, column=0, pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(DropdownStyle1)

    WRlabel1 = StringVar()
    WRlabel2 = StringVar()
    WRlabel3 = StringVar()


    PersonalBest(Styles1, AUTOBHOP_list1, Sideways_list1, HalfSideways_list1, Donly_list1, AOnly_list1, WOnly_list1,ScrollNormal_list1, EasyScroll_list1, Stamina_list1, Slowmotion_list1, LowGravity_list1, WRlabel1, WRlabel2, WRlabel3)


    laabel5 = Label(Footer, textvariable=WRlabel1, font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel5.grid(row=2, column=1, padx=(5, 0), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel5)

    laabel6 = Label(Footer, textvariable=WRlabel2, font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel6.grid(row=3, column=1, padx=(5, 0), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel6)

    laabel7 = Label(Footer, textvariable=WRlabel3, font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel7.grid(row=4, column=1, padx=(5, 0), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel7)

    MapList_button = tk.Button(Footer, text='Display', command=lambda: PersonalBest(Styles1, AUTOBHOP_list1,
        Sideways_list1, HalfSideways_list1, Donly_list1, AOnly_list1, WOnly_list1,ScrollNormal_list1, EasyScroll_list1,
        Stamina_list1, Slowmotion_list1, LowGravity_list1, WRlabel1, WRlabel2, WRlabel3))
    # Actually displays the label in a designated position through the use of grid
    MapList_button.grid(row=1, column=1, padx=(7, 0),pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(MapList_button)

    laabel2 = Label(Footer, text="Style:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel2.grid(row=2, column=0, padx=(6, 0), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel2)

    laabel3 = Label(Footer, text="Time:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel3.grid(row=3, column=0, padx=(6, 0), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel3)

    laabel4 = Label(Footer, text="Tick Rate:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel4.grid(row=4, column=0, padx=(0, 20), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel4)

    laabel9 = Label(gider, text="________________________________", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel9.grid(row=0, column=0, padx=(0, 10), pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel9)

    laabel10 = Label(Lower, text="Style:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel10.grid(row=1, column=0, padx=(30, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel10)

    laabel11 = Label(Lower, text="Time:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel11.grid(row=1, column=1, padx=(40, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel11)

    laabel12 = Label(Lower, text="Tick:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel12.grid(row=1, column=2, padx=(20, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel12)

    back_button1 = tk.Button(Bottom, text="Back", command=view, width=6)
    # Actually displays the label in a designated position through the use of grid
    back_button1.grid(row=3, column=0, padx=(0, 140), pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    #  through the use of "grid_remove"
    allList.append(back_button1)

    home3_button = tk.Button(Bottom, text="Home", command=home, width=6)
    # Actually displays the label in a designated position through the use of grid
    home3_button.grid(row=3, column=0, padx=(140,0), pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    #  through the use of "grid_remove"
    allList.append(home3_button)

    WRupdate(WRstyle_list, WRtime_list, WRtickrate_list, WRlabel1, WRlabel2, WRlabel3)


def timelist(listvariable):
    print(listvariable)

    listbox2 = tk.Listbox(Bottom, width=25, height=6)
    # displays the Listbox in a designated position through the use of grid
    listbox2.grid(row=2, column=0, padx=(10, 10))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(listbox2)
    # create a vertical scrollbar to the right of the listbox
    yscroll2 = tk.Scrollbar(Bottom, command=listbox2.yview, orient=tk.VERTICAL)
    #displays the ScrollBar in a designated position through the use of grid
    yscroll2.grid(row=2, column=1, sticky='ns')
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(yscroll2)
    listbox2.configure(yscrollcommand=yscroll2.set)
    # now load the listbox with data
    for item in listvariable:
        # insert each new item to the end of the listbox
        listbox2.insert('end', item)

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
    # Actually displays the label in a designated position through the use of grid
    title1.grid(row=0, column=1, padx=(76,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title1)
    Label7 = Label(content, text="MAP:", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label7.grid(row=0, column=0,pady=(10,0), padx=20)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label7)

    entry1 = Entry(content, textvariable=MapAddSearch, width=16)
    # Actually displays the label in a designated position through the use of grid
    entry1.grid(row=0, column=1,pady=(10,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(entry1)
    MapList_button = tk.Button(content, text='Map List', command=maplist)
    # Actually displays the label in a designated position through the use of grid
    MapList_button.grid(row=1, column=1,padx=(76,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(MapList_button)

    ###################
    ##################


    Label8 = Label(content, text="STYLE:", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label8.grid(row=2, column=0,pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label8)
    Styles = StringVar()
    Styles.set(Style[0])  # default value
    DropdownStyle = OptionMenu(content, Styles, *Style)
    # Actually displays the label in a designated position through the use of grid
    DropdownStyle.grid(row=2, column=1,pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(DropdownStyle)

    TimeAdd = StringVar()
    Label9 = Label(content, text="TIME:", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label9.grid(row=5, column=0,pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label9)
    entry2 = Entry(content, textvariable=TimeAdd, width=16)
    # Actually displays the label in a designated position through the use of grid
    entry2.grid(row=5, column=1,pady=(10,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(entry2)

    Label10 = Label(content, text="TICK", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label10.grid(row=7, column=0,pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label10)
    Label11 = Label(content, text="RATE:", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label11.grid(row=8, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label11)

    statusSelect = StringVar()
    Tick128 = Radiobutton(content, text="128 Tick Rate", variable=statusSelect, value="128")
    # Actually displays the label in a designated position through the use of grid
    Tick128.grid(row=7, column=1,padx=(0,10))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Tick128)
    Tick100 = Radiobutton(content, text="100 Tick Rate", variable=statusSelect, value="100")
    # Actually displays the label in a designated position through the use of grid
    Tick100.grid(row=8, column=1,padx=(0,10))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Tick100)
    Tick64 = Radiobutton(content, text=" 64 Tick Rate", variable=statusSelect, value="64")
    # Actually displays the label in a designated position through the use of grid
    Tick64.grid(row=9, column=1, padx=(0,14))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Tick64)

    MapConfirm_button4 = tk.Button(Footer, text= "Add Time", width=10, command=lambda: AddFile(MapAddSearch, Styles,
                                                                                               TimeAdd, statusSelect))
    # Actually displays the label in a designated position through the use of grid
    MapConfirm_button4.grid(row=10, column=1, pady=(0,10), padx=(5,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(MapConfirm_button4)

    Home_button1 = tk.Button(Footer, text= "Home", command=home, width=10)
    # Actually displays the label in a designated position through the use of grid
    Home_button1.grid(row=10, column=0, pady=(0,10), padx=(0,5))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Home_button1)

    back_list.append("AddPage")



##################################################################################################################

def MainPage():

    title = Label(header, text="BHOP Time Recorder", fg="White", bg="grey", font="Verdana 17 bold", )
    # Actually displays the label in a designated position through the use of grid
    title.grid(row=0, column=0, padx=(25,30))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title)
    packer = Label(content, text="                   ")
    # Actually displays the label in a designated position through the use of grid
    packer.grid(row=0, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(packer)
    packer1 = Label(content, text="                   ")
    # Actually displays the label in a designated position through the use of grid
    packer1.grid(row=0, column=2)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(packer1)
    Label1 = Label(content, text="Welcome User")
    # Actually displays the label in a designated position through the use of grid
    Label1.grid(row=0, column=1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label1)
    Label4 = Label(content, text="Previous Map:")
    # Actually displays the label in a designated position through the use of grid
    Label4.grid(row=1, column=1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label4)
    PrevMap = StringVar()
    PrevMap.set("")
    Label5 = Label(content, textvariable=PrevMap)
    # Actually displays the label in a designated position through the use of grid
    Label5.grid(row=2, column = 1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label5)
    Label2 = Label(content, text="Previous Time:")
    # Actually displays the label in a designated position through the use of grid
    Label2.grid(row=3, column=1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label2)
    PrevTime = DoubleVar()
    PrevTime.set(0.0)
    Label3 = Label(content, textvariable=PrevTime)
    # Actually displays the label in a designated position through the use of grid
    Label3.grid(row=4, column=1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label3)

    try:
        position_maplist = len(maplist_list)
        position_maplist = position_maplist - 1

        MapPrevious = maplist_list[position_maplist]
        PrevMap.set(MapPrevious)

        PrevTime_List = []
        mapfile = open('./maps/' + MapPrevious, "r")
        for line in mapfile:
            line = line.strip('\n')
            line = line.split(",")
            PrevTime_List.append(line)

        TimePosition = len(PrevTime_List)
        TimePrevious = TimePosition - 1

        PrevTime_final = PrevTime_List[TimePrevious][1]
        PrevTime.set(PrevTime_final)
        print(PrevTime_List)

    except:
        PrevMap.set("")


    Label6 = Label(Footer, text="_________________________________________")
    # Actually displays the label in a designated position through the use of grid
    Label6.grid(row=0, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label6)

    add_button = tk.Button(Footer, text='Add Time', width=15, command=addpage)
    # Actually displays the label in a designated position through the use of grid
    add_button.grid(row=1, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(add_button)

    view_button = tk.Button(Footer, text='View', width=15, command=view)
    # Actually displays the label in a designated position through the use of grid
    view_button.grid(row=2, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(view_button)

    delete_button = tk.Button(Footer, text='Delete', width=15, command=delete)
    # Actually displays the label in a designated position through the use of grid
    delete_button.grid(row=3, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(delete_button)

    settings_button = tk.Button(Footer, text='Settings', width=15, command=settings)
    # Actually displays the label in a designated position through the use of grid
    settings_button.grid(row=4, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(settings_button)

    quit_button = tk.Button(Footer, text='Quit', width=15, command=root.destroy)
    # Actually displays the label in a designated position through the use of grid
    quit_button.grid(row=5, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
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
    # Actually displays the label in a designated position through the use of grid
    title2.grid(row=0, column=0, padx=(100, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title2)

    Label12 = Label(content, text="Search for Map", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    Label12.grid(row=0, column=0,pady=(10,0), padx=(34, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label12)

    entry3 = Entry(content, textvariable=SearchMap, width=20)
    # Actually displays the label in a designated position through the use of grid
    entry3.grid(row=1, column=0, padx=(28, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(entry3)

    listbox1 = tk.Listbox(Footer, width=20, height=10)
    # Actually displays the label in a designated position through the use of grid
    listbox1.grid(row=3, column=0, padx=(28, 0))
    # create a vertical scrollbar to the right of the listbox
    yscroll1 = tk.Scrollbar(Footer, command=listbox1.yview, orient=tk.VERTICAL)
    # Actually displays the label in a designated position through the use of grid
    yscroll1.grid(row=3, column=1, sticky='ns')
    listbox1.configure(yscrollcommand=yscroll1.set)
    listbox1.bind('<<ListboxSelect>>', select_item)
    # now load the listbox with data
    for item in maplist_list:
        # insert each new item to the end of the listbox
        listbox1.insert('end', item)

    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(listbox1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(yscroll1)

    Home_button2 = tk.Button(gider, text="Home", command=home, width=5)
    # Actually displays the label in a designated position through the use of grid
    Home_button2.grid(row=0, column=0, padx=(32,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Home_button2)

    view_button1 = tk.Button(gider, text= "View", command=lambda: view_func(SearchMap),width=5)
    # Actually displays the label in a designated position through the use of grid
    view_button1.grid(row=0, column=1,padx=(30,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
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
    # Actually displays the label in a designated position through the use of grid
    title3.grid(row=0, column=0, padx=(86, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title3)

    Label14 = Label(content, text="Clear Wipe", font="Arial 18 bold", bg="#FFF8DC")
    # Actually displays the label in a designated position through the use of grid
    Label14.grid(row=0, column=0,pady=(10,0), padx=(80, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label14)

    Label15 = Label(Footer, text="Are you sure?", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label15.grid(row=1, column=0, pady=(10, 0), padx=(71, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label15)

    ClearWipeQuerry = StringVar()
    wipeyes = Radiobutton(Footer, text="Yes", variable=ClearWipeQuerry, value="yes")
    # Actually displays the label in a designated position through the use of grid
    wipeyes.grid(row=2, column=0,padx=(65,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(wipeyes)

    confirmwipe_button = tk.Button(Footer, text="WIPE", command= lambda: ClearWipe(ClearWipeQuerry), width=5)
    # Actually displays the label in a designated position through the use of grid
    confirmwipe_button.grid(row=4, column=0, padx=(65,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(confirmwipe_button)

    Home_button3 = tk.Button(Footer, text="Home", command=home, width=5)
    # Actually displays the label in a designated position through the use of grid
    Home_button3.grid(row=5, column=0,pady=(10,0),padx=(0, 120))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Home_button3)

##################################################################################################################


##################################################################################################################

def delete():
    root.geometry('250x330')
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
    # Actually displays the label in a designated position through the use of grid
    title4.grid(row=0, column=0, padx=(92, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title4)

    Label16 = Label(content, text="Search Map", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    Label16.grid(row=0, column=0, pady=(10, 0), padx=(40, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label16)

    entry4 = Entry(content, textvariable=MapDeleteSearch, width=18)
    # Actually displays the label in a designated position through the use of grid
    entry4.grid(row=1, column=0, padx=(37,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(entry4)

    MapList_button2 = tk.Button(content, text='Map List', command=maplist)
    # displays the Button in a designated position through the use of grid
    MapList_button2.grid(row=2, column=0, padx=(20, 80))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(MapList_button2)
    MapConfirm_button6 = tk.Button(content, text="Delete Map", command= lambda: DeleteMap(MapDeleteSearch))
    # displays the Button in a designated position through the use of grid
    MapConfirm_button6.grid(row=2, column=0, padx=(116, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(MapConfirm_button6)

    Label18 = Label(content, text="Style Select", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    Label18.grid(row=3, column=0, pady=(10, 0), padx=(40, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label18)

    StyleSelect1 = StringVar()
    StyleSelect1.set(Style[0])  # default value
    DropdownStyleSelect3 = OptionMenu(content, StyleSelect1, *Style)
    # displays the dropdown box in a designated position through the use of grid
    DropdownStyleSelect3.grid(row=4, column=0, padx=(35, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(DropdownStyleSelect3)

    MapConfirm_button7 = tk.Button(content, text="Confirm", command=lambda: deleteupdate(MapDeleteSearch, StyleSelect1))
    # displays the Button in a designated position through the use of grid
    MapConfirm_button7.grid(row=5, column=0, padx=(30, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(MapConfirm_button7)

    Label19 = Label(content, text="Time Select", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    Label19.grid(row=6, column=0, pady=(10, 0), padx=(40, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label19)

    MapStyle = "AUTO-BHOP   "
    mapquery = ""
    TimeList_list = []

    TimeUpdate(TimeSelect_list, MapStyle, mapquery, TimeList_list)


def TimeUpdate(TimeSelect_list, MapStyle, mapquery, TimeList_list):

    TimeSelect = StringVar()
    TimeSelect.set(TimeSelect_list[0])  # default value
    DropdownTimeSelect = OptionMenu(content, TimeSelect, *TimeSelect_list)
    # displays the Dropdown box in a designated position through the use of grid
    DropdownTimeSelect.grid(row=7, column=0, padx=(35, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(DropdownTimeSelect)

    delete2_button = tk.Button(content, text="Delete", command= lambda: DeleteLine(TimeSelect, MapStyle,
                                                                                   mapquery, TimeList_list))
    # displays the Button in a designated position through the use of grid
    delete2_button.grid(row=10, column=0, padx=(30, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(delete2_button)

    Home_button4 = tk.Button(content, text='Home', command=home)
    # displays the Button in a designated position through the use of grid
    Home_button4.grid(row=11, column=0, padx=(0, 140), pady=(0, 10))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
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
    # Actually displays the label in a designated position through the use of grid
    title5.grid(row=0, column=0, padx=(86, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title5)

    Label20 = Label(content, text="Maps", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    Label20.grid(row=0, column=0, padx=(110, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label20)


    listbox = tk.Listbox(Footer, width=20, height=12)
    # displays the listbox in a designated position through the use of grid
    listbox.grid(row=0, column=0, padx=(28,0))
    # create a vertical scrollbar to the right of the listbox
    yscroll = tk.Scrollbar(Footer,command=listbox.yview, orient=tk.VERTICAL)
    # displays the scrollbar in a designated position through the use of grid
    yscroll.grid(row=0, column=1, sticky='ns')
    listbox.configure(yscrollcommand=yscroll.set)
    listbox.bind('<<ListboxSelect>>', select_item)
    # now load the listbox with data
    for item in maplist_list:
    # insert each new item to the end of the listbox
        listbox.insert('end', item)

    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(listbox)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(yscroll)

    back_button = tk.Button(gider, text="Back", command=backbutton, width=6)
    # displays the Button in a designated position through the use of grid
    back_button.grid(row=0, column=0, padx=(24, 0), pady=(10,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(back_button)

    home2_button = tk.Button(gider, text="Home", command=home, width=6)
    # displays the label in a designated position through the use of grid
    home2_button.grid(row=0, column=1, padx=(25,0), pady=(10,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(home2_button)

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
root.resizable(width=False, height=False)
root.mainloop()