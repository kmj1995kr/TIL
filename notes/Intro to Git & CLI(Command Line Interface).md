# Intro to Git & CLI(Command Line Interface)

#### Why Use Git?

- Version control
  - Commit - saving and leaving a message
  - Semantic versioning - there are some set conventions to what counts as major / minor / patch level changes
- til (today I learned): a folder to manage concepts that I've learned

#### **Command Line Basic**

- `>`: overwrite
- `>>`: append
- Cd: change directory
  - `cd <folder_name>`: move folder_name
  - `cd` / `cd ~`: move to home directory
  - `cd ..`: move one level up
  - `cd -`: backspace
- ls: list
  - `ls` : show all unhidden files
  - `ls -a`: show all files including the ones that are hidden
- touch: make a new file
  - `touch <file_name`: make a new file named file_name
- pip
  - `pip install <package_name>`: install a new package named package_name
  - `pip uninstall <package_name>`: uninstall a new package named package_name
  - `pip freeze > requirements.txt`: make a new file called requirements.txt with all the requirements needed for the project
  - `pip install -r requirements.txt`: install all packages that are listed in requirements.txt
- mv: move
  - `mv <file_name_1> <file_name_2>`: change file_name_1 to file_name_2
- cat: concatenate
  - `cat <function name>`: prints the function
- echo '# thi'



#### **Setting up Git on Pycharm**

- Settings → tools → terminal → shell path → bin/bash로 바꾸기 (windows에서는 program_files/git/bin/bash)
- User Setting: `git config --global` or `git config --local` if the changes are local
  - `git config --global user.name "<my_name>"`
  - `git config --global user.email "<my_email>"`



#### Basic Concepts and Commands with Git

- **Showing any changes in Git**: `git status`
- **Adding new/deleted/modified files** to be tracked (to the repository): `git add <file_name>`
  - Only the files / changes that have been added will be committed when we use "commit" command
- **Commit**- officially saving changes that I made into (taking a picture): `git commit -m "<commit_message>"`
- **Log** - showing the history of commits: `git log`
- Quit(q) - quitting during git commands 

- Ignoring files 
  - `touch .gitignore`
  - To know what to ignore: use www.gitignore.io

```python
#inside gitignore

.idea/
```



#### Setting up a Development Environment for Collaboration

- Create a virual environment venv
  - Create a new virtual environment: `python -m venv venv`
  - Direct the repository to this venv -- *this is not needed when the setting is done in the interpreter setting using Pycharm*
    - For Windows: `venv\Scripts\activate`
    - For Mac / Linux: `source venv/bin/activate`
- `git remote add origin <my_repo_url>`
- Checking the connection to the remote repo: `git remote -v`
- Creating



#### Getting Started with Git (Step by Step Creating a New Project)

1. Make a project folder: `mkdir <master_folder_name>`
2. Write a **.gitignore file** inside the project file: `touch .gitignore`
   1. Go to gitignore.io
   2. Select all the languages and app that I will be using in the project
   3. Copy and paste the entire thing into .gitignore file (+add .idea/ if not added already)
3. Create a virtual environment and activate
   1. `python -m venv venv`
   2. for windows: `source venv/Scripts/activate`
   3. for mac: `source venv/bin/activate` -- *this is not needed when the setting is done in the interpreter setting using Pycharm*
4. Start a django project: `Django-admin startproject <project_name> .`
5. Open project with PyCharm
6. Initialize git: `git init`
7. Create a README.md file: `touch README.md`
8. Install packages needed
9. Write requirements.txt: `pip freeze > requirement.txt`
10. Add and commit to the local git repository
    1. git add .
    2. git commit -m "commit_message"
    3. git push origin <project_name> // not sure if this is right?
11. Create a remote repository on git: typically use github.com
12. Add and commit changes to the remote git repository
    1. Connect to a remote repository: ``git remote add origin <link>``
    2. Push to origin:master: `git push origin master`

