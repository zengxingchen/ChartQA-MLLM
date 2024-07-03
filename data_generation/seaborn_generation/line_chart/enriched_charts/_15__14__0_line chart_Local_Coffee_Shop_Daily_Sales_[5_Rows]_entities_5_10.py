
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Hours": [20, 25, 30, 35, 40, 45, 50, 48, 42, 38, 33, 28]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type to maintain month order in the plot
df['Month'] = pd.Categorical(df['Month'], categories=[
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"], ordered=True)

# Create the line plot
plt.figure(figsize=(16, 10))
sns.lineplot(x="Month", y="Hours", data=df, marker='o', color='#ff5733')

# Annotate each point with the number of hours
for i in range(df.shape[0]):
    plt.text(x=df['Month'][i], y=df['Hours'][i] + 2, s=f"{df['Hours'][i]}",
             horizontalalignment='center')

# Set the title and labels
plt.title('Monthly Meditation Hours', pad=20, loc='center')
plt.xlabel('Month')
plt.ylabel('Hours of Meditation')

# Show the plot
plt.show()