
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    "Exercise_Duration": [
        30, 35, 45, 50, 60, 70, 75, 80, 85, 90, 100, 105, 110, 120, 130,
        135, 140, 150, 155, 160, 165, 170, 180, 185, 190, 200, 210, 220, 
        230, 240, 250, 260, 270, 280, 290, 300
    ]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(10, 8))

# Create the histogram
sns.histplot(df['Exercise_Duration'], 
             bins=15, 
             kde=False, 
             color='#ff5733', 
             binwidth=10, 
             orientation="horizontal")

# Set titles and labels
plt.title('Distribution of Daily Exercise Durations', loc='left')
plt.xlabel('Frequency')
plt.ylabel('Exercise Duration (Minutes)')

# Display the plot
plt.show()