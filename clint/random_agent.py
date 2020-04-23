import retro
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    myPath = os.path.join(SCRIPT_DIR, "..", "data")
    myPath = "/Users/clintherron/dev/mario-kart-ai/data"
    print("Attempting to add path '" + myPath + "'")
    retro.data.Integrations.add_custom_path(myPath)

    print("SuperMarioKart-Snes" in retro.data.list_games(inttype=retro.data.Integrations.ALL))
    env = retro.make("SuperMarioKart-Snes", inttype=retro.data.Integrations.ALL)
    print(env)
    obs = env.reset()
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            obs = env.reset()
    env.close()        


if __name__ == "__main__":
        main()


