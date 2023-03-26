import os
import requests
from urllib.parse import urlparse, parse_qs

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def download_images_from_drive_url(url, cookies=None):
    # parse the URL to get the base URL and the query parameters
    parsed_url = urlparse(url)
    base_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
    params = parse_qs(parsed_url.query)

    # create a directory to save images
    dir_name = "out/lesson_" + str(len(os.listdir("./out")) + 1)
    os.mkdir(dir_name)
    print(f"Created directory {dir_name}")

    # set the page parameter to 0
    params["page"] = 0

    # keep looping until all images have been downloaded
    while True:
        # make a request to the current page with cookies if they are provided
        response = requests.get(base_url, params=params,
                                cookies=cookies, headers=headers)

        # check if we have reached the end of the images or if there is an error
        if response.status_code == 404:
            print("All images downloaded!")
            break
        elif response.status_code >= 400 and response.status_code < 600:
            print(f"Error {response.status_code} occurred, stopping download.")
            break

        # save the image to the directory
        image_file_path = f"{dir_name}/image{params['page']}.png"
        with open(image_file_path, "wb") as f:
            f.write(response.content)
        print(f"Saved image to {image_file_path}")

        # increment the page number
        params["page"] = str(int(params["page"]) + 1)

    print("Done!")


# get URL input from user
url = input("Enter the Google Drive URL: ")

# Add your cookies here
cookies = {
    "cookie_name": "cookie_value"
}


download_images_from_drive_url(url, cookies=cookies)
