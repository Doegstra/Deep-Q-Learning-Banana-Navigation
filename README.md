# Deep Q-Learning Banana-Navigation
Deep Q-Learning applied to Banana Navigation using Unity Machine Learning Agents (ML-Agents). 

After successful training, the agent will behave similar to the one below:

<img src="https://github.com/Doegstra/Deep-Q-Learning-Banana-Navigation/blob/main/img/banana_trained.gif" width="400"/>

## Project details
#### Goal
Collect as many yellow bananas as possible while avoiding blue bananas. 

#### State and Action Spaces

The simulation contains a single agent that navigates a large environment.  At each time step, it has four actions at its disposal:
- `0` - walk forward 
- `1` - walk backward
- `2` - turn left
- `3` - turn right

The state space has `37` dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  A reward of `+1` is provided for collecting a yellow banana, and a reward of `-1` is provided for collecting a blue banana. 

The task is episodic, and in order to solve the environment, the agent must get an average score of `+13` over `100` consecutive episodes.

## Getting started

`Python 3.6` was used to solve the problem at hand. 
Make sure [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation.md), [NumPy](http://www.numpy.org/) and [Torch](https://pytorch.org/docs/stable/torch.html) are installed.
The complete list of packages used in this project is given in the `requirements.txt`.

## Instructions

To train the agent, use `NavigationTraining.ipynb`. 
The agent itself is defined in `dqn_agent.py` and the neural network used to learn the actions is defined in `model.py`.
A detailed description of the interplay between the above mentioned files is given in `NavigationTraining.ipynb`.

The file `report.md` contains a summary of the methodology, hyperparameters and results of training.

To watch a trained and untrained agent in comparision, use `NavigationWatchAgents.ipynb`.
The pretrained network is stored in `checkpoint.pth`.

#### Download the Unity Environment
For this project, you will not need to install Unity - this is because Udacity has already built the environment for you, and you can download it from one of the links below. You need only select the environment that matches your operating system:
- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
- Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
- Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

Then, place the file in your project folder, and unzip the file.
