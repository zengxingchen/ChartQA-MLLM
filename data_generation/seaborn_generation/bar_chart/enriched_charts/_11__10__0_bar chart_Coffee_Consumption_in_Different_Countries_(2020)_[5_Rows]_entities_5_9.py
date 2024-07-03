
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue from Concert Tickets ($1000s)': [120, 95, 130, 140, 160, 200, 220, 210, 180, 170, 150, 135]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 14))

# Plot the revenue
sns.barplot(x="Revenue from Concert Tickets ($1000s)", y="Month", data=df,
            palette=['#5DA5DA', '#FAA43A', '#60BD68', '#F17CB0', '#B2912F', 
                     '#B276B2', '#DECF3F', '#F15854', '#4D4D4D', '#1F77B4', 
                     '#FF7F0E', '#2CA02C'], edgecolor=".6", linewidth=2)

# Customize the axes and title
ax.set_xlabel('Revenue from Concert Tickets ($1000s)')
ax.set_ylabel('Month')
ax.set_title('Monthly Revenue from Concert Tickets')

# Adjust bar height
for container in ax.containers:
    plt.setp(container, height=0.6)

# Show the plot
plt.show()