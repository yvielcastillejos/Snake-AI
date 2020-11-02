# Snake-AI
Teaching an AI to play the snake game using neural networks. The repo also includes code incase the player wants to play. More below.

## The Game
The snake game is a very popular game in which the objective is for the "the snake" to acquire the "apple." Once it "eats" the apple, the snake becomes longer. The game ends when:
 - The snake collides with its own body
 - The snake collides with the wall (The wall generator can be turned off in this version, and the snake will just simply pass through and show up on the other side)

Here is a clip of the Snake game generated:              
<img src = "https://github.com/yvielcastillejos/Snake-AI/blob/main/game.gif" width = "250" height = "250">
## Repo Description
| Script | Description|
|:--:|:--:|
|`main.py`| Run this in order to play the game with keyboard using arrow keys or "wasd". |
|`grid_drawing`| Function used to generate the checkered background of pygame |
|`parameters.py`| Parameters for the size of the game window|
|`game.py`| I made the snake game into a conventional game environment one can see in other libraries such as openAI (I added observation acquisition, reward, and a choice to render the screen or not (useful for making data gathering faster)|
|`play.py`| main code for data acquisition by reading the state of the game and the action of the snake|
|`player.py`| contains the functions that generate the input data (8 directions x 3 distances calculation) and an unstructured version of main.py (not using classes)|
|`nn.py`| contains the Pytorch code for the Neural Network|
|`data_gen*.npy`| contains the training data gathered from `play.py`|

## Design of the Neural Network
- We will have 8 inputs (observation state) corresponding to 8 directions relative to the head. Each direction will have 3 extra numbers that conveys information about the snake's distance to its body, to a wall and to the apple.
- we will train it with X generations of snakes. We will implement a "mutation" mechanism in which for each generation, we will clone the best snake from the X generation and start anew.
- Each generation will contain 1000 snakes; My computer is slow :((
- Design Diagram (24 inputs, 2 hidden layers, 3 outputs) TBA
- More info TBA
- We will use pytorch to train the snake.

#### Input Data Logicistics
- The observation (input values) include the distance of the snake from the wall, apple, and its own body through 8 different directions relative to its head. A figure that may help explain this is shown below:

<img src = "https://github.com/yvielcastillejos/Snake-AI/blob/main/Generation/Input.jpg" height = 200 width = "200">

## Results
- To make it a substantially faster project for me, I have changed the gridsize to be 50 from 25 (which is what I used for the example shown above). This will allow the neural network to train faster. The essence of the project has not changed so I believe it is fine. Note: the game may be "slow" as I set the fps to a low number (useful for debugging and understanding data). Training takes quite a long time especially if we want a higher score (that is why the population is small as my computer is not fast enough sadly; although I do have access to a supercomputer, I have to line up for that, I'll use that next time)

| Gen| Visualization| Avg Score* | Snake Population**| Notes|
|:---------:|:------------:|:------------:|:---------------:|:---:
|     1     |<img src = "https://github.com/yvielcastillejos/Snake-AI/blob/main/Generation/Gen1.gif"  width = "180" height = "150">  |     30.0  |75|The moves are made using a random generator|
|     5     |  <img src = "https://github.com/yvielcastillejos/Snake-AI/blob/main/Generation/Gen5_cropped.gif" width  = "180" height = "150"  > | 120 | 75|The snake decided that it's best to just stay alive if it can't find the apple; hence, the snake goes in circle if the apple is not in its field of view. (This makes sense as the penalty for staying alive at this time was much smaller than the penalty for dying)|
|     10    | <img src = "https://github.com/yvielcastillejos/Snake-AI/blob/main/Generation/GEN10.gif" width = "180" height = 150>                          |   50 |TBA|At Gen6, I changed the penalty to -10 per move to avoid the snake going in circles|
|     20     | TBA|TBA|TBA
* (100 for one apple; -1 for each move; -50 for dying); This is the score defined by the environment I made and not by the conventional means.
** Because my population size was too small (I was contrained by how fast my computer can get and by how fast python can simulate), it will generally take more generations to fully train the snake.
## Next steps
 - Use a Deep Reinforcement Learning approach, which is not neccesarily harder; however, it may turn out better than the NN approach
 - Employ different algorithms such as the Greedy Algorithm

## Acknowledgement
 - This video inspired me to start this. However, it ended there. I did not copy any algorithms from this resource or anywhere online.   
[1] https://www.youtube.com/watch?v=vhiO4WsHA6c&t=2s&ab_channel=Chrispresso

- The structure of my code as can be seen in `game.py` is inspired by a library by openai gym in resource 3. The reason I reconstructed it in a way is that it is a very standard way to represent your game environment.      
[2] https://gym.openai.com/
