import pandas as pd
from datetime import datetime

def calculate_streak(csv_file):

    try:
        df = pd.read_csv(csv_file)

        dates = pd.to_datetime(df["Date"]).dt.date.unique()
        dates = sorted(dates)

        if len(dates) == 0:
            return 0

        streak = 1

        for i in range(len(dates)-1,0,-1):

            diff = (dates[i]-dates[i-1]).days

            if diff == 1:
                streak += 1
            else:
                break

        return streak

    except:
        return 0