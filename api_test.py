import requests
from PIL import Image
import os
from os import listdir


#--------------------------------------Testing Api inference------------------------------------------------------------------------------------
# input path to test dataset
imgpath = 'path goes here'

#output path to save api response
output_path = 'path goes here/output_file{0}.txt' 

#iterate through files in input path, posting them to the api endpoint
for filename in os.listdir(imgpath):
	#img = Image.open(imgpath+filename)
	files = {
    'files': (imgpath, open(imgpath+filename, 'rb')),}
	response = requests.post('api endpoint', files=files, verify=False)
	response.raise_for_status() #notice the bad responses
    
	# write to output files
	out = open(output_path.format(filename), "w")# save response to mulltiple files with corresponding filenames 
	out.write(response.text)
	out.close()

#----------------------------------------------------------------------------------------------------------------------------------------------
