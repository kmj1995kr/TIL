## Linux: Packages & System Recovery

- dpkg
  - Has problems when installing packages with dependencies
- apt-get



1. Download a package
   - `wget <package_download_url>`: downloads the package using the link
2. Install the package -- using dpkg
   - To check whether the package has been installed or not: `dpkg -l <package_name>`
   - To check info about the package: `dpkg --info <package_name_with_version>`
   - To install the package: `dpkg -i <package_name_with_version>`
   - To uninstall the package: `dpkg -r <package_name>`

3. Install the package with dependecies -- using dpkg
   - Would have to manually download all the packages that this package depends on --> not ideal (X)
4. Install the package using apt-get



#### System Recovery

recover system password