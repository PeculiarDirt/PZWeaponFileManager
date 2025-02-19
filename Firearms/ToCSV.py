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

weaponstatslist=[  
    "item",
    "DisplayName",
    "Icon",
    "DisplayCategory",
    "SubCategory",
    "Tags",
    "Type",
    "WeaponSprite",
    "AttachmentType",
    "IdleAnim",
    "RunAnim",
    "SwingAnim",
    "WeaponReloadType",
    "TwoHandWeapon",
    "RequiresEquippedBothHands",
    "AmmoBox",
    "AmmoType",
    "MagazineType",
    "ClipSize",
    "MaxAmmo",
    "FireMode",
    "FireModePossibilities",
    "HaveChamber",
    "InsertAllBulletsReload",
    "ManuallyRemoveSpentRounds",
    "RackAfterShoot",
    "AimingMod",
    "AimingPerkCritModifier",
    "AimingPerkHitChanceModifier",
    "AimingPerkMinAngleModifier",
    "AimingPerkRangeModifier",
    "AimingTime",
    "ConditionLowerChanceOneIn",
    "ConditionMax",
    "CritDmgMultiplier",
    "CriticalChance",
    "DoorDamage",
    "HitChance",
    "ToHitModifier",
    "IsAimedFirearm",
    "IsAimedHandWeapon",
    "JamGunChance",
    "KnockBackOnNoDeath",
    "KnockdownMod",
    "MaxDamage",
    "MinDamage",
    "MaxHitCount",
    "MaxRange",
    "MinRange",
    "MaxSightRange",
    "MinSightRange",
    "MetalValue",
    "AngleFalloff",
    "MinAngle",
    "MultipleHitConditionAffected",
    "PiercingBullets",
    "ProjectileCount",
    "ProjectileSpread",
    "ProjectileWeightCenter",
    "PushBackMod",
    "Ranged",
    "RangeFalloff",
    "RecoilDelay",
    "ReloadTime",
    "ShareDamage",
    "StopPower",
    "SwingAmountBeforeImpact",
    "SwingTime",
    "MinimumSwingTime",
    "UseEndurance",
    "Weight",
    "SplatBloodOnNoDeath",
    "SplatNumber",
    "SplatSize",
    "BreakSound",
    "BringToBearSound",
    "ClickSound",
    "DropSound",
    "EjectAmmoSound",
    "EjectAmmoStartSound",
    "EjectAmmoStopSound",
    "EquipSound",
    "HitSound",
    "ImpactSound",
    "InsertAmmoSound",
    "InsertAmmoStartSound",
    "InsertAmmoStopSound",
    "NPCSoundBoost",
    "RackSound",
    "ShellFallSound",
    "SoundGain",
    "SoundRadius",
    "SoundVolume",
    "SwingSound",
    "UnequipSound",
    "Bayonnet",
    "GunLight",
    "IronSight",
    "Laser",
    "RecoilPad",
    "RedDot",
    "x2Scope",
    "x4Scope",
    "x8Scope",
    "ChokeTubeFull",
    "ChokeTubeImproved",
]
finalweaponstatslist = [[]]

whatismissing = [
    "AimingMod",
    "IsAimedHandWeapon",
    "ProjectileSpread",
    "ProjectileWeightCenter",
    "Bayonnet"
    ] #found missing from original list

def converttocsv(): 
    global inputfolderpath 
    filesfound = os.listdir(inputfolderpath)      #find all file names
    print("\n>>>Found " + str(len(filesfound)) + " weapon packs:")
    for number, file in enumerate(filesfound):
        print("\t" + str(number) + " - " + str(file))
    print("\n>>>Please select each weapon pack you wish to convert with a space inbetween each one")
    print(">>>Your choices can be in any order")
    print(">>>For example: 2 1 4 16 8\n")
    selectedinput = input("Selection: ")


    for number, file in enumerate(filesfound):     
        if str(number) in selectedinput.split(" "):

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
                
                        if curline[0] == "ModelWeaponPart":     #if the line is an attachment
                            if "Bayonnet" in curline[1]:
                                if "Bayonnet" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                            elif "GunLight" in curline[1]:
                                if "GunLight" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                            elif "IronSight" in curline[1]:
                                if "IronSight" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                            elif "Laser" in curline[1]:
                                if "Laser" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                            elif "RecoilPad" in curline[1]:
                                if "RecoilPad" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                            elif "RedDot" in curline[1]:
                                if "RedDot" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                            elif "x2Scope" in curline[1]:
                                if "x2Scope" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                            elif "x4Scope" in curline[1]:
                                if "x4Scope" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                            elif "x8Scope" in curline[1]:
                                if "x8Scope" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                            elif "ChokeTubeFull" in curline[1]:
                                if "ChokeTubeFull" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                            elif "ChokeTubeImproved" in curline[1]:
                                if "ChokeTubeImproved" in finalweaponstatslist[index][0]:
                                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                                    break
                        elif curline[0] == finalweaponstatslist[index][0]:     #if the current line's stat equals the weapon stat in column 1 of the final list
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