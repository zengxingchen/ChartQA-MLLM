
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Books_Read': [3, 4, 5, 6, 7, 8, 9, 10, 8, 7, 5, 4],
    'Study_Hours': [25, 28, 30, 35, 40, 45, 50, 55, 48, 42, 35, 30]
}

df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Books_Read', y='Study_Hours', data=df,
                palette=['#1f77b4', '#ff7f0e'])

plt.title('Monthly Study and Reading Habits', fontsize=18, y=1.05)
plt.xlabel('Books Read per Month')
plt.ylabel('Study Hours per Month')

# Display the plot
plt.show()