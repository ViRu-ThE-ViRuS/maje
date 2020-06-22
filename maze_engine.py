import pygame
import random
import numpy as np

pygame.init()
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
window_height = 100
window_width = 100

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
directions = [up, down, left, right]
block_size = 10

game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('maje')


class Maze:
    n_actions = 4
    observation_space = (window_width//block_size, window_height//block_size)

    def __init__(self):
        self.width = window_width // block_size
        self.height = window_height // block_size
        self.reset()

    def reset(self):
        self.done = False
        self.state = [0, 0]

        self.maze_data = self.generate_maze()
        self.render()

        return tuple(self.state)

    def generate_maze(self):
        self.blocks = [[1, 2], [2, 2], [3, 2], [0, 7], [1, 7], [2, 7], [4, 5]]
        self.goal = [self.width - 1, self.height - 1]
        self.max_distance = np.linalg.norm(np.array([0, 0]) - np.array(self.goal))

        maze = np.zeros((self.width, self.height))

        for block in self.blocks:
            maze[block[0], block[1]] = -1

        maze[self.state[0], self.state[1]] = 1
        return maze

    def render(self):
        for row in range(self.width):
            for col in range(self.height):
                if [row, col] == self.goal:
                    color = red
                elif self.maze_data[row, col] == 0:
                    color = white
                elif self.maze_data[row, col] == 1:
                    color = green
                elif self.maze_data[row, col] == -1:
                    color = black

                pygame.draw.rect(game_display, color,
                                 [row*block_size, col*block_size,
                                     block_size, block_size])

        pygame.display.update()

    def step(self, move):
        assert not self.done
        direction = directions[move]
        self.state = [self.state[0] + direction[0], self.state[1] + direction[1]]

        reward = 0
        if not(self.state[0] >= 0 and self.state[0] < self.width) or \
                not(self.state[1] >= 0 and self.state[1] < self.height):
            reward = -50
            self.done = True
        else:
            self.maze_data[self.state[0], self.state[1]] = 1

            self.done = self.state == self.goal or self.state in self.blocks
            if self.state in self.blocks:
                reward = -50
            elif self.state == self.goal:
                reward = 100

        self.render()
        return tuple(self.state), reward, self.done

    def useless_move(self, move):
        direction = directions[move]
        new_state = [self.state[0] + direction[0], self.state[1] + direction[1]]
        try:
            return self.maze_data[new_state[0], new_state[1]] == 1
        except IndexError:
            return False

    def trapped(self):
        return not any([not self.useless_move(move) for move in range(self.n_actions)])

    def distance_heuristic(self):
        # return self.max_distance / np.linalg.norm(np.array(self.state) - np.array(self.goal))
        return -(np.linalg.norm(np.array(self.state) - np.array(self.goal)) / self.max_distance)

    def deinit(self):
        pygame.quit()
