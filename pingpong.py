from pygame import *
font.init()
window = display.set_mode((700, 500))
display.set_caption("Пинг Понг")
background = transform.scale(image.load('background.jpg'), (700, 500))
clock = time.Clock()
run = True
finish = False


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_width, player_height, player_x, player_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_firstplayer(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    
    def update_secondplayer(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

player1 = Player(player_image='rocketcka.png', player_speed=4, player_width=50, player_height=150, player_x=50, player_y=200)
player2 = Player(player_image='rocketcka.png', player_speed=4, player_width=50, player_height=150, player_x=600, player_y=200)
ball = GameSprite(player_image='ball.jpg', player_speed=4, player_width=50, player_height=50, player_x=325, player_y=125)

speed_x = 3
speed_y = 3

win_font = font.Font(None, 40)
win1 = win_font.render('PLAYER 1 WIN!', True, (255, 195, 122))
win2 = win_font.render('PLAYER 2 WIN!', True, (195, 255, 122))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    if finish != True:
        window.blit(background, (0, 0))
        player1.reset()
        player2.reset()
        player1.update_firstplayer()
        player2.update_secondplayer()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1


        if ball.rect.x < 0:
            window.blit(win2, (250, 200))
            finish = True    
        elif ball.rect.x > 650:
            window.blit(win1, (250, 200))
            finish = True
        
  
    display.update()
    clock.tick(60)