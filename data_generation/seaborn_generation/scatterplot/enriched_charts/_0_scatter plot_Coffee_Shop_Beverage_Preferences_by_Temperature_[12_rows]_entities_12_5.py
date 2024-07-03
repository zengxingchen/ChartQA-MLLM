
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Replace the following dict with the provided table data
data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
             "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
             "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
             "Indianapolis", "Seattle", "Denver", "Boston", "El Paso",
             "Detroit", "Nashville", "Memphis", "Portland", "Las Vegas", 
             "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson"],
    "AverageTemperature": [15.5, 19.2, 13.0, 20.3, 23.4, 
                           14.7, 22.1, 18.5, 21.2, 17.8, 
                           21.0, 19.9, 20.7, 12.6, 17.2, 
                           13.7, 10.6, 16.1, 13.2, 21.8, 
                           12.1, 16.9, 18.8, 11.9, 24.5, 
                           15.9, 14.3, 11.7, 18.6, 21.6],
    "HumidityPercentage": [78, 64, 70, 83, 45, 
                           71, 60, 69, 65, 78, 
                           68, 75, 66, 70, 73, 
                           68, 85, 52, 77, 44, 
                           73, 69, 74, 83, 22, 
                           71, 76, 75, 45, 39]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the dimensions of the plot
plt.figure(figsize=(14, 8))

# Create the scatter plot with a custom color palette
scatter_plot = sns.scatterplot(x="AverageTemperature", y="HumidityPercentage", data=df, s=100,
                               palette=["#FF5733", "#33FF57", "#3357FF", "#57FF33", "#FF3357"],
                               hue="City", legend=False)

# Set the title and labels of the plot
scatter_plot.set_title("Average Temperatures and Humidity Percentages by City")
scatter_plot.set_xlabel("Average Temperature (°C)")
scatter_plot.set_ylabel("Humidity Percentage (%)")

# Show the plot
plt.show()