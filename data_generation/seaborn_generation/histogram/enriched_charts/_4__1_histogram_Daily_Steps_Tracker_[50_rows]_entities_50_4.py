
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# New data for student test scores
data = {
    'Score': [
        88, 92, 85, 78, 94, 89, 85, 82, 93, 87, 88, 91, 90, 95, 77, 84, 86, 83,
        92, 91, 79, 94, 88, 81, 89, 90, 87, 92, 96, 85, 82, 94, 89, 78, 84, 91
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(12, 8))

# Create the histogram
sns.histplot(data=df, y='Score', bins=10, color='#e74c3c', binwidth=2)

# Customizing the plot's aesthetics
plt.title('Histogram of Student Test Scores', fontsize=16)
plt.xlabel('Frequency', fontsize=14)
plt.ylabel('Score', fontsize=14)

# Show the plot
plt.show()