
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [200, 210, 190, 220, 230, 215, 205, 202, 218, 230, 210, 220]

# Create horizontal bar chart
plt.figure(figsize=(12, 8))  # Width, Height of the chart
plt.barh(months, sales, color=['#FFA07A', '#20B2AA', '#778899', '#7FFF00', '#DC143C', '#FF8C00', 
                               '#00FFFF', '#ADFF2F', '#FF69B4', '#8A2BE2', '#A0522D', '#6495ED'], 
         height=0.5)  # Height of the bands

# Set the title and labels
plt.title('Monthly Sales Data')
plt.xlabel('Sales in USD')
plt.ylabel('Month')

# Show the plot
plt.show()