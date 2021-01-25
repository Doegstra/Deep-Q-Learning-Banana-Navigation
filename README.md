# Deep-Q-Learning-Banana-Navigation
Deep Q-Learning applied to Banana Navigation using Unity Machine Learning Agents (ML-Agents). 

Untrained agent

<img src="https://github.com/Doegstra/Deep-Q-Learning-Banana-Navigation/blob/main/img/banana_random.gif" width="400"/>

Trained agent
<img src="https://github.com/Doegstra/Deep-Q-Learning-Banana-Navigation/blob/main/img/banana_trained.gif" width="400"/>

### Project details
#### State and Action Spaces

The simulation contains a single agent that navigates a large environment.  At each time step, it has four actions at its disposal:
- `0` - walk forward 
- `1` - walk backward
- `2` - turn left
- `3` - turn right

The state space has `37` dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  A reward of `+1` is provided for collecting a yellow banana, and a reward of `-1` is provided for collecting a blue banana. 

TODO: The README describes the the project environment details (i.e., the state and action spaces, and when the environment is considered solved).

### Getting started
TODO: The README has instructions for installing dependencies or downloading needed files.

### Instructions
The README describes how to run the code in the repository, to train the agent.
