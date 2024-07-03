
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the dataset
data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
             "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", 
             "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte"],
    "Population": [8419000, 3990000, 2706000, 2306000, 1662000, 
                   1584000, 1532000, 1426000, 1343000, 1029000,
                   993000, 911000, 890000, 892000, 885000],
    "MedianAge": [36.2, 35.1, 34.1, 32.9, 33.5, 
                  34.5, 33.2, 34.9, 32.8, 36.5,
                  33.3, 35.5, 31.8, 31.4, 34.3],
    "AverageIncome": [71000, 65120, 60450, 57030, 48020,
                      52260, 49800, 66570, 57100, 87000,
                      58040, 50260, 52600, 48360, 58870]
}

df = pd.DataFrame(data)

# Define the seaborn style
sns.set_context("talk")
sns.set_style("whitegrid")

# Plotting
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(
    data=df, 
    x="MedianAge", 
    y="AverageIncome", 
    hue="City", 
    size="Population",
    sizes=(100, 2000),
    palette=["#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#9b59b6",
             "#34495e", "#16a085", "#95a5a6", "#d35400", "#1abc9c",
             "#27ae60", "#2980b9", "#8e44ad", "#2c3e50", "#f39c12"]
).set_title('City Demographics: Population, Median Age, and Average Income')

# Modify axes labels
plt.xlabel("Median Age (years)")
plt.ylabel("Average Income ($)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.tight_layout()
plt.show()