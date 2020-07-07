import pygame
from ML.RecognizeDigits3x5grid.RecognizeDigits import Model


class Field:
    def __init__(self, width, height, left=100, top=100, cell_size=100):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]

        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        font = pygame.font.Font(None, 50)
        text = font.render("It can be: " + str(prediction), True, pygame.Color("white"))
        text_rect = text.get_rect()
        text_rect.center = (self.left + self.cell_size * self.width + self.cell_size * 1.1 + text_rect.height // 2,
                            self.top + text_rect.height // 2)
        screen.blit(text, text_rect)
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.rect(screen,
                                     pygame.Color("red"),
                                     (x * self.cell_size + self.left,
                                      y * self.cell_size + self.top,
                                      self.cell_size,
                                      self.cell_size))
                else:
                    pygame.draw.rect(screen,
                                     pygame.Color("white"),
                                     (x * self.cell_size + self.left,
                                      y * self.cell_size + self.top,
                                      self.cell_size,
                                      self.cell_size),
                                     1)

    def get_cell(self, mouse_pos):
        if (mouse_pos[0] < self.left or
                mouse_pos[0] > self.left + self.width * self.cell_size or
                mouse_pos[1] < self.top or
                mouse_pos[1] > self.top + self.height * self.cell_size):
            return None

        else:
            return (mouse_pos[0] - self.left) // self.cell_size, \
                   (mouse_pos[1] - self.top) // self.cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell_coords):
        self.board[cell_coords[1]][cell_coords[0]] = 1 - self.board[cell_coords[1]][cell_coords[0]]


pygame.init()
height = 1000
width = 1000
size = width, height
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
fps = 120
running = True
field = Field(3, 5)
model = Model()
prediction = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                field.get_click(event.pos)
                input_data = []
                for row in field.board:
                    input_data += row
                prediction = model.make_prediction(input_data)

    screen.fill((0, 0, 0))
    field.render()
    pygame.display.flip()
    clock.tick(fps)
