img_ids = open('chairs_nuswide_imgids.txt','r')
nus_urls = open('NUS-WIDE-urls.txt', 'r')
dict_urls = {}
for line in nus_urls:
    dict_urls[line.split()[0]] = line.split()[3]
chairs_urls = []
count = 0
for line in img_ids:
    print('searching url ' + str(count))
    count = count +1
    if not dict_urls[line.split()[0]] == 'null':
        chairs_urls.append(dict_urls[line.split()[0]])
          
