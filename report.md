## Report 


### Learning algorithm
The algorithm is based on Deep Q-Learning as presented in the seminal paper by [Mnih et al. (2015)](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf).

#### Neural network architecture
The Neural Network (NN) consists of an input layer, three hidden layers, and an output layer. 
The input layer takes a vector representing the properties of the observed state. 
The hidden layers are fully connected layers with the following sizes `[512, 256, 256]`.
The output layer corresponds to the actions that the agent can take. 
Dropout is applied to each hidden layer (see [Hinton et al. 2012](https://arxiv.org/abs/1207.0580)).

```Python
QNetwork(
  (hidden_layers): ModuleList(
    (0): Linear(in_features=37, out_features=512, bias=True)
    (1): Linear(in_features=512, out_features=256, bias=True)
    (2): Linear(in_features=256, out_features=256, bias=True)
  )
  (output): Linear(in_features=256, out_features=4, bias=True)
  (dropout): Dropout(p=0.05, inplace=False)
)
```

#### Hyperparameters
The following hyperparameters define how the agent learned:
- replay buffer size: `1e6`
- minibatch size: `64`
- discount factor: `0.995`
- soft update parameter: `1e-3`
- learning rate: `5e-4`
- Steps till next update of NN: `16`

For the training, the following parameters were used:
- maximum steps per episode: `2000`
- epsilon start: `1.0`
- epsilon end: `0.01`
- epsilon decay: `0.995`

### Plot of rewards
The following scores were reached during training.
The goal was to reach an average score of 13 over 100 consecutive episodes. 
This goal was reached after 975 episodes of training.

<img src="https://github.com/Doegstra/Deep-Q-Learning-Banana-Navigation/blob/main/img/rewards_over_time_rolling_dark_v2.png"/>

```
Episode 100	Average Score: 0.32
Episode 200	Average Score: 1.09
Episode 300	Average Score: 2.17
Episode 400	Average Score: 4.57
Episode 500	Average Score: 4.96
Episode 600	Average Score: 5.37
Episode 700	Average Score: 7.48
Episode 800	Average Score: 9.17
Episode 900	Average Score: 10.89
Episode 1000	Average Score: 11.37
Episode 1075	Average Score: 13.03
Environment solved in 975 episodes!	Average Score: 13.03
```

### Ideas for future work
The algorithm can be further improved as it does not have state-of-the-art methods in all its parts.
For example, one could incorporate the following algorithmic enhancements.
- Double DQN (DDQN) ([van Hasselt et al. 2015](https://arxiv.org/abs/1509.06461))
- Prioritized experience replay ([Schaul et al. 2016](https://arxiv.org/abs/1511.05952))
- Dueling DQN ([Wang et al. 2016](https://arxiv.org/abs/1511.06581))
- Learning from multi-step bootstrap targets ([Mnih et al. 2016](https://arxiv.org/abs/1602.01783))
- Distributional DQN ([Bellemare et al. 2017](https://arxiv.org/abs/1707.06887))
- Noisy DQN ([Fortunato et al. 2019](https://arxiv.org/abs/1706.10295))
- Rainbow which combines the above mentioned improvements ([Hessel et al. 2017](https://arxiv.org/abs/1710.02298))
