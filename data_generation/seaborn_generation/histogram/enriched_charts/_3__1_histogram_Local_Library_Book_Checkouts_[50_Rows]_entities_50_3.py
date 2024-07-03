
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame from the given table data.
data = {
    'Score': [
        50, 55, 52, 48, 49, 53, 45, 60, 57, 54, 50, 51, 58, 65, 62, 70, 75, 78, 80, 72,
        68, 66, 63, 61, 59, 55, 53, 52, 49, 47, 46, 44, 50, 56, 58, 60, 62, 64, 67, 69,
        71, 73, 76, 77, 78, 80, 82, 85, 87, 90, 92, 95, 98, 100, 102, 105, 108, 110, 112, 115,
        65, 68, 70, 72, 74, 76, 78, 80, 83, 85, 88, 90, 92, 95, 97, 99, 102, 105, 107, 110,
        112, 115, 118, 120, 123, 125, 128, 130, 132, 135, 138, 140, 143, 145, 148, 150, 153, 155, 158, 160
    ]
}

df = pd.DataFrame(data)

# Setting the aesthetic style of the plots.
sns.set_style('whitegrid')

# Setting the size of the plot.
plt.figure(figsize=(10, 8))

# Creating a horizontal histogram with the specified bin width and color.
sns.histplot(df['Score'], bins=15, color='#ff5733', kde=False, orientation='horizontal')

# Customizing plot labels and title.
plt.title('Score Distribution in a Competency Test', fontsize=18, pad=20)
plt.xlabel('Frequency', fontsize=15)
plt.ylabel('Score', fontsize=15)

# Show the plot.
plt.show()