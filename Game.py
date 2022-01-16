import pygame
from Field import Field


class Game:
    def __init__(self, width=1024, height=720, cell_size=8, speed=1):
        if width % cell_size != 0 or height % cell_size != 0:
            raise RuntimeError('Can not fill evenly cells on screen')

        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.cell_num_width = self.width // self.cell_size
        self.cell_num_height = self.height // self.cell_size
        self.field = Field(self.cell_num_width, self.cell_num_height, self.cell_size)

        self.speed = speed

    def draw_grid(self):
        BLACK = (0, 0, 0)
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, BLACK, (0, y), (self.width, y))

    def draw_field(self):
        GREEN = (0, 255, 0)
        # self.field.print_field()
        for row in self.field.field:
            for cell in row:
                if cell:
                    pygame.draw.rect(self.screen, GREEN, cell.rect)

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        WHITE = (255, 255, 255)

        run = True
        stop = False
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        stop = not stop
            if not stop:
                self.screen.fill(WHITE)
                self.draw_field()
                self.draw_grid()
                self.field.update_field()
                pygame.display.flip()
                clock.tick(self.speed)

        pygame.quit()
