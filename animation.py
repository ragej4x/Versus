import player

class sasukeAnim():
    def __init__(self) -> None:
        self.x = 1
        self.y = 1

        self.runanimlist = []
        self.runanimlistleft = []
        self.runcount = 0
        self.runcountleft = 0

        self.idleanimlist = []
        self.idleanimlistleft = []
        self.idlecount = 0
        self.idlecountleft = 0

    #RUN ANIM +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def update_p1(self,pg,window , keyinput):

        if player.p1.sasuke == True:
            self.x = player.p1.x -3
            self.y = player.p1.y -14
    

            if keyinput[pg.K_RIGHT] and keyinput[pg.K_LEFT] == False and player.p1.right == True:

                for num in range(1,7):
                    runframe = pg.image.load(f"data/bin/sasuke/run{num}.anim")
                    runframe.set_colorkey((255,0,255))
                    self.runanimlist.append(runframe)
                    if player.p1.jump == False:
                        window.blit(self.runanimlist[int(self.runcount)] , (self.x ,self.y))

                self.runcount += 0.2
                self.idlecount = 0
                self.idlecountleft = 0


            if not keyinput[pg.K_RIGHT]:
                self.runcount = 0


            if keyinput[pg.K_LEFT] and keyinput[pg.K_RIGHT] == False and player.p1.left == True:
                for num in range(1,7):
                    runframeleft = pg.image.load(f"data/bin/sasuke/run{num}.anim")
                    runframeleft = pg.transform.flip(runframeleft  , True , False)
                    runframeleft.set_colorkey((255,0,255))
                    self.runanimlistleft.append(runframeleft)

                    if player.p1.jump == False:
                        window.blit(self.runanimlistleft[int(self.runcountleft)], (self.x - 14, self.y))
                    
                self.runcountleft += 0.2
                self.idlecount = 0
                self.idlecountleft = 0


            if not keyinput[pg.K_LEFT]:
                self.runcountleft = 0


            if keyinput[pg.K_LEFT] == True  and keyinput[pg.K_RIGHT] == True :
                for num in range(1,7):
                    runframe = pg.image.load(f"data/bin/sasuke/run{num}.anim")
                    runframe.set_colorkey((255,0,255))
                    self.runanimlist.append(runframe)

                    if player.p1.jump == False:
                        window.blit(self.runanimlist[int(self.runcount)] , (self.x ,self.y))

                
                player.p1.right = True
                player.p1.x += 5
                self.runcount += 0.2

            if not keyinput[pg.K_LEFT] == True  and keyinput[pg.K_RIGHT] == True:
                self.runcountleft = 0
                self.idlecount = 0
                self.idlecountleft = 0

        #IDLE ANIM +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            
            if player.p1.right == True and keyinput[pg.K_LEFT] == False and keyinput[pg.K_RIGHT] == False:
                for num in range(1,5):
                    idleframe = pg.image.load(f"data/bin/sasuke/idle{num}.anim")
                    idleframe.set_colorkey((255,0,255))
                    self.idleanimlist.append(idleframe)

                    if player.p1.jump == False:
                        window.blit(self.idleanimlist[int(self.idlecount)] , (self.x ,self.y))                    

            if player.p1.left == True and keyinput[pg.K_LEFT] == False and keyinput[pg.K_RIGHT] == False:
                for num in range(1,5):
                    idleframeleft = pg.image.load(f"data/bin/sasuke/idle{num}.anim")
                    idleframeleft = pg.transform.flip(idleframeleft , True , False)               
                    idleframeleft.set_colorkey((255,0,255))
                    self.idleanimlistleft.append(idleframeleft)

                    if player.p1.jump == False:
                        window.blit(self.idleanimlistleft[int(self.idlecountleft)],(self.x , self.y))

            self.idlecount += 0.2
            self.idlecountleft += 0.2

        #JUMP ANIM +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


sasuke = sasukeAnim()