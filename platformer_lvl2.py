def levelTwo(timeTaken):
    import pygame, sys, time
    pygame.mixer.music.stop()
    yes = ['Y', 'y', 'yes', 'Yes', 'Sure', 'sure', 'Yeah', 'yeah']
    file = open('Resolution.txt', 'r')
    tempText = ''
    readText = file.read()
    for character in readText:
        if character != ',':
            tempText += character
        else:
            x = int(tempText)
            tempText = ''
    y = int(tempText)
    file.close()
    size = length, width = x, y
    left = False
    right = False
    down = 0
    canJump = True
    blue = 0, 0, 255
    red = 255, 0, 0
    yellow = 255, 255, 0
    green = 0, 255, 0
    black = 0, 0, 0
    magenta = 255, 0, 255
    print('Level 2')
    pygame.display.init()
    import Ready_screen
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)    
    Ready_screen.ready(2, screen, 'No special messages')
    pygame.font.init()
    fontForGame = pygame.font.Font('Courier New.ttf', 24)
    counter = time.time() - timeTaken
    def pause():
        timer = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print('You have quit the game')
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        pygame.quit()
                        print('You have quit the game')
                        sys.exit(0)
                    if event.key == pygame.K_r:
                        return (time.time() - timer)
    class Platform():
        def __init__(self, x, y, size, color):
            self.color = color
            self.rect = pygame.Rect(x, y, size[0]/25, size[1]/100)
        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)
    platforms = []
    platforms.append(Platform(size[0]/4, size[1]/2, size, yellow))
    platforms.append(Platform(size[0]/3, size[1]/7, size, yellow))
    platforms.append(Platform(size[0]/5, size[1]/5, size, yellow))
    platforms.append(Platform(size[0]/7, size[1]/4, size, yellow))
    platforms.append(Platform(size[0]/4, size[1]/5 * 3, size, yellow))
    platforms.append(Platform(size[0]/8, size[1]/3, size, yellow))
    platforms.append(Platform(size[0]/5, size[1]/3 * 2, size, yellow))
    platforms.append(Platform(size[0]/3, size[1]/8 * 5, size, yellow))
    platforms.append(Platform(size[0]/6, size[1]/7 * 4, size, yellow))
    platforms.append(Platform(size[0]/7, size[1]/5 * 2, size, yellow))
    platforms.append(Platform(size[0]/3, size[1]/5 * 4, size, yellow))
    platforms.append(Platform(size[0]/4 * 2, size[1]/4 * 3, size, yellow))
    platforms.append(Platform(size[0]/2, size[1]/8 * 7, size, green))
    playerx = 0
    playery = 0
    pygame.mixer.music.load('BGM#2.wav')
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    while True:
        text = fontForGame.render(str(int(time.time() - counter)), False, red)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print('You have quit the game')
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    print('You have quit the game')
                    sys.exit(0)
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_DOWN and canJump:
                    down = size[1]/50
                    canJump = False
                if event.key == pygame.K_p:
                    counter += pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
        if left and playerx > 0:
            playerx -= 5
        if right and playerx < size[0]:
            playerx += 5
        screen.fill(blue)
        for platform in platforms:
            platform.draw()
            if down < 0:
                if platform.rect.x < playerx + size[0]/100:
                    if platform.rect.x + size[0] / 25 > playerx:
                        if platform.rect.y < playery + size[0]/100:
                            if platform.rect.y  + size[1]/100 > playery:
                                variable = size[1] / 100
                                playery = platform.rect.y + variable + 2
                                canJump = True
                                down = 0
                                if platform.color == green:
                                    print('You finished in ' + str(time.time()-counter) + ' seconds!')
                                    return float(time.time() - counter)
        if playery >= 0:
            down -= size[1]/768
            playery += down
        else:
            playery = 0
            down = 0
            canJump = True
        player = pygame.Rect(playerx, playery, size[0]/100, size[0]/100)
        eye1 = pygame.Rect(playerx + size[0]/500, playery + size[0]/500, 2, 2)
        eye2 = pygame.Rect(playerx + size[0]/150, playery + size[0]/500, 2, 2)
        pygame.draw.rect(screen, magenta, player)
        pygame.draw.rect(screen, black, eye1)
        pygame.draw.rect(screen, black, eye2)
        pygame.draw.polygon(screen, black, ((playerx + size[0]/200, playery + size[0]/350), (playerx + size[0]/200 + 2, playery + size[0]/250), (playerx + size[0]/200 - 2, playery + size[0]/250)))
        pygame.draw.line(screen, black, (playerx + size[0]/500, playery + size[0]/165), (playerx + size[0]/150 + 1, playery + size[0]/165))
        screen.blit(text, (0, 0))
        pygame.display.flip()
        clock.tick(60)
