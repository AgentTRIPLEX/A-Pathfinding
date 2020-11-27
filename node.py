import pygame

import settings
import astar

# 0 --> NORMAL
# 1 --> CLOSED
# 2 --> OPENED
# 3 --> BARRIER
# 4 --> START
# 5 --> END
# 6 --> PATH

class Node(astar.Node):
    def __init__(self, row, col, grid):
        super().__init__(row, col)
        self.grid = grid

    def get_rect(self):
        return self.grid[self.row][self.col]

    def get_color(self):
        return settings.colors[self.mode]

    def draw(self, win):
        pygame.draw.rect(win, self.get_color(), self.get_rect())