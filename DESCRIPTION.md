# Project Description: Dark Impact

## 1. Project Overview

- **Project Name:** Dark Impact
- **Brief Description:** Dark Impact is a 2D side-scrolling action-RPG built with Python and Pygame. Players control a knight navigating through increasingly difficult levels, battling various fantasy creatures and powerful bosses. The game features a robust combat system involving stamina management, diverse enemy types, and a permanent progression system where players can upgrade their stats using points earned in battle. A unique feature of the project is the integration of a full data-science suite that tracks player performance and generates visual reports using Pandas and Matplotlib.

- **Problem Statement:** Many modern action games prioritize accessibility to the point where the sense of genuine achievement is lost, often providing a "power fantasy" that requires little effort. Dark Impact addresses this by reintroducing high-stakes difficulty and a steep learning curve. By focusing on punishing combat mechanics and formidable boss encounters that require pattern recognition and precise timing, the game forces players to grow through failure. It restores the "triumph of overcoming", ensuring that every victory is earned through genuine skill and perseverance rather than luck.

- **Target Users:** Players who enjoy challenging 2D combat, fans of pixel-art aesthetics, Individual who enjoy Soulsborne genre, and developers or students interested in seeing how database management and data visualization can be integrated into a functional game engine.

- **Key Features:**
  - Fast-paced 2D combat with jumping, dashing, and combo attacks.
  - Resource management system involving Health and Stamina.
  - Progressive difficulty across multiple stages.
  - Permanent upgrade shop to enhance Health, Power, Critical Chance, and Stamina.
  - Advanced Boss AI with multi-phase patterns and procedural naming.
  - Automated Data Visualization: Generates Bar, Pie, and Line charts of gameplay stats.
  - Persistent storage using SQLite to save progress across sessions.

- **Screenshots:**

  ### Gameplay
  ![Menu 1](screenshots/gameplay/01.png)
  ![Menu 2](screenshots/gameplay/02.png)
  ![Menu 3](screenshots/gameplay/03.png)
  ![Gameplay 1](screenshots/gameplay/a1.png)
  ![Gameplay 2](screenshots/gameplay/a2.png)
  ![Gameplay 3](screenshots/gameplay/a3.png)
  ![Gameplay 4](screenshots/gameplay/a4.png)
  ![Gameplay 5](screenshots/gameplay/a5.png)
  ![Gameplay 6](screenshots/gameplay/a6.png)
  ![Gameplay 7](screenshots/gameplay/a7.png)
  ![Gameplay 8](screenshots/gameplay/a8.png)
  ![Game over](screenshots/gameplay/screenshots/dead.png)

  ### Data Visualization
  ![barplot](screenshots/visualization/dt1.png)
  ![lineplot](screenshots/visualization/dt2.png)
  ![pieplot](screenshots/visualization/dt3.png)
  ![table](screenshots/visualization/dt4.png)

- **Proposal:** [Project Proposal](./proposal.pdf)

- **YouTube Presentation:** *...*

---

## 2. Concept

### 2.1 Background
Dark Impact was inspired by classic "Souls-like" and Metroidvania titles where positioning and resource management are key to survival. The project was developed as a way to combine game development with data analytics, demonstrating how player behavior (like enemy kill counts or spending habits) can be captured in real-time and transformed into actionable visual data.

### 2.2 Objectives
- Implement a responsive 2D physics and combat engine using Pygame.
- Create an extensible Enemy and Boss framework.
- Develop a persistent database schema for character progression and session history.
- Integrate data analysis libraries (Pandas/Matplotlib) directly into the game UI.
- Deliver a polished aesthetic using high-quality pixel art and AI-generated environmental assets.

---

## 3. UML Class Diagram

The UML class diagram illustrates the inheritance structure between the base `Enemy` class and its specialized subclasses, as well as the relationship between the `System` controller and the various UI and Data modules.

**Attachment:** [UML Class Diagram](./uml.pdf)

---

## 4. System Architecture (Classes)

### Core Engine & Environment
- **System:** The central engine controller responsible for initializing the Pygame environment, managing resolution scaling, and providing global drawing utilities for text and shapes.
- **Level:** The primary game loop controller for stages. It manages the lifecycle of a level, including background rendering, enemy wave logic, collision detection, and victory/defeat transitions.
- **Background:** A utility class that facilitates the loading and retrieval of specific background image surfaces based on the active stage or menu state.

### Entity & Combat Logic
- **Player:** The core entity class representing the user. It handles state machine transitions for movement, jumping, dashing, and combat, while managing resource consumption (Health/Stamina).
- **Enemy:** The base class for all standard hostile AI, implementing decision-making logic for patrolling, player detection, and basic attack states.
- **Boss:** An advanced entity class inherited from Enemy that incorporates complex multi-phase combat logic and specialized state management for major encounters.
- **Individual Entities (Skeleton, Goblin, Mushroom, Big Mushroom, Flying Eye, Minotaur, Golem, Tarnished Widow):** Specialized subclasses that implement unique attribute values and frame-specific behaviors for their respective species.

### Data & Statistics System
- **GameDB:** The primary database abstraction layer that manages SQLite connections and provides methods for data retrieval, updates, and resetting tables.
- **PlayerStats:** A specialized database class used to track permanent character progression, including current health, power, critical chance, and accumulated points.
- **EnemyDefeated:** A data container class that records the specific number of kills for each species to provide detailed post-game metrics.
- **InGameTimeStamp:** A time-series database class that captures snapshots of player status (HP and Points) at fixed intervals for performance analysis.
- **PointUsage:** Tracks the distribution of spent points across different upgrade categories to analyze player investment trends.
- **Plotter:** The data visualization engine that utilizes Pandas and Matplotlib to transform SQL database records into visual PNG reports.

### User Interface & Graphics
- **Summary:** The reporting interface responsible for fetching generated visualizations from the Plotter and presenting statistical reports to the player.
- **Upgrade:** A persistent menu system where players interact with the database to exchange earned points for permanent attribute enhancements.
- **Selection:** A menu interface for stage navigation that manages level unlocking and environment initialization.
- **main_menu:** The entry-point interface that coordinates transitions between the game, upgrade shop, and summary screens.
- **Button:** A modular UI component that handles mouse collision detection and event-driven triggers.
- **HealthBar / StaminaBar / BossHealthBar:** Visual feedback components that render real-time attribute levels.

### Asset Management
- **SpriteLoader / Knight:** Specialized asset managers that handle the loading and slicing of player sprite sheets into indexed animation frames.
- **Enemy Sprite Loaders (Skeleton, Goblin, Mushroom, FlyingEye):** Handle coordinate mapping and frame slicing for standard enemy animations.
- **Boss Sprite Loaders (Minotaur, Golem, TarnishedWidow):** Manage high-resolution coordinate mapping for complex boss animation sets.
- **BossNameGennerator:** A utility that reads CSV data to procedurally generate unique names and titles for boss encounters.

---

## 5. Statistical Data

### 5.1 Data Recording Method

All gameplay data is recorded by the `StatsLogger` and database classes, saving information to an SQLite database (`histories.db`). Data is recorded through three main methods:
* **Event-Based Logging:** Data such as enemy kills or shop purchases are recorded immediately when the event occurs.
* **Periodic Snapshots:** The `InGameTimeStamp` class captures a snapshot of player health and points at regular intervals during a level to track survival trends over time.
* **Persistence:** Files are managed using the `sqlite3` library to ensure data accumulates across different sessions, allowing for long-term progression analysis.

### 5.2 Data Features

| Category | What It Records | Key Attributes |
|---|---|---|
| **Player Progression** | Permanent character stats | health, power, critical, stamina, stamina_regen, accumulative_points |
| **Combat Metrics** | Enemy defeat counts | skeleton, goblin, mushroom, big_mushroom, flying_eye, boss_kills |
| **Time-Series** | Real-time performance | health_at_time, points_at_time, time_stamp |
| **Economy** | Spending habits | points_spent_on_health, points_spent_on_power, points_spent_on_crit |

---

## 6. Changed Proposed Features (Optional)

- **Dynamic Boss Personalization:** Added a `BossNameGennerator` to provide randomized, unique titles for bosses, increasing variety in encounters.
- **Stamina-Based Action Economy:** Implemented a resource cost for dashing and attacking to add tactical depth and resource management to the combat loop.
- **Automated Visualization Suite:** Integrated a full `Plotter` engine to automatically generate visual PNG reports from the database instead of providing only raw numbers.

---

## 7. External Sources

### Sprites & Artwork
- **Fantasy Knight (Player):** [Itch.io - Fantasy Knight](https://aamatniekss.itch.io/fantasy-knight-free-pixelart-animated-character) by aamatniekss.
- **Monsters (Skeleton, Goblin, Mushroom, Eye):** [Itch.io - Monsters Creatures Fantasy](https://luizmelo.itch.io/monsters-creatures-fantasy) by LuizMelo.
- **Bosses (Minotaur, Golem):** [Itch.io - xzany](https://xzany.itch.io/) by xzany.
- **Tarnished Widow Boss:** [Itch.io - The Dark Series](https://penusbmic.itch.io/the-dark-series-the-tarnished-widow-boss) by Penusbmic.
- **Backgrounds:** AI-generated assets via [Google Gemini](https://gemini.google.com).

### Libraries & Frameworks
- **Pygame:** Core game loop and 2D rendering engine.
- **Pandas & NumPy:** Data analysis and numerical processing.
- **Matplotlib & Seaborn:** Generation of bar, pie, and line charts.
- **SQLAlchemy:** Database engine abstraction and connectivity.

### Music, Ambient
- **Ambients:** "Ashen Crown Dust" generated via [Suno AI](https://suno.com).
- **Boss Themes:** "Ashen Crown" generated via [Suno AI](https://suno.com).
- **UI Sound Effects:** `click.mp3` for button interactions.
- **Character Sound Effects:** `flesh_swing.mp3 / roll.mp3 / sword_swing.mp3 / walking_sound.mp3` for character actions.