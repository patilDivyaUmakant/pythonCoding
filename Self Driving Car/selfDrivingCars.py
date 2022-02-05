import pygame
pygame.init()
window = pygame.display.set_mode((1200,400))
pygame.display.set_caption("Tesla Race")
track = pygame.image.load("track6.png")
car = pygame.image.load("tesla.png")
car = pygame.transform.scale(car,(30,80))
car_x = 155
car_y = 300
camx_offset = 0
camy_offset = 0  
focal_distance = 25
direction = "up"  
drive = True
clock = pygame.time.Clock()
while drive : 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            drive = False
    camx = car_x + 15 + camx_offset
    camy = car_y + 15 + camy_offset
    right_px = window.get_at((camx + focal_distance ,camy))[0]
    up_px = window.get_at((camx,camy - focal_distance))[0]
    down_px = window.get_at((camx,camy + focal_distance))[0]
    print(up_px,right_px,down_px)
    clock.tick(60)
    if right_px == 255 and direction == "up" and up_px != 255: 
        direction = "right"
        camx_offset = 40 
        car = pygame.transform.rotate(car,-90)

    if direction == "right" and right_px != 255 and down_px == 255 :
        direction = "down"
        car_x += 40
        camy_offset = 40
        camx_offset = 0
    
        car = pygame.transform.rotate(car,-90)  

    if direction == "down" and down_px != 255 and right_px == 255 : 
        direction = "right"
        car_y += 40
        camx_offset = 40
        camy_offset = 0
        car = pygame.transform.rotate(car,90)

    if direction == "right" and up_px == 255 and right_px != 255 : 
        direction = "up"
        car_x += 40
        camx_offset = 0
        # camy_offset = 40
        car = pygame.transform.rotate(car,90)

    if up_px == 255 and direction == "up" : 
        car_y -= 1 

    if right_px == 255 and direction == "right" :
        car_x += 1

    if down_px == 255 and direction == "down" :
        car_y += 1  
   
    window.blit(track,(0,0))
    window.blit(car,(car_x,car_y))
    pygame.draw.circle(window,(0,10,100),(camx,camy),5,5)
    pygame.display.update()