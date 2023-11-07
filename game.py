from pygame import *

ball_y = 7
ball_x = 7
clock = time.Clock()
win_height = 1000 # Высотва
win_width = 1200 # Ширина
racket_png = 'racket.png'
ball_png = 'tenis_ball.png'
GAME = True
NO = False

class Sprite_1(sprite.Sprite):
    """ Класс-родитель для других спрайтов. """
    def __init__(self, player_image, player_x, player_y,
                 size_x, size_y, player_speed):
        # вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image),
                                     (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник,
        # в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, отрисовывающий героя на окне

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Racket(Sprite_1):
    """ Класс Главного героя. """
    # метод для управления спрайтом кнопками клавиатуры
    def right_racket(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def left_racket(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 LOSE!', True, (0, 255, 0))
lose2 = font1.render('Player 2 LOSE!', True, (0, 255, 0))

# создаем окошко    
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
background = (255, 0, 0)
window.fill(background)

ball = Sprite_1(ball_png, 600, 500, 70, 70, 35)
racket1 = Racket(racket_png, 30, 200, 10, 100, 40)
racket2 = Racket(racket_png, 1170, 200, 10, 100, 40)

while GAME:
        # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            GAME = False
    
    if not NO:
        window.fill(background)

        racket1.left_racket()
        racket2.right_racket()

        ball.rect.x += ball_x
        ball.rect.y += ball_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_x *= -1
            ball_y *= 1
        
        if ball.rect.y > win_height -75 or ball.rect.y < 0:
            ball_y *= -1
        
        if ball.rect.x < 0:
            NO = True
            window.blit(lose1, (600, 500))

        if ball.rect.x > 1200:
            NO = True
            window.blit(lose2, (600, 500))
            

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(30)
