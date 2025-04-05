import numpy as np

from random import randint
from typing import Literal
from os import system


class Game:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.amount_separators = (2 * self.size) - 1

        self.matrix: np.ndarray = np.zeros((size, size), dtype=np.int64)

        self._add_new_block()
        self._add_new_block()

    def print(self) -> None:
        system("cls")
        max_number_space: int = len(str(self.matrix.max()))

        horizontal_bar: str = "--" + ("-" * max_number_space * self.amount_separators)

        print(horizontal_bar)

        for line in self.matrix:
            print("|" +
                  "|".join([(" " * abs(max_number_space - len(str(_)))) + str(_) for _ in line]) +
                  "|")

        print(horizontal_bar)

    def _add_new_block(self) -> None:
        while True:
            x, y = randint(0, self.size - 1), randint(0, self.size - 1)

            if self.matrix[y][x] == 0:
                self.matrix[y][x] = 2
                return

    def move(self, move_id: Literal[0, 1, 2, 3]) -> None:
        self.matrix = np.rot90(self.matrix, move_id)

        for y_index in range(self.size):
            for index in range(self.size):
                if self.matrix[y_index][index] == 0:
                    continue

                for r_index in range(index - 1, -1, -1):
                    if self.matrix[y_index][r_index] == 0:
                        self.matrix[y_index][r_index] = self.matrix[y_index][r_index + 1]
                        self.matrix[y_index][r_index + 1] = 0
                    elif self.matrix[y_index][r_index] == self.matrix[y_index][r_index + 1]:
                        self.matrix[y_index][r_index] *= 2
                        self.matrix[y_index][r_index + 1] = 0
                    else:
                        break

        self.matrix = np.rot90(self.matrix, abs(4 - move_id))

    def _simulate(self, move_id: Literal[0, 1, 2, 3]) -> np.ndarray:
        buffer_matrix = np.rot90(self.matrix, move_id).copy()

        for y_index in range(self.size):
            for index in range(self.size):
                if buffer_matrix[y_index][index] == 0:
                    continue

                for r_index in range(index - 1, -1, -1):
                    if buffer_matrix[y_index][r_index] == 0:
                        buffer_matrix[y_index][r_index] = buffer_matrix[y_index][r_index + 1]
                        buffer_matrix[y_index][r_index + 1] = 0
                    elif buffer_matrix[y_index][r_index] == buffer_matrix[y_index][r_index + 1]:
                        buffer_matrix[y_index][r_index] *= 2
                        buffer_matrix[y_index][r_index + 1] = 0
                    else:
                        break

        return np.rot90(buffer_matrix, abs(4 - move_id))

    def start_game(self) -> None:
        buffer: list[np.ndarray] = [self._simulate(_) for _ in range(4)]

        while not all([np.array_equal(_, buffer[0]) for _ in buffer]):
            self.print()
            player_in = input()
            while player_in not in ["0", "1", "2", "3"]:
                player_in = input()

            self.matrix = buffer[int(player_in)]
            self._add_new_block()
            buffer = [self._simulate(_) for _ in range(4)]


def main():
    g = Game(3)

    g.start_game()


if __name__ == '__main__':
    main()
