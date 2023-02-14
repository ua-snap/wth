import geopandas
import pandas as pd

huc8 = geopandas.read_file("./data/WBD_19_HU2_Shape/Shape/WBDHU8.shp")

huc8.drop(
    [
        "tnmid",
        "metasource",
        "sourcedata",
        "sourceorig",
        "sourcefeat",
        "loaddate",
        "referenceg",
        "areaacres",
        "states",
        "shape_Leng",
        "shape_Area",
        "ObjectID",
    ],
    axis=1,
    inplace=True,
)
huc8.rename(columns={"huc8": "hucId"}, inplace=True)
huc8["hucLevel"] = 8

huc10 = geopandas.read_file("./data/WBD_19_HU2_Shape/Shape/WBDHU10.shp")
huc10.drop(
    [
        "tnmid",
        "metasource",
        "sourcedata",
        "sourceorig",
        "sourcefeat",
        "loaddate",
        "referenceg",
        "areaacres",
        "states",
        "hutype",
        "humod",
        "shape_Leng",
        "shape_Area",
        "ObjectID",
    ],
    axis=1,
    inplace=True,
)
huc10.rename(columns={"huc10": "hucId"}, inplace=True)
huc10["hucLevel"] = 10

huc12 = geopandas.read_file("./data/WBD_19_HU2_Shape/Shape/WBDHU12.shp")
huc12.drop(
    [
        "tnmid",
        "metasource",
        "sourcedata",
        "sourceorig",
        "sourcefeat",
        "loaddate",
        "referenceg",
        "areaacres",
        "states",
        "hutype",
        "humod",
        "tohuc",
        "noncontrib",
        "noncontr_1",
        "shape_Leng",
        "shape_Area",
        "ObjectID",
    ],
    axis=1,
    inplace=True,
)
huc12.rename(columns={"huc12": "hucId"}, inplace=True)
huc12["hucLevel"] = 12

merged = pd.concat([huc8, huc10, huc12])
merged.to_crs(3338, inplace=True)
merged.to_file("merged_hucs_3338")
print(merged.crs)
