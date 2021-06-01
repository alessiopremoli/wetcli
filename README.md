
# WETCLI
## WET(ransfer)CLI

A very basic wip python :snake: cli for uploading files to WeTranser. Uses an headless browser to speed up the usual stuff you do when you generate a link by hand.

### PREREQUISITES
You need to have python (3.9.5) installed and ```geckodriver``` since the cli uses an headless Firefox to do its stuff.

### INSTALL
```bash
python3 -m venv env
source env/bin/activate

pip install -r requirements.txt

export PATH="$PATH:${PWD}"
ln -s ${PWD}/wetcli.py $HOME/bin/wetcli

``` 

### RUN
```bash
python wetcli.py
```

## NEXT STEPS:
- [x] make it an actual cli
- [x] files only in test_files
- [x] validate file size and unique name
- [ ] email mode?

