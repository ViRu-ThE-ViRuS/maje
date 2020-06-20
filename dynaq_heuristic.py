import numpy as np
import random
from maze_engine import Maze


class DynaQHeuristic:
    def __init__(self, n, alpha, gamma, epsilon, max_steps):
        self.env = Maze()

        self.q = np.zeros((*self.env.observation_space, self.env.n_actions))
        self.model = {}

        self.memory = []

        self.n = n
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.max_steps = max_steps

    def play_episode(self):
        state = self.env.reset()
        done = False
        total_reward = 0
        n_steps = 0

        while not done:
            if np.random.random() < self.epsilon:
                move = np.random.choice(4)
            else:
                move = np.argmax(self.q[state])

            if self.env.trapped():
                break

            if self.env.useless_move(move):
                continue

            self.memory.append([state, move])

            new_state, reward, done = self.env.step(move)

            heuristic = self.env.distance_heuristic()
            reward += heuristic

            target_delta = 0 if done else self.gamma * np.argmax(self.q[new_state])
            self.q[(*state, move)] += self.alpha * (reward + target_delta - self.q[(*state, move)])
            self.model[(*state, move)] = [reward, new_state, done]

            state = new_state

            n_steps += 1
            total_reward += reward

            for _ in range(self.n):
                _state, _move = random.sample(self.memory, 1)[0]
                _reward = self.model[(*_state, _move)][0]
                _new_state = self.model[(*_state, _move)][1]
                _done = self.model[(*_state, _move)][2]

                _target_delta = 0 if _done else self.gamma * np.argmax(self.q[_new_state])
                self.q[(*_state, _move)] += self.alpha * (_reward + _target_delta - self.q[(*_state, _move)])

        return total_reward, n_steps

    def learn(self, n_episodes):
        rewards, steps = [], []
        for episode in range(n_episodes):
            reward, step = self.play_episode()
            rewards.append(reward)
            steps.append(step)

            print(f'{episode:4d} : {reward:5.4f} : {step:3d} : {self.epsilon:.5f}')

            self.epsilon = 0.05 if self.epsilon <= 0.05 else self.epsilon * 0.95

        return rewards, steps


model = DynaQHeuristic(1000, 0.75, 0.9, 1.0, 1000)
reward, steps = model.learn(10000)
model.env.deinit()
