import player

class sasukeAnimP1():
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

        self.jumpanimlist = []
        self.jumpcount = 0
        self.jumpanimlistleft = []
        self.jumpcountleft = 0

        self.fallanimlist = []
        self.fallcount = 0


#PLAYER 1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def update_p1(self,pg,window , keyinput):

        if player.p1.sasuke == True:
            self.x = player.p1.x -3
            self.y = player.p1.y -14

    #RUN ANIM +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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


            if keyinput[pg.K_LEFT] == True and keyinput[pg.K_RIGHT] == True :
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
                        window.blit(self.idleanimlistleft[int(self.idlecountleft)],(self.x - 14, self.y))

            self.idlecount += 0.2
            self.idlecountleft += 0.2

        #JUMP AND FALL ANIM +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


            if player.p1.vel_y < 9 and player.p1.right == True and player.p1.left == False:
                for num in range(1,5):
                    jumpframe = pg.image.load(f"data/bin/sasuke/jump{num}.anim")
                    self.jumpanimlist.append(jumpframe)
                    jumpframe.set_colorkey((255,0,255))
                    window.blit(self.jumpanimlist[int(self.jumpcount)],(self.x , self.y))
            
                self.jumpcount += 0.1

            if player.p1.vel_y < 9 and player.p1.left == True  and player.p1.right == False:
                for num in range(1,5):
                    jumpframeleft = pg.image.load(f"data/bin/sasuke/jump{num}.anim")
                    jumpframeleft = pg.transform.flip(jumpframeleft , True , False)
                    self.jumpanimlistleft.append(jumpframeleft)
                    jumpframeleft.set_colorkey((255,0,255))
                    window.blit(self.jumpanimlistleft[int(self.jumpcountleft)],(self.x -14, self.y))
            
                self.jumpcountleft += 0.1

            if keyinput[pg.K_RIGHT] == True and keyinput[pg.K_LEFT] == True and player.p1.jump == True:
                for num in range(1,5):
                    jumpframe = pg.image.load(f"data/bin/sasuke/jump{num}.anim")
                    self.jumpanimlist.append(jumpframe)
                    jumpframe.set_colorkey((255,0,255))
                    window.blit(self.jumpanimlist[int(self.jumpcount)],(self.x , self.y))
            
                self.jumpcount += 0.1


            if player.p1.vel_y == 10:
                self.jumpcount = 0
                self.jumpcountleft = 0


# PLAYER 2 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


sasuke_p1 = sasukeAnimP1()

class sasukeAnimP2():
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

        self.jumpanimlist = []
        self.jumpcount = 0
        self.jumpanimlistleft = []
        self.jumpcountleft = 0

        self.fallanimlist = []
        self.fallcount = 0

    def update_p2(self,pg,window , keyinput):

        if player.p2.sasuke == True:
            self.x = player.p2.x -3
            self.y = player.p2.y -14

    #RUN ANIM +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            if keyinput[pg.K_d] and keyinput[pg.K_a] == False and player.p2.right == True:

                for num in range(1,7):
                    runframe = pg.image.load(f"data/bin/sasuke/run{num}.anim")
                    runframe.set_colorkey((255,0,255))
                    self.runanimlist.append(runframe)
                    if player.p2.jump == False:
                        window.blit(self.runanimlist[int(self.runcount)] , (self.x ,self.y))

                self.runcount += 0.2
                self.idlecount = 0
                self.idlecountleft = 0


            if not keyinput[pg.K_d]:
                self.runcount = 0


            if keyinput[pg.K_a] and keyinput[pg.K_d] == False and player.p2.left == True:
                for num in range(1,7):
                    runframeleft = pg.image.load(f"data/bin/sasuke/run{num}.anim")
                    runframeleft = pg.transform.flip(runframeleft  , True , False)
                    runframeleft.set_colorkey((255,0,255))
                    self.runanimlistleft.append(runframeleft)

                    if player.p2.jump == False:
                        window.blit(self.runanimlistleft[int(self.runcountleft)], (self.x - 14, self.y))
                    
                self.runcountleft += 0.2
                self.idlecount = 0
                self.idlecountleft = 0


            if not keyinput[pg.K_a]:
                self.runcountleft = 0


            if keyinput[pg.K_a] == True and keyinput[pg.K_d] == True :
                for num in range(1,7):
                    runframe = pg.image.load(f"data/bin/sasuke/run{num}.anim")
                    runframe.set_colorkey((255,0,255))
                    self.runanimlist.append(runframe)

                    if player.p2.jump == False:
                        window.blit(self.runanimlist[int(self.runcount)] , (self.x ,self.y))

                
                player.p2.right = True
                player.p2.x += 5
                self.runcount += 0.2

            if not keyinput[pg.K_a] == True  and keyinput[pg.K_d] == True:
                self.runcountleft = 0
                self.idlecount = 0
                self.idlecountleft = 0

        #IDLE ANIM +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            
            if player.p2.right == True and keyinput[pg.K_a] == False and keyinput[pg.K_d] == False:
                for num in range(1,5):
                    idleframe = pg.image.load(f"data/bin/sasuke/idle{num}.anim")
                    idleframe.set_colorkey((255,0,255))
                    self.idleanimlist.append(idleframe)

                    if player.p2.jump == False:
                        window.blit(self.idleanimlist[int(self.idlecount)] , (self.x ,self.y))                    

            if player.p2.left == True and keyinput[pg.K_a] == False and keyinput[pg.K_d] == False:
                for num in range(1,5):
                    idleframeleft = pg.image.load(f"data/bin/sasuke/idle{num}.anim")
                    idleframeleft = pg.transform.flip(idleframeleft , True , False)               
                    idleframeleft.set_colorkey((255,0,255))
                    self.idleanimlistleft.append(idleframeleft)

                    if player.p2.jump == False:
                        window.blit(self.idleanimlistleft[int(self.idlecountleft)],(self.x - 14, self.y))

            self.idlecount += 0.2
            self.idlecountleft += 0.2

        #JUMP AND FALL ANIM +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


            if player.p2.vel_y < 9 and player.p2.right == True and player.p2.left == False:
                for num in range(1,5):
                    jumpframe = pg.image.load(f"data/bin/sasuke/jump{num}.anim")
                    self.jumpanimlist.append(jumpframe)
                    jumpframe.set_colorkey((255,0,255))
                    window.blit(self.jumpanimlist[int(self.jumpcount)],(self.x , self.y))
            
                self.jumpcount += 0.1

            if player.p2.vel_y < 9 and player.p2.left == True  and player.p2.right == False:
                for num in range(1,5):
                    jumpframeleft = pg.image.load(f"data/bin/sasuke/jump{num}.anim")
                    jumpframeleft = pg.transform.flip(jumpframeleft , True , False)
                    self.jumpanimlistleft.append(jumpframeleft)
                    jumpframeleft.set_colorkey((255,0,255))
                    window.blit(self.jumpanimlistleft[int(self.jumpcountleft)],(self.x -14, self.y))
            
                self.jumpcountleft += 0.1

            if keyinput[pg.K_d] == True and keyinput[pg.K_a] == True and player.p2.jump == True:
                for num in range(1,5):
                    jumpframe = pg.image.load(f"data/bin/sasuke/jump{num}.anim")
                    self.jumpanimlist.append(jumpframe)
                    jumpframe.set_colorkey((255,0,255))
                    window.blit(self.jumpanimlist[int(self.jumpcount)],(self.x , self.y))
            
                self.jumpcount += 0.1


            if player.p2.vel_y == 10:
                self.jumpcount = 0
                self.jumpcountleft = 0

sasuke_p2 = sasukeAnimP2()