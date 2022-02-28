import sys
import os
import re

#setting string to search
string1 = 'SCF Done:'

#creating results file
resultfileName = 'dataSearch'

f = open(resultfileName, 'a')

#creating list
resultList = []
fileList =[]

#create list of directory
a_directory = r"\Users\seana\OneDrive\Desktop\Mlogcheck3.0"
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
        else:
            test_str = line
            res = re.findall('.[-+]?\d+', test_str)
            resultList.insert(0,res)
            del resultList[0][0]
            del resultList[0][2]
            fileList.insert(0,fileName)
             

        #Extra information on file/line   
        #f.write("Line ")
        #f.write(str(index))
        #f.write(" In File ")
        #f.write(fileName )
        #f.write(" RESULT ")
        #f.write(line)
        #f.write("\n")
        
        continue
    else:
           
        continue
#file to number match var
correctFile = resultList.index(max(resultList))
#finding smallest negative number in list
result = max(resultList)

#converting ints to list
string_ints = [str(int) for int in result]
string_of_ints = ",".join(string_ints)
string_of_ints = string_of_ints.replace(',','')

#Testing results
#printing results to verify
#print("result")
#print(fileList[correctFile])
#print(string_of_ints)

#converting results to vars for external use
resultInt = float(string_of_ints)
resultFile = str(fileList[correctFile])

#writing result to file
f.write(string_of_ints)
f.write("   ")
f.write(str(resultFile))

#Print write to console
print(resultInt)
print(resultFile)