import subprocess
import gdal
import os
import config


def img2geotiff(src, dst):
	"""
	Use gdal utils to create a copy of the image file as a geotiff
	:param src: path to the source file (.img)
	:param dst: path to the new file (.tif)
	:return: geotiff
	"""
	#Open existing dataset
	src_ds = gdal.Open(src)

	#Open output format driver, see gdal_translate --formats for list
	format = "GTiff"
	driver = gdal.GetDriverByName(format)

	#Output to new format
	dst_ds = driver.CreateCopy(dst, src_ds, 0)

	#Properly close the datasets to flush to disk
	dst_ds = None
	src_ds = None


def uploadtobucket(bucket, filename):
	"""
	Uploads a file to a google cloud bucket
	:param bucket: path to the bucket
	:param filename: full path to the file to upload
	:return:
	"""
	print("Uploading {} to {}".format(filename, bucket))
	p = subprocess.Popen(['gsutil', 'cp', filename, bucket], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = p.communicate()
	if p.returncode != 0:
		print("{} \n {}".format(output, error))
	return


def cleanbucket(bucket):
	"""
	Removes all files in a bucket subfolder
	:param bucket: path to the bucket
	:return:
	"""
	bucketfolder = bucket + "/*"
	print("Removing all files in {}".format(bucketfolder))
	p = subprocess.Popen(['gsutil', 'rm', bucketfolder], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = p.communicate()
	if p.returncode != 0:
		print("{} \n {}".format(output, error))
	return


# transfer to ee asset
def buck2ee(bucket_file, assetid):
	"""
	Transfer a .tif that is in a bucket to google earth engine
	:param bucket_file: full path to the item in the google bucket
	:param assetid: full path for the destination EE asset (ie users/username/collection/assetname)
	:return:
	"""
	print("Copying {} to earthengine as {}".format(bucket_file, assetid))
	p = subprocess.Popen(['earthengine', 'upload', 'image',  "--asset_id=" + assetid,  bucket_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = p.communicate()
	if p.returncode != 0:
		print("{} \n {}".format(output, error))
	return


def rmasset(assetid):
	"""
	Removes an EarthEngine Asset
	:param assetid: full path for the destination EE asset (ie users/username/collection/assetname)
	:return:
	"""
	print("Deleting {}".format(assetid))
	p = subprocess.Popen(['earthengine', 'rm', assetid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = p.communicate()
	if p.returncode != 0:
		print("{} \n {}".format(output, error))
	return


def getMostRecentTask():
	"""
	Gets the most recent EE task
	:return:
	"""
	p = subprocess.Popen(['earthengine', 'task', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.stdout.seek(0)
	out = p.stdout.read()
	recent_task = out.splitlines()[0]
	print(recent_task)
	task_num = recent_task.split()[0]
	print(task_num)
	return task_num


def wait4task(task):
	"""
	Waits for a task to finish uploading the EarthEngine Asset
	:param task:
	:return:
	"""
	print("Waiting for Asset Ingestion {}".format(task))
	p = subprocess.Popen(['earthengine', 'task', 'wait', task], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = p.communicate()
	if p.returncode != 0:
		print("{} \n {}".format(output, error))
	return


def makeAssetPublic(assetid):
	"""
	Makes EarthEngine Asset public
	:param assetid: full path for the destination EE asset (ie users/username/collection/assetname)
	:return:
	"""
	print("Making asset publicly available")
	p = subprocess.Popen(['earthengine', 'acl', 'set', 'public', assetid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = p.communicate()
	if p.returncode != 0:
		print("{} \n {}".format(output, error))
	return


def main(image_file, geotif, ee_asset_path, bucket, public=True):

	# convert img to geotiff
	img2geotiff(image_file, geotif)

	# upload tif to bucket
	uploadtobucket(bucket, geotif)

	# remove any existing files for the asset path
	rmasset(ee_asset_path)

	# copy to earth engine
	basename = os.path.basename(geotif)
	file_in_bucket = bucket + "/" + basename
	buck2ee(file_in_bucket, ee_asset_path)

	if public:

		# wait for task to finish
		task = getMostRecentTask()
		wait4task(task)

		# change access to public
		makeAssetPublic(ee_asset_path)

	return

if __name__ == '__main__':
	main(image_file=config.input_image, geotif=config.geotif_image, ee_asset_path=config.ee_asset, bucket=config.bucket, public=True)
