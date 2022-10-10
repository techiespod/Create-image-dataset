#Techiespod
#Creating Image dataset

from bing_image_downloader import downloader
# Bing to extract images from internet

query_string = ['Elon Musk', 'Obama', 'Jef
# Here insert the names of object/person whose data is to be collected

for content in query_string:
    downloader.download(content, limit=10,  output_dir='Data set');
# set limit for every object in list

#for example if you need 10 images of each object present in list than set limit as per your need
