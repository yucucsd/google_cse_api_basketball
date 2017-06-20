from apiclient.discovery import build
import urllib
import os
import time
def image_format_jpg(s):
    for i in range(len(s)):
        if s[i] == 'j':
            if i + 1 < len(s) and s[i + 1] == 'p':
                if i + 2 < len(s) and s[i + 2] == 'g':
                    if i + 3 == len(s) or s[i + 3] <> '?':
                        return True
                elif i + 2 < len(s) and s[i + 2] == 'e':
                    if i + 3 < len(s) and s[i + 3] == 'g':
                        return True

def make_query(brand, pic_num):

    service = build("customsearch", "v1",
               developerKey="your API key")

    for start in range(1, 101, 10):# if get results after 100, API will return 400: invalid error
        res = service.cse().list(
            q = brand + 'basketball',
            cx ='your custom search engine ID',
            start = start,
            searchType ='image',
            num = 10, #available value 1 - 10
            imgType = 'clipart',
            safe = 'off'
        ).execute()
        time.sleep(5)# make requests politely
        if not 'items' in res:
            print 'No result !!\nres is: {}'.format(res)
        else:
            output_dir = os.path.join(os.getcwd(), 'basketball_output')
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            for item in res['items']:
                if image_format_jpg(item['link']):
                    pic_num += 1
                    urllib.urlretrieve(item['link'], output_dir + '/' + str(pic_num) + '.jpg')
                    print('{}:\n\t{}'.format(item['title'].encode('ascii', 'ignore'), item['link'].encode('ascii', 'ignore')))

    return pic_num
if __name__ == '__main__':
    brand_list = [' ']#['Spalding', 'Wilson', 'Molten','Rawlings', \
    #'Baden', 'Mikasa']
    pic_num = 0# for naming the downloaded file
    for brand in brand_list:
        pic_num = make_query(brand, pic_num)
        print "Save {} images".format(pic_num)
