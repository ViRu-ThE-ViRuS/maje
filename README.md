# maje
Learning to solve mazes using reinforcement learning algorithms like DynaQ,
DynaQ+, DQN and testing their performance compared to traditional algorithms
like A*, BFS etc. Goal is also to visualize the algorithms thinking.

### gen1 dynaQ naive
added dynaQ agent, which shows quick learning from experience, but still takes
10000 episodes to finally start building towards the target policy due to the
nature of the maze, and the reward being very far off

- a possible solution is to optimise exploration even more for the problem
- dynaQ+ algorithm solves this problem efficiently, that will be gen3

### gen2 dynaQ + heuristic reward
added a heuristic reward, less negative the closer you get to the goal... this
speeds up training by a large factor and dynq q agents starts focusing on
figuring out the shortest path to the solution while modelling the environment
maze

- next steps is to move on to dynaq+ with time weighted exploration incentives
  with heuristics for faster convergence


