import random #musimy file randomowo nazwać
import urllib.request #data from websites allows us to get

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://i.kinja-img.com/gawker-media/image/upload/s--HwoaJMpy--/c_fit,fl_progressive,q_80,w_636/17f8rtrv2zibpjpg.jpg")