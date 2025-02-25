# PZ Weapon File Manager
# made by PeculiarDirt

import os

inputfolderpath = "import/"       #what weapons folder to look at
outputfilename = str        #name of the final folder
outputfolderpath = "potentialstats/"
weaponpackname = str        #user inputs name of weapon pack
readingweapon = False
internalcomponent = False   #if there is an internal weapon stat that uses {} within a weapon
allweaponstats = [""]

    
def countimportstats(): 
    global readingweapon
    global outputfolderpath
    global allweaponstats
    global internalcomponent
    selectedinput = str
    
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
    
    for number, file in enumerate(filesfound):          #for every weapon pack
        if str(number) in selectedinput.split() or "all" in selectedinput:
            outputfilename = outputfolderpath + str(file)
            weaponcounter = int(0)  
        
            
            print(">>>Created file: " + str(outputfilename))
            outputfile = open(outputfilename, mode='w')     #create the final file
            print(">>>Opening " + str(file))
            currentfile = open(inputfolderpath + "/" + file,"rt")     #open the file
        
        
            for line in currentfile:       #for each line in the file
                #print("current line= " + line)
                if line.strip() == "":
                    #print("skipping empty line")
                    continue
                
                if line.strip().startswith("/*"):
                    #print("skipping commented out line")
                    continue
                
                if line.strip() == "{":
                    #print("skipping line with no useful info")
                    continue
                
                #if internalcomponent == True:
                #    #print("current line= " + str(line))
                #    #if readingweapon == True:
                #    if "}" in line.strip():
                #        #print("internal component end")
                #        internalcomponent = False
                #        continue
                #    else:
                #        continue
                
                if line.strip().startswith("item"):
                    if readingweapon == False:
                        readingweapon = True
                        curline = line.strip()
                        #curline = line.replace(" ","")      #removes the spaces
                        #curline = curline.replace(",","")   #removes the comma
                        #curline = curline.replace("\n","")  #removes new line text
                        curline = curline.replace("\t","")  #removes tabs
                        curline = curline.split()
                        currentweapon = curline[1]
                        #print("started reading item= " + str(curline[1]))
                        continue
                        
                if line.strip() == "}":
                    if readingweapon == True:
                        readingweapon = False
                        #print(">>>Finished reading weapon: " + currentweapon)
                        weaponcounter += 1
                        continue
                    else:
                        #print("reached end of file")
                        continue
                
                
                        
                if readingweapon:
                    #if "component" in line:
                    #    #print("found internal component")
                    #    internalcomponent = True
                    #    continue
                    if "=" not in line:
                        continue
                    curline = line.strip()
                    curline = curline.replace("\t","")  #removes tabs
                    curline = curline.replace("{","")  #removes tabs
                    if curline.strip() == "":
                        #print("skipping empty line")
                        continue
                    curline = curline.split("=")
                    if curline[0] not in allweaponstats:
                        allweaponstats.append(str(curline[0]))
                        #allweaponstats
                        #print("added stat= " + str(curline[0]))
                    
                        

            print(">>>Finished file")
            for num, stat in enumerate(allweaponstats):
                outputfile.write(allweaponstats[num].strip() + "\n")
            outputfile.close
            print(">>>Total weapons searched: " + str(weaponcounter))
            print(">>>Total unique stats found: " + str(len(allweaponstats)-1))
            print("")
                
                        
            currentfile.close()
                        



    
            
            






    

print()
print(">>>PZ Weapon File Manager by PeculiarDirt")
print(">>>Beginning collection of possible weapon stats in 'import' folder\n")

try:
    countimportstats()
except Exception as e:
    print(f"\n>>>An error occurred: {e}")

print("\n>>>Separation completed, list(s) located in '" + str(outputfolderpath) + "'")