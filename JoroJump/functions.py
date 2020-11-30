from platform_class import *
from player_class import *
from powerup_class import *

def platform_manager(platforms):
    #remove plataformas que saem da tela
    for p in platforms:
        if p.ypos > height:
            platforms.remove(p)
        else:
            pass
    #sempre 6 plataformas na tela
    while len(platforms) < 6:
        new_platform = platform([random(400), 700-(145*len(platforms))])
        platforms.append(new_platform)
        
def powerup_manager(powerups):
    #remove powerups que saem da tela
    for p in powerups:
        if p.ypos > height * 3.5:
            powerups.remove(p)
        else:
            pass
    #powerup com frequencia de 3.5 telas    
    while len(powerups) < 1:
        new_powerup = powerup([random(425), 100-(145*len(powerups))])
        powerups.append(new_powerup)
