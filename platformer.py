import platformer_lvl1, platformer_lvl2, platformer_lvl3, platformer_lvl4, platformer_lvl5, platformer_lvl6, pygame
timeTaken = platformer_lvl1.levelOne()
timeTaken = platformer_lvl2.levelTwo(timeTaken)
levelPassed = False
while not levelPassed:
    timeTaken, levelPassed = platformer_lvl3.levelThree(timeTaken)
levelPassed = False
while not levelPassed:
    timeTaken, levelPassed = platformer_lvl4.levelFour(timeTaken)
levelPassed = False
while not levelPassed:
    timeTaken, levelPassed = platformer_lvl5.levelFive(timeTaken)
levelPassed = False
while not levelPassed:
    timeTaken, levelPassed = platformer_lvl6.levelSix(timeTaken)
pygame.quit()
