import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./Austin_Animal_Center_Intakes.csv")

ages = df['Age upon Intake']

time_dict = {}

for i in ages:
    n, times = map(str, i.split())
    n = int(n)
    if 'day' in times:
        pass
    elif 'week' in times:
        n *= 7
    elif 'month' in times:
        n *= 30
    elif 'year' in times:
        n *= 365

    if n > 0:
        if n not in time_dict:
            time_dict[n] = 1
        else:
            time_dict[n] += 1

x_axis = sorted(time_dict.keys())
print(x_axis)

y_axis = []
for i in x_axis:
    y_axis.append((time_dict[i] / len(x_axis)) * 100)

x_axis = [str(i) + " days" for i in x_axis]
plt.pie(y_axis, labels=x_axis, autopct='%.1f%%', startangle=0, counterclock=False)
plt.show()
