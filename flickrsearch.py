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

	
api_key = u'3724c5fcd02af2a224329c086d64a68c' #TODO: Put this into a file of .gitignore
api_secret = u'6e80f744db6eb5c3'
flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json')

#Obtain medium sized (maxdim = 500px) images URLS hosted in flickr for the provided label
#https://www.flickr.com/services/api/misc.urls.html
def get_catimgs_urls(label='chair', show_samples=0):
    #The search query is stored in a  JSON object
    imgs_urls = []
    photos = flickr.photos_search(tags=label,sort='relevance', geo_context=1, extras='url_m')
    #photos['photos']['photo'] is a list with all the results imgs as dicts with ids, captions, urls and so forth
    for img_id in range(len(photos['photos']['photo'])):
        cur_img_id = photos['photos']['photo'][img_id]
        imgs_urls.append(cur_img_id['url_m']) #medium size
        #photoSizes = flickr.photos_getSizes(photo_id=cur_img_id['id'])
    #cur_img_id['sizes']['size'][0] contains the diferent sources of the img in diferent sizes:
    #{u'height': 75,
    # u'label': u'Square',
    # u'media': u'photo',
    # u'source': u'https://farm6.staticflickr.com/5836/22322409944_1498c04fb6_s.jpg',
    # u'url': u'https://www.flickr.com/photos/g20_turkey/22322409944/sizes/sq/',
    # u'width': 75}

    #photos = flickr.photos_search(tags='chair', lat='42.355056', lon='-71.065503', radius='5')
    #sets = flickr.photosets.getList(user_id='73509078@N00')
    #lets parse the source URL
    if show_samples:
        img_idt = 0
        URL = imgs_urls[img_idt]
        img_file = cStringIO.StringIO(urllib.urlopen(URL).read())
        img = Image.open(img_file)
        #lets look at the image with plt
        plt.imshow(img) 
        plt.show()
        return imgs_urls 
#lets save all the image urls to process with the opencv gui

