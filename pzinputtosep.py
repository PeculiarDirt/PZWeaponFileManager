# pz weapon file splitter
# made by PeculiarDirt

#import datetime
import os

inputfolderpath = "rawimport/"       #what weapons folder to look at
outputfilename = str        #name of the final folder
outputfolderpath = str
weaponpackname = str        #user inputs name of weapon pack
readingweapon = False
currentweapon = ""

    
def readinputfolder(): 
    global readingweapon
    global currentweapon
    filelist = os.listdir(inputfolderpath)      #find all file names
    print("\n>>>Found " + str(len(filelist)) + " files:")
    print(filelist)
    print("")
    
    for file in filelist:     #for every item in the list
        outputfolderpath = "separateweaps/" + file
        try:
            os.mkdir(outputfolderpath)
            print(f"\n>>>Directory '{outputfolderpath}' created successfully.")
        except FileExistsError:
            print(f"\n>>>Directory '{outputfolderpath}' already exists.")
        except PermissionError:
            print(f"\n>>>Permission denied: Unable to create '{outputfolderpath}'.")
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
                    outputfile = open(outputfolderpath + "/" + currentweapon + ".txt", mode='w', newline ='')     #create the final file
               
            if readingweapon:
                outputfile.write(line)
            
            if "}" in line:
                if readingweapon == True:
                    readingweapon = False
                    outputfile.close 
                    print(">>>Finished weapon:" + currentweapon)
                    
        print(">>>Finished sorting file: " + file)
            
        currentfile.close()






    

print()
print(">>>PZ Weapon Stats File Converter by PeculiarDirt")
print(">>>Beginning auto conversion of input files to separate weapons\n")
readinputfolder()
print("\n>>>Separation completed...")