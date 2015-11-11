""" Copyright (C) 2015  Sebastian Otalora

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

""" 

import flickrapi
import json 
import matplotlib.pyplot as plt
import Image
import urllib, cStringIO
import numpy as np

	
api_key = u'3724c5fcd02af2a224329c086d64a68c'
api_secret = u'6e80f744db6eb5c3'

flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json')
#The search query is stored in a rsp object which can be parsed to JSON
#lets say we want to increase 'chair' class performance, a possible query would be:
photos = flickr.photos_search(tags='chair',sort='relevance', geo_context=1, extras='url_m')
#photos is a dict with all the results ids, captions, urls and so forth
img_id = 0 
cur_img_id = photos['photos']['photo'][img_id]
photoSizes = flickr.photos_getSizes(photo_id=cur_img_id['id'])
#photoSizes['sizes']['size'][0] contains the diferent sources of the img in diferent sizes:
#{u'height': 75,
# u'label': u'Square',
# u'media': u'photo',
# u'source': u'https://farm6.staticflickr.com/5836/22322409944_1498c04fb6_s.jpg',
# u'url': u'https://www.flickr.com/photos/g20_turkey/22322409944/sizes/sq/',
# u'width': 75}

#photos = flickr.photos_search(tags='chair', lat='42.355056', lon='-71.065503', radius='5')
#sets = flickr.photosets.getList(user_id='73509078@N00')
#lets parse the source URL
URL = photoSizes['sizes']['size'][0]['source']
img_file = cStringIO.StringIO(urllib.urlopen(URL).read())
img = Image.open(img_file)
#lets look at the image with plt
plt.imshow(img)
plt.show()

#lets save all the image urls to process with the opencv gui

imgs_ursl = []
for imagen in photoSizes:
	if 