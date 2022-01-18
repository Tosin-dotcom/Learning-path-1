import matplotlib.pyplot as plt
import pandas as pd


# read data from csv
df = pd.read_csv('data.csv')



month_data = df["Month"]
celebrant_data = df["Number_of_celebrant"]


# plot a pie chart
plt.pie(celebrant_data, labels=month_data, autopct='%1.0f%%')
plt.title("Number of celebrant in a given month")
plt.show()


# plot a bar chart
plt.bar(month_data, celebrant_data)
plt.title("Number of celebrant in a given month")
plt.show()


# plot scatter plot
plt.scatter(month_data, celebrant_data)
plt.title("Number of celebrant in a given month")
plt.show()
