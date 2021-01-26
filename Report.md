## Report 


### Learning algorithm
The algorithm is based on Deep Q-Learning as presented in the seminal paper by [Mnih et al. (2015)](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf).

#### Neural network architecture
The Neural Network (NN) consists of an input layer, three hidden layers, and an output layer. 
The input layer takes a vector representing properties of the observed state. 
The hidden layers are fully connected layers with ReLU activation and with the following sizes `[64, 64]`.
The output layer corresponds to the actions that the agent can take. 

```Python
QNetwork(
  (hidden_layers): ModuleList(
    (0): Linear(in_features=37, out_features=64, bias=True)
    (1): Linear(in_features=64, out_features=64, bias=True)
  )
  (output): Linear(in_features=64, out_features=4, bias=True)
)
```

#### Hyperparameters
The following hyperparameters define how the agent learns:
- replay buffer size: `1e5`
- minibatch size: `64`
- discount factor: `0.99`
- soft update parameter: `1e-3`
- learning rate: `5e-4`
- Steps till next update of NN: `4`

For the training, the following parameters were used:
- maximum steps per episode: `1000`
- epsilon start: `1.0`
- epsilon end: `0.02`
- epsilon decay: `0.98`

### Plot of rewards
The following scores were reached during training.
The goal was to reach an average score of `13` over `100` consecutive episodes. 
This goal was reached after `248` episodes of training.

<img src="https://github.com/Doegstra/Deep-Q-Learning-Banana-Navigation/blob/main/img/rewards_over_time_dark_v4.png"/>

<img src="https://github.com/Doegstra/Deep-Q-Learning-Banana-Navigation/blob/main/img/rewards_over_time_rolling_dark_v4.png"/>

```
Episode 100	Average Score: 2.61
Episode 200	Average Score: 10.12
Episode 300	Average Score: 12.49
Episode 348	Average Score: 13.00
Environment solved in 248 episodes!	Average Score: 13.00
```

### Ideas for future work
The algorithm can be further improved as it does not have state-of-the-art methods in all its parts.
For example, one could incorporate the following algorithmic enhancements.
- Double DQN (DDQN) ([van Hasselt et al. 2015](https://arxiv.org/abs/1509.06461))
- (Prioritized experience replay ([Schaul et al. 2016](https://arxiv.org/abs/1511.05952)), might not help too much here)
- Dueling DQN ([Wang et al. 2016](https://arxiv.org/abs/1511.06581))
- Learning from multi-step bootstrap targets ([Mnih et al. 2016](https://arxiv.org/abs/1602.01783))
- Distributional DQN ([Bellemare et al. 2017](https://arxiv.org/abs/1707.06887))
- Noisy DQN ([Fortunato et al. 2019](https://arxiv.org/abs/1706.10295))
- Rainbow which combines the above mentioned improvements ([Hessel et al. 2017](https://arxiv.org/abs/1710.02298))
