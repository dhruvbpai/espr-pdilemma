"""
Basic prisoner's dilemma agents
Dhruv Pai, 8/23/22
"""
import torch.utils.data as data
from abc import ABC, abstractmethod
import numpy as np


class Agent(data.Dataset, ABC):
    """
    High level class for various agents
    """

    def __init__(self):
        self.agent_history = np.array()

    @property
    def get_agent_hist(self):
        return self.agent_history

    @property
    def mod_agent_hist(self, val: np.float):
        self.agent_history = np.append(self.agent_history, val)

    @abstractmethod
    def get_action(self, history: torch.Tensor):
        raise NotImplementedError


# Rock that cooperates (duh)
class CooperateRock(Agent):
    def get_action(self, history):
        action = 0
        self.mod_agent_hist(action)
        return action


# Rock that defects (duh)
class CooperateRock(Agent):
    def get_action(self, history):
        action = 1
        self.mod_agent_hist(action)
        return action


# Rock that gets revenge (duh)
class TitForTat(Agent):
    def get_action(self, history):
        data = history.detach().numpy()
        if not data[-1]:
            action = 0
        else:
            action = 1
        self.mod_agent_hist(action)
        return action
