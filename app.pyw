import pygame
import threading

import messagebox
import settings
from grid import Grid
from node import Node
import astar

pygame.init()

class App:
    def __init__(self):
        self.grid = Grid(settings.cols, settings.rows, settings.cell_width, settings.cell_height)

        self.WIDTH = self.grid.width
        self.HEIGHT = self.grid.height

        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("A* Pathfinding")

        self.clock = pygame.time.Clock()
        self.FPS = 20

        self.reset_grid()

    def mainloop(self):
        self.run = True

        while self.run:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            keys = pygame.key.get_pressed()
            buttons = pygame.mouse.get_pressed()

            if buttons[0]:
                astar.reset_algorithm(self.nodes)

                row, col = self.get_node(pygame.mouse.get_pos())
                node = self.nodes[row][col]

                if not self.start_node or not self.end_node:
                    if self.start_node:
                        self.start_node.reset()

                    node.make_start()
                    self.start_node = node

                elif node not in [self.start_node, self.end_node]:
                    astar.reset_algorithm(self.nodes)
                    node.make_barrier()

            if buttons[2]:
                astar.reset_algorithm(self.nodes)

                row, col = self.get_node(pygame.mouse.get_pos())
                node = self.nodes[row][col]

                if self.start_node and not self.end_node and node.is_normal():
                    node.make_end()
                    self.end_node = node

                elif node.is_barrier():
                    node.reset()

            if keys[pygame.K_SPACE]:
                self.reset_grid()

            if keys[pygame.K_RETURN] and self.start_node and self.end_node:
                astar.reset_algorithm(self.nodes)

                if settings.visual == 0:
                    astar.algorithm(self.start_node, self.end_node, self.nodes, self.draw)
                else:
                    astar.algorithm(self.start_node, self.end_node, self.nodes)

                    if settings.visual == 2:
                        astar.reset_algorithm(self.nodes, path=False)

            if keys[pygame.K_1]:
                settings.visual = 0

            if keys[pygame.K_2]:
                settings.visual = 1

            if keys[pygame.K_3]:
                settings.visual = 2

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.fill(settings.bg_color)

        for row in self.nodes:
            for node in row:
                node.draw(self.win)

        if settings.cell_outline > 0:
            self.draw_grid()

        pygame.display.update()

    def draw_grid(self):
        for row in self.grid.grid:
            for rect in row:
                pygame.draw.rect(self.win, settings.cell_outline_color, rect, settings.cell_outline)

    def reset_grid(self):
        self.start_node = None
        self.end_node = None

        self.nodes = []
        for row, cols in enumerate(self.grid.grid):
            self.nodes.append([])
            for col, rect in enumerate(cols):
                n = Node(row, col, self.grid.grid)
                self.nodes[row].append(n)

    def get_node(self, m_pos):
        m_x, m_y = m_pos
        row = m_y // settings.cell_height
        col = m_x // settings.cell_width
        return row, col

if __name__ == "__main__":
    a = App()
    a.mainloop()
