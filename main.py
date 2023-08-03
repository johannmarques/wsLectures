# Loading necessary packages

import requests
from bs4 import BeautifulSoup
from google_drive_downloader import GoogleDriveDownloader as gdd

response = requests.get("https://sites.google.com/view/yvanbecard/graduate-macroeconomics-1?authuser=0")

# Using tag to find elements for each lecture
# The first one is not associated with a lecture
items = BeautifulSoup(response.content).find_all('p')[1:]

# How many lectures will we download?
print("There are {} lectures available".format(len(items)))

for item in items :
    lecture_title = item.text # Extract lecture title
    lecture_url = item.find('a')["href"] # The url
    # From urls, we must extract it's id
    # However, there are two-types URL
    # Since this is a quite simple case, an if statement is enough
    if 'id=' in lecture_url :
        file_id = lecture_url.replace('https://drive.google.com/open?id=', '')
    else :
        file_id = lecture_url.replace('https://drive.google.com/file/d/', '').replace('/view?usp=sharing', '')

    print('Downloading {} lecture'.format(lecture_title))

    output = './slides/' + lecture_title + '.pdf' # The output path

    # Finally, download pdf

    gdd.download_file_from_google_drive(file_id=file_id,
                                        dest_path=output)