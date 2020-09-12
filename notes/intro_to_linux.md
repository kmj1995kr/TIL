## Intro to Linux

#### Important Concepts & Terminologies

- **Linux**: Free & widely distributed Unix system
- **Kernel**: The kernel is a [computer program](https://en.wikipedia.org/wiki/Computer_program) at the core of a computer's [operating system](https://en.wikipedia.org/wiki/Operating_system) with complete control over everything in the system
- **Ubuntu**: Linux distribution based on Debian mostly composed of free and open-source software
- **Kubuntu**: Official flavour of the Ubuntu operating system that uses the KDE Plasma Desktop instead of the GNOME desktop environment

#### Snapshot: Why use snapshot?

- To save different versions of the same application to run tests in parallel
- To go back to older versions when things don't work out in the system
- To save records of the version history for troubleshooting

#### **Taking snapshots**

- VirtualBox 관리자페이지 에서 원하는 서버 클릭
- 찍기 버튼을 눌러서 스냅샷을 찍을 수 있고, 복구로 이전 버전 복구 가능



#### How to Read File Information

- Use command `ls -l` to view file information

![img](https://lh5.googleusercontent.com/Uhy85PvSOarcH0YG_NXlsie_PrxmkhNDOoPZqs7UhCsKgG5q6IE820Tpg_iDsRfRgit3-UFaygYZ1ZhlY6h2h1qeVIZGUEZaY0KAjmlpI8c5Vlm8mC77CX8ssdUl4Qg6UEdUDugZ) 



![img](https://lh4.googleusercontent.com/Po3AnKBz1OxMHi_o8uaNiQ2FxKm00QY4KFBZ7CGCRSK2JCD2TyaJbaLJv8Ns5FFpaxtpn4So9SSdhQQS1AxSTT-2Xad9j0AkFdeYzFbUSNSEX9lE1C9df8n1PW5Xr3Ty5sVknEzm)

**File Types**

- d: directory
- -: regular file
- b: block device(hard drive, USB, CD/DVD)
- c: input device(keyboard, mouse, printer)
- l: link



**Permission Types**

- r: read-only
- w: read & write
- x: can execute/operate



#### Virtual Console

- Virtual console is like having a virtual monitor
- Ubuntu has 7 consoles by default
- Using the virtual console `ctrl + alt + <F1~F7>`



#### Run Level

- Number that comes after init - indicates the running status of the system
- To change the run level ex) `ln -sf /lib/systemd/system/multi-user.target /lib/systemd/system/default.target` --> change the run level from multi-user to default



![img](https://lh6.googleusercontent.com/jQauZ0LYfiI6InJGEJW1qA988WaD1oC80TWwbHQ_WMvRonnxoufqrxZBsAhfyjvoqTzvGVhkJ7JVMHa3OXxlgH_BXwAw-Yscx6C9iejix9G1TvF-6dlRlC0SFmoHrMqYN9z1IJIn-5w)



#### Mount

- Mount is like plugging in a CD-ROM into the disk, since there is no physical location to "plug in" the CD-ROM, mount works as a function to execute what's in the CD

**Mount CD-ROM to a specific location**

1. Using VirtualBox, insert a CD-ROM --> which can be found under /dev/cdrom
2. Mount this CD-ROM: `mount <mount_from> <mount_to>` --> `mount /dev/cdrom /mnt/cdrom `
3. Use the command `mount` to check the list of all mounted items
4. Unmount this CD-ROM: `umount <mounted_location>` --> if the location is busy, use `umount -l <mounted_location>` / or move to a different directory where the cdrom is not mounted and try the command again

**Create an ISO file**

1. Check whether genisoimage package exists: `dpkg --get-selections genisoimage`
2. Using genisoimage package create an iso file: `genisoimage -r -J -o <file_name.iso> <directory_path>`
   - Ex. `genisoimage -r -J -o boot.iso /boot`
3. Try mounting the ISO file: `mount -o loop boot.iso /mnt/iso`
4. Unmount: `umount /mnt/iso`



#### VI Editor

- vi editor is included by defeault in all unix, linux systems
- gedit is a VI editor that is provided in X Window

**To run python codes on terminal:**

- Default shell does not support python
- Run python with `python3 -i <file_name>`

