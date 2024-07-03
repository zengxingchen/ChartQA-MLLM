
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame from the given table data.
data = {
    'Age': [
        23, 26, 22, 35, 29, 33, 41, 27, 34, 25, 31, 29, 38, 45, 42, 36, 47, 50, 53, 56,
        49, 48, 37, 39, 40, 32, 28, 24, 21, 19, 18, 20, 22, 23, 25, 27, 30, 33, 35, 36,
        38, 40, 43, 46, 49, 52, 55, 58, 60, 62, 65, 67, 23, 26, 28, 30, 32, 34, 36, 38,
        40, 41, 43, 45, 47, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 20, 19,
        17, 23, 26, 25, 24, 28, 29, 31, 33, 36, 35, 38, 40, 42, 44, 46, 47, 49, 50, 52,
        54, 56, 57, 58, 60, 61, 63, 66, 68, 70, 72, 74, 75, 77
    ]
}

df = pd.DataFrame(data)

# Setting the aesthetic style of the plots.
sns.set_style('whitegrid')

# Setting the size of the plot.
plt.figure(figsize=(10, 12))

# Creating a horizontal histogram with the specified bin width and color.
sns.histplot(df['Age'], bins=15, color='#FF6347', kde=False, orientation='horizontal')

# Customizing plot labels and title.
plt.title('Age Distribution in a Sample Population', fontsize=18, loc='right')
plt.xlabel('Frequency', fontsize=15)
plt.ylabel('Age', fontsize=15)

# Show the plot.
plt.show()