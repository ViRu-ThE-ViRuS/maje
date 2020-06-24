import numpy as np
import random
from maze_engine import Maze


class DynaQPlus:
    def __init__(self, n, alpha, gamma, epsilon, max_steps):
        self.env = Maze()
        self.time_weight = 1

        self.q = np.random.random((*self.env.observation_space, self.env.n_actions))
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

        while not done and n_steps < self.max_steps:
            if np.random.random() < self.epsilon:
                move = np.random.choice(4)
            else:
                move = np.argmax(self.q[state])

            # if self.env.trapped():
            # break

            # if self.env.useless_move(move):
            # continue

            if [state, move] not in self.memory:
                self.memory.append([state, move])

            new_state, reward, done = self.env.step(move)

            target_delta = 0 if done else self.gamma * np.max(self.q[new_state])
            self.q[(*state, move)] += self.alpha * (reward + target_delta - self.q[(*state, move)])
            self.model[(*state, move)] = [reward, new_state, n_steps, done]

            state = new_state
            total_reward += reward
            n_steps += 1

            for _ in range(self.n):
                _state, _move = random.sample(self.memory, 1)[0]
                _reward = self.model[(*_state, _move)][0]
                _new_state = self.model[(*_state, _move)][1]
                _n_steps = self.model[(*_state, _move)][2]
                _done = self.model[(*_state, _move)][3]

                change = self.time_weight * np.sqrt(n_steps - _n_steps)
                _reward += change
                # print(_reward, change)

                _target_delta = 0 if _done else self.gamma * np.max(self.q[_new_state])
                self.q[(*_state, _move)] += self.alpha * (_reward + _target_delta - self.q[(*_state, _move)])
        return total_reward, n_steps

    def learn(self, n_episodes):
        rewards, steps = [], []
        for episode in range(n_episodes):
            reward, step = self.play_episode()
            rewards.append(reward)
            steps.append(step)

            print(f'{episode:4d} : {reward:3f} : {step:3d} : {self.epsilon:.5f}')
            self.epsilon = 0.05 if self.epsilon <= 0.05 else self.epsilon * 0.95

        return rewards, steps


model = DynaQPlus(25, 0.5, 0.9, 1, 500)
reward, steps = model.learn(200)
model.env.deinit()
