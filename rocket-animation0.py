import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()


size = width, height = 1000,1500
screen = pygame.display.set_mode(size)

#screen.fill((92,92,92))

image = pygame.image.load("/home/rezan/Pictures/long-range missile.png")                                            
image7 = pygame.image.load("/home/rezan/Pictures/long-range missile.png")
image1 = pygame.image.load("/home/rezan/Pictures/mountain.png")
image2 = pygame.image.load("/home/rezan/Pictures/explosion.png")####
image3 = pygame.image.load("/home/rezan/Pictures/helicopter.png")##
image5 = pygame.image.load("/home/rezan/Pictures/long-range missile (changed).png")
image6 = pygame.image.load("/home/rezan/Pictures/long-range missile (changed).png")


# Sound&Music
pygame.mixer.init()
sound = pygame.mixer.Sound("/home/rezan/Music/missle.ogg") #/home/rezan/Music/missle1.ogg
sound.play()

pygame.mixer.music.load('/home/rezan/Music/missle1.ogg')
pygame.mixer.music.play()









# Koordinaten:
x = 250 #
y = 500

x6 = 540####
y6 = 40

x1 = 200 ###
y1 = 500

x2 = 50
y2 = 600

x4 = 90####
y4 = 40

x5 = 250 #
y5 = 500

x3 = 200 ###
y3 = 500


pygame.display.flip()


clock = pygame.time.Clock()

running = False

while not running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = True
         
             
          
    screen.fill((92,92,92))
    screen.blit(image,(x,y))

# Explosion und Verschwinden von Rakete:

    if y5 == 40:

        y5+=1000
        x4-=1000
        screen.blit(image2,(x6,y6))
        screen.blit(image2,(540,70))
        screen.blit(image2,(550,60))
        screen.blit(image2,(560,50))
        screen.blit(image2,(570,40))
        screen.blit(image2,(530,30))
        screen.blit(image2,(520,20))
        screen.blit(image2,(510,10))
        screen.blit(image2,(500,0))
        screen.blit(image2,(490,30))
        
        
    x4+=1
        
        
   

# Aufzeigen der Bilder:
      
    #screen.blit(image2,(x6,y6))   
    screen.blit(image1,(x2,y2))
    #screen.blit(image6,(x1,y1))
    screen.blit(image3,(x4,y4))##
    screen.blit(image5,(x5,y5))
    #screen.blit(image7,(x3,y3))
    
    #y3-=1
    #y1-=1
    y5-=1                                                                  
    y-= 1
    if y == 400:
        y+=1000
    if y3 == 400:
        y3 += 1000
    
      
  
    #if y5 == 40:
        y+=1


 





       
        

        
   
    
        



        
    #if y3 == 50:
        #screen.blit(image1,(x2,200))
        
    #if y3 == 20:
        #y = 1000
        #y3=1000
    

        

    



    clock.tick(80)
    



    

    #if y == 410:
       


        
        






    
    pygame.display.flip()
    
