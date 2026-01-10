# 15 Days of Building

This repository documents my 15-day learning sprint where I:
- Strengthen Python fundamentals through real projects
- Learn Git & GitHub by using them daily
- Build a public portfolio of work and learning progress
- Move toward building software + hardware systems

---

## 📁 Repository Structure

- Each **project** has its own folder  
- A project may span **multiple days**  
- Daily progress and learning are documented here

---

## Day 1 — CLI Greeting Tool (Python)

### Overview
A simple command-line greeting tool built to practice:
- Python basics
- Project structure
- Git & GitHub workflow

### What I Learned
- Using functions properly
- The purpose of `if __name__ == "__main__"`
- Initial Git workflow (`init`, `add`, `commit`, `push`)

---

## Day 2 — CLI File Organizer (Python)

### Overview
A command-line file organizer that scans a source directory, categorizes files based on their extensions, and organizes them into folders.

### Features
- Categorizes files into Images, Documents, Videos, and Others
- Supports copy or move operations
- Skips files that already exist in the destination
- Creates required folders automatically
- Safe and non-destructive by default

### ▶️ How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/kei-araya/15-days-of-building.git
   ```
2. Navigate to the file organizer project:
   ```bash
   cd 15-days-of-building/project2_file_organizer
   ```
3. Run the script:
   ```bash
   python organize.py
   ```

### What I Learned
- Working with the filesystem using `os` and `shutil`
- Handling user input safely
- Structuring CLI tools
- Incremental feature development using Git

---

## Day 3 — Code Refactoring & Cleanup

### Overview
Focused on improving the internal structure of the file organizer project.

### What I Did
- Refactored repeated logic into reusable functions
- Improved readability and maintainability of the code
- Separated concerns for better extensibility

### What I Learned
- Importance of clean code
- How refactoring improves scalability
- Writing functions with clear responsibilities

---

## Day 4 — CLI Task Manager (Core Features)

### Overview
Built a command-line task manager application using Python, focusing on core application logic and safe user interaction.

### What I Did
- Designed a command-driven CLI interface
- Implemented task creation, viewing, completion, and deletion
- Used dictionaries to manage structured in-memory state
- Added input validation and error handling
- Generated unique task IDs for reliable task management

### What I Learned
- Managing application state in memory
- Parsing and validating user input
- Working with dictionaries and nested data structures
- Writing defensive code to prevent runtime crashes
- Designing CLI tools with usability in mind

---

## Day 5 — Persistent Storage with JSON

### Overview
Enhanced the CLI task manager by adding persistent storage so tasks are retained across program runs.

### What I Did
- Designed a JSON-based data storage format
- Implemented loading and saving of application state
- Handled first-run and corrupted-file edge cases
- Converted data safely between Python and JSON formats
- Ensured tasks are saved cleanly on program exit

### ▶️ How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/kei-araya/15-days-of-building.git
   ```
2. Navigate to the task manager project:
   ```bash
   cd 15-days-of-building/project3_task_manager
   ```
3. Run the program:
   ```bash
   python manage.py
   ```

### What I Learned
- File I/O in Python
- JSON serialization and deserialization
- Handling type differences between JSON and Python
- Designing reliable program startup and shutdown flows
- Understanding persistence as a core application concept

---

## Goals Going Forward

- Build more advanced Python projects
- Explore backend development concepts
- Integrate software projects with hardware systems
- Continue strengthening problem-solving and system design skills
