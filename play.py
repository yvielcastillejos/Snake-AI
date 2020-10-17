from game import Game
import random
import numpy as np
from collections import Counter

# For data gathering

env = Game()
ascore = 100
LR = 1e-3
goal_steps = 300
score_requirement = 50
episodes = 1000
observation_q = []
acceptedscores = []
traindata = []
scores =[]
def gather(model_isTrue, model):
     observation = env.reset()
     for j  in range(episodes):
         print(f'Simulation {j}  out of {episodes} games')
         i = 0
         observation = env.reset()
         # game memory
         game_memory = []
         # prev obs
         prev_observation  = []
         score = 0
         for time_step in range(0,goal_steps,1):
             # We won't render it for now to quicken data gathering up
             # env.render()
             print(time_step) 
             if len(prev_observation) == 0:
                 # randomize first action
                 action = random.randrange(0,3)
             else:
                 # If we have no model
                 if model_isTrue == False:
                     action = random.randrange(0,3)
                 # If we have a model
                 else:
                     action = model(prev_observation)
             # get data from the game with the action this includes a 24 x1 observation array, scalar matrix, bool done, and {} info as I havent set it yet, but that is not really important.
             observation, reward, done, info = env.step(action)
             if len(prev_observation) > 0:
                 game_memory.append([prev_observation, action])
             prev_observation = observation
             score += reward
             if done:
                  break 
             # Now we can check if the specific game out of episodes has a high score (or it meets the score we defined
         if score >= score_requirement:
             acceptedscores.append(score)
             for data, action in game_memory:
             # Convert outputs to one hot code
                 if action == 0:
                     a = np.array([1,0,0])
                 if action == 1:
                     a = np.array([0,1,0])
                 if action == 2:
                     a = np.array([0,0,1])
                 traindata.append([data, a])  
         # Save all scores
         scores.append(score) 
     # Numbers to help us see whether neural network helps 
     print('Average accepted score:', np.mean(acceptedscores))
     print('Score Requirement:', score_requirement)
     print('Median score for accepted scores:',np.median(acceptedscores))
     print(Counter(acceptedscores))
     # print(np.array(traindata))
     np.save("data_gen1.npy", np.array(traindata))
     return

def random_game():
    observation = env.reset()
    for _ in range(500):
        env.render()
        action = 1
        observation, reward, done, info =env.step(action)
        #env.prints()
        #print(done)
        if done:
            observation = env.reset()

if __name__ == '__main__':
    gather(False, None)
