# PZ Weapon File Manager
# made by PeculiarDirt

import os

inputfolderpath = "importseparated/"       #what weapons folder to look at
outputfilename = str        #name of the final folder
outputfolderpath = "final/" 
selectedfileslist = []


def readinputfolder():
    filesfound = os.listdir(inputfolderpath)      #find all folder names
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


    for number, file in enumerate(filesfound):     #for every folder in the list, try to make the final file
        if str(number) in selectedinput.split(" ") or "all" in selectedinput:
            outputfilename = outputfolderpath + file.replace("csv","txt")
            weaponpackitems = os.listdir(inputfolderpath + file)        #find all weapons in the pack
            
            currentfilefinal = open(outputfilename,"w")       #create the final file and start writing
            print(f"\n>>>Created file '{file.replace("csv","txt")}'")
            print(">>>Found " + str(len(weaponpackitems)) + " weapons:")
            print(weaponpackitems)
            currentfilefinal.write("module Base\n")
            currentfilefinal.write("{\n")
            currentfilefinal.write("\timports{Base}\n\n")
            for weapon in weaponpackitems:          #for each weapon txt in the folder, add the entirety of the txt to the final file
                print(">>>Reading " + inputfolderpath + file + "/" + weapon)
                currentweapon = open(inputfolderpath + file + "/" + weapon,"r")
                currentfilefinal.writelines(currentweapon)
                currentfilefinal.write("\n")
            currentfilefinal.write("}")
            print(">>>Finished reading file")
            currentfilefinal.close()
        
    

print()
print(">>>PZ Weapon File Manager by PeculiarDirt")
print(">>>Beginning conversion of separated import to final file\n")

try:
    readinputfolder()
except Exception as e:
    print(f"\n>>>An error occurred: {e}")

print(f"\n>>>Final weapon pack(s) completed, your files are located in '{outputfolderpath}'")