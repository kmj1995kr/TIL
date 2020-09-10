## Linux Commands

#### **Syntax**

- Meta Characters: characters that have innate meanings by default
  - To escape the meta character (to not use it with its meaning): use \
  - Ex. Want to query something that includes `'` in SQL
    - `content like '%John's name%'` --> wouldn't work because ' would close the query statement
    - To escape(use the meta character without its innate meaening), `content like '%John\'s name%`
  - Escape methods differ based on the language
  - Or there are some alternate rules dependiing on the language --> encoding
- #- root user
- $- regular user
- `>`: overwrite
- `>>`: append
- pipe (|): connecting two different programs

  - ex. `ls -l /etc | less` : show results from `ls -l /etc` in a less mode (being able to scroll up and down) 



#### Commands

- `cd`: change directory

  - `cd <folder_name>`: move folder_name
  - `cd` / `cd ~`: move to home directory
  - `cd ..`: move one level up
  - `cd -`: backspace

- `ls`: list

  - `ls` : show all unhidden files
  - `ls -a`: show all files including the ones that are hidden

- `touch`: make a new file

  - `touch <file_name`: make a new file named file_name

- `pip`

  - `pip install <package_name>`: install a new package named package_name
  - `pip uninstall <package_name>`: uninstall a new package named package_name
  - `pip freeze > requirements.txt`: make a new file called requirements.txt with all the requirements needed for the project
  - `pip install -r requirements.txt`: install all packages that are listed in requirements.txt

- `mv`: move file to a different directory

  - `mv <file_name_1> <file_name_2>`: change file_name_1 to file_name_2 (if "move to" location is set to be another file, it means to rename the file)

- `rm`: remove

  - `rm <file_name>` or `rm -rf <folder_name>`

- `rmdir`: remove directory

- `cat`: concatenate

  - `cat <function name>`: prints the function

- `vim`: terminal text editor

  - `vim <file_name>`: 
  - when exiting out of the vim page: esc + `:x` or `:wq`

- `echo`: print

  - `echo '# thi'1`

- `head`, `tail`: shows the first 10 or last 10 lines

- `less`: similar to more but supports other features such as moving with arrow keys

- `file`: show the file type

  - `file /etc/systemd/system.conf`

- `clear`: clears up the terminal window

- `./file_name`: executes the program line by line 

- Powering off the device

  - `poweroff`, `shutdown -P now`, `halt -p`, `init 0`
  - Shutting down at a designed time: `shutdown -r <time>`

- Rebooting the system

  - `reboot`, `shutdown -r now`, `init 6`

- Logout

  - `logout`, `exit`

- `history`: shows the history of all the commands used previously on this terminal window

  

  





