
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
             "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
             "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
             "Indianapolis", "Seattle", "Denver", "Boston", "El Paso",
             "Detroit", "Nashville", "Memphis", "Portland", "Las Vegas", 
             "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson"],
    "AverageCaloriesBurned": [550, 680, 500, 720, 750, 
                              600, 700, 670, 710, 690, 
                              720, 640, 680, 530, 650, 
                              560, 620, 600, 530, 710, 
                              540, 590, 650, 540, 750, 
                              580, 570, 530, 680, 710],
    "ExerciseDuration": [45, 60, 40, 55, 50, 
                         47, 52, 55, 58, 60, 
                         57, 50, 53, 42, 48, 
                         45, 50, 47, 44, 59, 
                         41, 49, 54, 45, 65, 
                         46, 45, 43, 55, 60]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the dimensions of the plot
plt.figure(figsize=(16, 10))

# Create the scatter plot with a custom color palette
scatter_plot = sns.scatterplot(x="AverageCaloriesBurned", y="ExerciseDuration", data=df, s=100,
                               palette=["#FF6347", "#4682B4", "#32CD32", "#FFD700", "#8A2BE2"],
                               hue="City", legend=False)

# Set the title and labels of the plot
scatter_plot.set_title("Average Calories Burned vs. Exercise Duration by City")
scatter_plot.set_xlabel("Average Calories Burned")
scatter_plot.set_ylabel("Exercise Duration (minutes)")

# Show the plot
plt.show()