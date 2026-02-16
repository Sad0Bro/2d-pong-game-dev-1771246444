import pygame
import sys

class PongGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.title = "2D Pong Game"
        pygame.display.set_caption(self.title)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

if __name__ == "__main__":
    game = PongGame()
    game.run()