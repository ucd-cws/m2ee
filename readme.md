# Simple uploader to EE

A one click method to upload an asset to EarthEngine

This script will take an .img convert it to a geotiff and upload it to the CWS's shared EE account.


## Quick setup
- Install [Anacoda](https://www.continuum.io/downloads) Python 3.6 version -64 bit for single user
- Clone this repo 
- run `conda env create -f environment.yml`
- authenticate earthengine and gsutil
- update `config.py` for configuration paths for the bucket, assetid, path to source file
- change `run.bat` to match the anaconda install location `{anaconda}\Scripts\activate.bat`

### Authenticating Accounts

Make sure the virtual env is activated `activate m2eepy27` then run `earthengine authenticate`, sign into the shared cws EE account ucd.cws.ee.data@gmail.com in the browswer window that opens. Copy the auth code back to the command line. 

Run `gsutil config` and follow instructions to copy the auth code


### Detailed Setup Notes

- Install [Anacoda](https://www.continuum.io/downloads) Python 3.6 version -64 bit
- Create new env `conda create --name m2eepy27 python=2.7`
- Activate environment `activate m2eepy27`
- `pip install google-api-python-client`
- `pip install earthengine-api`
- `pip install gsutil`
- `conda install -c anaconda gdal=2.1.0`


## How to Use

1. Copy `.img` file to the `image` and rename to `upload2ee.img`
2. Double click `run.bat`. This will open a console window and run the python script. It converts the .img to geotiff and uploads it to a google bucket. This is then copied over to EarthEngine as an asset. Be patient - this process takes a few minutes!
3. Open https://code.earthengine.google.com/ and open the `Tasks` tab. You should see a task running for the image Asset Ingestion.
4. Asset will be available at `users/ucd-cws-ee-data/metric_upload_from_img`

Note: these instructions are for the default config settings. You might have changed something in `config.py`. 
