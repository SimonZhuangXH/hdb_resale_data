"""Extract location data."""
import grequests
import requests
import numpy as np
import csv


def exception_handler(request, exception):
    with open("failed_url.txt", "a") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([request.url])
    print(f"Request {request.url} failed")


class Location(object):

    def __init__(self):
        self.url1 = "https://developers.onemap.sg:443/commonapi/search?searchVal="
        self.url2 = "&&returnGeom=Y&getAddrDetails=Y&pageNum=1"

    def get_response(self, link: str):
        """Takes in a link and return json response."""
        page = requests.get(link, timeout=1)
        return page

    def json_load(self, response):
        """Takes in a response and return json format."""
        return response.json()

    def get_gresponse(self, links: list):
        """Uses grequests for get_response."""
        locations = np.array(links)
        result = np.array(list(
            map(lambda link: grequests.get(link, timeout=1), locations))
        )
        return grequests.map(result, exception_handler=exception_handler)


def main():
    loc = Location()
    location = "406 ANG MO KIO AVE 10"
    location = loc.url1 + location + loc.url2
    response = loc.get_response(location)
    content = loc.json_load(response)
    return content


def gmain():
    loc = Location()
    locations = [
        "406 ANG MO KIO AVE 10",
        "108 ANG MO KIO AVE 4"
    ]
    for i, location in enumerate(locations):
        locations[i] = loc.url1 + location + loc.url2
    responses = loc.get_gresponse(locations)
    content = []
    for response in responses:
        content.append(loc.json_load(response))
    return content


if __name__ == "__main__":
    result = main()
    gresult = gmain()
