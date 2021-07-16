"""Retrive data from Data.gov.sg."""
import pandas as pd
import requests
import zipfile
from io import StringIO


class Data(object):
    """Reads csv file from Data.gov.sg."""
    def __init__(self, url):
        """Takes in a url to download data from."""
        self.url = url

    def download(self, filename):
        """Download the file content from the url and writes in file."""
        data = requests.get(self.url, stream=True)
        with open(filename, "wb") as f:
            f.write(data.content)
        return self

    def zip_filename(self, zip_file):
        """Read the available files in zipfile."""
        with zipfile.ZipFile(zip_file, "r") as zipp:
            return zipp.namelist()

    def read_zip(self, zip_file, filename):
        """Reads the file inside zip file and return a Pandas dataframe."""
        with zipfile.ZipFile(zip_file, "r") as zipp:
            data = zipp.read(filename)
            data = data.decode("utf-8")
            data = StringIO(data)
            return pd.read_csv(data)


def main():
    url = "https://data.gov.sg/dataset/7a339d20-3c57-4b11-a695-9348adfd7614/download"  # noqa
    _data = Data(url)
    _data.download("data/data.zip")
    _data.zip_filename("data/data.zip")
    mydata = _data.read_zip("data/data.zip",
                            "resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv")  # noqa
    return mydata


if __name__ == "__main__":
    data = main()
