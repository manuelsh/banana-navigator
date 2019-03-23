# Report with results

## Introduction

We have implemented a deep reinforcement learning agent, trained with a deep Q-Network algorithm similar to the one of the Nature paper [Playing Atari with Deep Reinforcement Learning](https://arxiv.org/pdf/1312.5602.pdf). The objective of the agent is to solve one of the Unity's environment, in concrete the "Banana Collector" environment.

## Methodology

The learning algorithm implemented has been the Deep Q-Networks algorithm. The algorithm maps a state to the values of the Q-function for each possible action using a neural network.

### Techniques

To help model convergence, we have used the following techniques: 

(1) Experience replay, which breaks the sequential order of one experience and keeps track of a replay buffer of (State, Action, Rewards, Next state). When the model is trained it samples at random from the replay buffer, which will break the correlations happening from repeating always similar actions plus allows to train multiple times from different events, including rare events.

(2) Fixed Q-Targets, where the target used in the loss function is the same Q function that we are training but with a weighted average of previous learned parameters. This ensures that we don't shift the parameters chasing a constantly moving target.

(3) Double DQN, based on the following [research paper](https://arxiv.org/abs/1509.06461), where the best action selected to calculate the target comes from a different set of parameters on the Q function (we can used the two sets of parameters from the Fixed Q-Targets technique). This helps in the training of the early stages, as otherwise the Q-Values will be overestimated.

### Hyper parameters selected

We have trained the model for 2000 episodes, each one of 1000 steps maximum, with an epsilon greedy policy with an initial epsilon of 1 and a terminal epsilon of 0.01, and a decay rate of 0.995. 

The neural network representing the Q-function is composed by 4 layers of 200, 100, 50 and 4 neurons respectively, with RELU activations.

## Results

The model converges to a value higher than +13 after 500 episodes for the average of the past 100 episodes. The average score and loss function values during training are:

Episode 100		Average Score: 0.24 	Loss: 0.020
Episode 200		Average Score: 2.36 	Loss: 0.0100
Episode 300		Average Score: 6.46 	Loss: 0.0200
Episode 400		Average Score: 10.88 	Loss: 0.0600
Episode 500		Average Score: 13.86 	Loss: 0.0100
Episode 600		Average Score: 14.97 	Loss: 0.0100
Episode 700		Average Score: 14.98 	Loss: 0.0300
Episode 800		Average Score: 14.83 	Loss: 0.0300
Episode 900		Average Score: 15.72 	Loss: 0.0300
Episode 1000	Average Score: 15.69 	Loss: 0.0300
Episode 1100	Average Score: 16.09 	Loss: 0.2000
Episode 1200	Average Score: 15.79 	Loss: 0.0500
Episode 1300	Average Score: 15.82 	Loss: 0.0400
Episode 1400	Average Score: 15.84 	Loss: 0.0200
Episode 1500	Average Score: 15.60 	Loss: 0.0300
Episode 1600	Average Score: 15.91 	Loss: 0.0100
Episode 1700	Average Score: 15.76 	Loss: 0.0400
Episode 1800	Average Score: 15.04 	Loss: 0.0200
Episode 1900	Average Score: 15.11 	Loss: 0.0100
Episode 2000	Average Score: 15.88 	Loss: 0.2600

and the score plot during training is:

![score plot](https://github.com/manuelsh/banana-navigator/blob/master/images/scores.png)

Note that the parameters of the function can be found in the file `Q_network_parameters.pt`.

# Next steps

There are a few next steps that can be researched:

1. Train from pixels, which can be done with the Unity environment
2. Apply Prioritized Experience Replay, as described in https://arxiv.org/abs/1511.05952
3. Dueling DQN, as described in https://arxiv.org/abs/1511.06581
4. Using multi-step bootstrap targets, as described in https://arxiv.org/abs/1602.01783

In a personal note, I have enjoyed this project very much, and also the fact that there is so much to learn and try.