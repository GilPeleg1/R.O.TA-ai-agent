from Rota import Rota
from DQN_Agent import DQN_Agent
from ReplayBuffer import ReplayBuffer
from Random_Agent import Random_Agent
from MinMaxAgent import MinMaxAgent
import torch
from Tester import Tester
import wandb
import numpy as np


env = Rota()
player1 = DQN_Agent(player=-1, env=env,parametes_path ="Data\\params_1.pth")
arr =torch.tensor(np.array([[1.,0.,-1.,0.,-1.,0.,-1.,1.,1.,0.,0.,0.,0.],[1.,0.,-1.,0.,-1.,0.,-1.,1.,1.,0.,0.,0.,0.]]), dtype=torch.float32)
print(arr)
t = player1.DQN.forward(arr)
print(t)
 