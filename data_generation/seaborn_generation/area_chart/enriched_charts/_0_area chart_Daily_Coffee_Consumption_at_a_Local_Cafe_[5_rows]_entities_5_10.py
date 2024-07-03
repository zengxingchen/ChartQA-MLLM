
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data creation
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature': [4.6, 5.2, 8.3, 11.5, 15.8, 19.1, 22.4, 22.1, 18.5, 13.6, 8.7, 5.9]
}

df = pd.DataFrame(data)

# Convert 'Month' from string to categorical to ensure correct order
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

# Seaborn plot
plt.figure(figsize=(12, 6))
chart = sns.lineplot(x='Month', y='Average_Temperature', data=df, color="#3498db")

# Filling the area under the line
plt.fill_between(x=df['Month'], y1=df['Average_Temperature'], color="#3498db", alpha=0.3)

# Annotate
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Average_Temperature'][i]+0.3, f"{df['Average_Temperature'][i]}°C", horizontalalignment='center')

plt.title('Average Monthly Temperatures')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

# Show plot
plt.tight_layout()
plt.show()