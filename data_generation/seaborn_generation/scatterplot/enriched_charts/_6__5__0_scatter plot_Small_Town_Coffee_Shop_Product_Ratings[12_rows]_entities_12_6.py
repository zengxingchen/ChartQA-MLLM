
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Exercise_Hours': [15, 18, 20, 22, 25, 30, 35, 28, 26, 24, 22, 18],
    'Sleep_Hours': [7, 6.5, 7.5, 8, 7, 6.5, 6, 7, 7.5, 8, 7, 6.5]
}

df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Exercise_Hours', y='Sleep_Hours', data=df,
                palette=['#3498db', '#e74c3c'])

plt.title('Monthly Exercise vs. Sleep Hours', fontsize=18, pad=20)
plt.xlabel('Exercise Hours', fontsize=14)
plt.ylabel('Sleep Hours', fontsize=14)

# Display the plot
plt.show()