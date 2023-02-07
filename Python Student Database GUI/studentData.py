# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
from tkinter import ttk
studentLt = []
updateIndex= [0]



#Student class 
class Student:
  def __init__(self, nameF, nameL, ID, SSN, M, BD, adr, GPA):
    self.nameF = nameF
    self.nameL = nameL
    self.ID = ID
    self.SSN = SSN
    self.M = M
    self.BD = BD
    self.adr = adr
    self.GPA = GPA

#Create new student object and add to list
  def newSt(self, FN, LN, ID, SSN, M, BD, adr, GPA):
    ob = Student(FN, LN, ID, SSN, M, BD, adr, GPA)
    studentLt.append(ob)


#Initial dummy data
obj = Student('', '', 0, 0, '', '', '',0)
obj.newSt('Joe', 'Smith', 22222, '123-22-477', 'CS', '7/28/1999', 'Boston', 4)

obj.newSt('William', 'Chen', 54321, '436-23-933', 'Math', '6/12/2001', 'Boston', 3.7)

obj.newSt('Bob', 'Johnson', 12345, '997-61-426', 'CS', '4/06/2001', 'Boston', 4)

obj.newSt('Zoey', 'Brown', 98764, '005-88-821', 'Crimial Justice', '06/17/2002', 'Boston', 3.3)

obj.newSt('Tim', 'Drake', 33333, '877-55-974', 'Crimial Justice', '07/19/2004', 'Boston', 4)


#Clears data inside table
def eraseTree():
    for i in tree.get_children():
      tree.delete(i)


#Display all data inside list of student
def showSt():
    eraseTree()
    for i in range(studentLt.__len__()):
      tree.insert('', 'end', text="1", values=(studentLt[i].nameF, studentLt[i].nameL, studentLt[i].ID, studentLt[i].SSN, studentLt[i].M, studentLt[i].BD, studentLt[i].adr, studentLt[i].GPA ))

    boxFN.delete(0, END)
    boxLN.delete(0, END)
    boxID.delete(0, END)
    boxSSN.delete(0, END)
    boxM.delete(0, END)
    boxBD.delete(0, END)
    boxAdr.delete(0, END)
    boxGPA.delete(0, END)
    
    buttonUpdate['state'] = DISABLED


#Searches student in list
def searchStudent():
    if e.get() == '':
        return
    eraseTree()
    ID = int(e.get())
    for i in range(studentLt.__len__()):
        if (int(studentLt[i].ID) == ID):
            tree.insert('', 'end', text="1", values=(studentLt[i].nameF, studentLt[i].nameL, studentLt[i].ID, studentLt[i].SSN, studentLt[i].M, studentLt[i].BD, studentLt[i].adr, studentLt[i].GPA ))
            e.delete(0, END)
            updateIndex[0] = i
            buttonUpdate['state'] = NORMAL
            boxFN.insert(0, studentLt[i].nameF)
            boxLN.insert(0, studentLt[i].nameL)
            boxID.insert(0, studentLt[i].ID)
            boxSSN.insert(0, studentLt[i].SSN)
            boxM.insert(0, studentLt[i].M)
            boxBD.insert(0, studentLt[i].BD)
            boxAdr.insert(0, studentLt[i].adr)
            boxGPA.insert(0, studentLt[i].GPA)
            return
    e.delete(0,END)
    

#Update existing data
def updateStudent():

    if  boxFN.get() == '' or boxLN.get() == '' or boxID.get() == '' or boxSSN.get() == '' or boxM.get() == '' or boxBD.get() == '' or boxAdr.get() == '' or boxGPA.get() == '' or len(str(boxID.get())) != 5:
        return
    i = updateIndex[0]
    for x in range(studentLt.__len__()):
        if (x == i):
            continue
        if (int(studentLt[x].ID) == int(boxID.get())):
            return
    
    studentLt[i].nameF = boxFN.get()
    studentLt[i].nameL = boxLN.get()
    studentLt[i].ID = int(boxID.get())
    studentLt[i].SSN = boxSSN.get()
    studentLt[i].M = boxM.get()
    studentLt[i].BD = boxBD.get()
    studentLt[i].adr = boxAdr.get()
    studentLt[i].GPA = float(boxGPA.get())
    
    boxFN.delete(0, END)
    boxLN.delete(0, END)
    boxID.delete(0, END)
    boxSSN.delete(0, END)
    boxM.delete(0, END)
    boxBD.delete(0, END)
    boxAdr.delete(0, END)
    boxGPA.delete(0, END)
    
    buttonUpdate['state'] = DISABLED
    
    showSt()
            
            
#Deleting students from list
def deleteStudent():
    if d.get() == '':
        return
    ID = int(d.get())
    for i in range(studentLt.__len__()):
        if (int(studentLt[i].ID) == ID):
            d.delete(0, END)
            del studentLt[i]
            showSt()
            return


#Create new student
def createStudent():
    if  boxFN.get() == '' or boxLN.get() == '' or boxID.get() == '' or boxSSN.get() == '' or boxM.get() == '' or boxBD.get() == '' or boxAdr.get() == '' or boxGPA.get() == '' or len(str(boxID.get())) != 5:
        return
    ID = int(boxID.get())
    for i in range(studentLt.__len__()):
        if (int(studentLt[i].ID) == ID):
            return
    
    obj.newSt(boxFN.get(), boxLN.get(), int(boxID.get()), boxSSN.get(), boxM.get(), boxBD.get(), boxAdr.get(), boxGPA.get())
    boxFN.delete(0, END)
    boxLN.delete(0, END)
    boxID.delete(0, END)
    boxSSN.delete(0, END)
    boxM.delete(0, END)
    boxBD.delete(0, END)
    boxAdr.delete(0, END)
    boxGPA.delete(0, END)
    
    buttonUpdate['state'] = DISABLED
    
    showSt()
    
    
#Sort data
def queryData():
    if clicked.get() == 'First Name':
        studentLt.sort(key=sort_itemFN)
    elif clicked.get() == 'Last Name':
        studentLt.sort(key=sort_itemLN)
    elif clicked.get() == 'ID':
        studentLt.sort(key=sort_itemID)
    else:
        studentLt.sort(key=sort_itemFN)
    showSt()
    
        
    

def sort_itemFN(item):
    return item.nameF

def sort_itemLN(item):
    return item.nameL

def sort_itemID(item):
    return item.ID




#tkinter GUI
root = Tk()

root.geometry('1800x500')


#Table and table titles
labelTitle = Label(root, text="Students:")
labelTitle.grid(row=0, column=0)

tree = ttk.Treeview(root, column=("First Name", "Last Name", 'ID', 'SSN', 'Major', 'Birthdate', 'Address', 'GPA'), show='headings', height=10)

tree.column("# 1", anchor=CENTER, stretch=NO,  minwidth=0, width=150)
tree.heading("# 1", text="FirstN")

tree.column("# 2", anchor=CENTER, stretch=NO,  minwidth=0, width=150)
tree.heading("# 2", text="LastN")

tree.column("# 3", anchor=CENTER, stretch=NO,  minwidth=0, width=150)
tree.heading("# 3", text="ID")

tree.column("# 4", anchor=CENTER, stretch=NO,  minwidth=0, width=150)
tree.heading("# 4", text="SSN")

tree.column("# 5", anchor=CENTER, stretch=NO,  minwidth=0, width=150)
tree.heading("# 5", text="Major")

tree.column("# 6", anchor=CENTER, stretch=NO,  minwidth=0, width=150)
tree.heading("# 6", text="Birthdate")

tree.column("# 7", anchor=CENTER, stretch=NO,  minwidth=0, width=150)
tree.heading("# 7", text="Address")

tree.column("# 8", anchor=CENTER, stretch=NO,  minwidth=0, width=150)
tree.heading("# 8", text="GPA")

tree.grid(row=1, column=0, columnspan=8)


#Search Student
labelTitle = Label(root, text="Search Student: ")
labelTitle.grid(row=2, column=0)
labelTitle2 = Label(root, text="Enter ID: ")
labelTitle2.grid(row=3, column=0)
e = Entry(root, width = 20)
e.grid(row=3, column=1)
buttonSearch = Button(root, text = 'Search', command = searchStudent)
buttonSearch.grid(row=3,column=2)





#View all students
view= Button(root, text='View All Students', command = showSt)
view.grid(row=2, column=7)




#sort data
clicked = StringVar()
clicked.set("Sort By")
drop = OptionMenu(root, clicked, 'First Name', 'Last Name', 'ID')
drop.grid(row=2, column=5)

buttonSort= Button(root, text='Sort', command = queryData)
buttonSort.grid(row=2, column=6)




#Delete student
labelDel = Label(root, text='Delete Student: ')
labelDel.grid(row=4,column=0)
labelDel = Label(root, text='Enter ID: ')
labelDel.grid(row=5,column=0)
d = Entry(root, width = 20)
d.grid(row=5, column=1)
buttonSearch = Button(root, text = 'Delete', command=deleteStudent)
buttonSearch.grid(row=5,column=2)



#Student Info
labelFN = Label(root, text='First Name:')
labelFN.grid(row=6,column=0)
labelLN = Label(root, text='Last Name:')
labelLN.grid(row=6,column=1)
labelID = Label(root, text='ID(5 digits):')
labelID.grid(row=6,column=2)
labelSSN = Label(root, text='SSN:')
labelSSN.grid(row=6,column=3)
labelM = Label(root, text='Major:')
labelM.grid(row=6,column=4)
labelBD = Label(root, text='Birthdate:')
labelBD.grid(row=6,column=5)
labelAdr = Label(root, text='Address:')
labelAdr.grid(row=6,column=6)
labelGPA = Label(root, text='GPA:')
labelGPA.grid(row=6,column=7)

#Student Info Boxes
boxFN = Entry(root, width=20)
boxFN.grid(row=7,column=0)
boxLN = Entry(root, width=20)
boxLN.grid(row=7,column=1)
boxID = Entry(root, width=20)
boxID.grid(row=7,column=2)
boxSSN = Entry(root, width=20)
boxSSN.grid(row=7,column=3)
boxM = Entry(root, width=20)
boxM.grid(row=7,column=4)
boxBD = Entry(root, width=20)
boxBD.grid(row=7,column=5)
boxAdr = Entry(root, width=20)
boxAdr.grid(row=7,column=6)
boxGPA = Entry(root, width=20)
boxGPA.grid(row=7,column=7)


#Update/Create student button
buttonCreate = Button(root, text='Create', command=createStudent)
buttonCreate.grid(row=7, column=8)
buttonUpdate = Button(root, text='Update Student', command=updateStudent, state=DISABLED)
buttonUpdate.grid(row=7, column=9)

showSt()




root.mainloop()

print('cool')