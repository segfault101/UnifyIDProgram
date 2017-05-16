from PIL import Image
import urllib2

def get_random():
	request = urllib2.Request('http://www.random.org/integers/?num=1&min=0&max=255&col=1&base=10&format=plain&rnd=new')
	request.add_header('User-Agent', 'rahul\'s random image generator')
	opener = urllib2.build_opener()
	numlist = opener.open(request).read()
	num = numlist.split()[0]
	return int(num)


data = ""
for i in range( 128**2 ):
    	data += chr(get_random()) + chr(get_random()) + chr(get_random())
random_image = Image.frombytes("RGB", (128,128), data)
random_image.save("random.png", "PNG")
