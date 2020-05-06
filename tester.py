from fetcher.base import PickUp
import pandas as pd
from matplotlib import pyplot as plt 

def main():
    # resp = fetcher("https://covidtracking.com/api/v1/us/daily.csv")
    df = pd.read_csv("https://covidtracking.com/api/v1/states/daily.csv")
    ca = df[df.state == "CA"]
    ca = ca[["date", "state", "positive"]]
    ca.plot(x="date", y="positive")
    plt.show()

if __name__ == "__main__":
    main()
