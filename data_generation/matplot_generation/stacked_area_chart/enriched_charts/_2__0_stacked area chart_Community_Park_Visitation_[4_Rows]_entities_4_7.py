
import matplotlib.pyplot as plt

# Data for plotting
quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022',
            'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023',
            'Q1 2024', 'Q2 2024']
streaming_a = [12000, 18000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000]
streaming_b = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000]
streaming_c = [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000]

# Plotting the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(quarters, streaming_a, streaming_b, streaming_c, 
              labels=['Streaming Service A', 'Streaming Service B', 'Streaming Service C'],
              colors=['#FF6347', '#4682B4', '#32CD32'])

# Adding title and labels
plt.title('Quarterly Revenue from Streaming Services', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Revenue (in USD)')

# Annotation
plt.annotate('Steady Increase', xy=(12, 76000), xytext=(10, 85000),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Adding legend
plt.legend(loc='upper left')

# Display the plot
plt.show()