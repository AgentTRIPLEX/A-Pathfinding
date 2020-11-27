class Grid(object):
    def __init__(self, cols, rows, width, height):
        self.grid = [] # (x, y, w, h)
        self.width = cols * width
        self.height = rows * height
        x = 0
        y = 0

        for r in range(rows):
            y = r * height
            self.grid.append([])

            for c in range(cols):
                x = c * width
                rect = (x, y, width, height)
                self.grid[r].append(rect)