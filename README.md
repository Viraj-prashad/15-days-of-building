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

### Project Overview
A command-line file organizer built using Python.  
The tool scans a source directory, categorizes files based on their extensions, and either **copies or moves** them into organized folders.

This project focuses on:
- Safe filesystem operations
- Clean CLI design
- Incremental feature building
- Practical use of Git during development

---

### ⚙️ Features

- Organizes files into categories:
  - Images
  - Documents
  - Videos
  - Other
- User can choose between **copy** or **move**
- Skips files if they already exist in the destination
- Creates folders automatically if missing
- Non-destructive and safe by default

---

### 🛠️ How to Run the File Organizer

1. Clone the repository:
   ```bash
   git clone https://github.com/kei-araya/15-days-of-building.git
   ```

2. Navigate to the project folder:
   ```bash
   cd 15-days-of-building/project2_file_organizer
   ```

3. Run the script:
   ```bash
   python organize.py
   ```

4. Follow the prompts:
   - Enter the source directory path
   - Enter the destination directory path
   - Choose copy or move

### What I Learned
- Working with the filesystem using os and shutil
- Safely handling files and directories
- Designing CLI tools with user input
- Handling edge cases to avoid data loss
- Structuring projects and commits cleanly with Git

