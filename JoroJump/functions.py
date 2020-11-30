from platform_class import *
from player_class import *
from powerup_class import *

def platform_manager(platforms):
    #checks if platforms have fallen off the bottom of the screen and deletes them
    for p in platforms:
        if p.ypos > height:
            platforms.remove(p)
        else:
            pass
    #makes sure that there are always 6 platforms on the screen
    while len(platforms) < 6:
        new_platform = platform([random(400), 700-(145*len(platforms))])
        platforms.append(new_platform)
        
def powerup_manager(powerups):
    for p in powerups:
        if p.ypos > height * 3.5:
            powerups.remove(p)
        else:
            pass
        
    while len(powerups) < 1:
        new_powerup = powerup([random(425), 100-(145*len(powerups))])
        powerups.append(new_powerup)
