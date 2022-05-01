
Usage:
0. download chrome driver
Ref here https://chromedriver.chromium.org/downloads

1. Env setup
```
pip install -r requirements
source ./envsetp.sh
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
```

Note:
1. chromdriver version should match with chrome desktop.