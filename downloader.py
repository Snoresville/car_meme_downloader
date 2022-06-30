# use pip install for both imports
# and run the program
import requests
import os

# Reads the big list of car memes to download from
website = requests.get("https://awesomecars.neocities.org/biglist.html")
if website.status_code != 200:
    print("Big list of cars unable to be accessed")
    exit(1)

links = list(filter(lambda line: "a href=\"images" in line, website.text.split('\n')))
file_content = []

for link in links:
    content = []
    x = link.split("images/")[1].split("\"")
    content.append(x[0])
    content.append(x[1][1:].split("</a>")[0].replace(" ", "_").replace("/", "-") + ".mp4")
    file_content.append(content)

# Creates a download folder near the program to contain all of the files in
download_folder_path = os.path.dirname(__file__) + "\car_download"
if not os.path.isdir(download_folder_path):
    os.mkdir(download_folder_path)

for file in file_content:
    # Skips already downloaded files
    if not os.path.isfile(download_folder_path + "\\" + file[1]):
        link = "https://awesomecars.neocities.org/images/" + file[0]
        car_meme = requests.get(link)

        print("Downloading " + file[1] + "...")
        open(download_folder_path + "\\" + file[1], "wb").write(car_meme.content)
    else:
        print("Already downloaded " + file[1] + ", skipping...")