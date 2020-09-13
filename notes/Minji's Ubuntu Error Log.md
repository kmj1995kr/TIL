## Minji's Ubuntu Error Log

**SSH Port Fowarding Connection refused**

![Screen Shot 2020-09-12 at 4.32.43 PM](/Users/minji/Library/Application Support/typora-user-images/Screen Shot 2020-09-12 at 4.32.43 PM.png)

**Cause**: Openssh wasn't installed properly (openssh-client was installed but openssh-server wasn't)

**How to fix it**:

1. Check with code `sudo service ssh status` to check if ssh is running properly
2. If ssh is not installed properly run the following codes:
   1. `sudo apt-get remove openssh-client`
   2. `sudo apt-get autoclean`
   3. `sudo apt-get install openssh-server`
3. Recheck the status of ssh to ensure that it's running: if it's installed but not running --> `sudo service ssh start`
4. Reboot and check whether ssh is running from the host