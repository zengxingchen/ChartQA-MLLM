
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Visitors": [350, 380, 420, 460, 500, 550, 600, 580, 520, 480, 400, 370]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type to maintain month order in the plot
df['Month'] = pd.Categorical(df['Month'], categories=[
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"], ordered=True)

# Create the line plot
plt.figure(figsize=(14, 8))
sns.lineplot(x="Month", y="Visitors", data=df, marker='o', color='#1f77b4')

# Annotate each point with the number of visitors
for i in range(df.shape[0]):
    plt.text(x=df['Month'][i], y=df['Visitors'][i] + 10, s=f"{df['Visitors'][i]}",
             horizontalalignment='center')

# Set the title and labels
plt.title('Monthly Visitors to the Art Museum', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

# Show the plot
plt.show()