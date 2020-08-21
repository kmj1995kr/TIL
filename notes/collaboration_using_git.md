#### Working on Multiple Devices on My Own

1. Make sure to add, commit, push for all the changes that I made
2. On a different device, make sure to `git pull` first



**Mistakes can happen...**

refer to this file: https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things

- When the commit message was written wrong
- When wrong files were brought onto the stage (either not added, or extra files were brought onto the stage)
- When files were overwritten by accident
  - `git checkout -- board.py`: retrieves the last commited version (assuming that the file was committed)
  - `git restore -- board.py` 

When following this message, 



**Working with Branches**

- By default, master branch is created and the repository will be connected to that branch
- Creating a branch is creating your own version of the file
- Showing all branches: `git branch`
- How to create a branch
  - Commit all files
  - Create a new branch: `git branch <branch_name>`
  - Switch to the new branch that I created
    - `git checkout <branch_name>`
    - `git switch <branch_name>`







When pulling a from a remote when :x

