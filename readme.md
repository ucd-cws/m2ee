# Simple uploader to EE

## Setup

- Install [Anacoda](https://www.continuum.io/downloads) Python 3.6 version -64 bit
- Create new env `conda create --name m2eepy27 python=2.7`
- Activate environment `activate m2eepy27`
- `pip install google-api-python-client`
- `pip install earthengine-api`
- `pip install gsutil`
- `conda install -c anaconda gdal=2.1.0`


or run `conda env create -f environment.yml` from this repo

### Authenticating Accounts

Make sure the virtual env is activated `activate m2eepy27` then run `earthengine authenticate`, sign into the shared cws EE account ucd.cws.ee.data@gmail.com in the browswer window that opens. Copy the auth code back to the command line. 

Run `gsutil config` and follow instructions to copy the auth code


