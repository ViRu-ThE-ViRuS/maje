# maje
Learning to solve mazes using reinforcement learning algorithms like DynaQ,
DynaQ+, DQN and testing their performance compared to traditional algorithms.
Goal is also to visualize the algorithms thinking and learning process.

### gen1 dynaQ naive
added dynaQ agent, which shows quick learning from experience, but still takes
10000 episodes to finally start building towards the target policy due to the
nature of the maze, and the reward being very far off

- a possible solution is to optimise exploration even more for the problem
- dynaQ+ algorithm solves this problem efficiently, that will be gen4

### gen2 dynaQ + heuristic reward
added a heuristic reward, less negative the closer you get to the goal... this
speeds up training by a large factor and dynq q agents starts focusing on
figuring out the shortest path to the solution while modelling the environment
maze

- next steps is to move on to dynaq+ with time weighted exploration incentives
  with heuristics for faster convergence

<br>
<img src="res/gen2.gif" height="250" width="250" />
<br>

### gen3 dynaQ naive and dynaQ + heuristic
fixed a lot of edge case bugs, and improved reward hypothesis, resulting
algorithms almost always converge withing 50 episodes and find optimal path(s)
soon after... dynaq heuristic finds more of the shortest paths withing the same
time frame
<br>
both models show high learning speed, and almost never repeat a blunder class
mistake they once made (hitting a wall or exiting the game scope), this is a
major advantage of dynaq planning+learning algorithms over naive q learning

- next step is to compare these 2 against dynaq+

<br>
<img src="res/gen3.gif" height="250" width="250" />
<br>

### gen4 dynaQ+
adding a last-visit-time-delta based heuristic to the rewards in the planning
phase to enhance explorative behaviour, dynaQ+, doesn't really help performance
in this static maze problem setting. In some runs, it even reduces convergence
speed because the agent starts exploring behaviour when it doesnt need to and
already has a fact base

