import pygame as pg
import player
import animation
import zipfile

width , height = 1024 , 600
display = pg.display.set_mode((width , height))
window = pg.Surface((width//1.5 , height//1.5))
pg.display.set_caption("Versus")
clock = pg.time.Clock()
pg.init()


def fps_display():
    font = pg.font.Font("data/Fipps-Regular.otf" , 18 , bold = True)
    count = str(int(clock.get_fps()))
    fps = font.render(count,True , (30,30,30))
    display.blit(fps,(5,5))

def event_handler():
    global loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False


    surface = pg.transform.scale(window , (width , height))
    display.blit(surface,(0,0))

    fps_display()
    pg.display.flip()
    clock.tick(60)


# MAIN LOOP ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

loop = True
while loop == True:
    window.fill((255,255,255))
    keyinput = pg.key.get_pressed()

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    player.p1.update(window , keyinput)

    animation.sasuke.update_p1(pg, window , keyinput)

    event_handler()