# PZ Weapon File Manager
# made by PeculiarDirt

#import datetime
import os
import csv

inputfolderpath = "importseparated/"       #what weapons folder to look at
outputfilename = str        #name of the final folder
outputfilepath = "csvexport/"
weaponpackname = str        #user inputs name of weapon pack
filelist = []               #current list of files read in the folder
filesfound = []
weaponstatslistfolder = "weaponstatlists/"
weaponstatslistfile = ""

weaponstatslist=[  
    "item"
]

finalweaponstatslist = [[]]


def converttocsv(): 

    global inputfolderpath 
    filesfound = os.listdir(inputfolderpath)      #find all file names
    if len(filesfound) == int(0):
        print(f">>>No file(s) found in '{inputfolderpath}', please consider adding some\n")
        quit()
    print("\n>>>Found " + str(len(filesfound)) + " weapon packs:")
    for number, file in enumerate(filesfound):
        print("\t" + str(number) + " - " + str(file))
    print("\n>>>Please select each weapon pack you wish to convert with a space inbetween each number")
    print(">>>Your choices can be in any order")
    print(">>>If you wish to convert all, please enter 'all'")
    print(">>>Example A: 2 1 4 16 8")
    print(">>>Example B: all\n")
    selectedinput = input("Selection: ")
    print("\n")

    statslistsfound = os.listdir(weaponstatslistfolder) #find all weapon stat lists
    if len(statslistsfound) == int(0):
        print(f">>>No file(s) found in '{weaponstatslistfolder}', please consider adding some\n")
        quit()
    print("\n>>>Found " + str(len(statslistsfound)) + " weapon stat lists:")
    for number, file in enumerate(statslistsfound):
        print("\t" + str(number) + " - " + str(file))
    print("\n>>>Please select the organized weapon stat list that you want to use")
    print(">>>Example: 2")
    selectedinputlist = input("Selection: ")
    print("\n")
    weaponstatslistfile = statslistsfound[int(selectedinputlist)]
    print(weaponstatslistfile)
    
    statslist = open(weaponstatslistfolder + weaponstatslistfile,"rt")      #open the file
    for num, line in enumerate(statslist):          #add all weapon stats to the weaponstatslist list
        if line.strip() == "":
            continue
        curstat = line.strip()
        weaponstatslist.append(str(curstat))



    for number, file in enumerate(filesfound):     
        if str(number) in selectedinput.split(" ") or "all" in selectedinput:

            weaponpackname = file
            inputfolderpath = "importseparated/" + weaponpackname
    
            filelist = os.listdir(inputfolderpath)      #find all file names
            print("\n>>>Found " + str(len(filelist)) + " weapons in '" + str(inputfolderpath) + "/'")
            print(filelist)
            listlength = int(len(filelist))+1
            finalweaponstatslist = [["" for weapon in range(listlength)]for stat in weaponstatslist]      #sets length of final list based on number of files found

    
            weapstat = 0
            for row in finalweaponstatslist:
                finalweaponstatslist[weapstat][0] = weaponstatslist[weapstat]     #inserts the weapon stat name in each row
                weapstat+=1
       
            #print(finalweaponstatslist)
            #print("\n\n")
            currentweaponnum = 1
    
            for weaponname in filelist:     #for every weapon file found in the weapon pack
        
                #print(">>>Opening " + weaponname)
                currentfile = open(inputfolderpath + "/" + weaponname,"rt")     #open the file
                finalweaponstatslist[0][currentweaponnum] = weaponname.replace(".txt","")
                #print("weapon " + weaponname.replace(".txt","") + " in spot [0][" + str(currentweaponnum) + "]")
        

                for line in currentfile:       #for each line in the file
                    if line.strip().startswith("/*"):
                        #print(">>>Skipping commented out line")     #skip commented out lines
                        continue
            
            
                    curline = line.strip()
                    #print("current line: " + curline)
            
                    if "=" not in curline:
                        continue            #skips line if it is not a weapon stat
            
                    curline = curline.split("=")        #split the line into a list
            
                    #curline[0] = curline[0].replace(" ","")      #removes the spaces
                    curline[0] = curline[0].replace("{","")
                    curline[0] = curline[0].replace("}","")
                    curline[0] = curline[0].replace(",","")   #removes the comma
                    curline[0] = curline[0].replace("\n","")  #removes new line text
                    curline[0] = curline[0].replace("\t","")  #removes tabs
                    curline[0] = curline[0].strip()           #removes the spaces at the front and end
            
                    #if curline[0] !=  "DisplayName":
                    #    curline[1] = curline[1].replace(" ","")      #removes the spaces, do not use
                    curline[1] = curline[1].replace("{","")
                    curline[1] = curline[1].replace("}","")
                    curline[1] = curline[1].replace(",","")   #removes the comma
                    curline[1] = curline[1].replace("\n","")  #removes new line text
                    curline[1] = curline[1].replace("\t","")  #removes tabs
                    curline[1] = curline[1].strip()           #removes the spaces at the front and end
            
            
            
            
            
            
                
                    for index, stat in enumerate(finalweaponstatslist):
                        #for sanity, list[row, or the parameter, left right][column, or the specific weapons stat, up down]
                
                        #name       |       ak      |       m16     |
                        #accuracy   |       0.5     |       0.6     |
                        #sound      |       ak shot |       m16 shot|
                
                        
                        if curline[0] == finalweaponstatslist[index][0]:     #if the current line's stat equals the weapon stat in column 1 of the final list
                            #print("weapon stat found " + curline[0] + "==" + finalweaponstatslist[index][currentweaponnum] + "\n")
                            
                            finalweaponstatslist[index][currentweaponnum] = curline[1]
                            break
                        else:
                            #print("Weapon stat not listed " + curline[0]) 
                            #print(curline[0] + "=/=" + finalweaponstatslist[index][0]+ "\n")
                            continue            
                currentfile.close()
        
                #print(finalweaponstatslist)
                #print("\n\n")

                if (int(currentweaponnum)) == (int(len(filelist))):     #ends the loop when out of files
                    print(">>>Finished weapon: " + weaponname)
                    print(">>>Finished reading all weapon files")
                    break
                else:       #continues the loop
                    currentweaponnum += 1
                    print(">>>Finished weapon: " + weaponname)
            

            outputfilename = outputfilepath + weaponpackname + ".csv"
    
            with open(outputfilename, mode='w', newline ='') as outputfile:     #create the final file
                writer = csv.writer(outputfile)
                writer.writerows(finalweaponstatslist)
            outputfile.close()
    
            print(">>>Finished file")








print()
print(">>>PZ Weapon File Manager by PeculiarDirt")
print(">>>Beginning conversion of 'importseparated' files to CSV\n")

try:
    converttocsv()
except Exception as e:
    print(f"\n>>>An error occurred: {e}")

print("\n>>>Conversion completed, your file(s) are located in '" + str(outputfilepath) + "'")