import requests
import urllib
import urllib.request
import urllib.parse
import time
from bs4 import BeautifulSoup


#Currently it works on images with a 4 number system


# website url
url = str(r'http://vfxlessons.tv/test/')
print(url)
file_extention = '.jpg'
subtract_letters_from_end = 0
image_rootname = "foto_"

# Connect URL
response = requests.get(url)

# HTML parsing
soup = BeautifulSoup(response.text, "html.parser")



#  rllib.request.urlretrieve("http://www.vfxlessons.tv/tmp/img/weblogo.png","foto.png")

mijn_url_zonder_filename = url[:-subtract_letters_from_end]
print(mijn_url_zonder_filename )

my_index= []

# datalijst downloaden2


line_count = 1 #waar ben ik
for index, one_a_tag in enumerate(soup.findAll('a')):  #'a' tags
    my_index.append(index)
    #print(index)
    Complete_filenumber = "{0:0=4d}".format(index)
    #print(Complete_filenumber)

    name = str(one_a_tag)

    name_sliced = name[2:-8]
    nieuwe_naam =  name + file_extention

    #print(nieuwe_naam)
    #print("naam sliced : " + name_sliced + ".exr")
    mijn_filename = mijn_url_zonder_filename + image_rootname + str(Complete_filenumber) + file_extention
    save_filenaam = "iets" + str(Complete_filenumber)
    print(mijn_filename)

    urllib.request.urlretrieve(mijn_filename,save_filenaam)