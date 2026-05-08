# Python Mini-Projects

A collection of basic and intermediate Python projects to practice programming concepts, including console applications, games, and database interactions.

## 📋 Table of Contents

- [Projects](#projects)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Projects

This repository contains the following mini-projects:

### 1. CRUD Console Application
**Location:** `CRUD_Console_Application/`

A console-based CRUD (Create, Read, Update, Delete) application for managing student records using Python and MySQL.

**Features:**
- Add new students
- Display student details
- Update student information
- Delete students
- MySQL database integration

**Requirements:** Python, MySQL Server, `mysql-connector-python`

**Run:** `python Main.py`

### 2. Perfect Guess Game
**Location:** `Perfect_Guess/`

A number guessing game where the player tries to guess a randomly generated number between 1 and 100.

**Features:**
- Random number generation
- User input validation
- Attempt counter
- Feedback for higher/lower guesses

**Requirements:** Python (built-in modules only)

**Run:** `python main.py`

### 3. Snake Water Gun Game
**Location:** `Snake_Water_Gun_Game/`

A console-based game similar to Rock-Paper-Scissors, implementing the Snake-Water-Gun rules:
- Snake drinks Water (Snake wins)
- Gun shoots Snake (Gun wins)
- Water rusts Gun (Water wins)

**Features:**
- Random computer choice
- User input for choices (s/w/g)
- Win/lose/draw determination
- Display of choices

**Requirements:** Python (built-in modules only)

**Run:** `python main.py`

## 📦 Requirements

- **Python 3.x** - All projects require Python 3.x
- **MySQL Server** - Required only for the CRUD Console Application
- **MySQL Connector** - Install via `pip install mysql-connector-python` for CRUD app

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KabileshwaranKabil/python-projects.git
   cd python-projects
   ```

2. For the CRUD application, install MySQL connector:
   ```bash
   pip install mysql-connector-python
   ```

3. Set up MySQL database (for CRUD app):
   - Install MySQL Server
   - Run the SQL script in `CRUD_Console_Application/sql-scripts.sql` to create the database and table

## 💻 Usage

Navigate to each project directory and run the respective main file as indicated above.

For detailed instructions on the CRUD application, refer to `CRUD_Console_Application/README.md`.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 M.Kabileshwaran 
