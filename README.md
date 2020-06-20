# maje
Learning to solve mazes using reinforcement learning algorithms like DynaQ,
DynaQ+, DQN and testing their performance compared to traditional algorithms
like A*, BFS etc. Goal is also to visualize the algorithms thinking.

### gen1
added dynaQ agent, which shows quick learning from experience, but still takes
10000 episodes to finally start building towards the target policy due to the
nature of the maze, and the reward being very far off

- a possible solution is to optimise exploration even more for the problem
- dynaQ+ algorithm solves this problem efficiently, that will be gen3
