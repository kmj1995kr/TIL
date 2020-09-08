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