
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
             "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", 
             "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte"],
    "NumberOfLibraries": [220, 150, 120, 100, 80, 
                          95, 60, 75, 85, 55,
                          45, 40, 50, 70, 65],
    "ReadingHabitRate": [85, 80, 75, 78, 82, 
                         83, 76, 84, 81, 88,
                         79, 77, 73, 74, 82],
    "BookBorrowRate": [70, 65, 60, 62, 68,
                       66, 63, 69, 67, 73,
                       65, 64, 61, 60, 72],
    "Population": [8419000, 3990000, 2706000, 2306000, 1662000, 
                   1584000, 1532000, 1426000, 1343000, 1029000,
                   993000, 911000, 890000, 892000, 885000]
}

df = pd.DataFrame(data)

sns.set_context("talk")
sns.set_style("whitegrid")

plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(
    data=df, 
    x="ReadingHabitRate", 
    y="BookBorrowRate", 
    hue="City", 
    size="Population",
    sizes=(100, 2000),
    palette=["#FF4500", "#00FF7F", "#1E90FF", "#FF1493", "#9370DB",
             "#FF6347", "#3CB371", "#9400D3", "#FF0000", "#00CED1",
             "#ADFF2F", "#FF00FF", "#40E0D0", "#FFD700", "#48D1CC"]
).set_title('City Literature Statistics: Reading Habit and Book Borrow Rate', pad=20)

plt.xlabel("Reading Habit Rate (%)")
plt.ylabel("Book Borrow Rate (%)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.tight_layout()
plt.show()