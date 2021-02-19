class LedTable:
    def __init__(self, columns = 0, rows = 0):
        self.columns = columns
        self.rows = rows
        self.table = [[False for x in range(columns)] for y in range (rows)]

    def set_pixel(self, x ,y, value):
        self.table[x][y] = False
        pass

    def set_pixels(self, pixel_table):
        if pixel_table.count !=  self.rows or pixel_table[0].count != self.columns:
            raise IndexError
        pass

test = LedTable(10, 5)
print(test.table)