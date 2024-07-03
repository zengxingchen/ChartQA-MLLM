
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a DataFrame using the provided table data
data = {
    'Day': [i for i in range(1, 32)],
    'Steps_Taken': [7500, 7600, 7550, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8350, 8400, 8500, 8550, 8600, 
                    8700, 8750, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000, 10100]
}

df = pd.DataFrame(data)

# Customizing plot size
plt.figure(figsize=(14, 6))

# Creating a line plot
sns.lineplot(x='Day', y='Steps_Taken', data=df, color='#4682B4')

# Adding annotations
for day, steps in zip(data['Day'], data['Steps_Taken']):
    if day == 20:  # example of specific annotation on Day 20
        plt.text(day, steps, f"{steps} steps", fontsize=9, ha='center')

# Setting plot title and labels
plt.title('Daily Steps Taken Over a Month', fontsize=18, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Steps Taken', fontsize=14)

# Display the plot
plt.show()