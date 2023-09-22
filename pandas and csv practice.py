# with open("weather_data.csv") as weather:
#     weather_forcast = weather.readlines()
#     print(weather_forcast)
import csv

import pandas
# import csv
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)




import pandas as pd

data = pd.read_csv("weather_data.csv")
data_list = (data["temp"])

data_list2 = data["temp"].tolist()
# print(data_list)
# print(len(data_list2))


average = sum(data_list2) / len(data_list2)
# print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)
# print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp_F = monday.temp[0] * 9/5 +32
# print(monday_temp_F)
data_dict = {
    "studendts": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)


