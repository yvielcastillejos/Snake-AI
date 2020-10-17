# Snake-AI
Teaching an AI to play the snake game using neural networks. Snake game is visualized using a python library called pygame. 

## Design of the Neural Network
- We will have 8 inputs (observation state) corresponding to 8 directions relative to the head. Each direction will have 3 extra numbers that conveys information about the snake's distance to its body, to a wall and to the apple.
- we will train it with X generations of snakes. We will implement a "mutation" mechanism in which for each generation, we will clone the best snake from the X generation and start anew.
- Each generation will contain 1000 snakes; My computer is slow :((
- Design Diagram (24 inputs, 2 hidden layers, 3 outputs) TBA
- More info TBA
- We will use pytorch to train the snake.

## The Game
The snake game is a very popular game in which the objective is for the "the snake" to acquire the "apple." Once it "eats" the apple, the snake becomes longer. The game ends when:
 - The snake collides with its own body
 - The snake collides with the wall (The wall generator can be turned off in this version, and the snake will just simply pass through and show up on the other side)

Here is a clip of the Snake game generated using pygame (code is included in the repo):                   
<img src = "https://github.com/yvielcastillejos/Snake-AI/blob/main/game.gif" width = "250" height = "250">

## Results
- To make it a substantially faster project for me, I have changed the gridsize to be 50 from 25 (which is what I used for the example shown above). This will allow the neural network to train faster. The essence of the project has not changed so I believe it is fine.

| Generation| Visualization| Average Score (100 for one apple; 1 for each move)| Snake Population|
|:---------:|:------------:|:------------:|:---------------:|
|     1     |<img src = "https://github.com/yvielcastillejos/Snake-AI/blob/main/Generation/Gen1.gif"  width = "150" height = "150">  |     0  |     1000    |
|     2     |  TBA | 0 | 500|
 
## Next steps
 - Use a Deep Reinforcement Learning approach, which is not neccesarily harder; however, it may turn out better than the NN approach
 - Employ different algorithms such as the Greedy Algorithm

## Acknowledgement
TBA
