# PZ Weapon File Manager
# made by PeculiarDirt

import os

inputfolderpath = "csvimport/"       #what weapons folder to look at
outputfilename = str        #name of the final folder
outputfolderpath = "csvseparated/"
weaponcounter = int      

def separatecsv(): 
    global weaponcounter
    weaponlist = []
    
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

    for number, file in enumerate(filesfound):     #for every item in the list, try to make a file
        if str(number) in selectedinput.split(" ") or "all" in selectedinput:
            try:
                os.mkdir(outputfolderpath + str(file).replace(" ",""))
                print(f"\n>>>Directory '{outputfolderpath + str(file).replace(" ","")}' created successfully.")
            except FileExistsError:
                print(f"\n>>>Directory '{outputfolderpath + str(file).replace(" ","")}' already exists.")
            except PermissionError:
                print(f"\n>>>Permission denied: Unable to create '{outputfolderpath + str(file).replace(" ","")}'.")
            except Exception as e:
                print(f"\n>>>An error occurred: {e}")
        
        

            print(">>>Opening " + file)
            currentfile = open(inputfolderpath + "/" + file,"rt")     #open the csv file
        
        
            for line in currentfile:                        #for every line in the file
                weaponcounter = int(1)
                curline = line.strip()                  #clean up
                curline = curline.replace("\n","")
                curline = curline.split(",")
                
                
            
                if line.startswith("item"):                 #if it is the item line, and the first line should always be the item line
                    weaponlist = ["" for weapon in range(len(curline)-1)]       #create a weapon name list for the csv file
                    #print(weaponlist)
                
                    for weaponstat in curline:
                        if weaponstat != "item":
                            outputfilename = outputfolderpath + str(file).replace(" ","") + "/" + weaponstat.replace("\n","") + ".txt"
                            with open(outputfilename, 'w') as curfile:      #create the txt file for each weapon
                                curfile.write("\titem " + weaponstat + "\n")
                                curfile.write("\t{\n")
                            weaponlist[weaponcounter-1] = curline[weaponcounter]
                            #print(weaponlist)
                            weaponcounter += 1
                    continue
            
                for weap in range(len(weaponlist)):          #for the length of the weapon list
                    outputfilename = outputfolderpath + str(file).replace(" ","") + "/" + weaponlist[weaponcounter-1].replace("\n","") + ".txt"  #the current weapon file
                    
                    curfile = open(outputfilename, 'a')      #add to the existing file
                
                    if curline[0] == "Bayonnet":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    elif curline[0] == "GunLight":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    elif curline[0] == "IronSight":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    elif curline[0] == "Laser":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    elif curline[0] == "RecoilPad":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    elif curline[0] == "RedDot":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    elif curline[0] == "x2Scope":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    elif curline[0] == "x4Scope":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    elif curline[0] == "x8Scope":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    elif curline[0] == "ChokeTubeFull":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    elif curline[0] == "ChokeTubeImproved":
                        if curline[weaponcounter] != "":
                            curfile.write("\t\tModelWeaponPart = " + curline[weaponcounter] + ",\n")    #all of these used for weapon attachments
                        curfile.close
                        weaponcounter += 1
                        continue
                    else:
                        if curline[weaponcounter] != "":
                            curfile.write("\t\t" + curline[0] + " = " + curline[weaponcounter] + ",\n")    #if the line isnt empty, add it to the file
                            curfile.close
                            weaponcounter += 1
                            continue
                        else:
                            curfile.close
                            weaponcounter += 1
                            continue
                    #print("weapon #" + str(weaponcounter-1) + outputfilename)
                    #print("current line " + str(curline))
            

            for weap in range(len(weaponlist)):          #for the length of the weapon list
                outputfilename = outputfolderpath + str(file).replace(" ","") + "/" + weaponlist[weap-1].replace("\n","") + ".txt"  #the current weapon file
                curfile = open(outputfilename, 'a')      #add to the existing file
                curfile.write("\t}")    #add the weapon state name
                print(">>>Finished weapon: " + weaponlist[weap])
                curfile.close
                
            
            print(">>>Finished file")
            currentfile.close()
            print(">>>Total weapons found: " + str(weaponcounter - 1))
        
        
    

print()
print(">>>PZ Weapon File Manager by PeculiarDirt")
print(">>>Beginning conversion of 'csvimport' to separate weapon files\n")

try:
    separatecsv()
except Exception as e:
    print(f"\n>>>An error occurred: {e}")

print(f"\n>>>Separation completed, your file(s) are located in '{outputfolderpath}'")