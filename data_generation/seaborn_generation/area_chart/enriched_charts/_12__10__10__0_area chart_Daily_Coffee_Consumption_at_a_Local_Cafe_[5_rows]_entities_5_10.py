
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data creation
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Number_of_Books_Read': [5, 4, 6, 7, 8, 10, 12, 11, 9, 8, 7, 6]
}

df = pd.DataFrame(data)

# Convert 'Month' from string to categorical to ensure correct order
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

# Seaborn plot
plt.figure(figsize=(14, 8))
chart = sns.lineplot(x='Month', y='Number_of_Books_Read', data=df, color="#1f77b4")

# Filling the area under the line
plt.fill_between(x=df['Month'], y1=df['Number_of_Books_Read'], color="#1f77b4", alpha=0.3)

# Annotate
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Number_of_Books_Read'][i] + 0.5, f"{df['Number_of_Books_Read'][i]} books", horizontalalignment='center')

plt.title('Monthly Number of Books Read', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Books Read')

# Show plot
plt.tight_layout()
plt.show()