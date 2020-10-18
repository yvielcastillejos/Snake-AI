import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
import random
import time
#import sklearn as sk
#from sklearn import preprocessing, model_selection
import torch.nn.functional as F
from collections import Counter
from play import gather

i=6

class NN(nn.Module):
   def __init__(self):
       super(NN, self).__init__()
       #self.fc1 = nn.Linear(24, 12)
       self.fc2 = nn.Linear(24,6)
       self.fc3 = nn.Linear(6,3)
   def forward(self, x):
      # x = self.fc1(x)
       x = F.tanh(self.fc2(x))
       x = F.log_softmax(self.fc3(x), dim = 1)
       return x

def initialize(learningrate):
   torch.manual_seed(1)
   model = NN()
   loss = torch.nn.CrossEntropyLoss()
   opt = torch.optim.SGD(model.parameters(), lr= learningrate)
   return model, loss, opt

def accuracy(predict, trainlabel):
   predict = np.expand_dims(np.array([np.argmax(i) for i in predict.detach().numpy()]), axis =1)
  # print(predict)
   a = 1 - np.sum(np.clip(abs(predict-trainlabel.numpy()),0,1))/len(trainlabel)
   return a

def train(traindata, trainlabel, validationdata, validationlabel):
   lossRec = []
   vlossRec = []
   nRec = []
   trainAveRec = []
   trainAccRec = []
   validAccRec = []
   validfreqRec = []
   trainsum = []
   mdl, lsf, op = initialize(0.08)
   for i in range(150):
       #print(f"EPOCH {i}")
       # I will not implement batch sizing
       for k in range(39):
       # Training Loop
          traindata1 = traindata[100*k:100*k+100]
          trainlabel1 = trainlabel[100*k:k*100+100]
          op.zero_grad()
          predict = mdl(traindata1.float())
          ls = lsf(input = predict.squeeze(), target = trainlabel1.float().squeeze().long())
          ls.backward()
          op.step()
          # Training Accuracy Calculation
          t_predict = mdl(traindata)
          trainAcc =  accuracy(t_predict, trainlabel)
          trainAccRec.append(trainAcc)
          # Validation Accuracy Calculation
          v_predict = mdl(validationdata.float())
          validAcc = accuracy(v_predict, validationlabel)
          validAccRec.append(validAcc)
          if k%39 == 0:
                print(f"EPOCH {i}")
                print(f"Then training accuracy is {trainAcc:2f}, the validation accuracy is {validAcc: .2f}")
   return mdl, trainAccRec, validAccRec

if __name__ == "__main__":
# for i in range(0,5):
   #i = 2
   print("------------------------------------------------------------------------------------------")
   print(f"gen{i}") 
   print("------------------------------------------------------------------------------------------")
   # For data gathering
   # Later
   if i == 0:
       k = False
   else: 
       k = True
   FILE = "model.pth"
   loaded_model = NN()
   loaded_model.load_state_dict(torch.load(FILE))
   loaded_model.eval()
   gather(k ,loaded_model, i, score_requirement = -0.4, episodes = 500, goal_steps = 100 )
   traindata = np.load(f"/Users/yvielcastillejos/python_code/Snake-AI/data/data_gen{i}.npy", allow_pickle=True)
   X = np.array([i[0] for i in traindata])
   y = np.expand_dims(np.array([np.argmax(i[1]) for i in traindata]), axis = 1)
   print((Counter(y.squeeze().tolist())))
   print("the shapes of Input and labels are:")
   print(np.shape(X))
   print(np.shape(y))
   X_tens = torch.from_numpy(X).float()
   y_tens = torch.from_numpy(y).float()
   X_tensor = X_tens[0:int(len(X_tens)-1)]
   y_tensor = y_tens[0:int(len(y_tens)-1)]
   X_validation = X_tens[int(len(X_tens)*0.8):int(len(X_tens)-1)]
   y_validation = y_tens[int(len(y_tens)*0.8):int(len(y_tens)-1)]
   global model
   global Tacc
   global Vacc
   model, Tacc, Vacc = train(X_tensor, y_tensor, X_validation, y_validation)
   FILE = "model.pth"
   torch.save(model.state_dict(), FILE)



