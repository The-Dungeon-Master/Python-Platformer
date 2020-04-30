def levelOne():
    import pygame, sys, time
    yes = ['Y', 'y', 'yes', 'Yes', 'Sure', 'sure', 'Yeah', 'yeah']
    existing = input('Have you played the game before?')
    if existing in yes:
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
    else:
        file = open('Resolution.txt', 'w')
        x = int(input('How many pixels does your display have on the X axis?'))
        y = int(input('How many pixels does your display have on the Y axis?'))
        file.write(str(x) + ',')
        file.write(str(y))
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
    magenta = 255, 0, 255
    GotIt = ''
    while GotIt not in yes:
        print('To play this game, use left and right to move and down to jump.')
        print('Q anc ESC exit, and click to pass ready screen')
        print('The goal is to get to the green platform')
        print('You restart the level if you touch a red enemy')
        GotIt = input('Got it?')
        print('Level 1')
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.font.init()
    import Ready_screen
    Ready_screen.ready(1, screen)
    fontForGame = pygame.font.SysFont('Courier New Bold.ttf', 24)
    counter = time.time()
    class Platform():
        def __init__(self, x, y, size, color):
            self.color = color
            self.rect = pygame.Rect(x, y, size[0]/25, size[1]/100)
        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)
    platforms = []
    platforms.append(Platform(size[0]/4, size[1]/8, size, yellow))
    platforms.append(Platform(size[0]/5, size[1]/7, size, yellow))
    platforms.append(Platform(size[0]/7, size[1]/6, size, yellow))
    platforms.append(Platform(size[0]/6, size[1]/5, size, yellow))
    platforms.append(Platform(size[0]/5 * 2, size[1]/4, size, yellow))
    platforms.append(Platform(size[0]/3, size[1]/3, size, yellow))
    platforms.append(Platform(size[0]/6, size[1]/3 * 2, size, yellow))
    platforms.append(Platform(size[0]/4, size[1]/8 * 5, size, yellow))
    platforms.append(Platform(size[0]/5, size[1]/7 * 4, size, yellow))
    platforms.append(Platform(size[0]/7, size[1]/6 * 2, size, yellow))
    platforms.append(Platform(size[0]/6, size[1]/5 *4, size, yellow))
    platforms.append(Platform(size[0]/5 * 2, size[1]/4 * 3, size, yellow))
    platforms.append(Platform(size[0]/3, size[1]/6 * 3, size, yellow))
    platforms.append(Platform(size[0]/6, size[1]/3 * 2, size, yellow))
    platforms.append(Platform(size[0]/4, size[1]/8 * 7, size, yellow))
    platforms.append(Platform(size[0]/5, size[1]/7 * 3, size, yellow))
    platforms.append(Platform(size[0]/7, size[1]/6 * 4, size, yellow))
    platforms.append(Platform(size[0]/6, size[1]/5 * 3, size, yellow))
    platforms.append(Platform(size[0]/5 * 2, size[1]/6 * 5, size, yellow))
    platforms.append(Platform(size[0]/3, size[1]/5 * 4, size, yellow))
    platforms.append(Platform(size[0]/6, size[1]/3 * 2, size, yellow))
    platforms.append(Platform(size[0]/4, size[1]/4, size, yellow))
    platforms.append(Platform(size[0]/5, size[1]/5, size, yellow))
    platforms.append(Platform(size[0]/7, size[1]/4, size, yellow))
    platforms.append(Platform(size[0]/6, size[1]/9*2, size, yellow))
    platforms.append(Platform(size[0]/5 * 2, size[1]/5, size, yellow))
    platforms.append(Platform(size[0]/3, size[1]/4, size, yellow))
    platforms.append(Platform(size[0]/6, size[1]/7 * 2, size, yellow))
    platforms.append(Platform(size[0]/5, size[1]/8 * 7, size, green))
    playerx = 0
    playery = 0
    while True:
        player = pygame.Rect(playerx, playery, size[0]/100, size[0]/100)
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
            down -= 1
            playery += down
        else:
            playery = 0
            down = 0
            canJump = True
        pygame.draw.rect(screen, magenta, player)
        screen.blit(text, (0, 0))
        pygame.display.flip()
