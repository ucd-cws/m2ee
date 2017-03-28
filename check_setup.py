import subprocess

# first let's check that earthengine cmd is working
try:
	p = subprocess.Popen(['earthengine', 'ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	output, error = p.communicate()
	if p.returncode != 0:
		print("{} \n {}".format(error, "Run earthengine authenticate!"))
except WindowsError as e:
	print(e)
	print("Virtual Environment is not activated - shell cannot find earthengine")


# check gsutil
try:
	p = subprocess.Popen(['gsutil', 'ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	output, error = p.communicate()
	if p.returncode != 0:
		print("{} \n {}".format(error, "Run gs authenticate!"))
except WindowsError as e:
	print(e)
	print("Virtual Environment is not activated - shell cannot find gsutil")