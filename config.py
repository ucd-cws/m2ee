# config setting for m2ee
import os

# current wd
dir_path = os.path.dirname(os.path.realpath(__file__))

# path to google bucket
bucket = "gs://bucket-name/subfolder"

# path to ee_asset to overwrite
ee_asset = "users/username/collection/asset-name"

# path to input file (.img) and converted geotiff (.tif)
input_image = os.path.join(dir_path, "image", "upload2ee.img")
geotif_image = os.path.join(dir_path, "image", "upload2ee.tif")
