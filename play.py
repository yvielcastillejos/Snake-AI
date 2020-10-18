from game import Game
import random
import numpy as np
from collections import Counter
#from nn import *
import torch

# For data gathering
# Later
#FILE = "model.pth"
#loaded_model = NN()
#loaded_model.load_state_dict(torch.load(FILE))
#loaded_model.eval()

#op = 4
#env = Game()
#LR = 1e-3
#goal_steps = 100
#score_requirement = -0.3
#episodes = 50
##episodes = 5
#observation_q = []
#acceptedscores = []
#traindata = []
#scores =[]
def gather(model_isTrue, model,op, score_requirement=-0.3, episodes =50, goal_steps = 100):
     env = Game()
     observation_q = []
     acceptedscores = []
     traindata = []
     scores =[]
     observation = env.reset()
     score = 0
     corr= 0
     for j  in range(episodes):
         print(f'Simulation {j}  out of {episodes} games')
         i = 0
         observation = env.reset()
         # game memory
         game_memory = []
         # prev obs
         prev_observation  = []
         print(f"score is {score}")
         score = 0
         print(np.mean(scores))
         for time_step in range(0,goal_steps,1):
             # We won't render it for now to quicken data gathering up
             env.render()
       #      print(f"timestep {time_step}")
             if len(prev_observation) == 0: # or i%2 == 0: #or i%3 == 0:
                 # randomize first action
                 action = random.randrange(0,3)
                 print(action)
                 i+=1
        #     elif i == 20 or i == 21  or i == 71 or i == 70 or i == 100 or i ==101: # or i ==51: # or i ==80 or i == 81:
        #         action = 2
        #         print(action)
                 i+=1
             else:
                 # If we have no model
                 if model_isTrue == False:
                     action = random.randrange(0,3)
                 # If we have a model
                 else:
          #           print("pred")
                     data = np.expand_dims(np.array(prev_observation), axis = 0)
                     predict = model(torch.from_numpy(data).float())
                     #print((predict).detach().numpy()[0])
                     action = np.argmax((predict).detach().numpy()[0])
         #            print(action)
                     i+=1
             # get data from the game with the action this includes a 24 x1 observation array, scalar matrix, bool done, and {} info as I havent set it yet, but that is not really important.
             observation, reward, done, info = env.step(action)
             if len(prev_observation) > 0:
                 game_memory.append([prev_observation, action])
             prev_observation = observation
       #      print(f"reward is {reward}")
             score += reward
       #      print(f"score is {score}")
             if done:
                  break 
             # Now we can check if the specific game out of episodes has a high score (or it meets the score we defined
         if score >= score_requirement:
             corr+=1
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
     print(f"shape is {len(traindata)}")
     print(f"meets the score requirement {corr}/{episodes}")
     # print(np.array(traindata))
     np.save(f"data/data_gen{op}.npy", np.array(traindata))
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

#if __name__ == '__main__':
#    gather(True, loaded_model)
