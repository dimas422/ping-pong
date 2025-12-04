import pygame
pygame.init()


pygame.display.set_mode((900,600))
pygame.display.set_caption("Ping pong")
icon = pygame.image.load('pingp.jpeg')
pygame.display.set_icon(icon)


player1=pygame.Rect(20,250,10,100)
player2=pygame.Rect(870,250,10,100)

ball = pygame.Rect(445,295,10,10)
ball_speed_x = 5
ball_speed_y = 5


score1 = 0
score2 = 0
font = pygame.font.Font(None,400)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player1.y -= 6
    if keys[pygame.K_s]:
        player1.y += 6

    if keys[pygame.K_UP]:
        player2.y -= 6
    if keys[pygame.K_DOWN]:
        player2.y += 6


    if player1.top < 0:
        player1.top = 0
    if player1.bottom > 600:
        player1.bottom = 600

    if player2.top < 0:
        player2.top = 0
    if player2.bottom > 600:
        player2.bottom = 600

        