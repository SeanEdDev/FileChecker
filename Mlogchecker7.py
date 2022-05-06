
import os
import datetime


#line 13- result line identifier
#line 16- result file name
#line 25- folder path
#line 27- chose which type of files to check, upto two at once


#setting string to search
string1 = 'SCF Done:'

#creating results file
resultfileName = 'dataSearch'

f = open(resultfileName, 'a')

#creating list
resultList = []
fileList =[]
finalList = []
#create list of directory
a_directory = r"\Users\Sean\Desktop\Code Projects\Mlogcheck3.0"
for filename in os.listdir(a_directory):
    if filename.endswith(".log") or filename.endswith(".log"):
        #setting flag and index to 0
        flag = 0
        index = 0

        #setting file path
        file1 = open(filename,"r")

        #setting name of open file
        fileName = file1.name

        #Loop through the file line by line
        for line in file1:  
            index += 1 
                        
        #checking string is present in line or not
            if string1 in line:
                flag = 1
                break
                            
        #checking condition for string found or not
        if flag == 0: 
            print('String', string1 , 'Not Found') 
        elif string1 in line:
            #splitting line and taking the number needed
            test_str = line.split()
            resultList.insert(0, test_str[4])
            finalList =[float(item) for item in resultList]
            fileList.insert(0,fileName)
        else:
            continue

correctFile = finalList.index(min(finalList))

    
lowestFile = fileList[correctFile]
lowestInt = (min(finalList))

f.write(str(datetime.datetime.now()))
f.write("   ")
f.write(lowestFile)
f.write("   ")
f.write(str(lowestInt))
f.write("\n")
