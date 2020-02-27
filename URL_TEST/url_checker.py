import urllib.request
import re 

# Check if the URL is well formed
def check_url_sanity(url):
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

# Check if the URL exists
def check_url_validity(url):
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.request.HTTPError as e:
        return False

# Get the URL from user
def get_url():
    url = input("URL: ")
    return url

# Store the URL if it is valid
def store_url(url):
    f=open("urls.txt", "a+")
    f.write("{}\n".format(url))
    f.close()

# Fetch stored URLs
def get_urls():
    url_list = []
    with open("urls.txt") as f:
        url_list = f.readlines()
    return url_list

def main():
    choice = 3
    while choice > 0 and choice < 4:
        choice = int(input("1.Enter a new URL\n2.Use previous URL\n3.Exit\n"))
        if choice == 1:
            url = get_url()
            if check_url_sanity(url):
                if check_url_validity(url):
                    store_url(url)
                    print("Valid")
            else:
                print("Invalid")
        elif choice == 2:
            urls = get_urls()
            ctr = 1
            for url in urls:
                print("{}. {}".format(ctr,url.rstrip()))
                ctr += 1
            run_url = int(input("Which URL would you like to run?\n"))
            if check_url_validity(urls[run_url-1]):
                print("Valid")
            else:
                print("Invalid")
        elif choice == 3:
            exit(0)

if __name__ == '__main__':
    main()