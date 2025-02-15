# pz weapon files to csv converter
# made by PeculiarDirt

#import datetime
import os
import csv

inputfolderpath = str       #what weapons folder to look at
outputfilename = str        #name of the final folder
outputfilepath = str
weaponpackname = str        #user inputs name of weapon pack
filelist = []               #current list of files read in the folder

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

def readweapfolder(): 
    filelist = os.listdir(inputfolderpath)      #find all file names
    print("\n>>>Found " + str(len(filelist)) + " weapons:")
    print(filelist)
    print("")
    listlength = int(len(filelist))+1
    finalweaponstatslist = [["" for weapon in range(listlength)]for stat in weaponstatslist]      #sets length of final list based on number of files found

    
    weapstat = 0
    for row in finalweaponstatslist:
        finalweaponstatslist[weapstat][0] = weaponstatslist[weapstat]     #inserts the weapon stat name in each row
        weapstat+=1
       
    #print(finalweaponstatslist)
    #print("\n\n")
    currentweaponnum = 1
    
    for weaponname in filelist:     #for every item in the list
        
        print(">>>Opening " + weaponname)
        currentfile = open(inputfolderpath + "/" + weaponname,"rt")     #open the file
        finalweaponstatslist[0][currentweaponnum] = weaponname.replace(".txt","")
        #print("weapon " + weaponname.replace(".txt","") + " in spot [0][" + str(currentweaponnum) + "]")
        currentmodelpart = 0
        

        for line in currentfile:       #for each line in the file
            if line.strip().startswith("/*"):
                print(">>>Skipping commented out line")     #skip commented out lines
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
                    if curline[0] == "ModelWeaponPart":
                        print(curline[0])
                    finalweaponstatslist[index][currentweaponnum] = curline[1]
                    break
                else:
                    #print("weapon stat not listed " + curline[0]) 
                    #print(curline[0] + "=/=" + finalweaponstatslist[index][0]+ "\n")
                    continue            
        currentfile.close()
        
        #print(finalweaponstatslist)
        #print("\n\n")

        if (int(currentweaponnum)) == (int(len(filelist))):     #ends the loop when out of files
            print(">>>Finished reading\n")
            print("\n>>>Finished reading all weapon files")
            break
        else:       #continues the loop
            currentweaponnum += 1
            print(">>>Finished reading\n")
            

    outputfilepath = "csv/" + weaponpackname + ".csv"
    
    with open(outputfilepath, mode='w', newline ='') as outputfile:     #create the final file
        writer = csv.writer(outputfile)
        writer.writerows(finalweaponstatslist)
    outputfile.close()
    
    print(">>>Created file: " + outputfilepath)





print()
print(">>>PZ Weapon Stats File Converter by PeculiarDirt")
print()
weaponpackname = input(">>>Please enter the name of the folder in 'separateweaps':")
inputfolderpath = "separateweaps/" + weaponpackname
readweapfolder()
print("\n>>>Conversion to CSV completed...")