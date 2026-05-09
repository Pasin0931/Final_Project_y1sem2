# Dark Impact

## Project Description

- Project by: Pasin Makcharoen
- Game Genre: Action, Dark Fantasy, Soulsborne

Dark Impact is a fixed-screen 2D soulslike action game set in a dark fantasy world. Players can challenge any of the five stages freely, with each stage offering increasing difficulty, stronger enemies, and intense boss fights.
The game focuses on skill-based combat, emphasizing movement, attacking, and dodge mechanics to deliver a challenging and rewarding experience inspired by soulborne gameplay. Players fight through series of enemies such as Skeletons, Goblins, Mushrooms, and Flying Eyes before facing powerful bosses including the Minotaur, Golem, and Tarnished Widow.
Defeating enemies grants upgrade points that can be used to improve player stats, allowing progression through harder stages while tracking performance through the in-game statistics summary menu.

---

## Installation
To Clone this project:
```sh
git clone https://github.com/Pasin0931/Final_Project_y1sem2.git
```

To create and run Python Environment for This project:

Window:
```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Mac:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Running Guide
After activate Python Environment of this project, you can process to run the game by:

Window:
```bat
python main.py
```

Mac:
```sh
python3 main.py
```

---

## Tutorial / Usage
1) Install all dependencies
Window:
```sh
pip install -r requirements.txt
```
Mac:
```sh
pip3 install -r requirements.txt
```
2) Launch the game using python main.py or python3 main.py
3) Click "play" and select a stage from the level selection menu
4) Control the knight using keyboard inputs:
    - A               -> Move left
    - D               -> Move right
    - space           -> Jump
    - LEFT SHIFT      -> Dodge (roll)
    - LEFT CLICK & K  -> Normal attack
    - RIGHT CLICK & L -> Combo attack (Only increase critical chance but same damage)
5) Defeat series of enemies and survive until the boss appears
6) Earn upgrade points after completing a stage or dying during battle
7) Use collected points to upgrade player stats before entering harder stages
8) View gameplay statistics and progression from the summary menu

You can also reset your character shrength and progress anytime in upgrade page.

---

## Game Features
1) Fast-paced 2D soulslike combat system
2) Fixed-screen dark fantasy gameplay
3) Five selectable stages with increasing difficulty
4) Five enemy types:
    - Skeleton
    - Goblin
    - Mushroom
    - Big Mushroom
    - Flying Eye
5) Three unique boss fights:
    - Minotaur
    - Golem
    - Tarnished Widow
6) Dodge mechanics with skill-based gameplay
7) Player stat upgrade system using earned points
8) Statistics tracking system for player performance
9) Session data recording using SQLite database

---

## Known Bugs
None

---

## Unfinished Works
None

---

### External sources

# Sprites
Acknowledge to:
1. Fantasy Knight (player sprite), https://aamatniekss.itch.io/fantasy-knight-free-pixelart-animated-character [sprite sheet]
2. Skeleton, Goblin, Mushroom, Big Mushroom, Flying Eye (Enemy sprite), https://luizmelo.itch.io/monsters-creatures-fantasy [sprite sheet]
3. Minotaur (boss sprite) https://xzany.itch.io/minotaur-2d-pixel-art [sprite sheet]
4. Golem (boss sprite) https://xzany.itch.io/stone-golem [sprite sheet]
5. Tarnished Widow (boss sprite) https://penusbmic.itch.io/the-dark-series-the-tarnished-widow-boss [sprite sheet]

# Music / Ambients
Acknowledge to:
1. Ashen Crown (AI Gennerated), suno.com [boss background music]
Prompt: soulborn boss fight ambient music theme: slow loop, length: 3 minutes
2. Ashen Crown Dusk (AI Gennerated), suno.com [stage ambient music]
Prompt: soulborn calm ambient music theme: slow loop, length: 3 minutes

# Backgrounds
Acknowledge to:
1. s1.png, gemini.google.com [stage 1 - background]
Prompt: gennerate me Pixel art panoramic landscape of a serene green meadow at sunrise, with layered hills in the background under a gradient sky. The foreground has a detailed cracked stone wall. A thick, wide black bar frames the top and bottom.
2. s2.png, gemini.google.com [stage 2 - background]
Prompt: gennerate me Pixel art panoramic landscape of a serene green meadow at sunrise, with layered hills in the background under a gradient sky. The foreground has a detailed cracked stone wall. A thick, wide black bar frames the top and bottom. 
night version, no fireflies
3. s3.png, gemini.google.com [stage 3 - background]
Prompt: gennerate me Pixel art panoramic landscape of a serene green meadow at sunrise, with layered hills in the background under a gradient sky. The foreground has a detailed cracked stone wall. A thick, wide black bar frames the top and bottom.      
night version, ruined fantasy medieval age village background with smoke rising far away, and flames, no moon, no sun
4. s4.png, gemini.google.com [stage 4 - background]
Prompt: gennerate me Pixel art panoramic landscape of a serene green meadow at sunrise, with layered hills in the background under a gradient sky. The foreground has a detailed cracked stone wall. A thick, wide black bar frames the top and bottom.       
night version, battle field, no moon, no sun
5. s5.png, gemini.google.com [stage 5 - background]
Prompt: gennerate me Pixel art panoramic landscape of a serene green meadow at sunrise, with layered hills in the background under a gradient sky. The foreground has a detailed cracked stone wall. A thick, wide black bar frames the top and bottom.         
night version, battle field, crimson moon at the center, blood red sky
6. selection.png, gemini.google.com [stage selection - background]
Prompt: gennerate me A 2D pixel art game selection screen with a dark gothic fantasy aesthetic. The gennerate me background features a silhouette of a massive crumbling dark castle with sharp spires and a ruined bridge. A giant, glowing blood-red moon dominates the upper left sky against a deep crimson gradient atmosphere. In the center foreground, five empty stone-textured square UI buttons are arranged in a horizontal row, each featuring a glowing red outline. Thick black cinematic bars frame the top and bottom. High-contrast 16-bit style, ominous and apocalyptic mood. no title needed, just five empty stone-textured square UI buttons arranged in a horizontal row at the center x and y of the screen, do not make the stone block lower than y axis
7. image.png, gemini.google.com [menu - background]
Prompt: gan u gennerate the main menu with my theme (bloodmoon) do not include any title or text, also have some space on the left side of the screen because I will put buttons and title there
REMOVE STONE BLOCKS

# All original background gennerated by gemini is stored in ../stage/old