
import matplotlib.pyplot as plt

# Data
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 
            'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 
            'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025']
revenue = [500, 520, 480, 550, 570, 590, 560, 600, 620, 640, 610, 650]

# Create vertical bar chart with truncated y-axis
plt.figure(figsize=(14, 10))  # Width, Height of the chart
plt.bar(quarters, revenue, color=['#1E90FF', '#32CD32', '#FFD700', '#FF4500', 
                                  '#8A2BE2', '#00FA9A', '#DC143C', '#7FFFD4', 
                                  '#FF1493', '#00BFFF', '#FF6347', '#FF7F50'], 
        width=0.6)  # Width of the bands

# Set the title and labels
plt.title('Quarterly Revenue Data')
plt.xlabel('Quarter')
plt.ylabel('Revenue in Thousands USD')
plt.ylim(450, 700)  # Truncate y-axis starting from 450

# Show the plot
plt.show()