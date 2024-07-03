
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the dataset
data = {
    'hours_of_study': [
        1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 15, 16,
        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
        35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
        53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
        71, 72, 73, 74, 75, 76, 77, 78, 79, 80
    ]
}
df = pd.DataFrame(data)

# Set the style and the figure size
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# Create the histogram chart
sns.histplot(
    data=df, 
    x="hours_of_study", 
    binwidth=5, 
    kde=False, 
    color="#34a853"
)

# Adjusting further aesthetics of the plot
plt.title("Distribution of Study Hours")
plt.xlabel("Hours of Study")
plt.ylabel("Frequency")
plt.xlim(0, 85)
plt.xticks(range(0, 85, 5))

# Display the plot
plt.show()