
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Book_Sales': [250, 300, 350, 280, 360, 390, 420, 410, 400, 380, 370, 365],
    'Online_Engagement': [40, 50, 60, 45, 65, 70, 75, 72, 68, 66, 64, 63]
}

df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(14, 9))
sns.scatterplot(x='Book_Sales', y='Online_Engagement', data=df,
                palette=['#FF5733', '#33FF57'])

plt.title('Monthly Book Sales vs Online Engagement', fontsize=16)
plt.xlabel('Book Sales (units)', fontsize=14)
plt.ylabel('Online Engagement (hours)', fontsize=14)

# Display the plot
plt.show()