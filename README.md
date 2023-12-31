# FQ Extractor
Extracts an NES ROM from Full Quiet (Windows).

This script is derived from anpage's script at https://gist.github.com/anpage/b895a34efb0bf1e4a9a4f52228067fa8

## Script Requirements
* Full Quiet (Windows)
  * Purchase from Steam at https://store.steampowered.com/app/2383920/Full_Quiet/
* Python 3
  * Download at https://python.org
 
## Instructions
* Install Full Quiet (Windows)
* Navigate to the default installation directory (normally "C:\Program Files (x86)\Steam\steamapps\common\Full Quiet").
* Copy the script into the "FullQuiet_Data" folder
* Run the script

## FAQ
### Are there any differences between the Windows ROM and the Game Pak release?
From what I can tell from screenshots (as I don't own the Game Pak), the only difference is that the Windows ROM refers to the Start Button as the "Menu" Button and the Select Button as the "View" Button. 

### The game received an update and now the script doesn't work
This is most likely due to the offsets the script uses to locate the ROM changing. I'll do my best to fix it ASAP.
