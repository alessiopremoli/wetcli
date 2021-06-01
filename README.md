
# WETCLI
## WET(ransfer)CLI

A very basic python :snake: cli for uploading files and directiory using WeTranser. Runs an headless browser to speed up the usual stuff you do when you generate a link by hand.

### PREREQUISITES
You need to have python (3.9.5) installed and ```geckodriver``` since the cli uses an headless Firefox to do its stuff.

### INSTALL
```bash
python3 -m venv env
source env/bin/activate

pip install -r requirements.txt

echo $(pwd)/env/bin/python
# copy the result on the first line of the wetcli.py script, to have a working shebang

export PATH="$PATH:${PWD}"
ln -s ${PWD}/wetcli.py $HOME/bin/wetcli

``` 

### USAGE
Use the option `-d` to upload a directory
```bash
wetcli -d my_awesome_directory
```
Use the option `-f` to upload a single file:
```bash
wetcli -f my_awesome_file.txt
```
In both cases the cli will sanitize the files (excluding unwanted files like .DS_Store), check for duplicates and that the total sum is below 2GB. You can also add a custom message using the `-m` option:
```bash
wetcli -f my_awesome_file.txt -m "Here my awesome file"
```


## NEXT STEPS:
- [x] make it an actual cli
- [x] files only in test_files
- [x] validate file size and unique name
- [ ] a proper installer
- [ ] email mode?

