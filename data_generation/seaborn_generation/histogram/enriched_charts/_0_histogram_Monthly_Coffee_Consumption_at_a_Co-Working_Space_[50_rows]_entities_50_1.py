
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data_points = {
    'value': [102, 150, 130, 115, 190, 105, 170, 125, 110, 195, 180, 
              135, 160, 100, 165, 155, 185, 120, 140, 175, 200, 145]
}

# Convert to DataFrame
df = pd.DataFrame(data_points)

# Set the style
sns.set(style="whitegrid")

# Size of the figure
plt.figure(figsize=(10, 8))

# Create the histogram
sns.histplot(data=df, x="value", color="#3498db", binwidth=10, orientation="horizontal")

# Set the title and labels
plt.title('Frequency Distribution of Exam Scores')
plt.xlabel('Frequency')
plt.ylabel('Exam Score')

# Show the plot
plt.show()