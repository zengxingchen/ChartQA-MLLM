
import matplotlib.pyplot as plt

# Data for plotting
quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022']
product_a = [12000, 18000, 14000, 15000, 16000, 17000, 18000, 19000]
product_b = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000]
product_c = [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000]

# Plotting the stacked area chart
plt.figure(figsize=(10, 6))  # changing width and height of the chart
plt.stackplot(quarters, product_a, product_b, product_c, 
              labels=['Product A', 'Product B', 'Product C'],
              colors=['#FFA07A', '#20B2AA', '#778899'])  # Modify the color scheme

# Adding title and labels
plt.title('Quarterly Sales Data for Products A, B, and C')
plt.xlabel('Quarter')
plt.ylabel('Sales (in USD)')

# Annotation
plt.annotate('Highest for B', xy=(7, 52000), xytext=(7.5, 60000),
             arrowprops=dict(facecolor='#8A2BE2', shrink=0.05))

# Adding legend
plt.legend(loc='upper left')

# Display the plot
plt.show()