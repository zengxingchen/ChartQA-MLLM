
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data creation
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Running_Distance': [30, 28, 35, 40, 45, 50, 55, 60, 55, 50, 45, 40]
}

df = pd.DataFrame(data)

# Convert 'Month' from string to categorical to ensure correct order
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

# Seaborn plot
plt.figure(figsize=(16, 10))
chart = sns.lineplot(x='Month', y='Average_Running_Distance', data=df, color="#2ca02c")

# Filling the area under the line
plt.fill_between(x=df['Month'], y1=df['Average_Running_Distance'], color="#2ca02c", alpha=0.3)

# Annotate
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Average_Running_Distance'][i] + 1, f"{df['Average_Running_Distance'][i]} km", horizontalalignment='center')

plt.title('Monthly Average Running Distance', pad=20)
plt.xlabel('Month')
plt.ylabel('Running Distance (km)')

# Show plot
plt.tight_layout()
plt.show()