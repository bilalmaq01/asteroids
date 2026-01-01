import pygame
<<<<<<< HEAD
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    infiniteloop = 0
    while(infiniteloop==0):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()






=======
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
>>>>>>> 8c1c53e496038cc80e93bd16279b0cb958ac5194


if __name__ == "__main__":
    main()
