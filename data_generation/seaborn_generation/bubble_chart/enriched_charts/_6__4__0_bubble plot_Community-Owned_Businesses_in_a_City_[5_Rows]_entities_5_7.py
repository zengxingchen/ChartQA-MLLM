
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the dataset
data = {
    "City": ["Paris", "Bangkok", "London", "Dubai", "Singapore",
             "New York", "Kuala Lumpur", "Tokyo", "Istanbul", "Seoul",
             "Barcelona", "Amsterdam", "Milan", "Rome", "Prague"],
    "GreenSpacesPerCapita": [15, 20, 25, 12, 30,
                             18, 22, 28, 10, 16,
                             19, 23, 13, 14, 21],
    "SatisfactionScore": [7.8, 8.5, 9.0, 7.0, 9.5,
                          8.0, 8.2, 8.7, 6.5, 7.5,
                          8.3, 8.8, 7.2, 7.4, 8.4],
    "AverageSpending": [1200, 1100, 1400, 1600, 1500,
                        1300, 900, 1350, 800, 950,
                        1000, 1450, 1050, 1000, 1150]
}

df = pd.DataFrame(data)

# Define the seaborn style
sns.set_context("talk")
sns.set_style("whitegrid")

# Plotting
plt.figure(figsize=(18, 14))
bubble_chart = sns.scatterplot(
    data=df, 
    x="GreenSpacesPerCapita", 
    y="AverageSpending", 
    hue="City", 
    size="SatisfactionScore",
    sizes=(100, 2000),
    palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#33FFA1",
             "#A133FF", "#FF7133", "#33FFEC", "#FFBD33", "#71FF33",
             "#FF3373", "#33FF93", "#3371FF", "#A1FF33", "#FF8D33"]
).set_title('Top Cities for Urban Green Spaces: Green Spaces Per Capita vs. Average Spending', pad=20)

# Modify axes labels
plt.xlabel("Green Spaces Per Capita (square meters)")
plt.ylabel("Average Spending ($)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.tight_layout()
plt.show()