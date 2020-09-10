## Intro to Linux

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

1. 

#### VI Editor

- vi editor is included by defeault in all unix, linux systems
- gedit is a VI editor that is provided in X Window

**To run python codes on terminal:**

- Default shell does not support python
- Run python with `python3 -i <file_name>`

