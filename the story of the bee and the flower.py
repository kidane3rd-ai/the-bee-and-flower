import pgzrun
import random
WIDTH=600
HEIGHT=700
bee=Actor("bee")
bee.pos=203,230
flower=Actor("flower")
flower.pos=400,450
score=0
def draw():
    screen.blit("grass",(0,0))
    screen.draw.text("score "+str(score),center=(400,60),fontsize=30)
    bee.draw()
    flower.draw()

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2  
    if keyboard.down:
        bee.y=bee.y+2 
    if bee.colliderect(flower):
        flower.x=random.randint(70,550)
        flower.y=random.randint(70,650)
        score=score+10  

pgzrun.go()
