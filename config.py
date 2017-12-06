# config setting for m2ee
import os

# current wd
dir_path = os.path.dirname(os.path.realpath(__file__))

# path to google bucket
bucket = "gs://earth-engine-staging"

# path to ee_asset to overwrite
ee_asset = "users/ucd-cws-ee-data/metric_upload_from_img"

# path to input file (.img) and converted geotiff (.tif)
input_image = os.path.join(dir_path, "image", "upload2ee.img")
geotif_image = os.path.join(dir_path, "image", "upload2ee.tif")

# path to earthenginge image collection
ee_ic = "users/ucd-cws-ee-data/kern/imageuploads"

# folder to upload
upload_folder = os.path.join(dir_path, "uploads")