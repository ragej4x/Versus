import pygame as pg

#PLAYER 1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class player_1():
    def __init__(self) -> None:

        #CHAR ++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.sasuke = True
        self.naruto = False

        self.x = 0
        self.y = 300
        self.vel_x = 5
        self.vel_y = 10
        self.action_list = []
        self.move_right = False
        self.move_left = False
        self.right = True
        self.left = False
        self.jump = False

        #SKILL +++++++++++++++++
        self.dash = False
        self.dashcount = 0

    def update(self,window,keyinput):
        collider = pg.draw.rect(window ,(255,0,0), (self.x ,self.y, 30,45),1)

        #MOVEMENT ++++++++++++++++++++++++++++++++++++++++++++++
        if keyinput[pg.K_RIGHT]:
            self.x += self.vel_x
            self.right = True
            self.left = False

        if keyinput[pg.K_LEFT]:
            self.x -= self.vel_x
            self.right = False
            self.left = True

        if keyinput[pg.K_UP]:
            self.jump = True
        
        if self.jump == True:
            if self.right == True:
                self.x += 2
            if self.left == True:
                self.x -= 2

            self.y -= self.vel_y *1.5
            self.vel_y -= 0.5
            if self.vel_y < -10:
                self.jump = False
                self.vel_y = 10
                self.y = 300

# BORDER
        if self.x < 0:
            self.x = 0
        if self.x > 650:
            self.x = 650


    def sasuke_skill_p1(self,keyinput):
        if keyinput[pg.K_r]:
            pass


p1 = player_1()


#PLAYER 2 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class player_2():
    def __init__(self) -> None:

        #CHAR ++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.sasuke = True
        self.naruto = False

        self.x = 650
        self.y = 300
        self.vel_x = 5
        self.vel_y = 10
        self.action_list = []
        self.move_right = False
        self.move_left = False
        self.right = False
        self.left = True
        self.jump = False

    def update(self,window,keyinput):
        collider = pg.draw.rect(window ,(255,0,0), (self.x ,self.y, 30,45),1)

        #MOVEMENT ++++++++++++++++++++++++++++++++++++++++++++++
        if keyinput[pg.K_d]:
            self.x += self.vel_x
            self.right = True
            self.left = False

        if keyinput[pg.K_a]:
            self.x -= self.vel_x
            self.right = False
            self.left = True

        if keyinput[pg.K_w]:
            self.jump = True
        
        if self.jump == True:
            if self.right == True:
                self.x += 2
            if self.left == True:
                self.x -= 2

            self.y -= self.vel_y *1.5
            self.vel_y -= 0.5
            if self.vel_y < -10:
                self.jump = False
                self.vel_y = 10
                self.y = 300

# BORDER
        if self.x < 0:
            self.x = 0
        if self.x > 650:
            self.x = 650


    def sasuke_skill_p2():
        pass


p2 = player_2()