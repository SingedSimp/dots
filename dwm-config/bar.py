from time import sleep
from subprocess import call
from os import system, popen
import json
while True:
    # Load file
    f = open("/home/eclipse/.cache/wal/colors.json")
    colors=json.load(f)
    f.close()
    # Get battery level and state
    bat=popen("cat /sys/class/power_supply/BAT0/capacity").read()
    stat=popen("cat /sys/class/power_supply/BAT0/status").read()
    bat="^b" + colors['colors']['color6'] + "^ " + bat.strip() + "%, " + stat.strip()
    # Get time in hours:minutes:seconds
    time=popen("date +%H:%M:%S").read()
    time="^b" + colors['colors']['color4'] + "^ " + time.strip()
    # Get if network is up or not
    ud=popen("cat /sys/class/net/wlo1/operstate").read().strip()
    if ud == "up":
        net = "Connected"
    else:
        net = "Disconnected"
    net = "^b" + colors['colors']['color3'] + "^ " + net
    # Get Current Theme
    theme = colors['wallpaper']
    name = theme.split("/")[4]
    name = name.split(".")[0]
    name = name.replace("-", " ")
    name = name.title()
    theme = "^b" + colors['colors']['color5'] + "^ " + name
    # Display all colors
    col0 = "^b" + colors["colors"]["color0"] + "^ "
    col1 = "^b" + colors["colors"]["color1"] + "^ "
    col2 = "^b" + colors["colors"]["color2"] + "^ "
    col3 = "^b" + colors["colors"]["color3"] + "^ "
    col4 = "^b" + colors["colors"]["color4"] + "^ "
    col5 = "^b" + colors["colors"]["color5"] + "^ "
    col6 = "^b" + colors["colors"]["color6"] + "^ "
    col7 = "^b" + colors["colors"]["color7"] + "^ "
    col8 = "^b" + colors["colors"]["color8"] + "^ "
    col9 = "^b" + colors["colors"]["color9"] + "^ "
    col10 = "^b" + colors["colors"]["color10"] + "^ "
    col11 = "^b" + colors["colors"]["color11"] + "^ "
    col12 = "^b" + colors["colors"]["color12"] + "^ "
    col13 = "^b" + colors["colors"]["color13"] + "^ "
    col14 = "^b" + colors["colors"]["color14"] + "^ "
    col15 = "^b" + colors["colors"]["color15"] + "^ "
    fcol = col0+col1+col2+col3+col4+col5+col6+col7+col8+col9+col10+col11+col12+col13+col14+col15

    # Make a divider to center the colors in the middle of the screen
    num = 70 - len(name)
    div = "^b" + colors['special']['background'] + "^"
    for i in range(num):
        div = div + " "
    system(f"xsetroot -name '{fcol}{div} {theme} {net} {bat} {time} '")
    sleep(1)
