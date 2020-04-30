import platformer_lvl1, platformer_lvl2, platformer_lvl3, pygame
timeTaken = platformer_lvl1.levelOne()
timeTaken = platformer_lvl2.levelTwo(timeTaken)
levelPassed = False
while not levelPassed:
    timeTaken, levelPassed = platformer_lvl3.levelThree(timeTaken)
pygame.quit()
