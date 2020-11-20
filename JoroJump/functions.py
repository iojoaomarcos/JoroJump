from platform_class import *
from player_class import *

def platform_manager(platforms):
    #checks if platforms have fallen off the bottom of the screen and deletes them
    for p in platforms:
        if p.ypos > height:
            platforms.remove(p)
        else:
            pass
    #makes sure that there are always 6 platforms on the screen
    while len(platforms) < 6:
        new_platform = platform([random(425), 700-(145*len(platforms))])
        platforms.append(new_platform)