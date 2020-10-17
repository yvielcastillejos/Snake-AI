from game import Game

# For data gathering
env = Game()
observation = env.reset()
for _ in range(500):
    env.render()
    action = 1
    observation, reward, done, info =env.step(action)
    #env.prints()
#    print(done)
    if done:
        observation = env.reset()
