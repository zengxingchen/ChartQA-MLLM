
import seaborn as sns
import matplotlib.pyplot as plt

# Table data
stress_levels = [
    4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16, 17, 17, 17, 18, 18, 19, 20
]

# Create the histogram
plt.figure(figsize=(12, 8))
sns.histplot(stress_levels, color="#e74c3c", binwidth=1, orientation="horizontal")

# Set titles and labels
plt.title('Distribution of Stress Levels')
plt.xlabel('Frequency')
plt.ylabel('Stress Level')

# Display the histogram
plt.show()