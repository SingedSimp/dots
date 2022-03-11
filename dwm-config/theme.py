import dmenu
from os import listdir
from subprocess import call
wp='/home/eclipse/.wallpapers/'
wpList=listdir(wp)
wpnList=[]
for wpn in wpList:
    wpn = wpn.split(".")[0]
    wpn = wpn.replace("-", " ")
    wpn = wpn.title()
    wpnList.append(wpn)
wpnList.sort()
wpList.sort()
prompt='Theme:'
sel = dmenu.show(wpnList, prompt=prompt, case_insensitive=True)
ind = wpnList.index(sel)
sel = wpList[ind]
if sel == "rias-stripes.png":
    call(f'wal --theme /home/eclipse/.config/wal/colorschemes/dark/rias.json',shell=True)
else:
    call(f'wal -i {wp+sel}',shell=True)
#call(f'xdotool key "Super+C"', shell=True)
