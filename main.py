import pygame

WINDOW_SIZE = (450, 450)
pygame.init()


class Cell:
    cell_size = (int(WINDOW_SIZE[0] / 9), int(WINDOW_SIZE[1] / 9))

    row = 0
    col = 0
    num = 0
    highlighted = False
    colour = (128, 128, 128)

    PADDING = 1

    def __init__(self, row, col, num):
        self.row = row
        self.col = col
        self.num = num
        self.font = pygame.font.SysFont(None, 40)
        self.img = self.font.render(str(num), True, (0, 0, 0))

    def render(self, surface):
        font_colour = (0, 0, 0)
        if self.highlighted:
            font_colour = (128, 128, 128)

        pygame.draw.rect(surface, self.colour, (self.col * self.cell_size[0],
                                                self.row * self.cell_size[1],
                                                self.cell_size[0],
                                                self.cell_size[1]))

        pygame.draw.rect(surface, (255, 255, 255), (self.col * self.cell_size[0] + self.PADDING,
                                                    self.row * self.cell_size[1] + self.PADDING,
                                                    self.cell_size[0] - self.PADDING * 2,
                                                    self.cell_size[1] - self.PADDING * 2))

        if self.num != 0:
            surface.blit(self.font.render(str(self.num), True, font_colour),
                         ((self.col * self.cell_size[0]) + self.img.get_width() + 2,
                          (self.row * self.cell_size[1]) + int(self.img.get_height() / 2)))


def board_to_string():
    s = ""
    for i, row in enumerate(board):
        if (i % 3 == 0):
            s += "-------------------------\n"
        for j, col in enumerate(row):
            if (j % 3 == 0):
                s += "| "
            s += str(col.num) + " "
        s += "|\n"
    print(s + "-------------------------")


def render_cells():
    for row in board:
        for col in row:
            col.render(window)


def render_lines():
    for i in range(1, 3):
        pygame.draw.line(window, (0, 0, 0), (i * int(WINDOW_SIZE[0] / 3), 0),
                         (i * int(WINDOW_SIZE[0] / 3), WINDOW_SIZE[0]), width=3)

    for i in range(1, 3):
        pygame.draw.line(window, (0, 0, 0), (0, i * int(WINDOW_SIZE[1] / 3)),
                         (WINDOW_SIZE[1], i * int(WINDOW_SIZE[1] / 3)), width=3)


def is_valid_choice(rowNum, colNum, num):
    for i in range(9):
        if board[rowNum][i].num == num or board[i][colNum].num == num:
            return False

    x0 = int(colNum / 3) * 3
    y0 = int(rowNum / 3) * 3

    for y in range(3):
        for x in range(3):
            if board[y0 + y][x0 + x].num == num:
                return False
    return True


def solve():
    for row in range(9):
        for col in range(9):
            if board[row][col].num == 0:
                for i in range(1, 10):
                    if is_valid_choice(row, col, i):
                        cell = Cell(row, col, i)
                        cell.highlighted = True
                        board[row][col] = cell

                        if solve():
                            return True
                        board[row][col] = Cell(row, col, 0)
                return False
    return True


board = []

try:
    with open(input("Enter the name of the input file: ")) as file:
        row = 0
        col = 0
        for line in file.read().split("\n"):
            rowList = []
            col = 0
            for num in line:
                rowList.append(Cell(row, col, int(num)))
                col += 1
            row += 1
            board.append(rowList)
except FileNotFoundError:
    print("Input file not found!")


window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Solver")

time_step = 5
clock = pygame.time.Clock()
running = True
solved = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not solved:
        solve()
        solved = True
        board_to_string()

    render_cells()
    render_lines()

    pygame.display.flip()
    clock.tick(time_step)
