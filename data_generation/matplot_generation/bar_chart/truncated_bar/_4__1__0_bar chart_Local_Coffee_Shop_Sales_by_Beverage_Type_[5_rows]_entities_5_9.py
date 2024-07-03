
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
steps = [12000, 15000, 10000, 18000, 16000, 17000, 14000, 
         15500, 16200, 13000, 17500, 18500, 16000, 15000]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the bar chart
ax.barh(days, steps, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', 
                            '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], height=0.4)

# Customizing the plot (labels, title, etc.)
ax.set_xlabel('Steps Taken')
ax.set_title('Daily Steps Count Over Two Weeks', pad=20)
ax.set_xlim([9000, 19000])

# Display the plot
plt.tight_layout()
plt.show()