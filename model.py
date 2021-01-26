import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, hidden_sizes=[64, 64]):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            hidden_sizes (int)[]: list of integers, the sizes of the hidden layers
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)

        self.hidden_layers = nn.ModuleList([nn.Linear(state_size, hidden_sizes[0])])
        
        # Add a variable number of more hidden layers
        layer_sizes = zip(hidden_sizes[:-1], hidden_sizes[1:])
        self.hidden_layers.extend([nn.Linear(h1, h2) for h1, h2 in layer_sizes])
        
        self.output = nn.Linear(hidden_sizes[-1], action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        for each in self.hidden_layers:
            state = F.relu(each(state))
        return self.output(state)
