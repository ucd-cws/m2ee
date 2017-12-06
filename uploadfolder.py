# upload all img files that are in a folder to an earthengine image collection
import os
import glob
import img2ee
import config

# geotif folder
tif_folder = os.path.join(config.upload_folder, "geotiffs")

# make geotif folder if it doesn't already exist
if not os.path.exists(tif_folder):
    os.makedirs(tif_folder)

# get list of all img files in the uploads folder
imgs = [f for f in os.listdir(upload_folder) if f.endswith('.img')]

for i in imgs:
	print(i)
	full_img_path = os.path.join(upload_folder, i) # full path to the img raster
	filename, file_extension = os.path.splitext(full_img_path)
	full_geotiff_path = os.path.join(tif_folder, filename + '.tif') # construct the geotiff path
	base = os.path.basename(filename)
	asset_name = config.ee_ic + '/' + base # construct the name for the asset
	img2ee.main(image_file=full_img_path, geotif=full_geotiff_path, ee_asset_path=asset_name, bucket=config.bucket, public=False) # assets in imagecollections take sharing properties of the image collection