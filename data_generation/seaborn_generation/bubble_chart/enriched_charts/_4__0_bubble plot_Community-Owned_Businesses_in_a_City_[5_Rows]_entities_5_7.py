
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the dataset
data = {
    "City": ["Paris", "Bangkok", "London", "Dubai", "Singapore",
             "New York", "Kuala Lumpur", "Tokyo", "Istanbul", "Seoul",
             "Barcelona", "Amsterdam", "Milan", "Rome", "Prague"],
    "VisitorsPerYear": [17500000, 22000000, 19300000, 16800000, 15700000,
                        13900000, 13800000, 12700000, 12500000, 11000000,
                        9300000, 8900000, 8600000, 7800000, 7500000],
    "AverageStay": [2.3, 3.2, 2.7, 4.1, 2.9,
                    2.4, 3.0, 2.5, 3.3, 2.8,
                    2.6, 2.7, 2.5, 2.9, 3.1],
    "AverageSpending": [1000, 900, 1100, 1500, 1300,
                        1250, 800, 1150, 700, 950,
                        850, 1200, 1050, 950, 900]
}

df = pd.DataFrame(data)

# Define the seaborn style
sns.set_context("talk")
sns.set_style("whitegrid")

# Plotting
plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(
    data=df, 
    x="AverageStay", 
    y="AverageSpending", 
    hue="City", 
    size="VisitorsPerYear",
    sizes=(100, 2000),
    palette=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0",
             "#ffb3e6", "#c4e17f", "#76d7c4", "#ff7f50", "#87cefa",
             "#da70d6", "#32cd32", "#ffd700", "#ff6347", "#4169e1"]
).set_title('Popular Tourist Destinations: Average Stay vs. Average Spending')

# Modify axes labels
plt.xlabel("Average Stay (days)")
plt.ylabel("Average Spending ($)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.tight_layout()
plt.show()