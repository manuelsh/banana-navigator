import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.linear1 = nn.Linear(state_size, 200)
        self.linear2 = nn.Linear(200, 100)
        self.linear3 = nn.Linear(100, 50)
        self.linear4 = nn.Linear(50, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        r = self.linear1(state)
        r = F.relu(r)
        r = self.linear2(r)
        r = F.relu(r)
        r = self.linear3(r)
        r = F.relu(r)
        r = self.linear4(r)
        #r = F.softmax(r, dim=1)
        return r
        
class QNetworkVisual(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetworkVisual, self).__init__()
        self.conv_1 = nn.Conv2d(3,32, kernel_size=8, stride=4)
        self.conv_2 = nn.Conv2d(32,64, kernel_size=4, stride=2)
        self.conv_3 = nn.Conv2d(64,64, kernel_size=3, stride=1)
        self.linear_1 = nn.Linear(3136, 512)
        self.linear_2 = nn.Linear(512, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        r = state.permute(0,3,1,2).float()
        r = self.conv_1(r)
        r = F.relu(r)
        r = self.conv_2(r)
        r = F.relu(r)
        r = self.conv_3(r)
        r = F.relu(r)
        r = self.linear_1(r.view(r.shape[0], -1))
        r = F.relu(r)
        r = self.linear_2(r)
        return r
