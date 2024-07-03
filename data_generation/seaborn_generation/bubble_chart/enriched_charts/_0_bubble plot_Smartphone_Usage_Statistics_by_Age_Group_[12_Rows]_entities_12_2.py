
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define the data as a dictionary, which then will be converted into a DataFrame
data = {
    'Age': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80],
    'Average_Sleep': [14, 14, 13, 13, 12, 12, 11.5, 11.5, 11, 11, 11, 10.5, 10.5, 10, 10, 9.5, 9.5, 9, 9, 8.5, 8.5, 7.5, 7, 7, 7, 7, 6.5],
    'Screen_Time': [1, 1, 1.5, 1.5, 2, 2, 2.5, 2.5, 2.5, 3, 3, 3.5, 3.5, 4, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 6, 5, 4, 3, 2],
    'Count': [5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 20, 22, 25, 28, 30, 32, 35, 37, 40, 42, 45, 50, 55, 60, 65, 70, 75]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Creating the bubble chart
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df, x='Age', y='Average_Sleep', hue='Screen_Time', size='Count', sizes=(20, 1000),
                               palette=['#FFD700', '#FF8C00', '#1E90FF', '#32CD32', '#6A5ACD', '#FF69B4'])

# Customize the axes and title
bubble_chart.set_title('Average Sleep and Screen Time by Age', fontsize=18)
bubble_chart.set_xlabel('Age (Years)', fontsize=14)
bubble_chart.set_ylabel('Average Sleep (Hours per Night)', fontsize=14)

# Show the plot
plt.show()