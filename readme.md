
## Usage:

0. download chrome driver
Ref here https://chromedriver.chromium.org/downloads

1. Env setup
```
# Python ~= 3.8.8
pip install -r requirements
```
2. Set cfg
```
CHROMEDRIVER_PATH: absolute path of chromedriver
email: account email
passwd: account password
```

3. Start dump

```
python dump_from_1st_page.py
# resume: no need to login again (use coookie)  default is False
```

## Note:
1. chromdriver version should match with chrome desktop.