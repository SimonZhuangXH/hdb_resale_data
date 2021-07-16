"""Extract Load and Transform."""
import pandas as pd  # dataframe
import pickle

from hdb_resale_data import (  # noqa: E402
        # retrive location data
        Location,
        # custom Data object
        Data,
)


def preprocess(download=False):
    """Preprocess data based on data preview.

    :param download: do we download the data?
    """
    url = "https://data.gov.sg/dataset/7a339d20-3c57-4b11-a695-9348adfd7614/download"  # noqa:E501
    data = Data(url)  # Data takes in a url: string

    if download:

        # Data stores the downloaded object with the given filename
        data.download(filename="data/data.zip")
        # display the file names we downloaded
        data.zip_filename(zip_file="data/data.zip")

    # read the file inside the zip file
    df = data.read_zip(zip_file="data/data.zip",
                       filename="resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv")  # noqa: E501

    ##########################
    # fix datetime for month #
    ##########################
    # problem: month is in yyyy-mm, common datetime format require day as well
    # solution: concatenate a string '-01' before converting to datetime
    # in order to ensure pandas convert our datetime object correctly,
    # we will explictly input the format
    df["month"] = pd.to_datetime(df["month"] + "-01", format="%Y-%m-%d")

    ####################################
    # fix datetime for remaining_lease #
    ####################################
    # problem: remaining_lease is in years and month (string),
    # we want a standardised unit
    # solution: convert remaining_lease to years (year = month/12)
    # we use Regex to extract out the years and month
    years = df["remaining_lease"].str.extract("(\d+) years").astype("float")  # noqa W605
    months = df["remaining_lease"].str.extract("years (\d+) [months]|[month]").astype("float")  # noqa W605
    # add a new column with remaining lease in years
    # and remove the old column
    df["remaining_lease_years"] = years + months/12
    df.pop("remaining_lease")

    ####################
    # fix storey_range #
    ####################
    # problem: storey_range is in string,
    # it is hard to have meaning comparision
    # solution: since the storey range is a numeric variable,
    # let's take the first storey
    df["storey_min"] = df["storey_range"].str.extract("(\d+) TO")  # noqa: W605
    df["storey_min"] = df["storey_min"].astype("int")
    df.pop("storey_range")

    ####################
    # export dataframe #
    ####################
    df.to_csv("data/hdb_cleaned.csv")
    return df


def retrive_location(df, first_n: int):
    """Fix location data.

    :param first_n: retrive first n rows, set as 0 for all rows
    """
    #####################
    # fix location data #
    #####################
    # problem: location data is in string,
    # it is hard to compare against different locations
    # solution: retrive geolocation
    loc = Location()
    location = df["block"] + " " + df["street_name"]
    links = loc.url1 + location + loc.url2
    if first_n > 0:
        responses = loc.get_gresponse(links.iloc[:first_n].values)
    else:
        responses = loc.get_gresponse(links.values)
    return responses


if __name__ == "__main__":
    df = preprocess(download=False)
    response = retrive_location(df, first_n=0)
    ####################
    # pickle responses #
    ####################
    with open("data/response", "wb") as f:
        pickle.dump(response, f)
