import Building
import Worker
import pygame
import numpy as np

class CommandCenter(Building.Building):
    def __init__(self, x, y, imgsurf, isEnemy):
        super().__init__(x, y, imgsurf, isEnemy)
        #render
        xsize = 200
        ysize = 200
        self.rect = pygame.Rect(x - xsize/2,y - ysize/2,xsize,ysize)
        self.img = imgsurf
        self.healthrectwidth = xsize
        self.healthrect = np.array([x - xsize/2,y - ysize/2 - 8,xsize, 5])
        #stats
        self.health = 500 #1500
        self.maxhealth = 500 #1500
        #physics
        self.circlecenter = np.array([int(x),int(y)])
        self.radius = int(xsize/5)

    def update(self, input):
        if(self.health <= 0):
            self.alive = False
        self.handle_input(input)

    def handle_input(self, input):
        if self.selected:
            if input.keys[pygame.K_s]:
                print("creating worker!")

    def buildWorker(self, entityList, scvsurf, entityquadtree, enemyEntityList, enemyEntityQuadtree, playerInfo):
        #Create units and enemies and set up data structures
        # (1,2) = x,y coords on background surface, (3,4) = image size
        if not self.enemy and playerInfo.resources >= 1:
            for x in range(50, 1000, 20):
                spotTaken = False
                for entity in entityList:
                    #Some entity is already in that location
                    if self.x + x == entity.rect[0]:
                        spotTaken = True

                # If we try to place a worker in the same spot of another the game will crash, here we have found an empty spot
                if spotTaken == False:
                    # print(self.x + x, self.y + x)
                    workerrect = pygame.Rect(self.x + x,self.y + x,45,45)
                    worker1 = Worker.Worker(15,scvsurf,workerrect,self.enemy)
                    #Handle if enemy/user was created
                    entityList.append(worker1)
                    entityquadtree.insertstart(worker1)  #W/out Node is none error
                    playerInfo.givepopulation(1)
                    playerInfo.removeresources(1)
                    #Stop looping
                    return
        elif self.enemy:
            #Enemy
            for x in range(50, 1000, 20):
                spotTaken = False
                for enemyEntity in enemyEntityList:
                    #Some entity is already in that location
                    if self.x + x == enemyEntity.rect[0]:
                        spotTaken = True

                if spotTaken == False:
                    workerrect = pygame.Rect(self.x + x,self.y + x,45,45)
                    worker1 = Worker.Worker(15,scvsurf,workerrect,self.enemy)
                    #Handle if enemy/user was created
                    enemyEntityList.append(worker1)
                    enemyEntityQuadtree.insertstart(worker1)  #W/out Node is none error
                    #Stop looping
                    return
