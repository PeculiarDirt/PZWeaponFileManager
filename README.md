# PZWeaponFileManager

Project to help manage weapon code, uses python 3 and comes with .bat files and a user friendly way of selecting files


***Allows you to do the following:***

- Find all possible weapon stats/parameters (DisplayName, Weight, WeaponSprite, etc) that are in your txts (lines that can be used multiple times like "ModelWeaponPart" will only show once)

- Convert your txt containing all weapons to separate weapon files

- Convert separate weapon files to CSV, allowing you to import it to a spreadsheet (Tested with Google Sheets only, theoretically it should also work with Microsoft Excel)

- Convert CSV files to separate weapons

- Convert separate weapon files to a final file for PZ



***Things to note:***

- For windows, please use the _"*****.bat"_ files to run the scripts

- Each section is dedicated to each item type: Firearms for guns, melee for melee, and other for anything else like throwables

- This has only been tested with vanilla weapons and vanilla friendly mods, custom content is not guaranteed to be supported

- For firearms, weapon attachment (ModelWeaponPart) sorting has been hardcoded in, currently supports Bayonnet/GunLight/IronSight/Laser/RecoilPad/RedDot/x2Scope/x4Scope/x8Scope/ChokeTubeFull/ChokeTubeImproved, may change it later to support custom lists of attachments, for now you may have to add them in manually if they are not vanilla

- For melee, items like "Saucepan" which included an advanced subsection in them (ie: component FluidContainer { ... }) may not be carried into the CSV file, they must be manually added back in afterwards

- Currently supports firearms, melee, and an "other" section for anything else like throwables/equipment (anything involving CSV does not 100% support modded content, this may require modifying the code, or simply adding a new list in "weaponstatlists")


***How to use the scripts:***

- (Vanilla weapon files have been included in this so you can see an example of what exactly happens in the folders at each stage)

0. **"INSTALLPYTHON"** - Python 3 is required to use these scripts, you can either download it by running the _"INSTALLPYTHON"_ bat file or downloading it through the official website: https://www.python.org/downloads/. These scripts should also be compatible with Linux, though I have not tested it there.

1. **"SeparateImport"** - To start, add your txt file with all your weapons in it to the _"import"_ folder, then you can use the _"SeparateImport"_ script to separate all the weapons into individual txt files, which will then appear in the _"importseparated"_ folder. From here, you can either edit each weapon txt to your liking and then use the _"ImportSepToFinal"_ script in step 4 to finalize them, or you can then convert them to CSV in step 2.

2. **"ImportSepToCSV"** - To convert your weapons into a CSV file which can be imported to a spreadsheet, run the _"ImportSepToCSV"_ script. This script will also ask you to select a "weapon stat list", I have supplied a vanilla list and a custom list that is just the vanilla list but sorted to my personal preference. All this does is tell the script what to look for and which order they should be in. This is explained more in the _"ListAllStats"_ step below. After the script is done, your CSV file will be located in the _"csvexport"_ folder. This file can then be imported to a spreadsheet to make managing everything at once easier. To import CSV in Microsoft Excel, follow these steps: https://support.microsoft.com/en-us/office/import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba. To import CSV files in Google Sheets, create a spreadsheet, then at the top left click _FILE > IMPORT > UPLOAD_ and add your CSV file into the box. Afterwards, select the _"Import location"_ (I prefer to insert new sheet) you can leave the rest as it is and click _"Import data"_. All the data should then show up right in front of you. Feel free to colorize and format what you want, you can move columns (the weapons) left/right or the rows (stats/parameters) up/down. 

   * **"ListAllStats"** - For most users, you will not need to touch this, unless you are working in the _"other"_ section or with weapons that have custom stats/parameters that are not in the vanilla game. This script simply searches the files in the _"import"_ folder for all potential stats/parameters in each txt file and prints them into a file in the _"potentialstats"_ folder. You can then copy these lists into the _"weaponstatlists"_ folder and reorganize the lines if you want.

3. **"SeparateCSVImport"** - Once you are done editing the spreadsheet, you can simply export it as a CSV. To export CSV in Microsoft Excel, follow these steps: https://support.microsoft.com/en-us/office/import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba. To export CSV files in Google Sheets, at the top left click _FILE > DOWNLOAD > CSV_. You can then copy the file that is downloaded and paste it in the _"csvimport"_ folder. Then simply run the _"SeparateCSVImport"_ script to separate the CSV file back into separate weapon files, these files will be located in the _"csvseparated"_ folder, this script functions similarly to the script in step 1.

4. **"CSVToFinal and ImportSepToFinal"** - To finalize your separated weapons from the CSV file, run the _"CSVToFinal"_ script to create the final txt file that can be copied directly to your mod folder. To finalize your separated weapons from the _"importseparated"_ folder, run the _"ImportSepToFinal"_ script to create the final txt file.

