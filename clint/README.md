
## Daily Log and Progress
### Tuesday, January 14th, 2020
Installed OpenAI Gym: https://github.com/openai/retro

```python3 -m pip install gym-retro```

Super Mario Kart is not included as one of the mapped ROMs, so the first step is going to be get the ROM and add integration support for it into Retro Gym: https://retro.readthedocs.io/en/latest/integration.html#game-integration

Downloaded SNES game ROMs from here:
https://archive.org/details/No-Intro-Collection_2016-01-03_Fixed

Loaded `Super Mario Kart (USA).sfc` into Gym Retro Integration app

Began mapping memory -- found the variable used for Coins, for final track times, and (perhaps most importantly) for current lap progress.

Each track is divided into 30 segments that the AI uses to track progress from one lap segment to another.  There's a counter that increases as you go around the track, and we can use this for AI progress.

Also found the current track timer, current acceleration value, and steering value.


### Wednesday, January 15th, 2020
Had trouble making progress on the memory map yesterday, so today I poked around online and found a few other places where people had mapped out some variables:

* https://datacrystal.romhacking.net/wiki/Super_Mario_Kart:RAM_map
* https://hack64.net/wiki/doku.php?id=mario_kart_64:memory_map
* https://smkdan.eludevisibility.org/smk.html
* https://www.smwcentral.net/?p=viewthread&t=93458
* http://www.arcaderestoration.com/memorymap/5382/Mario+Kart.aspx
* https://www.reddit.com/r/romhacking/comments/bmvn1s/ram_mapping_super_mario_kart/
* https://epicedit.stifu.fr/smk_doc/


Followed this blog post for information on setting up the reward function: https://medium.com/aureliantactics/setting-up-a-reward-function-in-retro-gym-and-other-utilities-886491849353

This one was also interesting: https://medium.com/aureliantactics/creating-a-custom-reward-function-in-retro-gym-and-other-utilities-33c9f783bd1a

Finally got a simple reward function written in Lua to work -- I think this will be just fine.  It "cheats" a little bit in that it looks at the RAM to track the current progress around the track, but I think this is acceptable.  Maybe in the future we will want to make one that only looks at the screen, but I think this is fine for now.

You can see the reward function in action here:
![AI Gym Integration Screenshot](docs/MarioKartAI_GymRetroIntegration.png)

Huzzah!


### Thursday, January 16th, 2020

Helpful link: https://www.freecodecamp.org/news/how-to-use-ai-to-play-sonic-the-hedgehog-its-neat-9d862a2aef98/
