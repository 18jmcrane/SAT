def Loadlanguage():
    termList = []
    meaningList = []
    f = open("Dictionary", "r")
    for line in f:
        line = line.strip('\n')
        line = line.split("-")
        termList.append(line[0])
        meaningList.append(line[1])
    f.close()
    return termList,meaningList


contactsList = Loadlanguage()
termList = contactsList[0]
meaningList = contactsList[1]

def display(d_contactlist):
    print("Ramu's Languages Dictionary")
    Index = 0
    for i in termList:
            print(i,"-",meaningList[Index])
            Index += 1
    return

def NewData(contactsList):
    term = input("Enter you new term: ")
    meaning = input("Enter the meaning for your term: ")
    contactsList[0].append(term)
    contactsList[1].append(meaning)
    return contactsList

def DeleteTerm(dt_contactList):
    print("----Delete contact----")
    position = Search(dt_contactList)
    print("Are you sure you wish to delete this record? (Yes/No) ", dt_contactList[0][position])
    userResponse = input(": ")
    if (userResponse == "Yes" or "yes" or "y"):
        dt_contactList[0].pop(position)
        dt_contactList[1].pop(position)
    return dt_contactList


def Search(l_contactList):
    searchName = input("What Term are you searching for?")
    print("Search Funtion")
    position = 0
    for name in l_contactList[0]:
        if name == searchName:
            return position
        position += 1
    return position

def SaveFile(c_termList, c_meaningList):
    dindex = 0
    f = open("Dictionary", "w")
    for i in c_termList:
        f.write(c_termList[dindex])
        f.write("-")
        f.write(c_meaningList[dindex])
        f.write("\n")
        dindex += 1
    f.close()
    return 1

while True:
    print("Please Enter the number of the option you wish to select:")
    print("    1. DISPLAY ALL")
    print("    2. Enter New Term")
    print("    3. Search")
    print("    4. Delete a Term")
    print("    5. Quit the program")
    menuOption = input("Selection: ")
    if menuOption == "1":
        print("")
        display(contactsList)
        print("")

    elif menuOption == "2":
        NewData(contactsList)
        termList = contactsList[0]
        meaningList = contactsList[1]
        SaveFile(termList, meaningList)

    elif menuOption == "3":
        print(contactsList)
        position = Search(contactsList)
        try:
            print(contactsList[0][position],"is under the",(position + 1), "line. ")
            print("The Meaning for this word is:","\n")
            print(contactsList[1][position])
            print("")
        except IndexError:
            print("You have entered a Term that is not in the dictionary")
            print("")
            menuOption = 0


    elif menuOption == "4":
        try:
            print(contactsList)
            DeleteTerm(contactsList)
            print(contactsList)
            termList = contactsList[0]
            meaningList = contactsList[1]
            SaveFile(termList, meaningList)
        except IndexError:
            print("You have entered a Term that is not in the dictionary")
            print("")
            menuOption = 0

    elif menuOption == "5":
        exit(0)
    else:
        print("Menu option entered does not exist")
        menuOption = 0

