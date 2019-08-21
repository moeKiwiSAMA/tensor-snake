import numpy as np
import time
import random

class snake:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.error = 0
        self.center = (int(height / 2), int(width / 2))
        self.location =  []
        self.foodlocation = (0, 0)
        self.dirct = "l"
        self.matrix = np.zeros([height,width], int)
        self.start()
        pass
    def spawn(self, place):
        try:
            self.matrix.itemset(place, 1)
            self.location.insert(0, place)
            print(self.location)
        except:
            self.error = 1
            pass

    def suicide(self):
        lo = len(self.location) - 1
        print("remove", self.location[lo])
        self.matrix.itemset(self.location[lo], 0)
        self.location.pop()
    def start(self):
        self.spawn((int(self.height / 2), int(self.width / 2) - 1))
        self.spawn((int(self.height / 2), int(self.width / 2)))
        self.spawn((int(self.height / 2), int(self.width / 2) + 1))
        self.genFood()
    def genFood(self):
        while True:
            self.foodlocation = (random.randint(0, self.height), random.randint(0, self.width))
            if self.foodlocation not in self.location:
                break
        self.matrix.itemset(self.foodlocation, 2)
    def checkspawn(self, x, y):
        if x > self.height - 1 or y > self.width - 1:
            self.error = 1
        else:
            self.spawn((x, y))
            if self.foodlocation != (x, y):
                self.suicide()
            else:
                self.genFood()
    def run(self):
        if self.dirct == "h":
            self.checkspawn(self.location[0][0], self.location[0][1] - 1)
        elif self.dirct == "j":
            self.checkspawn(self.location[0][0] + 1, self.location[0][1])
        elif self.dirct == "k":
            self.checkspawn(self.location[0][0] - 1, self.location[0][1])
        else:   # self.dirct == "l"
            self.checkspawn(self.location[0][0], self.location[0][1] + 1)
        if len(self.location)!=len(set(self.location)):
            self.error = 1
    def refresh(self, dirct):

        self.dirct = dirct
        self.run()
        print(self.matrix)

if __name__ == '__main__':
    s = snake(20, 20)
    while True:
        if s.error == 1:
            print("error")
            break
        s.refresh("j")
        time.sleep(0.1)