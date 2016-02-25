import os
import numpy as np
import pandas as pd
import matplotlib

import data as phdata

rizal_area = "Binangonan|Cainta|Taytay|Antipolo|Angono|Tanay"

ncr_routes_data = phdata.ncr_routes_data

def routes_by_area(cond_area):
    return ncr_routes_data[ncr_routes_data["route"].str.contains(cond_area)].groupby("puv")

print "Rizal"
print routes_by_area(rizal_area).count()

# seperate origins and destination into their own columns

ncr_routes_data["origin"] = pd.Series(
                                ncr_routes_data["route"].str.split(" - ").str[0],
                                index=ncr_routes_data.index)

ncr_routes_data["destination"] = pd.Series(
                                ncr_routes_data["route"].str.split(" - ").str[1],
                                index=ncr_routes_data.index)
