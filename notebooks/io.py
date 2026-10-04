import geopandas as gpd


def load_buildings(path):
    gdf = gpd.read_file(path)
    print("Loaded dataset")
    print("Number of features:", len(gdf))
    print("CRS:", gdf.crs)
    print("Columns:", gdf.columns.tolist())
    return gdf
