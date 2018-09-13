#
#                                      Username = "admin"
#                                      Password = "password"
#
#

from tkinter import *
import tkinter as tk
import os
from time import sleep
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
         "Sideways     ",
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
#
#                                      Complex Algorithm Function(MergeSort)
#
##################################################################################################################

#
#
#                               Funtion Called on line 636
#
#Merge sort function, recursively sorts 2 lists


def Mergesort(listToSort):
    # Initiate the list to return
    sortedlist = []

    # Check to see if the list is only a single item, if so return the single item list
    if len(listToSort) < 2:
        #returning Value as it lacks elements
        return listToSort

    # Setting up initial variable for splitting lists
    #this will find the index of the list
    middle = int(len(listToSort)/2)

    #This will create a list, that roughly the first half of elements will be added to.
    returnedList1 = Mergesort(listToSort[:middle])
    # This will create a list, that roughly the Second half of elements will be added to.
    returnedList2 = Mergesort(listToSort[middle:])

    #This loop will run based on the total length of both lists, As it counts how many elements
    # are remaining in each list till 0 as the elements are being popped out.
    while (len(returnedList1) > 0) or (len(returnedList2) > 0):

        #If both list don't have elements it will skip this block of code.
        if len(returnedList1) > 0 and len(returnedList2) > 0:

            #Pops the data, based on which interger is smaller
            # it will add the data to the sorted list, as it is smaller. (As we are going from smallest to largest)
            if returnedList1[0] > returnedList2[0]:
                #Adding returnList2 index of 0 element to list
                sortedlist.append(returnedList2[0])
                # Removes the element off the list at Index 0
                returnedList2.pop(0)

            #If the 0 Index element of the returnList1 is smaller than the 0 Index of returnList2,
            # it will add the data to the sorted list, as it is smaller. (As we are going from smallest to largest)
            else:
                # Adds the element to the sortedlist
                sortedlist.append(returnedList1[0])
                #Removes the element off the list at Index 0
                returnedList1.pop(0)

        #If length of returnedList2 is greater than 0 it will run block of code
        #This takes every element from returnList2 and adds it to the sorted list, and
        # removes the elements from the List, so the while loop will end then return the sorted list value.


        elif len(returnedList2) > 0:
            for i in returnedList2:
                #Adds the element to the sortedlist
                sortedlist.append(i)
                # Removes the element off the list at Index 0
                returnedList2.pop(0)

        # This takes every element from returnList1 and adds it to the sorted list, and
        # removes the elements from the List, so the while loop will end then return the sorted list value.

        else:
            for i in returnedList1:
                # Adds the element to the sortedlist
                sortedlist.append(i)
                # Removes the element off the list at Index 0
                returnedList1.pop(0)

    return sortedlist
##################################################################################################################
#
#                                                    FUNTIONS
#
##################################################################################################################

def LoginTest(UsernameEntry, PasswordEntry):
    UsernameTest = UsernameEntry.get()
    PasswordTest = PasswordEntry.get()

    if UsernameTest == "admin" and PasswordTest == "password":
        hide()
        MainWindowLayout()
        MainPage()
    else:
        Laabel30 = Label(gider, text="Password or Username is Incorrect")
        Laabel30.grid(row=0, column=0, padx=(10, 0))
        allList.append(Laabel30)


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

#This Function updates the Personal Best Times, though taking the list provided, finding the last position on that list
# and setting the values to that position.
def WRupdate(WRstyle_list, WRtime_list, WRtickrate_list, WRlabel1, WRlabel2, WRlabel3):

    #Counts how many elements are in the list
    w = len(WRstyle_list)
    # takes away 1 from the value to meet the Index Value
    w = w-1

    # Counts how many elements are in the list
    q = len(WRtime_list)
    # takes away 1 from the value to meet the Index Value
    q = q - 1

    # Counts how many elements are in the list
    e = len(WRtickrate_list)
    # takes away 1 from the value to meet the Index Value
    e = e - 1

    #Sets the value to the last postion(w) of the WRstyle_list
    WRstyle = WRstyle_list[w]
    # Sets the value to the last postion(q) of the WRtime_list
    WRtime = WRtime_list[q]
    # Sets the value to the last postion(e) of the WRtickrate_list
    WRtickrate = WRtickrate_list[e]

    #sets the WRlabel to the WRstyle variable
    WRlabel1.set(WRstyle)
    # sets the WRlabel2 to the WRtime variable
    WRlabel2.set(WRtime)
    # sets the WRlabel3 to the WRtickrate variable
    WRlabel3.set(WRtickrate)


#This Function is used to find the Personal Best Time, for each different Style.
#It grabs the Style to determine what list is needed, and then grabs the first index of that that sorted list,
#to get the best time in that selected style.
def PersonalBest(Styles1,AUTOBHOP_list1,Sideways_list1,HalfSideways_list1,Donly_list1,AOnly_list1,WOnly_list1,ScrollNormal_list1,EasyScroll_list1,Stamina_list1,Slowmotion_list1,LowGravity_list1, WRlabel1, WRlabel2, WRlabel3):

    #This retreives the Style, that the user had selected
    Style1 = Styles1.get()

    #This is used to determine which data is displayed, based on which Style is given.
    if Style1 == "AUTO-BHOP   ":
        WRstyle = AUTOBHOP_list1[0][0]
        WRtime =  AUTOBHOP_list1[0][1]
        WRtickrate = AUTOBHOP_list1[0][2]
        listvariable = AUTOBHOP_list1

    # This is used to determine which data is displayed, based on which Style is given.
    elif Style1 == "Sideways     ":
        WRstyle = Sideways_list1[0][0]
        WRtime =  Sideways_list1[0][1]
        WRtickrate = Sideways_list1[0][2]
        listvariable = Sideways_list1

    # This is used to determine which data is displayed, based on which Style is given.
    elif Style1 == "Half-Sideway":
        WRstyle = HalfSideways_list1[0][0]
        WRtime = HalfSideways_list1[0][1]
        WRtickrate = HalfSideways_list1[0][2]
        listvariable = HalfSideways_list1

    # This is used to determine which data is displayed, based on which Style is given.
    elif Style1 == "D-Only":
        WRstyle = Donly_list1[0][0]
        WRtime = Donly_list1[0][1]
        WRtickrate = Donly_list1[0][2]
        listvariable = Donly_list1

    # This is used to determine which data is displayed, based on which Style is given.
    elif Style1 == "A-Only":
        WRstyle = AOnly_list1[0][0]
        WRtime = AOnly_list1[0][1]
        WRtickrate = AOnly_list1[0][2]
        listvariable = AOnly_list1

    # This is used to determine which data is displayed, based on which Style is given.
    elif Style1 == "W-Only":
        WRstyle = WOnly_list1[0][0]
        WRtime = WOnly_list1[0][1]
        WRtickrate = WOnly_list1[0][2]
        listvariable = WOnly_list1

    # This is used to determine which data is displayed, based on which Style is given.
    elif Style1 == "Scroll/Normal":
        WRstyle = ScrollNormal_list1[0][0]
        WRtime = ScrollNormal_list1[0][1]
        WRtickrate = ScrollNormal_list1[0][2]
        listvariable = ScrollNormal_list1

    # This is used to determine which data is displayed, based on which Style is given.
    elif Style1 == "Easy Scroll":
        WRstyle = EasyScroll_list1[0][0]
        WRtime = EasyScroll_list1[0][1]
        WRtickrate = EasyScroll_list1[0][2]
        listvariable = EasyScroll_list1

    # This is used to determine which data is displayed, based on which Style is given.
    elif Style1 == "Stamina":
        WRstyle = Stamina_list1[0][0]
        WRtime = Stamina_list1[0][1]
        WRtickrate = Stamina_list1[0][2]
        listvariable = Stamina_list1

    # This is used to determine which data is displayed, based on which Style is given.
    elif Style1 == "Slowmotion":
        WRstyle = Slowmotion_list1[0][0]
        WRtime = Slowmotion_list1[0][1]
        WRtickrate = Slowmotion_list1[0][2]
        listvariable = Slowmotion_list1

    # This is used to determine which data is displayed, based on which Style is given.
    elif Style1 == "Low-Gravity":
        WRstyle = LowGravity_list1[0][0]
        WRtime = LowGravity_list1[0][1]
        WRtickrate = LowGravity_list1[0][2]
        listvariable = LowGravity_list1

    #Adds the data that has been set to a list, to be used to be called upon to display.
    WRstyle_list.append(WRstyle)
    WRtime_list.append(WRtime)
    WRtickrate_list.append(WRtickrate)

    #This Function updates the Personal Best Times with the data used from within this function
    WRupdate(WRstyle_list, WRtime_list, WRtickrate_list, WRlabel1, WRlabel2, WRlabel3)
    timelist(listvariable)


#This Function, extracts the data from the files and sorts the data into different list, based on Styles.
#It retrieves data from the Search function, of which map file to take data from.
def view_func(SearchMap):
    # This gets the Map, that the user had selected in SearchBox.
    mapquery = SearchMap.get()
    #sets a the Searchresult with data so no error is given.
    searchresult = ("test")
    # This hides all elements on a page
    hide()

    #views every element inside the maplist and checks if an entry matches, as if not an error with be produced.
    for i in maplist_list:
        if i == mapquery:
            searchresult = i

    #If Search result gets set in the previous stage it will, Open that Map datafile because it is on the maplist.
    if searchresult != ("test"):
        #opens the file, for reading the data.
        file = open('./maps/'+searchresult, "r")
        #creating a new list to store and sort data
        viewmapall_list = []

        #This goes through every line within the file and splits data into multiple elements.
        # Views every line of the file
        for line in file:
            # Takes away spacings, so elements can be put in list.
            line = line.strip('\n')
            # Seperates the elements with a ","
            line = line.split(",")
            # Add's all the elements read from file into a list
            viewmapall_list.append(line)

        #sets a new variable so data is not changed though its use in list modification
        stylelist_list = viewmapall_list

        #Creating new list for each Style, to append all data into different lists.
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

        #Views all elements inside the list
        for i in stylelist_list:
            #This Block of code is used to determine which style category each, time goes into.
            #it does this through viewing the Style of each Line of data
            # and appending that data into the designated list.
            if i[0] == "AUTO-BHOP   ":
                AUTOBHOP_list.append(i)

            if i[0] == "Sideways     ":
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

        #This block of code sorts all Style lists, based on the time which rest in the 1st index of each list.
        #And sorts the data from lowest number to highest numbers as they are intergers.
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

        #This calls the function that displays data from this functions, to be shown in a layout. (Calling the GUI)
        mapdisplay(AUTOBHOP_list1,Sideways_list1,HalfSideways_list1,Donly_list1,AOnly_list1,WOnly_list1,ScrollNormal_list1,EasyScroll_list1,Stamina_list1,Slowmotion_list1,LowGravity_list1,searchresult)

    #Else statement used to determine if an error is produced, shouldn't happen
    else:
        hide()
        view()
        Laabel33 = Label(Lower, text="Invalid Map Input")
        Laabel33.grid(row=0, column=0, padx=(60, 0))
        allList.append(Laabel33)


#This function is used to save data, when it is clicked within a listbox.
def select_item(event):
    #creates a update, to register when the box is clicked
    w = event.widget
    #This sets the index for the selection item.
    index = int(w.curselection()[0])
    #This sets the a variable when data is pressed, using the index of the selection and event widget.
    value = w.get(index)
    #Sets the data to be displayed within entry box.
    SearchMap.set(value)

    #This retreives the final element within a list, in this case used to go to the previous page as a "Back Button"
    x = len(back_list)
    y = 0
    if x > 1:
        y = (x - 1)

    #Sets which page was previously on.
    page = back_list[y]

    #Sets the different entry box based on which map was previously on.
    if page == "Delete":
        #sets value of entry.
        MapDeleteSearch.set(value)

    elif page == "AddPage":
        #sets value of entry
        MapAddSearch.set(value)

    elif page == "View":
        #sets value of entry
        SearchMap.set(value)

#This takes the user to the previous page, as a result of a button press.
# It hides and displays pages based on which map had previously been visited.
def backbutton():
    #This is used to find the last index of the list.
    x = len(back_list)
    y = 0
    if x > 1:
       y = (x-1)

    #takes the last entry on the list and sets it to a variable
    page = back_list.pop(y)

    #Finds last position of the map, hides the page and displays the previous page.
    if page == "Delete":
        #hides all elements on a page
        hide()
        #Displays the Delete page
        delete()

    elif page == "AddPage":
        # hides all elements on a page
        hide()
        #Displays the Add Time page
        addpage()

    elif page == "View":
        #hides all elements on a page
        hide()
        #Diplays the View Page
        view()


#Used to take data inputed on the "AddTime" page and input into a newly created file
# aswell adding the map into maplist
def AddFile(mapinput, styles, TimeAdd, statusSelect):
    #retreiving all data from the Add Time Page. (Map name, Style, Time and Tick Rate)
    map = mapinput.get()
    style = styles.get()
    try:
        time = str(TimeAdd.get())
    except:
        time = ""
    tickrate = statusSelect.get()
    #sets a default value, to determine if error has occured.

    if time == "":
        hide()
        addpage()
        Laabel29 = Label(gider, text="Invalid Time Input")
        Laabel29.grid(row=0,column=0, padx=(60,0))
        allList.append(Laabel29)

    else:
        print(tickrate)
        if tickrate == "64" or tickrate == "100" or tickrate == "128":
            k = True

            # Looks at every element in a list to determine if thet're is duplicate of a map.
            for i in maplist_list:
                if i == map:
                    k = False

            # If there is not a duplication of maps, it will add the map into maplist.
            if k == True:
                # appends the map to the list
                file = open("maplist", "a")
                # writes map into the list(at the end)
                file.write(map + ",\n")
                file.close()

            # Creates a file, if there is no existing file already. Writes in data of Style,Time and Tickrate.
            # seperating data with ",".
            try:
                fi = open('./maps/' + map, "a")
                fi.write(style)
                fi.write("," + time)
                fi.write("," + tickrate + "\n")
                fi.close()
            except IsADirectoryError:
                hide()
                addpage()
                Laabel31 = Label(gider, text="Please Enter a Map")
                Laabel31.grid(row=0, column=0, padx=(60, 0))
                allList.append(Laabel31)
        else:
            hide()
            print("error")
            addpage()
            Laabel32 = Label(gider, text="Please Select a Tick Rate")
            Laabel32.grid(row=0, column=0, padx=(35, 0))
            allList.append(Laabel32)

    return

#This function allows for Searching Capabilities in the View Page.
def Updatelist(SearchMap, listbox1):
    #presets a default value for the Index counter
    counter = 0
    #Retrieves the data from the entry box
    entryValue = str(SearchMap.get())
    #Deletes all entries within the listbox
    listbox1.delete(0, END)
    for i in maplist_list:
        #settings variable i to a element of the Maplist
        i = str(maplist_list[counter])
        counter += 1
        #If there are letters inside the i variable
        if entryValue in i:
            #Inserts the values back into the listbox.
            listbox1.insert(END, i)

#This function is used to delete all data within the program, and have a fresh start.
#It deletes all mapfiles and clears the wipelist.
def ClearWipe(ClearWipeQuerry):
    #This variable is used as varification to make sure the user actually want to wipe all data.
    ClearQuerry = ClearWipeQuerry.get()
    #Checks to see if user has confirmed they want to Clear Wipe.
    if ClearQuerry == "yes":
        #Takes every element from maplist and removes it
        for i in maplist_list:
            try:
                #deletes the file
                os.remove("maps/"+i)
                #If map is not displayed, shows a error message
            except OSError as e:  ## if failed, report it back to the user ##
                print("Error: %s - %s." % (e.filename, e.strerror))
        #Writes to the maplist, to clear the whole maplist.
        f = open("maplist", "w")
        f.close()

#Takes all data in the allList and removes the griding therfore hiding the elements.
def allremove():
    for i in allList:
        #removes the gridding of the element.
        i.grid_remove()

#This function deletes certain lines of code from the MapFiles and clears the "maplist", from the given data provided.
def DeleteLine(TimeSelect, MapStyle, mapquery, TimeList_list):
    #Resets Value so can be modified
    MapName = mapquery
    #Gets the value from the input
    Timechoice = TimeSelect.get()

    if Timechoice == "Select Time":
        hide()
        delete()



    #Views all elements inside the TimeList to retreive the tickrate of the time.
    for i in TimeList_list:
        if MapStyle == i[0] and Timechoice == i[1]:
            deletetickrate = i[2]

    #Opens up the mapfile
    try:
        f = open('./maps/' + MapName, "r+")

        #reads all lines
        d = f.readlines()
        # seek index 0
        f.seek(0)
        #For every element in d it will search for the line matching the MapStyle,Timechoice and Deletetickrate.
        for i in d:
            if i != MapStyle + "," + Timechoice + "," + deletetickrate + "\n":
                #writes over the line deleting the line.
                f.write(i)
        #Compressed file, shortening it
        f.truncate()
        #closes the file so it can no longer be altered
        f.close()

    except IsADirectoryError:
        DeleteError.set("    You need to Select a Time")

#This function is used to update the GUI with data, so the user can select which data they want to delete.
def deleteupdate(MapDeleteSearch, StyleSelect1):
    # Gets the value from the input
    mapquery = MapDeleteSearch.get()
    # Gets the value from the input
    MapStyle = StyleSelect1.get()
    # sets a the Searchresult with data so no error is given.
    searchresult = ("test")

    # views every element inside the maplist and checks if an entry matches, as if not an error with be produced.
    for i in maplist_list:
        if i == mapquery:
            searchresult = i

    # If Search result gets set in the previous stage, it will open that Map datafile because it is on the maplist.
    if searchresult != ("test"):
        # opens the file, for reading the data.
        file = open('./maps/' + searchresult, "r")
        # creating a new list to store and sort data
        viewmapall_list = []

        # This goes through every line within the file and splits data into multiple elements.
        # Views every line of the file
        for line in file:
            # Takes away spacings, so elements can be put in list.
            line = line.strip('\n')
            # Seperates the elements with a ","
            line = line.split(",")
            # Add's all the elements read from file into a list
            viewmapall_list.append(line)

        # sets a new variable so data is not changed though its use in list modification
        stylelist_list = viewmapall_list

        # Creating new list for each Style, to append all data into different lists.
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

        # Views all elements inside the list
        for i in stylelist_list:

            # This Block of code is used to determine which style category each, time goes into.
            # it does this through viewing the Style of each Line of data
            # and appending that data into the designated list.
            if i[0] == "AUTO-BHOP   ":
                AUTOBHOP_list.append(i)

            if i[0] == "Sideways     ":
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

        #This Block of code, sorts data depending on which MapStyle is selected,
        # aswell it sets the Time_List to the Style List therefore allowing the list to be shown in the GUI.
        if MapStyle == "AUTO-BHOP   ":
            print(AUTOBHOP_list)
            AUTOBHOP_list1 = Mergesort(AUTOBHOP_list)
            TimeList_list = AUTOBHOP_list1

        if MapStyle == "Sideways     ":
            Sideways_list1 = sorted(Sideways_list, key=lambda x: x[1])
            TimeList_list = Sideways_list1

        if MapStyle == "Half-Sideways":
            HalfSideways_list1 = sorted(HalfSideways_list, key=lambda x: x[1])
            TimeList_list = HalfSideways_list1

        if MapStyle == "D-Only":
            Donly_list1 = sorted(Donly_list, key=lambda x: x[1])
            TimeList_list = Donly_list1

        if MapStyle == "A-Only":
            AOnly_list1 = sorted(AOnly_list, key=lambda x: x[1])
            TimeList_list = AOnly_list1

        if MapStyle == "W-Only":
            WOnly_list1 = sorted(WOnly_list, key=lambda x: x[1])
            TimeList_list = WOnly_list1

        if MapStyle == "Scroll/Normal":
            ScrollNormal_list1 = sorted(ScrollNormal_list, key=lambda x: x[1])
            TimeList_list = ScrollNormal_list1

        if MapStyle == "Easy Scroll":
            EasyScroll_list1 = sorted(EasyScroll_list, key=lambda x: x[1])
            TimeList_list = EasyScroll_list1

        if MapStyle == "Stamina":
            Stamina_list1 = sorted(Stamina_list, key=lambda x: x[1])
            TimeList_list = Stamina_list1

        if MapStyle == "Slowmotion":
            Slowmotion_list1 = sorted(Slowmotion_list, key=lambda x: x[1])
            TimeList_list = Slowmotion_list1

        if MapStyle == "Low-Gravity":
            LowGravity_list1 = sorted(LowGravity_list, key=lambda x: x[1])
            TimeList_list = LowGravity_list1

        #Takes every element inside the assigned list, and adds it to the Dropdownbox selection list,
        # so the user choose which time they want to delete.
        for i in TimeList_list:
            TimeSelect_list.append(i[1])

        #This updates the delete DropdownBox and displays the Times, of which the user can choose to delete.
        TimeUpdate(TimeSelect_list, MapStyle, mapquery, TimeList_list)

#This function is used to delete the MapFile selected by the user.
def DeleteMap(MapDeleteSearch):
    #Retrieves the map name the user wants to delete
    Fileinput = MapDeleteSearch.get()
    #sets it in the correct format, so the file is in the right directory
    FileDelete = "maps/" + Fileinput
    #Sets default variable as no error.
    error = False
    try:
        #Attempts to delete the Map File
        os.remove(FileDelete)
        # if failed, report it back to the user
    except OSError as e:
        #sets the error variable, to return to the user.
        error = True

    # Opens up the mapfile
    f = open("maplist", "r+")
    # reads all lines
    d = f.readlines()
    # seek index 0
    f.seek(0)
    # For every element in d it will search for the line matching the MapName.
    for i in d:
        if i != Fileinput + "," + "\n":
            # writes over the line deleting the line.
            f.write(i)
    # Compressed file, shortening it
    f.truncate()
    # closes the file so it can no longer be altered
    f.close()
    #Returns the error value, to determine if a error has occured.
    return error

    #Takes the user to the Home Page with the options of what the user wants to do.
def home():
    #Hides all elements within a page
    hide()
    #Sets the default layout of the Window
    MainWindowLayout()
    #Calls to the MainPage() function, displaying the Home page.
    MainPage()

##################################################################################################################
##################################################################################################################

##################################################################################################################
#
#                                                    GUI
#
##################################################################################################################


def LoginScreen():
    root.geometry('270x180')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, pad=3)
    root.rowconfigure(1, pad=10)
    root.rowconfigure(2, pad=3)
    root.rowconfigure(3, pad=3)

    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')
    gider.grid(row=3, sticky='news')

    title7 = Label(header, text="Login", fg="White", bg="grey", font="Verdana 17 bold", )
    title7.grid(row=0,column=0, padx=(100,0))
    allList.append(title7)

    Label25 = Label(content, text="Username")
    Label25.grid(row=0,column=0,pady=(10,10), padx=(10,0))
    allList.append(Label25)

    UsernameEntry = StringVar()
    entry6 = Entry(content, textvariable=UsernameEntry, width=16)
    # Actually displays the label in a designated position through the use of grid
    entry6.grid(row=0, column=1, pady=(10, 0))
    allList.append(entry6)

    Label26 = Label(content, text="Password")
    Label26.grid(row=1, column=0,pady=(10,0), padx=(10,0))
    allList.append(Label26)

    PasswordEntry = StringVar()
    entry7 = Entry(content, textvariable=PasswordEntry, width=16)
    # Actually displays the label in a designated position through the use of grid
    entry7.grid(row=1, column=1, pady=(10, 0))
    allList.append(entry7)

    Login_button = tk.Button(Footer, text="Login", command=lambda: LoginTest(UsernameEntry, PasswordEntry), width=6)
    # Actually displays the label in a designated position through the use of grid
    Login_button.grid(row=0, column=0, padx=(154, 0), pady=(0, 0))
    allList.append(Login_button)



#This Funtion is used to display the Map details through the view funtion,
# it is the GUI of the page and is called after
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
    #Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title6)

    #Creates the "Person Best Time" subheading, displayed when mapdisplay() is activated
    laabel1 = Label(content, text="Personal Best Time", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel1.grid(row=0, column=1, padx=(10, 0), pady=(5, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(laabel1)

    # Assigning a variable a Label tkinter Operation, to be displayed.
    laabel8 = Label(content, text="________________________________", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel8.grid(row=1, column=1, padx=(0, 10), pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(laabel8)

    #Sets the variable to a StringVar to specify what type of element it is.
    ####### This is Refered to as "Assigning Variable Class"#################
    Styles1 = StringVar()
    #Sets the Style to the first position of the Style list, so it has a default displayed data .
    Styles1.set(Style[0])  # default value
    #Sets the variable to the Tkinter Operation of Optionmenu(Dropdownbox)
    DropdownStyle1 = OptionMenu(Footer, Styles1, *Style)
    # displays the dropdown box in a designated position through the use of grid
    DropdownStyle1.grid(row=1, column=0, pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(DropdownStyle1)

    #Assigning Variable Class (as indicated on Line 583)
    WRlabel1 = StringVar()
    # Assigning Variable Class
    WRlabel2 = StringVar()
    # Assigning Variable Class
    WRlabel3 = StringVar()

    #This is a call to a funtion, that uses the elements from the funtions arguments,
    # that takes the list and sorts the data, into different Style list and sorts the Style list
    # to create variables that include the Personal Best Times of each style.
    # Which are displayed on the following page.
    PersonalBest(Styles1, AUTOBHOP_list1, Sideways_list1, HalfSideways_list1, Donly_list1, AOnly_list1,
                 WOnly_list1,ScrollNormal_list1, EasyScroll_list1, Stamina_list1, Slowmotion_list1,
                 LowGravity_list1, WRlabel1, WRlabel2, WRlabel3)

    # Assigning a variable a Label tkinter Operation, to be displayed.
    #This WRLabel1 includes the Personal Best Style, and updates when it is set.
    laabel5 = Label(Footer, textvariable=WRlabel1, font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel5.grid(row=2, column=1, padx=(5, 0), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(laabel5)

    # Assigning a variable a Label tkinter Operation, to be displayed.
    # This WRLabel2 includes the Personal Best Time
    laabel6 = Label(Footer, textvariable=WRlabel2, font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel6.grid(row=3, column=1, padx=(5, 0), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(laabel6)

    # Assigning a variable a Label tkinter Operation, to be displayed.
    # This WRLabel3 includes the Personal Best TickRate
    laabel7 = Label(Footer, textvariable=WRlabel3, font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel7.grid(row=4, column=1, padx=(5, 0), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(laabel7)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    #This button updates the Personal Best Time updated, through recalling the PersonalBest funtion,
    # that takes the data from the dropdown box to display the different Style Personal Best.
    Display_button = tk.Button(Footer, text='Display', command=lambda: PersonalBest(Styles1, AUTOBHOP_list1,
        Sideways_list1, HalfSideways_list1, Donly_list1, AOnly_list1, WOnly_list1,ScrollNormal_list1, EasyScroll_list1,
        Stamina_list1, Slowmotion_list1, LowGravity_list1, WRlabel1, WRlabel2, WRlabel3))
    # Actually displays the label in a designated position through the use of grid
    Display_button.grid(row=1, column=1, padx=(7, 0),pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Display_button)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Style:"
    laabel2 = Label(Footer, text="Style:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel2.grid(row=2, column=0, padx=(6, 0), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(laabel2)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Time:"
    laabel3 = Label(Footer, text="Time:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel3.grid(row=3, column=0, padx=(6, 0), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(laabel3)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Tick Rate:"
    laabel4 = Label(Footer, text="Tick Rate:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel4.grid(row=4, column=0, padx=(0, 20), pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel4)

    # Assigning a variable a Label tkinter Operation
    laabel9 = Label(gider, text="________________________________", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel9.grid(row=0, column=0, padx=(0, 10), pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel9)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Style:"
    laabel10 = Label(Lower, text="Style:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel10.grid(row=1, column=0, padx=(30, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel10)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Time:"
    laabel11 = Label(Lower, text="Time:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel11.grid(row=1, column=1, padx=(40, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel11)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Tick Rate:"
    laabel12 = Label(Lower, text="Tick:", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    laabel12.grid(row=1, column=2, padx=(20, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected, through the use of "grid_remove"
    allList.append(laabel12)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the view() page
    # which is the Listbox Selection page for different maps.
    back_button1 = tk.Button(Bottom, text="Back", command=view, width=6)
    # Actually displays the label in a designated position through the use of grid
    back_button1.grid(row=3, column=0, padx=(0, 140), pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    #  through the use of "grid_remove"
    allList.append(back_button1)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the home() page
    # which is the homescreen with all the Selections of funtions(Add time, View, Delete, Settings and Quit)
    home3_button = tk.Button(Bottom, text="Home", command=home, width=6)
    # Actually displays the label in a designated position through the use of grid
    home3_button.grid(row=3, column=0, padx=(140,0), pady=(0, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    #  through the use of "grid_remove"
    allList.append(home3_button)

    #calls funtion that takes the data and sets the WRlabel variables,
    # so a different variable is displayed.
    WRupdate(WRstyle_list, WRtime_list, WRtickrate_list, WRlabel1, WRlabel2, WRlabel3)


    #This is still on the same displayed page as mapdisplay,
    # but is seperated so it can be called from to update the data
    #It displays the data within the List with all map data into a ListBox.
def timelist(listvariable):

    # Assigning a variable a Listbox tkinter Operation, to be displayed.
    #Having a Width of 25 and a height of 6.
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
    #This is used to attach the scrollbar to the Listbox, so they work together
    listbox2.configure(yscrollcommand=yscroll2.set)
    # now load the listbox with data
    #from the listvariable file including the data of the selected Map and Style.
    for item in listvariable:
        # insert each new item to the end of the listbox
        listbox2.insert('end', item)

##################################################################################################################

#This Page is used to display a new GUI page, by first hiding all previous page then displaying new tkinter
# operations, This funtion takes all inputed data into the page and saves the data inside a file, that has been
# creates, aswell adding the map name to a list. This data includes Map Name, Time, Style and Tick rate.
def addpage():
    # This hides all elements on a page
    hide()

    #WINDOW CONFIGURATION BLOCK
    root.geometry('250x325')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, pad=3)
    root.rowconfigure(1, pad=10)
    root.rowconfigure(2, pad=3)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')

##############################################
    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Add TIme"
    title1 = Label(header, text="Add Time", fg="White", bg="grey", font="Verdana 17 bold", )
    # Actually displays the label in a designated position through the use of grid
    title1.grid(row=0, column=1, padx=(76,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title1)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "MAP:"
    Label7 = Label(content, text="MAP:", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label7.grid(row=0, column=0,pady=(10,0), padx=20)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label7)

    # Assigning a variable a Entry tkinter Operation
    # This is used to input data, in this case, The data inputed is used to choose a map entered.
    entry1 = Entry(content, textvariable=MapAddSearch, width=16)
    # Actually displays the label in a designated position through the use of grid
    entry1.grid(row=0, column=1,pady=(10,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(entry1)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the maplist page
    # which is the Listbox Selection page for different maps, so the user can see if the map is already existing.
    MapList_button = tk.Button(content, text='Map List', command=maplist)
    # Actually displays the label in a designated position through the use of grid
    MapList_button.grid(row=1, column=1,padx=(76,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(MapList_button)

    ###################
    ##################

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "STYLE:"
    Label8 = Label(content, text="STYLE:", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label8.grid(row=2, column=0,pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label8)

    # Assigning Variable Class
    Styles = StringVar()
    # Sets the Style to the first position of the Style list, so it has a default displayed data .
    Styles.set(Style[0])  # default value
    # Sets the variable to the Tkinter Operation of Optionmenu, aswell what List, and saved element.
    DropdownStyle = OptionMenu(content, Styles, *Style)
    # Actually displays the label in a designated position through the use of grid
    DropdownStyle.grid(row=2, column=1,pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(DropdownStyle)

    # Assigning Variable Class
    TimeAdd = DoubleVar()
    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "TIME:"
    Label9 = Label(content, text="TIME:", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label9.grid(row=5, column=0,pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label9)

    # Assigning a variable a Entry tkinter Operation
    # This is used to input data, in this case, The data inputed is the time the user had set.
    entry2 = Entry(content, textvariable=TimeAdd, width=16)
    # Actually displays the label in a designated position through the use of grid
    entry2.grid(row=5, column=1,pady=(10,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(entry2)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "TICK"
    Label10 = Label(content, text="TICK", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label10.grid(row=7, column=0,pady=(10, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label10)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "RATE:"
    Label11 = Label(content, text="RATE:", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label11.grid(row=8, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label11)

    # Assigning Variable Class
    statusSelect = StringVar()

    # Assigning a variable a Radiobutton tkinter Operation
    # Displaying Text of "128 Tick Rate", when clicked assigning the value of "128"
    Tick128 = Radiobutton(content, text="128 Tick Rate", variable=statusSelect, value="128")
    # Actually displays the label in a designated position through the use of grid
    Tick128.grid(row=7, column=1,padx=(0,10))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Tick128)

    # Assigning a variable a Radiobutton tkinter Operation
    # Displaying Text of "100 Tick Rate", when clicked assigning the value of "100"
    Tick100 = Radiobutton(content, text="100 Tick Rate", variable=statusSelect, value="100")
    # Actually displays the label in a designated position through the use of grid
    Tick100.grid(row=8, column=1,padx=(0,10))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Tick100)

    # Assigning a variable a Radiobutton tkinter Operation
    # Displaying Text of "64 Tick Rate", when clicked assigning the value of "64"
    Tick64 = Radiobutton(content, text=" 64 Tick Rate", variable=statusSelect, value="64")
    # Actually displays the label in a designated position through the use of grid
    Tick64.grid(row=9, column=1, padx=(0,14))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Tick64)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button takes the data inputed and adds the information into the
    # maplist and creates another file for the individual map
    MapConfirm_button4 = tk.Button(Footer, text= "Add Time", width=10, command=lambda: AddFile(MapAddSearch, Styles,
                                                                                               TimeAdd, statusSelect))
    # Actually displays the label in a designated position through the use of grid
    MapConfirm_button4.grid(row=10, column=1, pady=(0,10), padx=(5,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(MapConfirm_button4)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the home() page
    # which is the homescreen with all the Selections of funtions(Add time, View, Delete, Settings and Quit)
    Home_button1 = tk.Button(Footer, text= "Home", command=home, width=10)
    # Actually displays the label in a designated position through the use of grid
    Home_button1.grid(row=10, column=0, pady=(0,10), padx=(0,5))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Home_button1)

    #Backlist is used for the back button, to detect what map was previously pressed.
    back_list.append("AddPage")



##################################################################################################################
#This funtion displays the main page which includes os the first page the user see's,
#It has five buttons for the different funtions which include the Add Time , View, Delete, Settings and quit button
#Aswell displays general information about previous map played for Accessable.
def MainPage():
    # Creates the Title or header at the top of the page. With a grey background and a font of "Verdana 17 bold".
    # This has uses a variable to find the map name selected then display it.
    title = Label(header, text="BHOP Time Recorder", fg="White", bg="grey", font="Verdana 17 bold", )
    # Actually displays the label in a designated position through the use of grid
    title.grid(row=0, column=0, padx=(25,30))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title)

    # Assigning a variable a Label tkinter Operation
    # This is used as a packer so text is in the right position.
    packer = Label(content, text="                   ")
    # Actually displays the label in a designated position through the use of grid
    packer.grid(row=0, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(packer)

    # Assigning a variable a Label tkinter Operation
    # This is used as a packer so text is in the right position.
    packer1 = Label(content, text="                   ")
    # Actually displays the label in a designated position through the use of grid
    packer1.grid(row=0, column=2)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(packer1)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Welcome User"
    Label1 = Label(content, text="Welcome User")
    # Actually displays the label in a designated position through the use of grid
    Label1.grid(row=0, column=1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label1)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Previous Map:"
    Label4 = Label(content, text="Previous Map:")
    # Actually displays the label in a designated position through the use of grid
    Label4.grid(row=1, column=1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label4)

    # Assigning Variable Class
    PrevMap = StringVar()
    # Sets the Map Displayed to the "" as default.
    PrevMap.set("")

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of Previous Map added
    Label5 = Label(content, textvariable=PrevMap)
    # Actually displays the label in a designated position through the use of grid
    Label5.grid(row=2, column = 1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label5)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Previous Map:"
    Label2 = Label(content, text="Previous Time:")
    # Actually displays the label in a designated position through the use of grid
    Label2.grid(row=3, column=1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label2)

    # Assigning Variable Class
    PrevTime = DoubleVar()
    # Sets the Map Displayed to the "0.0" as default.
    PrevTime.set(0.0)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of Previous Time added
    Label3 = Label(content, textvariable=PrevTime)
    # Actually displays the label in a designated position through the use of grid
    Label3.grid(row=4, column=1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label3)

    #Using a try block to prevent error if there is no map
    try:
        #determines how long the list is and sets position_maplist to the length
        position_maplist = len(maplist_list)
        #Takes the length of list and reduces it by one to match the Index(As Index's start at 0)
        position_maplist = position_maplist - 1

        #Sets "MapPrevious" as the final position on maplist_list
        # to return the last map that the user has added an entry to
        MapPrevious = maplist_list[position_maplist]
        # Sets the Map Displayed to the "MapPrevious" variable as default.
        PrevMap.set(MapPrevious)

        #Creates a new list to store data
        PrevTime_List = []
        #Opens the "'./maps/' + MapPrevious" file, to read the data inside.
        mapfile = open('./maps/' + MapPrevious, "r")
        #Views every line of the file
        for line in mapfile:
            #Takes away spacings, so elements can be put in list.
            line = line.strip('\n')
            #Seperates the elements with a ","
            line = line.split(",")
            #Add's all the elements read from file into a list
            PrevTime_List.append(line)

        # determines how long the list is and sets PrevTime_List to the length
        TimePosition = len(PrevTime_List)
        # Takes the length of list and reduces it by one to match the Index(As Index's start at 0)
        TimePrevious = TimePosition - 1

        #sets the variable with the element of list.
        # At a position of [TimePrevious][1] inside the list
        PrevTime_final = PrevTime_List[TimePrevious][1]
        # Sets the Time Displayed to the "PrevTime_final" variable as default.
        PrevTime.set(PrevTime_final)
        print(PrevTime_List)
    #If it faces an error it will set PrevMap to "" default.
    except:
        PrevMap.set("")

    # Assigning a variable a Label tkinter Operation
    # This is used as a Seperater between the two Frames, so the layout looks as designed.
    Label6 = Label(Footer, text="_________________________________________")
    # Actually displays the label in a designated position through the use of grid
    Label6.grid(row=0, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label6)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the addpage() Page, aswell hides the MainPage().
    # The Page is used for adding data into an existing file or creating a new file.
    # Aswell Appending maps being created into a maplist
    add_button = tk.Button(Footer, text='Add Time', width=15, command=addpage)
    # Actually displays the label in a designated position through the use of grid
    add_button.grid(row=1, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(add_button)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the view() Page, aswell hides the MainPage().
    # The Page is used for viewing maps that have been saved, first displaying a ListBox page where the user selects
    # which map they would like to view.
    # Aswell Appending maps being created into a maplist
    view_button = tk.Button(Footer, text='View', width=15, command=view)
    # Actually displays the label in a designated position through the use of grid
    view_button.grid(row=2, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(view_button)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the Delete() Page, aswell hides the MainPage().
    # The Page is used for Deleting selective time data from existing files or Delete whole Maps Files.
    delete_button = tk.Button(Footer, text='Delete', width=15, command=delete)
    # Actually displays the label in a designated position through the use of grid
    delete_button.grid(row=3, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(delete_button)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the settings() Page, aswell hides the MainPage().
    # The Page is used for Clear Wiping all data, therefore deleting all data.
    settings_button = tk.Button(Footer, text='Settings', width=15, command=settings)
    # Actually displays the label in a designated position through the use of grid
    settings_button.grid(row=4, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(settings_button)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # The Page is used for closing the window
    quit_button = tk.Button(Footer, text='Quit', width=15, command=root.destroy)
    # Actually displays the label in a designated position through the use of grid
    quit_button.grid(row=5, column=0)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(quit_button)
##################################################################################################################

#This Funtion is used for the searching of Map entered, this funtion hides the previosu elements on the page
# and displays a listbox where the user can select which map they want to view the map data.
def view():
    # This hides all elements on the page
    hide()
    #WINDOW CONFIGURATION BLOCK
    root.geometry('250x350')
    root.rowconfigure(0, pad=2)
    root.rowconfigure(1, pad=3)
    root.rowconfigure(2, pad=3)
    root.rowconfigure(3, pad=3)
    root.rowconfigure(4, pad=3)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')
    gider.grid(row=3, sticky='news')
    Lower.grid(row=4, sticky='news')
##############################################

    # Creates the Title or header at the top of the page. With a grey background and a font of "Verdana 17 bold".
    # This has uses a variable to find the map name selected then display it.
    title2 = Label(header, text="View", fg="White", bg="grey", font="Verdana 17 bold", )
    # Actually displays the label in a designated position through the use of grid
    title2.grid(row=0, column=0, padx=(100, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title2)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Search for Map"
    Label12 = Label(content, text="Search for Map", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    Label12.grid(row=0, column=0,pady=(10,0), padx=(34, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label12)

    # Assigning a variable a Entry tkinter Operation
    # Taking the Data entered and setting the variable of SearchMap as what the user has entered
    entry3 = Entry(content, textvariable=SearchMap, width=20)
    # Actually displays the label in a designated position through the use of grid
    entry3.grid(row=1, column=0, padx=(28, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(entry3)

    # Assigning a variable a Listbox tkinter Operation
    # Taking Data from a list displaying it on a page, so it can be interactable with the user.
    # Assigning a variable a Listbox tkinter Operation, to be displayed.
    # Having a Width of 20 and a height of 10.
    listbox1 = tk.Listbox(Footer, width=20, height=10)
    # Actually displays the label in a designated position through the use of grid
    listbox1.grid(row=3, column=0, padx=(28, 0))
    # create a vertical scrollbar to the right of the listbox
    yscroll1 = tk.Scrollbar(Footer, command=listbox1.yview, orient=tk.VERTICAL)
    # Actually displays the label in a designated position through the use of grid
    yscroll1.grid(row=3, column=1, sticky='ns')
    #Used to Join the scroll bar together to the listbox
    listbox1.configure(yscrollcommand=yscroll1.set)
    #Used to Select items when they have been clicked on
    listbox1.bind('<<ListboxSelect>>', select_item)
    # now load the listbox with data
    for item in maplist_list:
        # insert each new item to the end of the listbox
        listbox1.insert('end', item)

    Search_button = tk.Button(content, text="Search", command=lambda: Updatelist(SearchMap, listbox1), width=5)
    # Actually displays the label in a designated position through the use of grid
    Search_button.grid(row=2, column=0, padx=(32, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Search_button)


    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(listbox1)
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(yscroll1)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the home() page
    # which is the homescreen with all the Selections of funtions(Add time, View, Delete, Settings and Quit)
    Home_button2 = tk.Button(gider, text="Home", command=home, width=5)
    # Actually displays the label in a designated position through the use of grid
    Home_button2.grid(row=0, column=0, padx=(32,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Home_button2)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the mapdisplay() page
    # This and runs a function to take the selected data from the Listbox
    # and displaying the Map Data that had been chosen
    view_button1 = tk.Button(gider, text= "View", command=lambda: view_func(SearchMap),width=5)
    # Actually displays the label in a designated position through the use of grid
    view_button1.grid(row=0, column=1,padx=(30,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(view_button1)

    # Backlist is used for the back button, to detect what map was previously pressed.
    back_list.append("View")
##################################################################################################################

#This funtion hides the first previous page and has a use in Clear Wiping all data files. This delete's map files
# and clears the "maplist" file.

def settings():
    # This hides all elements on the page
    hide()

    # WINDOW CONFIGURATION BLOCK
    root.geometry('250x187')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, pad=1)
    root.rowconfigure(1, pad=2)
    root.rowconfigure(2, pad=1)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')


##############################################

    # Creates the Title or header at the top of the page. With a grey background and a font of "Verdana 17 bold".
    # This tittle has the text of "Settings"
    title3 = Label(header, text="Settings", fg="White", bg="grey", font="Verdana 17 bold", )
    # Actually displays the label in a designated position through the use of grid
    title3.grid(row=0, column=0, padx=(86, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title3)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Clear Wipe:"
    Label14 = Label(content, text="Clear Wipe", font="Arial 18 bold", bg="#FFF8DC")
    # Actually displays the label in a designated position through the use of grid
    Label14.grid(row=0, column=0,pady=(10,0), padx=(80, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label14)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Are you sure?"
    Label15 = Label(Footer, text="Are you sure?", font="Arial 14 bold")
    # Actually displays the label in a designated position through the use of grid
    Label15.grid(row=1, column=0, pady=(10, 0), padx=(71, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label15)

    #sets variable class
    ClearWipeQuerry = StringVar()

    #This buttons is used to varify whether the user wants to Wipe.
    # Assigning a variable a Radiobutton tkinter Operation
    # Displaying Text of "Yes", when clicked assigning the value of "yes" to the "ClassWipeQuery" variable
    wipeyes = Radiobutton(Footer, text="Yes", variable=ClearWipeQuerry, value="yes")
    # Actually displays the label in a designated position through the use of grid
    wipeyes.grid(row=2, column=0,padx=(65,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(wipeyes)

    # Assigning a variable a Button tkinter Operation
    # This will initiate the ClearWipe Funtion, that deletes every Map File and clears the "maplist" file
    confirmwipe_button = tk.Button(Footer, text="WIPE", command= lambda: ClearWipe(ClearWipeQuerry), width=5)
    # Actually displays the label in a designated position through the use of grid
    confirmwipe_button.grid(row=4, column=0, padx=(65,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(confirmwipe_button)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the MainPage().
    Home_button3 = tk.Button(Footer, text="Home", command=home, width=5)
    # Actually displays the label in a designated position through the use of grid
    Home_button3.grid(row=5, column=0,pady=(10,0),padx=(0, 120))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Home_button3)

##################################################################################################################


##################################################################################################################

#This Page is used to display a new GUI page, by first hiding all previous page elements
# then displaying the new tkinter operations
# This funtion is used to delete Map's and certain times based on what buttons are pressed or data inputed.
def delete():
    # This hides all elements on the page
    hide()

    # WINDOW CONFIGURATION BLOCK
    root.geometry('250x360')
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

    # Creates the Title or header at the top of the page. With a grey background and a font of "Verdana 17 bold".
    # This tittle has the text of "Delete"
    title4 = Label(header, text="Delete", fg="White", bg="grey", font="Verdana 17 bold", )
    # Actually displays the label in a designated position through the use of grid
    title4.grid(row=0, column=0, padx=(92, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title4)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Search Map:"
    Label16 = Label(content, text="Search Map", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    Label16.grid(row=0, column=0, pady=(10, 0), padx=(40, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label16)

    # Assigning a variable a Entry tkinter Operation
    # Taking the Data entered and setting the variable of MapDeleteSearch as what the user has entered
    entry4 = Entry(content, textvariable=MapDeleteSearch, width=18)
    # Actually displays the label in a designated position through the use of grid
    entry4.grid(row=1, column=0, padx=(37,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(entry4)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the maplist page
    # which is the Listbox Selection page for different maps, so the user can select a map.
    MapList_button2 = tk.Button(content, text='Map List', command=maplist)
    # displays the Button in a designated position through the use of grid
    MapList_button2.grid(row=2, column=0, padx=(20, 80))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(MapList_button2)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed follows the DeleteMap function, which takes the data received
    # and deletes the Map from entry box
    MapConfirm_button6 = tk.Button(content, text="Delete Map", command= lambda: DeleteMap(MapDeleteSearch))
    # displays the Button in a designated position through the use of grid
    MapConfirm_button6.grid(row=2, column=0, padx=(116, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(MapConfirm_button6)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Style Select"
    Label18 = Label(content, text="Style Select", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    Label18.grid(row=3, column=0, pady=(10, 0), padx=(40, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label18)

    #sets variable class
    StyleSelect1 = StringVar()
    # sets default value which is the first position of Style List being AUTOBHOP
    StyleSelect1.set(Style[0])
    DropdownStyleSelect3 = OptionMenu(content, StyleSelect1, *Style)
    # displays the dropdown box in a designated position through the use of grid
    DropdownStyleSelect3.grid(row=4, column=0, padx=(35, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(DropdownStyleSelect3)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed follows the DeleteUpdate function, which takes the data received
    # and Clears Map data from the selected data.
    MapConfirm_button7 = tk.Button(content, text="Confirm", command=lambda: deleteupdate(MapDeleteSearch, StyleSelect1))
    # displays the Button in a designated position through the use of grid
    MapConfirm_button7.grid(row=5, column=0, padx=(30, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(MapConfirm_button7)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Time Select"
    Label19 = Label(content, text="Time Select", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    Label19.grid(row=6, column=0, pady=(10, 0), padx=(40, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label19)

    #Settings Default Data, so no error occurs.
    MapStyle = "AUTO-BHOP   "
    mapquery = ""
    TimeList_list = []

    #Calls to Update function, that takes the data and updates it. \
    # Showing new data when displayed
    TimeUpdate(TimeSelect_list, MapStyle, mapquery, TimeList_list)

    #Called on to update, OptionMenu tkinter operation in the Delete Page, so certain times can be selected
def TimeUpdate(TimeSelect_list, MapStyle, mapquery, TimeList_list):

    #sets variable class
    TimeSelect = StringVar()
    #Sets Default Data
    TimeSelect.set(TimeSelect_list[0])
    # Sets the variable to the Tkinter Operation of Optionmenu(Dropdownbox)
    DropdownTimeSelect = OptionMenu(content, TimeSelect, *TimeSelect_list)
    # displays the Dropdown box in a designated position through the use of grid
    DropdownTimeSelect.grid(row=7, column=0, padx=(35, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(DropdownTimeSelect)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed follows the DeleteLine function, which takes the data received
    # and Searching Map File for Data requested to delete. and clear that line so data is deleted.
    delete2_button = tk.Button(content, text="Delete", command= lambda: DeleteLine(TimeSelect, MapStyle,
                                                                                   mapquery, TimeList_list))
    # displays the Button in a designated position through the use of grid
    delete2_button.grid(row=10, column=0, padx=(30, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(delete2_button)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the MainPage().
    Home_button4 = tk.Button(content, text='Home', command=home)
    # displays the Button in a designated position through the use of grid
    Home_button4.grid(row=11, column=0, padx=(0, 140), pady=(0, 10))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Home_button4)

    Laabel36 = Label(Footer, textvariable=DeleteError)
    Laabel36.grid(row=0, column=0, padx=(20, 0))
    allList.append(Laabel36)

    # Backlist is used for the back button, to detect what map was previously pressed.
    #This adds it to that list to know which map had been previously visited being Delete Map.
    back_list.append("Delete")
##################################################################################################################


def maplist():
    # This hides all elements on the page
    hide()

    # WINDOW CONFIGURATION BLOCK
    root.geometry('250x300')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, pad=1)
    root.rowconfigure(1, pad=2)
    root.rowconfigure(2, pad=1)
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')

##############################################

    # Creates the Title or header at the top of the page. With a grey background and a font of "Verdana 17 bold".
    # This tittle has the text of "Map List"
    title5 = Label(header, text="Map List", fg="White", bg="grey", font="Verdana 17 bold", )
    # Actually displays the label in a designated position through the use of grid
    title5.grid(row=0, column=0, padx=(86, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(title5)

    # Assigning a variable a Label tkinter Operation
    # Displaying Text of "Maps"
    Label20 = Label(content, text="Maps", font="Arial 15 bold")
    # Actually displays the label in a designated position through the use of grid
    Label20.grid(row=0, column=0, padx=(110, 0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(Label20)

    # Assigning a variable a Listbox tkinter Operation
    # Taking MapData from a list to display it on a page, so it can be interactable with the user.
    # Assigning a variable a Listbox tkinter Operation, to be displayed.
    # Having a Width of 20 and a height of 12.
    listbox = tk.Listbox(Footer, width=20, height=12)
    # displays the listbox in a designated position through the use of grid
    listbox.grid(row=0, column=0, padx=(28,0))
    # create a vertical scrollbar to the right of the listbox
    yscroll = tk.Scrollbar(Footer,command=listbox.yview, orient=tk.VERTICAL)
    # displays the scrollbar in a designated position through the use of grid
    yscroll.grid(row=0, column=1, sticky='ns')
    # Used to Join the scroll bar together to the listbox
    listbox.configure(yscrollcommand=yscroll.set)
    # Used to Select items when they have been clicked on
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

    #Takes the previous map, and heads to that page.
    back_button = tk.Button(gider, text="Back", command=backbutton, width=6)
    # displays the Button in a designated position through the use of grid
    back_button.grid(row=0, column=0, padx=(24, 0), pady=(10,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(back_button)

    # Assigning a variable a Button tkinter Operation, to be displayed.
    # This button when pressed takes the user to the MainPage().
    home2_button = tk.Button(gider, text="Home", command=home, width=6)
    # displays the label in a designated position through the use of grid
    home2_button.grid(row=0, column=1, padx=(25,0), pady=(10,0))
    # Used to add the grided term to a list, to then be used to remove it when another page is selected,
    # through the use of "grid_remove"
    allList.append(home2_button)

##################################################################################################################

def MainWindowLayout():
    #Window configuration block for MainPage()
    root.geometry('250x320')
    root.columnconfigure(0, weight=1) # 100%
    root.rowconfigure(0, pad=3) # 10%
    root.rowconfigure(1, pad=13) # 30%
    root.rowconfigure(2, pad=13) # 60%
    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    Footer.grid(row=2, sticky='news')
###################################################################################################################

#Sets Variable Class for MapDeleteSearch
MapDeleteSearch = StringVar(root, value="")
#Sets Variable Class for SearchMap
SearchMap = StringVar(root, value="")
#Sets Variable Class for MapAddSearch
MapAddSearch = StringVar(root, value="")
LoginScreen()
DeleteError = StringVar(root, value ="Select a Map and press Confirm.")
#Calls the Window Configuration
    #MainWindowLayout()
#Calls the MainPage to display the Menu at the beginning
    #MainPage()
#This makes it so, that the window page is static and cannot be changed
root.resizable(width=False, height=False)
root.mainloop()