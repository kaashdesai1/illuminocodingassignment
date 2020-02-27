from url_checker import *

urls = get_urls()
ctr = 1
for url in urls:
    print("{}. {}".format(ctr,url.rstrip()))
    if check_url_validity(url):
        print("Valid")
    else:
        print("Invalid")
    ctr += 1