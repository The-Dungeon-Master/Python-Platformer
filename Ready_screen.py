def ready(lvl, screen, message):
    import pygame, sys
    screen.fill((0, 0, 255))
    pygame.font.init()
    fontToUse = pygame.font.Font('Courier New.ttf', 48)
    fontToUse2 = pygame.font.Font('Courier New.ttf', 24)
    text = fontToUse.render('Ready?', False, (0, 255, 0))
    text2 = fontToUse.render('Level ' + str(lvl), False, (0, 255, 0))
    text3 = fontToUse2.render(message, False, (0, 0, 0))
    screen.blit(text, (screen.get_size()[0] / 6, screen.get_size()[1] / 6))
    screen.blit(text2, (screen.get_size()[0] / 6, screen.get_size()[1] / 6 + 96))
    for i in range(0, screen.get_size()[0], 4):
        pygame.draw.line(screen, (255, 255, 0), (i, 0), (i, screen.get_size()[1]))
    for i in range(0, screen.get_size()[1], 4):
        pygame.draw.line(screen, (255, 255, 0), (0, i), (screen.get_size()[0], i))
    screen.blit(text3, (screen.get_size()[0] / 6, screen.get_size()[1] / 6 + 192))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        mp = pygame.mouse.get_pressed()
        if mp[0]:
            return
        pygame.display.flip()
