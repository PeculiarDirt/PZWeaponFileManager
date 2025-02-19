# PZ Weapon File Manager
# made by PeculiarDirt

import os

inputfolderpath = "import/"       #what weapons folder to look at
outputfilename = str        #name of the final folder
outputfolderpath = "importseparated/"
weaponpackname = str        #user inputs name of weapon pack
readingweapon = False
currentweapon = ""

    
def separateimport(): 
    global readingweapon
    global currentweapon
    global outputfolderpath
    selectedinput = str
    
    filesfound = os.listdir(inputfolderpath)      #find all file names
    print("\n>>>Found " + str(len(filesfound)) + " weapon packs:")
    for number, file in enumerate(filesfound):
        print("\t" + str(number) + " - " + str(file))
    print("\n>>>Please select each weapon pack you wish to convert with a space inbetween each number")
    print(">>>Your choices can be in any order")
    print(">>>For example: 2 1 4 16 8\n")
    selectedinput = input("Selection: ")
    
    for number, file in enumerate(filesfound):     
        if str(number) in selectedinput.split(" "):
            outputfilename = outputfolderpath + file  
            weaponcounter = int(1)     
            try:
                os.mkdir(outputfilename)                   #for every item in the list, try to make a file
                print(f"\n>>>Directory '{outputfilename}' created successfully.")
            except FileExistsError:
                print(f"\n>>>Directory '{outputfilename}' already exists.")
            except PermissionError:
                print(f"\n>>>Permission denied: Unable to create '{outputfilename}'.")
            except Exception as e:
                print(f"\n>>>An error occurred: {e}")
        

            print(">>>Opening " + file)
            currentfile = open(inputfolderpath + "/" + file,"rt")     #open the file
        
        
            for line in currentfile:       #for each line in the file
            
                if "item" in line:
                    if readingweapon == False:
                        readingweapon = True
                        curline = line
                        #curline = line.replace(" ","")      #removes the spaces
                        #curline = curline.replace(",","")   #removes the comma
                        curline = curline.replace("\n","")  #removes new line text
                        curline = curline.replace("\t","")  #removes tabs
                        curline = curline.split(" ")
                        currentweapon = curline[1]
                        outputfile = open(outputfilename + "/" + currentweapon + ".txt", mode='w', newline ='')     #create the final file
               
                if readingweapon:
                    outputfile.write(line)
            
                if "}" in line:
                    if readingweapon == True:
                        readingweapon = False
                        outputfile.close 
                        print(">>>Finished weapon: " + currentweapon)
                        weaponcounter += 1
                    
            print(">>>Finished file")
            print("Total weapons found: " + str(weaponcounter - 1))
            
            currentfile.close()






    

print()
print(">>>PZ Weapon File Manager by PeculiarDirt")
print(">>>Beginning conversion of 'import' files to separate weapon files\n")

try:
    separateimport()
except Exception as e:
    print(f"\n>>>An error occurred: {e}")

print("\n>>>Separation completed, your file(s) are located in '" + str(outputfolderpath) + "'")