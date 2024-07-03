
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the DataFrame from the data above
data = {
    'Company': ['Apple', 'Microsoft', 'Amazon', 'Google', 'Facebook', 'Tesla', 'Alibaba', 'Tencent',
                'Berkshire Hathaway', 'Visa', 'Johnson & Johnson', 'Samsung', 'Walmart', 'Nestle',
                'Procter & Gamble', 'Toyota', 'Nvidia', 'Disney', 'Nike', 'Coca-Cola'],
    'Revenue': [2745, 1430, 3860, 1825, 859, 315, 1094, 736, 2455, 217, 825, 2000, 5592, 920, 701, 2750, 160, 659, 374, 373],
    'Employees': [147000, 163000, 1335000, 135301, 58604, 70757, 117600, 85858, 360000, 20500, 134500, 267937, 2300000, 273000, 99000, 359542, 18975, 223000, 75400, 80000],
    'Market_Cap': [2250, 1980, 1630, 1520, 870, 710, 611, 649, 622, 465, 434, 510, 401, 370, 340, 290, 354, 350, 236, 232]
}

df = pd.DataFrame(data)

# Adjusting the figure size
plt.figure(figsize=(16, 10))

# Creating the bubble chart
sns.scatterplot(data=df, x="Revenue", y="Employees", size="Market_Cap", sizes=(100, 1000),
                hue="Market_Cap", palette=["#4c78a8", "#f58518", "#54a24b", "#e45756", "#72b7b2",
                                           "#ff9da7", "#9d755d", "#bab0ac", "#bcbd22", "#17becf"])

# Customizing the appearance
plt.title("Top Companies: Revenue, Employees, and Market Capitalization", fontsize=18)
plt.xlabel("Revenue (in billions USD)", fontsize=14)
plt.ylabel("Number of Employees", fontsize=14)

# Adjusting legend to avoid covering data points
plt.legend(title="Market Cap (in billions USD)", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Showing the final result
plt.show()