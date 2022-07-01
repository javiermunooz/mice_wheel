from time import sleep
from random import randint

from PyQt5.QtGui import QCursor

from exceptions import CursorOutOfBoundsException

class QCursorController():
    def __init__(self, left_corner, right_corner) -> None:
        """Constructor. 

        :param left_corner: Coordinates of the upper left corner. (x1, y1)
        :type left_corner: tuple
        :param right_corner: Coordinates of the lower right corner. (x2, y2)
        :type right_corner: tuple
        """        
        self.cursor = QCursor()
        self.n_moves = 0
        self.min_x, self.min_y = left_corner
        self.max_x, self.max_y = right_corner

    def __rstPos(self):
        """Resets the move counter.
        """        
        self.n_moves = 0

    def __getPos(self):
        """Gets the current position of the cursor.

        :return: Position of the cursor.
        :rtype: PySide2.QtCore.QPoint
        """        
        return self.cursor.pos()

    def __setPos(self, x, y):
        """Moves the cursor to a new position.

        :param x: New x coordinate.
        :type x: int
        :param y: New y coordinate.
        :type y: int
        :raises CursorOutOfBoundsException: In case the cursor was moved to a position that does not exist.
        """        
        if x > self.max_x or y > self.max_y:
            raise CursorOutOfBoundsException(f"Cursor was moved to ({x},{y}) but screen size is ({self.max_x},{self.max_y})")
        self.cursor.setPos(x, y)
        self.n_moves += 1

    def __setRandomPos(self, min_x, min_y, max_x, max_y):
        """Moves the cursor to a new random position.

        :param min_x: Minimum x value.
        :type min_x: int
        :param min_y: Minimum y value.
        :type min_y: int
        :param max_x: Maximum x value.
        :type max_x: int
        :param max_y: Maximum y value.
        :type max_y: int
        """        
        x = randint(min_x, max_x)
        y = randint(min_y, max_y)
        self.__setPos(x, y)

    def __offset(self, x_offset, y_offset):
        """Moves the cursos by a pre-defined offset.

        :param x_offset: x-axis offset.
        :type x_offset: int
        :param y_offset: y-axis offset.
        :type y_offset: int
        """        
        x, y = self.__getPos()
        off_x = x + x_offset
        off_y = y + y_offset
        self.__setPos(off_x, off_y)

    def randomize(self, interval=60, n_moves=None):
        """Moves the cursor to a series of random positions every [interval] seconds. Stops moving the cursor after [n_moves], if defined.

        :param interval: number of seconds between moves, defaults to 60
        :type interval: int, optional
        :param n_moves: total number of moves, defaults to None
        :type n_moves: int, optional
        """
        while True:
            self.__setRandomPos(self.min_x, self.min_y, self.max_x, self.max_y)
            sleep(interval)
            if n_moves and self.n_moves >= n_moves:
                break