### Working on Multiple Devices on My Own

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



### Working with Others

**Managing Remote Server**

- Creating a new remote branch
  - At first, branches are created local, so it needs to be pushed
  - `git

**Working with Branches**

- By default, master branch is created and the repository will be connected to that branch
- Creating a branch is creating your own version of the file
- Showing all branches: `git branch`
- Create a branch
  - Commit all files
  - Create a new branch: `git branch <branch_name>`
  - Switch to the new branch that I created
    - `git checkout <branch_name>`
    - `git switch <branch_name>`
  - Create a new branch and switch to it
    - `git checkout -b <branch_name>`

- Push to a branch
  - Make sure I'm currently checked out to the branch that I want to work in
  - `git push origin <branch_name>`
  - Changes that are committed under my branch can't be pushed to master ()
- Delete a branch
  - `git branch -d <branch_name>`
- Merge branches
  - Go to the branch to be merged (usually master): `git checkout master`
  - Merge them: `git merge <branch_name_to_merge>`
  - After merging on github.com, you have to `git pull` from Pycharm in order to have the most up to date changes from the merge
- Resolving conflicts
  - Conflicts happen when the codes are different in the same file in different branches / devices
    - (e.g.) models.py in master branch different from model.py in minji branch
  - When the conflict happens, on Pycharm
    - Rightclick --> resolve conflicts
- Comparing versions: `git diff HEAD`



When pulling a from a remote when :x

git remote -v - shows all the servers that the project is connected to

- origin is usually the name of the master



### Contribute to an opensource repository 

- Go to github page url
- Click "fork"
- Clone the repository that I just forked
- Make changes to the cloned copy of the repository
- Commit and push
- Create a pull request from github website to the original github source code



### Starting a Django Project

**Project를 처음 시작하는 사람**

1. 프로젝트 폴더 만들기: `mkdir <project_name>	`

2. venv 만들기: `python -m venv venv`
3. Activate venv (가상환경 activate): `source venv/Scripts/activate`
4. Pip list 체크하고 필요한 패키지 설치: `pip list` --> `pip install django django_extensions ipython`
   1. django
   2. django_extensions
5. Package requirement 만들기: `pip freeze > requirements.txt`
6. Django project 시작하기: `django-admin startproject <project_name> .`
7. Ignore할 파일 목록 작성하기: `touch .gitignore`
8. PyCharm으로 프로젝트 실행
9. Configuration 바꾸기
   1. Settings --> interpreter 검색 --> Project Interpreter 선택
   2. 만약 자동으로 configuration이 생긴다면: 그 configuration 선택
   3. 만약 안생긴다면: + 버튼 누르기 --> project_folder/venv/Scripts/python.exe 선택
10. gitignore.io로 가서 ignore 파일 만들기
    1. 프로젝트에서 쓰는 언어 전부 다 검색
    2. 검색해서 나오는 파일 .gitignore에 복붙
    3. 맨위에 .idea/ 추가
11. 만약 git bash 설정이 안되있다면 Settings → tools → terminal → shell path → bin/bash로 바꾸기 (windows에서는 program_files/git/bin/bash)
12. 최초 master commit 하기 (아직까지는 로컬인 상태)
    1. `git add .`
    2. `git commit -m "init"`
13. github.com 가서 새로 repository 만들기
14. remote repository 설정하기:` git remote add origin <url>` (url이 https인지 확인)
15. Master repository 로 push 하기:  `git push origin master`
    1. 만약 `git push -u origin master` 하면 default를 origin master 로 push하게 설정하는 것이기 때문에 `git push` 까지만 쳐도 자동으로 origin master로 push가 됨
16. Setting --> manage access --> invite collaborator





 

**Project에 Collaborator로 초대받은 사람**

1. Project Clone하기: `git clone <path_url>`
2. Venv 설정하기: `python -m venv venv`
3. Configuration 바꾸기
   1. Settings --> interpreter 검색 --> Project Interpreter 선택
   2. 만약 자동으로 configuration이 생긴다면: 그 configuration 선택
   3. 만약 안생긴다면: + 버튼 누르기 --> project_folder/venv/Scripts/python.exe 선택
4. Requirement 다 설치하기: `pip install -r requirements.txt`



이제부터는 공통

- 내 branch 만들기: `git checkout -b <branch_name>`
- 만약에 다른 앱을 만들고 있을 경우: `



Shell 에서 import 다 할수 있는거



class User(AbstractUser):

followers: models.ManyToManyField(settings.AUTH_USER_MODEL)