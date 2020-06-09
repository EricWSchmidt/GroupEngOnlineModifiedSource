# -*- coding: utf-8 -*-
    # This file is part of GroupENG Online. 
    # Copyright (C) 2020  Dr. Gabriel Walton, Eric Schmidt, Jean Duong, Cole Callihan, Stephen Thoemmes 

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU Affero General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU Affero General Public License for more details.

    # You should have received a copy of the GNU Affero General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Created on Wed May 13 10:32:09 2020
@author: User
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import csv
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename
import ntpath
import webbrowser
import xlrd
import os

#This function will return the file from a path
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#Open a file 
master = Tk()
master.update()
fileNamePath = askopenfilename()
fileName=path_leaf(fileNamePath)


groupingAttributes = ['Don\'t use','Distribute','Aggregate','Cluster']
#data collected from file
studentIDValues=[]
studentAttributeList = []
allFileData = []
selectedValuesList = []

#Reading in file
if fileNamePath.endswith('.csv'):
    with open(fileNamePath) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        #Collect header names from input file
        for row in readCSV:
            studentAttributeList = row
            break
        #collect ID values for verification
        #make table of all data
        for row in readCSV:
            studentIDValues.append(row[0])
            allFileData.append(row)
        
#Read in .xlsx file and fill in varables the same as with the .csv readin above
elif fileName.endswith('.xlsx'):

    studentAttributeList=pd.read_excel(fileName).columns
    #Collect header names from input file
    wb = xlrd.open_workbook(fileName)
    ws = wb.sheet_by_index(0)
    studentIDValues = ws.col_values(0)
    studentIDValues.pop(0)
    for i in range (1,len(studentIDValues)):
        allFileData.append(ws.row_values(i))
else:
    print('Input file\'s type is not supported')
    master.destroy()
    exit

#Ensure all ID's are unique
if(len(set(studentIDValues)) != len(studentIDValues)):
    print('Student ID values are not all unique') 
    master.destroy()
    exit


arrayOfAllData = np.array(allFileData)  #convert panda's array to numpy for column simplicity


variableList = []
attributeGroupingList =[]

#---------------------------------------------GROUPING SIZE WINDOW FUNCTION---------------------------------------
h = Label(master, text='Choose how to group:',font='Helvetica 10 bold')
h.pack()

#what is this link: Window to explain how to use the "Choose how to group" section
def groupSizeWIT():
    whatIsThisWindow = Tk()
    labelWIT = Label(whatIsThisWindow, text='Using: \"Choose how to group:\"',font='Helvetica 10 bold')
    labelWIT.pack()
    labelWIT1 = Label(whatIsThisWindow, text='1.Pick between making groups bases on \"Group size\" or  \"Number of Groups\"\n\n2.In the following text box, enter the numeric quanity of \"Group size\" or \"Number of Groups\" you\'d like.\n(e.g if you want groups of size 4, you\'d select \"Group size\" and enter \"4\" in the text box)\n\n3.Finally, incase the number of students isn\'t divisable by the size or number of groups, \n you may select if groups may have one \"Extra member\" or \"One less member\"\n\n',anchor ='w')
    labelWIT1.pack()
    exitButtonWIT = Button(whatIsThisWindow, text="Got it!", command=whatIsThisWindow.destroy)
    exitButtonWIT.pack()
    
whatIsThis1 = Label(master, text="What is this?", fg="blue", cursor="hand2") #hand2
whatIsThis1.pack()
whatIsThis1.bind("<Button-1>", lambda e: groupSizeWIT())
#Radio buttons for group size/number selection
groupingMethod = StringVar()
groupingMethod.set(0)
Radiobutton(master, text="Group Size",padx = 20, variable=groupingMethod, value=0).pack()
Radiobutton(master, text="Number of Groups",padx = 20, variable=groupingMethod,value=1).pack()

#text box for number input
groupVal = StringVar()
ee = Entry(master, textvariable=groupVal,width=3)
ee.pack()
ee.delete(0, END)
ee.insert(0, "2")
if(groupVal == "3"):
    ff = Label(master, text='size is 3:\n')
    ff.pack()

#boxes for rounding up or down group size or number
label3 = Label(master, text='Groups may have:')
label3.pack()
groupingRounding= StringVar()
groupingRounding.set(0)
Radiobutton(master, text="Extra member",padx = 5, variable=groupingRounding, value=0,height = 1).pack()
Radiobutton(master, text="One less member",padx = 5, variable=groupingRounding,value=1,height = 1).pack()

label5 = Label(master, text='\nHow would you like to group students \nbased on their attrubutes?:',font='Helvetica 10 bold')
label5.pack()

#what is this link: Window to explain how to use the "How would you like to group students based on their attrubutes?:" section
def attributeWIT():
    whatIsThisWindow = Tk()
    labelWIT = Label(whatIsThisWindow, text='Using: \'How would you like to group students \nbased on their attributes?\':',font='Helvetica 10 bold')
    labelWIT.pack()
    labelWIT1 = Label(whatIsThisWindow, text='Each student attribute has a drop down menu containing \"Don\"t use\", \"Distribute\", \"Aggregate\", \"Cluster\", and \"Balance\" \nPick how students will be grouped based on each attribute.\n\n',anchor ='w',font='Helvetica 10')
    labelWIT1.pack()
    labelWIT = Label(whatIsThisWindow, text='Distribute: ',font='Helvetica 9 bold')
    labelWIT.pack()
    labelWIT2 = Label(whatIsThisWindow, text='Spread students with some attribute (major, a needed skill) across all groups so that each group has about the same number of them\n',anchor ='w')
    labelWIT2.pack()
    labelWIT = Label(whatIsThisWindow, text='Aggregate: ',font='Helvetica 9 bold')
    labelWIT.pack()
    labelWIT2 = Label(whatIsThisWindow, text='Group students with some attribute (project choice, section number) together in the same groups\n',anchor ='w')
    labelWIT2.pack()
    labelWIT = Label(whatIsThisWindow, text='Cluster: ',font='Helvetica 9 bold')
    labelWIT.pack()
    labelWIT2 = Label(whatIsThisWindow, text='Ensure that students with some attribute (women, minorities) are not isolated in a group (there will be at least 2 of them in a group).\n',anchor ='w')
    labelWIT2.pack()
    labelWIT = Label(whatIsThisWindow, text='Balance: ',font='Helvetica 9 bold')
    labelWIT.pack()
    labelWIT2 = Label(whatIsThisWindow, text='Ensure equal strength of groups based on some numeric score (GPA, pretest).\n',anchor ='w')
    labelWIT2.pack()
    exitButtonWIT = Button(whatIsThisWindow, text="Got it!", command=whatIsThisWindow.destroy)
    exitButtonWIT.pack()
whatIsThis1 = Label(master, text="What is this?", fg="blue", cursor="hand2") #hand2
whatIsThis1.pack()
whatIsThis1.bind("<Button-1>", lambda e: attributeWIT())


#Drop down menu for each student attribute (E.g GPA's downdown has selection of ['Don't use','Distribute','Aggregate','Cluster', 'Balance']
for i in range (1,len(studentAttributeList)):
    setOfColumnValues= set(arrayOfAllData[:,i])
    setOfColumnValues = list(setOfColumnValues)
    attributesNumeric = False
    try:
        setOfColumnValues=np.array(setOfColumnValues)
        setOfColumnValues=setOfColumnValues.astype(float)
        attributesNumeric = True
    except Exception as e:
                print(e)    
    #if(np.array_equal(df.v, df.v.astype(double)))
    variable = StringVar(master)
    variable.set(groupingAttributes[0]) # default value
    variableList.append(variable)
    a = Label(master, text=studentAttributeList[i])
    a.pack()
    if(attributesNumeric ==True):
        tempGroupingAttributes = ['Don\'t use','Distribute','Aggregate','Cluster', 'Balance']
        w = OptionMenu(master, variableList[i-1], *tempGroupingAttributes)
    else:
        w = OptionMenu(master, variableList[i-1], *groupingAttributes)

    w.pack()


#This function tells you in cosole choices selected
#It will also create a new menu for the 'Cluster' and 'Distrubute' variables
def ok():   
    makeCriteriaWindow=False
    criteriaWindow = Tk()
    tempPickedValues = []
    for i in range (1,len(studentAttributeList)):
        if(variableList[i-1].get() == 'Cluster' or variableList[i-1].get() == 'Distribute'):
            makeCriteriaWindow = True
    #If any attributes have 'Cluster' or 'distribute' as their criteria, the user must
    #also pick the values they want to specift
    
    #link window telling user why they must select variables
    if(makeCriteriaWindow == True):
        def variableWIT():
            whatIsThisWindow = Tk()
            labelWIT = Label(whatIsThisWindow, text='Using: \'Criteria options\':',font='Helvetica 10 bold')
            labelWIT.pack()
            labelWIT1 = Label(whatIsThisWindow, text='Student attributes selected as \"Cluster\" or \"Distribute\" must also specify which varibles\n the attribute holds should be clustered or distributed amoungst groups.\n',anchor ='w',font='Helvetica 10')
            labelWIT1.pack()
            labelWIT = Label(whatIsThisWindow, text='Please Note the Following:\n',font='Helvetica 9 bold')
            labelWIT.pack()
            labelWIT = Label(whatIsThisWindow, text='Distribute: ',font='Helvetica 9 bold')
            labelWIT.pack()
            labelWIT2 = Label(whatIsThisWindow, text='Spread students with some attribute (major, a needed skill) across all groups so that each group has about the same number of them.\n',anchor ='w')
            labelWIT2.pack()
            labelWIT = Label(whatIsThisWindow, text='Cluster: ',font='Helvetica 9 bold')
            labelWIT.pack()
            labelWIT2 = Label(whatIsThisWindow, text='Ensure that students with some attribute (women, minorities) are not isolated in a group (there will be at least 2 of them in a group).\n',anchor ='w')
            labelWIT2.pack()
            exitButtonWIT = Button(whatIsThisWindow, text="Got it!", command=whatIsThisWindow.destroy)
            exitButtonWIT.pack()
        af = Label(criteriaWindow, text='Criteria options',font='Helvetica 10 bold')
        af.pack()
        whatIsThis1 = Label(criteriaWindow, text="What is this?", fg="blue", cursor="hand2") #hand2
        whatIsThis1.pack()
        whatIsThis1.bind("<Button-1>", lambda e: variableWIT())
        af = Label(criteriaWindow, text='\n')
        af.pack()
        
        #make list of list's that represent the values in the columns the user wishes to cluster or distribute
        for i in range (1,len(studentAttributeList)):
            if(variableList[i-1].get() == 'Cluster' or variableList[i-1].get() == 'Distribute'):
                #Get set of vlaues in the attribute column
                setOfColumnValues= set(arrayOfAllData[:,i])
                setOfColumnValues = list(setOfColumnValues)
                newVariable = StringVar(criteriaWindow)
                newVariable.set(setOfColumnValues[0]) # default value
                variableList.append(newVariable)
                #string explination for user
                tempText = "Which " +studentAttributeList[i] +"(s) would you like to " +variableList[i-1].get()
                aa = Label(criteriaWindow, text=tempText)
                aa.pack(anchor="center")
                j=0
                tempselectedValuesList = []
                for element in setOfColumnValues:
                    variable1 = IntVar(criteriaWindow)
                    variable1.set(0) # default value
                    tempselectedValuesList.append(variable1)
                    
                    www = Checkbutton(criteriaWindow, text=element, variable=variable1)
                    www.pack(anchor="center")
                    j=j+1
                
                selectedValuesList.append(tempselectedValuesList)
            #This will make writing easier because the index of the studentAttributeList correleates to
            #the same index of selectedValuesList
            else:
                emptyList =[]
                selectedValuesList.append(emptyList)
                #tempselectedValuesList.clear()
    else:
        noVarLabel1 = Label(criteriaWindow, text='No attributes were selected as \'Cluster\' or \'Distribute\'',font='Helvetica 10 bold')
        noVarLabel1.pack()
        noVarLabel2 = Label(criteriaWindow, text='\nTo set variables to cluster or ditribute, \nplease pick \'Cluster\' or \'Distribute\' for one of the attributes in the previous winow')
        noVarLabel2.pack()
     #okay button to exit out of second window (criteriaWindow)
    #selectedValuesList.append(tempPickedValues[0])

       
    
    exitButton = Button(criteriaWindow, text="OK", command=criteriaWindow.destroy)
    exitButton.pack()
    mainloop()

labelF = Label(master, text='\n\n')
labelF.pack()
button = Button(master, text="Set Variables", command=ok)
button.pack()

#command that first checks if all attributes which have 'Cluster' or 'Distribute'
#also have variables set. If not, open criteria window
# also prevent's exiting without enough data for specification file

def exitChoice():
    #If the user wanted to cluster 
    openOk=False
    specificationHasContent1 = False
    for i in range (1,len(studentAttributeList)):
        if(variableList[i-1].get() != 'Don\'t use'):
            specificationHasContent1 =True
        if((variableList[i-1].get() == 'Cluster' or variableList[i-1].get() == 'Distribute')):      
            if((len(selectedValuesList) == 0)):
                openOk=True
            elif((len(selectedValuesList[i-1]) == 0)):
                openOk=True
    if(openOk):
        ok()
    #Notification that no file can be made 
    elif(specificationHasContent1==False):
        whatIsThisWindow = Tk()
        labelWIT = Label(whatIsThisWindow, text='Enter criteria for groups to be formed',font='Helvetica 10 bold')
        labelWIT.pack()
        exitButtonWIT = Button(whatIsThisWindow, text="Got it!", command=whatIsThisWindow.destroy)
        exitButtonWIT.pack()
    else:
        master.destroy()
    
exitButton = Button(master, text="Done!", command=exitChoice)
exitButton.pack()

#Refrence link
def callback(url):
    webbrowser.open_new(url)

link1 = Label(master, text="GroupEng v1.3", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://www.groupeng.org/"))

mainloop()


#-------------------------------------------------FILE WRITING--------------------------------------------------
specificationFile="TEST_sample_group_specification.groupeng"
f = open(specificationFile, "w")
f.write("classlist : " + fileNamePath + '\n')
f.write("\nstudent_identifier : " + studentAttributeList[0])
#group sizing or numbers with extra or less member criteria
text = groupVal.get()
plusOrMinus = "+"
if(groupingRounding.get() == "1"):
    plusOrMinus = "-"
if(groupingMethod.get() =="0"):
    f.write("\n\ngroup_size : " + text + plusOrMinus)
else:
    f.write("\n\nnumber_of_groups : " + text)
    
    
#wite attributes and their grouping values
    
specificationHasContent = False
for i in range (1,len(studentAttributeList)):
    if(variableList[i-1].get() != 'Don\'t use'):
        specificationHasContent =True
        f.write("\n\n- " + variableList[i-1].get().lower() + " : "  + studentAttributeList[i])
        if(variableList[i-1].get() == 'Cluster' or variableList[i-1].get() == 'Distribute'):
            setOfColumnValues= set(arrayOfAllData[:,i])
            setOfColumnValues = list(setOfColumnValues)
            f.write("\n  value : ")
            tempVariableString=""
            for j in range (0,len(selectedValuesList[i-1])):
                if(selectedValuesList[i-1][j].get()==1):
                    tempVariableString = tempVariableString+setOfColumnValues[j] + ", "
              
            tempVariableString = tempVariableString[:-2]     
            f.write(tempVariableString)                  
                 
f.close()


#-------------------------------------------------------RUN GroupEng----------------------------------------------
import GroupEng
import os
if(specificationHasContent):
    specificationFile =os.path.abspath(specificationFile)
    GroupEng.run(specificationFile)
