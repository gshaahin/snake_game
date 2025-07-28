# 🐍 Snake Game

<div align="center">

![Snake Game](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

*A classic Snake game built with Python and the Turtle graphics library*

</div>

---

## 📋 Quick Navigation

- [🎮 Features](#-features)
- [🚀 Installation](#-installation)
- [🎯 How to Play](#-how-to-play)
- [📁 Project Structure](#-project-structure)
- [🛠️ Development](#️-development)
- [🚀 Future Features](#-future-features)

---

## 🎮 Features

| Feature | Description |
|---------|-------------|
| 🎯 **Classic Snake Gameplay** | Control a snake using arrow keys to eat food and grow |
| 📊 **Score Tracking** | Real-time score display with persistent high score tracking |
| ⚡ **Collision Detection** | Game ends when snake hits walls or itself |
| 🎨 **Smooth Graphics** | Built with Python's Turtle graphics for smooth animations |
| 💾 **High Score Persistence** | High scores are saved between game sessions |
| 🎮 **Responsive Controls** | Intuitive arrow key controls with proper movement constraints |

---

## 🚀 Installation

### 📋 Prerequisites
- ✅ Python 3.x (Python 3.6 or higher recommended)
- ✅ No additional packages required (uses built-in `turtle` library)

### ⚙️ Setup
1. **Clone or download this repository**
2. **Navigate to the project directory:**
   ```bash
   cd "Snake game"
   ```
3. **Run the game:**
   ```bash
   python main.py
   ```

---

## 🎯 How to Play

### 🎮 Controls
| Key | Action |
|-----|--------|
| ⬆️ **Up Arrow** | Move snake upward |
| ⬇️ **Down Arrow** | Move snake downward |
| ➡️ **Right Arrow** | Move snake right |
| ⬅️ **Left Arrow** | Move snake left |

### 📜 Game Rules
1. 🎯 **Objective**: Eat the red food to grow your snake and increase your score
2. 🎮 **Movement**: Use arrow keys to control the snake's direction
3. 📈 **Growth**: Each time you eat food, your snake grows longer
4. ⚠️ **Collision**: Avoid hitting the walls or your own tail
5. 🏆 **Scoring**: Each food eaten adds 1 point to your score
6. 🏅 **High Score**: Your highest score is saved and displayed

### ❌ Game Over Conditions
- 🧱 Snake head collides with the wall boundaries
- 🐍 Snake head collides with any part of its own body

---

## 📁 Project Structure

```
Snake game/
├── 🎮 main.py              # Main game loop and entry point
├── 🐍 snake.py             # Snake class with movement and growth logic
├── 🍎 food.py              # Food class for random food placement
├── 📊 scoreboard.py        # Score tracking and display functionality
├── 💾 highest_score.txt    # Persistent high score storage
├── 📖 README.md           # This file
└── 🚫 .gitignore          # Git ignore file
```

---

## 🔧 Technical Details

### 🏗️ Core Components

#### 🎮 `main.py`
- 🚀 Game initialization and setup
- 🔄 Main game loop with collision detection
- 🖥️ Screen configuration and event handling

#### 🐍 `snake.py`
- 🐍 `Snake` class with movement logic
- 📏 Segment management and growth mechanics
- 🎯 Direction control with collision prevention

#### 🍎 `food.py`
- 🍎 `Food` class for random food placement
- 🔄 Automatic refresh when eaten

#### 📊 `scoreboard.py`
- 📊 `Scoreboard` class for score tracking
- 💾 High score persistence using file I/O
- ⏱️ Real-time score display

### ⭐ Key Features
- 🏗️ **Object-Oriented Design**: Clean separation of concerns with dedicated classes
- ⚡ **Collision Detection**: Precise collision detection for walls and self
- 💾 **Score Persistence**: High scores saved to `highest_score.txt`
- 🎬 **Smooth Animation**: 0.1-second delay for smooth gameplay
- 🧱 **Boundary Management**: Proper game boundaries and collision detection

---

## 🎨 Game Specifications

| Specification | Details |
|---------------|---------|
| 🖥️ **Game Window** | 600x600 pixels with black background |
| 🐍 **Snake** | White square segments, 20-pixel movement distance |
| 🍎 **Food** | Red circular food, randomly placed |
| 📊 **Score Display** | White text at top of screen |
| ⚡ **Game Speed** | 0.1-second delay between moves |

---

## 🛠️ Development

### 📋 Requirements
- 🐍 Python 3.x
- 🎨 Turtle graphics library (built-in)

### 🚀 Running the Game
```bash
python main.py
```

### 🔧 Modifying the Game
- ⚡ Adjust game speed by changing the `time.sleep()` value in `main.py`
- 📏 Modify snake movement distance in `snake.py` (`MOVE_DISTANCE`)
- 🍎 Change food appearance in `food.py`
- 📊 Customize scoring system in `scoreboard.py`

---

## 🚀 Future Features

Here are some exciting features that could be added to enhance the game:

| Feature | Description |
|---------|-------------|
| ⚡ **Power-ups** | Speed boost, invincibility, or score multipliers |
| 🔊 **Sound Effects** | Eating sounds, collision sounds, and background music |
| 👥 **Multiplayer** | Local two-player competitive mode |
| ⚙️ **Settings Menu** | Adjustable game speed, colors, and controls |
| 🎯 **Difficulty Options** | Easy, normal, and hard modes |

---

## 📝 License

This project is open source and available under the **MIT License**.

---

## 👨‍💻 Author

<div align="center">

**Shahin Gholoubi** - Snake Game Developer

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)

</div>

---

<div align="center">

### 🎮 **Ready to play? Run the game and enjoy!** 🐍

```bash
python main.py
```

**Happy Gaming! 🐍🎮**

</div> 