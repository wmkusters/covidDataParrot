from fetcher.base import PickUp
import pandas as pd
from matplotlib import pyplot as plt 

def main():
    # resp = fetcher("https://covidtracking.com/api/v1/us/daily.csv")
    df = pd.read_csv("https://covidtracking.com/api/v1/states/daily.csv")
    print(df.columns)
    raise SystemError(0)
    ca = df[df.state == "CA"]
    ca = ca[["date", "state", "positive"]]
    ca["date"] = pd.to_datetime(ca.date, format="%Y%m%d")
    ca = ca.reset_index(drop=True)
    # ca = ca.set_index("date")
    # ca.plot(x="date", y=["positive", tested)
    plt.show()

if __name__ == "__main__":
    main()
