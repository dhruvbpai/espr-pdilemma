import random


agent_dict = {}

def CooperateBot(my_moves, op_moves):
  return 1
agent_dict["CooperateBot"]=CooperateBot


def DefectBot(my_moves, op_moves):
  return 0
agent_dict["DefectBot"]=DefectBot


def TitForTat(my_moves, op_moves):
  if len(op_moves)==0:
    return 1
  if op_moves[-1] == 0:
    action = 0
  else:
    action = 1
  return action
agent_dict["TitForTat"]=TitForTat

def MeanTat(my_moves, op_moves):
  if len(op_moves)==0:
    return 0
  if op_moves[-1] == 0:
    action = 0
  else:
    action = 1
  return action
agent_dict["MeanTat"]=MeanTat


def run_game(bot1, bot2, n_steps):
  moves1 = []
  moves2 = []
  for i in range(n_steps):
    action1 = bot1(moves1, moves2)
    action2 = bot2(moves2, moves1)
    moves1 += [action1]
    moves2 += [action2]
  return moves1, moves2


def get_reward(moves1, moves2):
  T, R, P, S = [3,2,1,0]
  reward1 = 0
  reward2 = 0
  for i in range(len(moves1)):
    if (moves1[i] == 0) and (moves2[i] == 0):
      reward1 += P
      reward2 += P
    if (moves1[i] == 1) and (moves2[i] == 1):
      reward1 += R
      reward2 += R
    if (moves1[i] == 1) and (moves2[i] == 0):
      reward1 += S
      reward2 += T
    if (moves1[i] == 0) and (moves2[i] == 1):
      reward1 += T
      reward2 += S
  return [reward1, reward2]


def simulate(n_simulations = 100, n_steps = 100):
  training_data = []

  for i in range(n_simulations):
    bot1_name = random.choice(list(agent_dict.keys()))
    bot2_name = random.choice(list(agent_dict.keys()))
    moves1, moves2 = run_game(agent_dict[bot1_name], agent_dict[bot2_name], n_steps)
    reward1, reward2 = get_reward(moves1, moves2)
    
    sequence = [reward1, reward2]
    for j in range(n_steps):
      sequence += [moves1[j], moves2[j]]

    training_data += [sequence]

  return training_data


training_data = simulate(n_simulations = 100, n_steps = 5) # training_data = [[r1,r2,m1,m2,m1,m2,...],...]
print(training_data)

