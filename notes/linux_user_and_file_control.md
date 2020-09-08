## Linux User & File Control

#### Types of Users

- All users must belong to one of more user groups 
  - **RBAC**: Role based access control (역할 기반 접근 통제)
- **Super User** has all permissions, including creating users and conducting other operations
  - If there are too many super users, the system is exposed to security risks
- *Look up other roles on Google as well*



#### Viewing & Modifying User/Group Information

- `cat /etc/passwd`: User account information is stored in this file
  - Each row is consisted of: <user name>:<password>:<user ID>:<user group>:<other info>:<home directory>:<shell>
  - When password is all displayed as x, it's shadowed --> not openly displayed in the file
- `cat /etc/group`: Group related information is store in this file
  - Each row is consisted of: <group name>:<password>:<group ID>:<sub user groups>
- `groupadd`: adds a new group
- `adduser`: Adduser: adding to users and their information to /etc/passwd, /etc/shadow, /etc/group
  - When adding a user, if group is not specified, Ubuntu automatically creates a user group after the name of the user
    - This is inefficient because you don't need a group per user
  - Therefore, it is usually recommended to create user groups first, then assign users into the groups as needed
- `passwd`: Setting password: setting initial password for the user
- `usermod`: Changing attributes of a user
  - Ex. `usermod --shell /bin/csh cookuser1`: changes cookuser1's default shell to /bin/csh
- `userdel`: Deleting users
- `change`: Command that requires users to change password periodically
- `groups`: shows the group information that the user belongs to
- `whoami`: shows who I am./



#### Creating Groups & Users Exercise

- Building skeleton: `/etc/skel` file modify
  - Files that are in `/etc/skel` are automatically copied to user's home directory when a new user is created
  - When there's info that needs to be distributed to all users, /etc/skel



#### File Control Settings

**Changing Permission Setting**

- Symbolic Method
- Access can only be passed down (ex. from root --> regular user)
- `chmod`: changes permission ot the file
  - Ex. `chmod 777 mydata.txt`: in binary form it's 111 111 111 (rwx rwx rwx) --> all users can read, write, and execute
  - Ex. `chmod u+x mydata.txt`: gives execution permission to mydata.txt to all owners

| Symbol |  Function  | Description  |
| :----: | :--------: | :----------: |
|   u    |    Who     | User (Owner) |
|   g    |    Who     |    Group     |
|   o    |    Who     |    Ohters    |
|   a    |    Who     |     All      |
|   =    |  Operator  |    Assign    |
|   +    |  Operator  |     Add      |
|   -    |  Operator  |    Remove    |
|   r    | Permission |     Read     |
|   w    | Permission |    Write     |
|   x    | Permission |   Execute    |

- `chown`: changes the owner of the file
  - Ex.`chwon`: `chown ubuntu.ubuntu sample`: sample file을 ubuntu 그룹에 있는 ubuntu 사용자에게 권한 넘기기
  - Although ubuntu is the owner, the user still can't access the file because the file is under the root directory
- Change the location of the file so that it is accessible to ubuntu user
  - `mv ./sample -ubuntu`: move ./sample to ubuntu file



#### Link

- **Hard link**: points to the esame inode block as the original file
  - Ex. `ln <file_name> hardlink`: link <file_name> as a hard link and name the file as hardlink
- **Symbolic link**: points to a diffrent inode that points to the original file as the original inode
  - Ex. `ln -s <file_name> softlink`: link <file_name> as a soft link and name the file as softlink
    

![img](https://lh3.googleusercontent.com/bxt9mcAD_gHnDMXlw_6HpD9fpFJLiQkzFgFBcuKQj5ymCEatgmsP5QCLmLRrJ1V8AhYglFWNaxMsGc4izXQiKL_UPix8D_26quZAfmYDtiDPKkqxD2NvIW7MmesyTzlNyJZuazQM9zY)



#### Difference between hard & soft link

| Scenario                                                     | Hard Link                        | Soft Link                                  | Why?                                                         |
| ------------------------------------------------------------ | -------------------------------- | ------------------------------------------ | ------------------------------------------------------------ |
| Move the original file to a **different location**           | Still shows the original content | Link is broken (can't locate the original) | inode is what helps locate the location of the file, but since<br />symbolic link uses a different inode,<br />it can no longer locate the original file |
| Move original file **back to the original location**         | No change                        | Link comes back again                      |                                                              |
| Change the **file content**                                  | Content changes                  | Content changes                            |                                                              |
| Move the original file to a different location then change the content then move back | Shows the updated content        | Shows the updated content                  | Although the change happened when the link was broken, when it comes back again, it points to the updated original content |
| Move the original file to a different location and then make a new file with the same name is the current directory | Shows the original content       | Shows the new content with the same name   | Hardlink: locates the file by its file inode (id)<br />Softlink: locates the file by its location + name --> since the new file has the same location + name, now it refers to the new file |



#### Process

**Process**: A process is an active program i.e a program that is under execution

- **Foreground Process**: A *foreground process* is any command or task you run directly and wait for it to complete.
  - Process ID

- **Background Process**: Unlike with a foreground process, the shell does not have to wait for a *background process* to end before it can run more processes
  - Job ID

- **Parent Process**
- **Child Process**



#### Commands related to processes

- `ps`: checks the status of the current process
  - `ps -ef | grep <desired_process>`: process number and status
- `kill` or `ctrl + c`: force quits the process

- `pstree`: 
- Switch between processes (back --> front, front --> back)
  - `ctrl + z`: pauses the process temporarily
  - `bg`: turns the process into a background process
  - `jobs`: shows all the processes that are running on the background --> we can locate **job_id** from here
  - `fg <job_id>`: brings the process <job_id> onto foreground
- `<app_name> &`: initially runs the program in the background
  - Can run commands in the terminal while running the program



#### Service

- **Service(Daemon)**: processes that are running on the background that is not visible to the users on a GUI --> always running
  - `systemctl start/stop/restart <service_name>`: starts, stops, restarts the service
- **Socket**: Similar to service but runs only when it's requested externally
  - run by systemd
  - All script files releated to sockets are in /lib/systemd/system with an extension of .socket

