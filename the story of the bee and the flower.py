import pgzrun

WIDTH=600
HEIGHT=700
bee=Actor("bee")
bee.pos=203,230
flower=Actor("flower")
flower.pos=400,450
def draw():
    screen.blit("green screen",(0,0))
    bee.draw()
    flower.draw()
    




pgzrun.go()