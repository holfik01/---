from pygame import *
mixer.init()
window = display.set_mode((700, 500))
display.set_caption("пинг понг")
ping = transform.scale(image.load("1642879824_1-abrakadabra-fun-p-tennisnii-stol-vid-sverkhu-2.jpg"), (700, 500))
window.blit(ping,(0, 0))  
class GameSprite(sprite.Sprite):
    def __init__(self, pimage, speed, x, y,w=110, h=150):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
class Raketka(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 60:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 60:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

igrok = Raketka('red.png', 3, 0, 100, 100, 100)
igrok_2 = Raketka('blue.png', 3, 590, 100, 100, 100)
mach = GameSprite('mach.png', 3, 320, 230, 50, 40)
clock = time.Clock() 
FPS = 60
run = True
mixer.music.load('music.ogg')
mixer.music.play()
while run == True: 
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(ping,(0, 0))  



    igrok.update_l()        
    igrok.reset()
    igrok_2.update_r()        
    igrok_2.reset()
    mach.update()
    mach.reset()
    clock.tick(FPS)
    display.update()