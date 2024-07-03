
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided as a list of dictionaries
data = [
    {'Month': 'January', 'Members': 30},
    {'Month': 'February', 'Members': 35},
    {'Month': 'March', 'Members': 37},
    {'Month': 'April', 'Members': 45},
    {'Month': 'May', 'Members': 50},
    {'Month': 'June', 'Members': 55},
    {'Month': 'July', 'Members': 60},
    {'Month': 'August', 'Members': 65},
    {'Month': 'September', 'Members': 70},
    {'Month': 'October', 'Members': 75},
    {'Month': 'November', 'Members': 80},
    {'Month': 'December', 'Members': 90}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Convert 'Month' column to categorical type with proper order for plotting
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

# Start the plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# Create line plot
line = sns.lineplot(x='Month', y='Members', data=df, sort=False, marker='o')

# Get the current axis for additional plotting
ax = plt.gca()

# Fill the area under the plot
ax.fill_between(df['Month'], df['Members'], color='skyblue', alpha=0.4)

# Beautify the plot
ax.set_title('Monthly Membership Growth')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Members')

# Show the final plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()