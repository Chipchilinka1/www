import pygame,sys, os
pygame.init()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image
pygame.key.set_repeat(70, 10)
clock = pygame.time.Clock()
fps = 50
size = 1200, 800
screen = pygame.display.set_mode(size)

def terminate():
    pygame.quit()
    sys.exit()
    
def startScreen():
    introText = ["Graviti Rush",
                 'Управление: любая кнопка мыши.',
                 "",
                 '',
                 'Пусть будет счастлив всяк в это игращий',
                 'Пусть будет вечен всяк это пройдящий',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 "Нажмите любую кнопку для начала."]
    image = load_image('Zastavka.jpg')
    image1 = pygame.transform.scale(image, (1200, 800))
    screen.blit(image1, (0, 0))
    font = pygame.font.Font(None, 50)
    textCoord = 50
    for line in introText:
        stringRendered = font.render(line, 1, pygame.Color('Yellow'))
        introRect = stringRendered.get_rect()
        textCoord += 10
        introRect.top = textCoord
        introRect.x = 10
        textCoord += introRect.height
        screen.blit(stringRendered, introRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)
def terminate():
    pygame.quit()
    sys.exit();
fon = load_image('fon1.png')
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
pol_group = pygame.sprite.Group()
polkill_group = pygame.sprite.Group()
susestvo_group = pygame.sprite.Group()
lvlnext =  pygame.sprite.Group()

def LostScreen():


    introText = ["Game Over",
                 '',
                 "",
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 "Нажмите любую кнопку для повтора."]

    image = load_image('Zastavka.jpg')
    image1 = pygame.transform.scale(image,(1200,800))
    screen.blit(image1,(0,0))
    font = pygame.font.Font(None, 50)
    textCoord = 50
    for line in introText:
        stringRendered = font.render(line, 1, pygame.Color('Yellow'))
        introRect = stringRendered.get_rect()
        textCoord += 10
        introRect.top = textCoord
        introRect.x = 10
        textCoord += introRect.height
        screen.blit(stringRendered, introRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)
        
def EndScreen():


    introText = ["Вы прошли игру",
                 'Спасибо за прохождение!',
                 "",
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 ""]

    image = load_image('Zastavka.jpg')
    image1 = pygame.transform.scale(image,(1200,800))
    screen.blit(image1,(0,0))
    font = pygame.font.Font(None, 50)
    textCoord = 50
    for line in introText:
        stringRendered = font.render(line, 1, pygame.Color('Yellow'))
        introRect = stringRendered.get_rect()
        textCoord += 10
        introRect.top = textCoord
        introRect.x = 10
        textCoord += introRect.height
        screen.blit(stringRendered, introRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)
        
def NextScreen():


    introText = ["Вы прошли уровень",
                 '',
                 "",
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 '',
                 "Нажмите любую кнопку для продолжения."]

    image = load_image('Zastavka.jpg')
    image1 = pygame.transform.scale(image,(1200,800))
    screen.blit(image1,(0,0))
    font = pygame.font.Font(None, 50)
    textCoord = 50
    for line in introText:
        stringRendered = font.render(line, 1, pygame.Color('Yellow'))
        introRect = stringRendered.get_rect()
        textCoord += 10
        introRect.top = textCoord
        introRect.x = 10
        textCoord += introRect.height
        screen.blit(stringRendered, introRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return 
        pygame.display.flip()
        clock.tick(fps)
        
class Susestvo(pygame.sprite.Sprite):
    image = load_image("fire.png")
    
    def __init__(self):
        super().__init__(all_sprites)
        self.image = Susestvo.image
        self.add(susestvo_group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 940
        self.rect.y = 300
        self.speed = 2

    def dvig(self):
        if self.rect.y < 35 or self.rect.y > 450:
            self.speed = - self.speed
        self.rect.y += self.speed
        self.rect.x += 5

    def attac(self):
        meteor = Meteor(self.rect.x - 100,self.rect.y + 30 )

class Meteor(pygame.sprite.Sprite):
    image = load_image("meteor.png")

    def __init__(self,x,y):
        super().__init__(all_sprites)
        self.image = Meteor.image
        self.add(polkill_group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image) 
        
class Camera:

    def __init__(self):
        self.dx = 100
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        
class Player(pygame.sprite.Sprite):
    image = load_image('hero.png')
    
    def __init__(self):
        super().__init__(all_sprites)
        self.image = Player.image
        self.add(player_group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 600
        self.rect.y = 600
        self.speed = 7

    def update(self):
        if pygame.sprite.spritecollideany(self, polkill_group):
            LostScreen()
            StartGame(lvl)
        elif pygame.sprite.spritecollideany(self, lvlnext):
            if lvl == 3:
                EndScreen()
            NextScreen()
            StartGame(lvl+1)              
        elif not pygame.sprite.spritecollideany(self, pol_group):
            self.rect = self.rect.move(5, self.speed)          
        else:
            self.rect = self.rect.move(5, 0)
            
def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    maxWidth = max(map(len, level_map))
    return list(map(lambda x: x.ljust(maxWidth, '0'), level_map))

class Pol(pygame.sprite.Sprite):
    image = load_image("pol10.png")

    def __init__(self, hl, wl):
        super().__init__(all_sprites)
        self.image = Pol.image
        self.add(pol_group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = hl*50+50
        self.rect.right = wl*50+50
        
class Prep(pygame.sprite.Sprite):
    image = load_image("pika.png")

    def __init__(self, hl, wl):
        super().__init__(all_sprites)
        self.image = Prep.image
        self.add(polkill_group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = hl*50+50
        self.rect.right = wl*50+50
        
class Prep2(pygame.sprite.Sprite):
    image = load_image("pika2.png")

    def __init__(self, hl, wl):
        super().__init__(all_sprites)
        self.image = Prep2.image
        self.add(polkill_group)
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = hl*50+50
        self.rect.right = wl*50+50
        
class Prep3(pygame.sprite.Sprite):
    image = load_image("pika3.png")

    def __init__(self, hl, wl):
        super().__init__(all_sprites)
        self.image = Prep3.image
        self.add(polkill_group)
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = hl*50+50
        self.rect.right = wl*50+50 
        
class Prep4(pygame.sprite.Sprite):
    image = load_image("pika4.png")

    def __init__(self, hl, wl):
        super().__init__(all_sprites)
        self.image = Prep4.image
        self.add(polkill_group)
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = hl*50+50
        self.rect.right = wl*50+50 
        
class Finish(pygame.sprite.Sprite):
    image = load_image("finish.png")

    def __init__(self, hl, wl):
        super().__init__(all_sprites)
        self.image = Finish.image
        self.add(lvlnext)
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = hl*50+50
        self.rect.right = wl*50+50

def StartGame(lvl):
    width = 1200
    height = 800
    fon = pygame.transform.scale(fon, (1200, 800))
    size = width, height
    screen = pygame.display.set_mode(size)
    running = True
    level = load_level('level0'+str(lvl)+'.txt')
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Pol(y,x)
            if level[y][x] == '#':
                Prep(y,x)
            if level[y][x] == '@':
                Prep2(y,x)  
            if level[y][x] == '-':
                Prep3(y,x)    
            if level[y][x] == '+':
                Prep4(y,x)                  
            if level[y][x] == '1':
                Finish(y,x)
    player = Player()
    camera = Camera()
    clock = pygame.time.Clock()
    if lvl == 3:
        susestv = Susestvo()
    time1 = pygame.time.get_ticks() 
    pygame.mixer.music.load(str(lvl)+'.mp3')
    pygame.mixer.music.play()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.sprite.spritecollideany(player, polkill_group):
                StartGame(lvl)
            elif pygame.sprite.spritecollideany(player, pol_group):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player.speed < 0:
                        player.rect.y = player.rect.y + 7
                    else:
                        player.rect.y = player.rect.y - 7
                    player.speed = - player.speed
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        player_group.update()    
        if lvl == 3:
            susestv.dvig()
            time2 = pygame.time.get_ticks()
            if time2 - time1 >= 1000:
                susestv.image = load_image("fire.png")
            if time2 - time1 >= 2000:
                susestv.image = load_image("fire2.png")
            if time2 - time1 >= 3000:
                susestv.attac()
                susestv.image = load_image("fire3.png")
                time1 = pygame.time.get_ticks()            
        pygame.display.flip()
    pygame.quit()
startScreen()
StartGame(1)