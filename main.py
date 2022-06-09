import pandas as pd


def tt1():
    df = pd.read_csv('C:\\PycharmProjects\\Pandas\\nyc_weather.csv')
    print(df)
    print('Max temperature is: ')
    print(df['Temperature'])
    # Not clean data
    print('Wind Speed Mean not correct: ')
    print(df['WindSpeedMPH'].mean())
    # Clean data mean (No data place filling with 0)
    print('Wind Speed Mean correct: ')
    df.fillna(0, inplace=True)
    print(df['WindSpeedMPH'].mean())


# Dataframe is a main object in Pandas. It is used to represent data with rows and columns (tabular or excel
# spreadsheet like data)
def tt2():
    # creating dataframe
    df = pd.read_csv('C:\\PycharmProjects\\Pandas\\weather_data.csv')
    print(df)
    # we can create dataframe using python dictionary
    # weather_data = {
    #     'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017', '1/6/2017'],
    #     'temperature': [32, 35, 28, 24, 32, 31],
    #     'windspeed': [6, 7, 2, 7, 4, 2],
    #     'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
    # }
    # df = pd.DataFrame(weather_data)
    # print(df)

    print(df.shape)
    rows, columns = df.shape
    print(rows)
    print(columns)
    # will print first 2 rows
    print(df.head(2))
    # will print last 1 row
    print(df.tail(1))
    # will print row 2 to 4, So df[2:5] here 5 is excluded
    print(df[2:5])
    # To print everything we need df or df[:]
    print(df[:])
    # To print column
    print(df.columns)
    # To print content of the column df.day or df['day]
    print(df.day)
    # To print certain column
    print(df[['event', 'day']])
    # To print maximum temperature
    print(df['temperature'].max())
    # To print standard deviation
    print(df['temperature'].std())
    # To print statistic
    print(df.describe())
    # using condition
    print(df[df.temperature >= 32])
    print(df[['day', 'temperature']][df.temperature == df.temperature.max()])
    # To change index, here inplace=True is for modifying original df
    print(df.set_index('day', inplace=True))
    print(df.loc['1/3/2017'])
    # To reset to original
    print(df)
    df.reset_index(inplace=True)
    print(df)



def main():
    # tt1()
    tt2()


if __name__ == "__main__":
    main()
