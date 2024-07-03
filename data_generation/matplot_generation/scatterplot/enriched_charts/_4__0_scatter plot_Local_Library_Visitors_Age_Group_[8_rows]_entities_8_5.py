
import matplotlib.pyplot as plt

# Data
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", 
          "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", 
          "Seattle", "Denver", "El Paso", "Detroit", "Boston"]
hours_of_sleep = [6.5, 7.0, 6.8, 6.2, 6.9, 6.3, 7.1, 7.3, 6.7, 7.2, 
                  7.0, 6.4, 6.6, 6.5, 6.8, 7.4, 7.1, 6.1, 6.3, 7.0]
stress_level = [8.2, 7.5, 7.8, 8.0, 7.2, 7.9, 6.8, 6.5, 7.4, 6.6, 
                6.9, 7.7, 7.3, 7.6, 7.1, 6.4, 6.7, 8.3, 8.1, 6.9]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 10))

# Scatter plot
ax.scatter(hours_of_sleep, stress_level, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
                                                "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", 
                                                "#aec7e8", "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5", 
                                                "#c49c94", "#f7b6d2", "#c7c7c7", "#dbdb8d", "#9edae5"])

# Title and labels
plt.title('Average Hours of Sleep vs. Average Stress Levels in Different Cities', pad=20)
plt.xlabel('Average Hours of Sleep per Night')
plt.ylabel('Average Stress Level (1-10)')

# Show plot
plt.show()