# Project Description: Dark Impact

## 1. Project Overview

- **Project Name:** Dark Impact
- **Brief Description:** Dark Impact is a 2D side-scrolling action-RPG built with Python and Pygame. Players control a knight navigating through increasingly difficult levels, battling various fantasy creatures and powerful bosses. 

  The game features a robust combat system involving stamina management, diverse enemy types, and a permanent progression system where players can upgrade their stats using points earned in battle. A unique feature of the project is the integration of a full data-science suite that tracks player performance and generates visual reports using Pandas and Matplotlib.

- **Problem Statement:** Many modern action games prioritize accessibility to the point where the sense of genuine achievement is lost, often providing a "power fantasy" that requires little effort. Dark Impact addresses this by reintroducing high-stakes difficulty and a steep learning curve. By focusing on punishing combat mechanics and formidable boss encounters that require pattern recognition and precise timing, the game forces players to grow through failure. It restores the "triumph of overcoming," ensuring that every victory is earned through genuine skill and perseverance rather than luck.

- **Target Users:** Players who enjoy challenging 2D combat, fans of pixel-art aesthetics, individuals who enjoy the Soulsborne genre, and developers or students interested in seeing how database management and data visualization can be integrated into a functional game engine.

- **Key Features:**
  - Fast-paced 2D combat with jumping, dashing, and combo attacks.
  - Resource management system involving Health and Stamina.
  - Progressive difficulty across multiple stages and advanced Boss AI.
  - Automated Data Visualization generates Bar, Pie, Line charts, and scatterplot of gameplay stats.

- **Screenshots:**

  ### Gameplay
  ![1](screenshots/gameplay/01.png)
  ![2](screenshots/gameplay/02.png)
  ![3](screenshots/gameplay/03.png)
  ![4](screenshots/gameplay/a1.png)
  ![5](screenshots/gameplay/a2.png)
  ![6](screenshots/gameplay/a3.png)
  ![7](screenshots/gameplay/a4.png)
  ![8](screenshots/gameplay/a5.png)
  ![9](screenshots/gameplay/a6.png)
  ![10](screenshots/gameplay/a7.png)
  ![11](screenshots/gameplay/a8.png)
  ![12](screenshots/gameplay/dead.png)

  ### Data Visualization
  ![g1](screenshots/visualization/dt1.png)
  ![g2](screenshots/visualization/dt2.png)
  ![g3](screenshots/visualization/dt3.png)
  ![g4](screenshots/visualization/dt4.png)
  ![g5](screenshots/visualization/dt5.png)

- **Proposal:** [Project Proposal](./proposal.pdf)

- **YouTube Presentation:** *https://www.youtube.com/watch?v=DZbk7HASFBg*

---

## 2. Concept

### 2.1 Background
- **Why this project exists:** To combine traditional action-heavy gameplay with modern data analytics in a skill-based environment.
- **What inspired the project:** Classic "Souls-like" and Metroidvania titles where positioning and resource management are key to survival.
- **Importance of solving this problem:** It addresses the lack of challenge in modern "power fantasy" games by restoring the rewarding feeling of overcoming difficult obstacles through skill.

### 2.2 Objectives
- Implement a responsive 2D physics and combat engine using Pygame.
- Create an extensible Enemy and Boss framework.
- Develop a persistent database schema for character progression and session history.
- Integrate data analysis libraries (Pandas/Matplotlib) directly into the game UI.
- Deliver a polished aesthetic using high-quality pixel art and AI-generated environmental assets.

---

## 3. UML Class Diagram
The UML class diagram illustrates the inheritance structure between the base `Enemy` class and its specialized subclasses, as well as the relationship between the `System` controller and the various UI and Data modules.

**Submission Requirement:**
- [UML Class Diagram](./uml.pdf)

---

## 4. Object-Oriented Programming Implementation

- **System:** Central engine controller for Pygame initialization, scaling, and global drawing utilities.
- **Level:** Primary game loop controller managing backgrounds, enemy waves, and collision.
- **Background:** Utility class for loading and retrieving stage-specific background surfaces.
- **Player:** Core entity handling state machine transitions (movement, combat) and resource management.
- **Enemy:** Base class for standard hostile AI implementing patrolling and detection logic.
- **Boss:** Advanced entity subclass with multi-phase combat logic and specialized state management.
- **Individual Entities (Skeleton, Goblin, Mushroom, Big Mushroom, Flying Eye, Minotaur, Golem, Tarnished Widow):** Specialized subclasses implementing unique attributes and frame-specific behaviors.
- **GameDB:** Database abstraction layer for SQLite connections and data management.
- **PlayerStats:** Specialized class tracking permanent progression (Health, Power, Critical, etc.).
- **EnemyDefeated:** Data container recording specific kill counts per species for metrics.
- **InGameTimeStamp:** Time-series class capturing snapshots of player status at fixed intervals.
- **PointUsage:** Tracks distribution of spent points across upgrade categories.
- **Plotter:** Visualization engine utilizing Pandas and Matplotlib to generate PNG reports.
- **Summary:** Reporting interface that presents generated visualizations to the player.
- **Upgrade:** Persistent menu for interacting with the database to enhance attributes.
- **Selection:** Interface for stage navigation and level unlocking.
- **Button:** Modular UI component handling collision and event-driven triggers.
- **SpriteLoaders:** Asset managers for slicing sprite sheets into indexed animation frames.

---

## 5. Statistical Data

### 5.1 Data Recording Method
All gameplay data is recorded by the `StatsLogger` and database classes into an SQLite database (`histories.db`). Data is collected via **Event-Based Logging** (immediate recording of kills/purchases), **Periodic Snapshots** (intervals for performance trends), and **Persistence** (sqlite3 management across sessions).

### 5.2 Data Features
- **Player Progression:** Permanent stats including health, power, critical, and stamina.
- **Combat Metrics:** Enemy defeat counts categorized by species (Skeleton, Goblin, Bosses, etc.).
- **Time-Series:** Real-time performance snapshots (health and points at specific timestamps).
- **Economy:** Spending habits regarding point distribution in the upgrade shop.

---

## 6. Changed Proposed Features (Optional)

- **Dynamic Boss Personalization:** Added a `BossNameGennerator` to provide randomized, unique titles for bosses.
- **Stamina-Based Action Economy:** Implemented a resource cost for dashing and attacking to add tactical depth.
- **Automated Visualization Suite:** Integrated a full `Plotter` engine to automatically generate visual PNG reports instead of raw numbers.

---

## 7. External Sources

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