import numpy as np

from random import randint
from typing import Literal


class Game:
    def __init__(self, size: int) -> None:
        self.size = size

        self.matrix = np.zeros((size, size), dtype=np.int64)

        self._add_new_block()
        self._add_new_block()

    @property
    def print(self) -> None:
        print("--" + "-" * ((2 * self.size) - 1))

        for line in self.matrix:
            print("|" + "|".join([str(_) for _ in line]) + "|")

        print("--" + "-" * ((2 * self.size) - 1))

    def _add_new_block(self) -> None:
        while True:
            x, y = randint(0, self.size - 1), randint(0, self.size - 1)

            if self.matrix[y][x] == 0:
                self.matrix[y][x] = 2
                return

    def move(self, move_id: Literal[1, 2, 3, 4]) -> None:
        pass


def main():
    g = Game(3)
    g.print


if __name__ == '__main__':
    main()
