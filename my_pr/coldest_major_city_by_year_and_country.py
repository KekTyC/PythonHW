import zipfile
import pandas as pd
import argparse
import warnings
warnings.filterwarnings("ignore")

def coldest_major_city_by_year_and_country(year,country):
    with zipfile.ZipFile("./archive.zip") as z:
        with z.open("GlobalLandTemperaturesByMajorCity.csv") as f:
            df = pd.read_csv(f, parse_dates=["dt"])


    df = df[(df['dt'].dt.year == year) & (df.Country == country)]
    df = df.groupby('City',as_index=False).aggregate({'AverageTemperature':'mean'}).sort_values('AverageTemperature')
    try:
        res = str(df.head(1)['City'].iloc[0])
    except:
        res = "None"
    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get coldest city by year and country")
    parser.add_argument("year", type=int, help="Year")
    parser.add_argument("country", type=str, help="Contry")
    args = parser.parse_args()
    res = coldest_major_city_by_year_and_country(args.year, args.country)
    print(res)
