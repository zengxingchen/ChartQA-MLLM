
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

books_sold = [150, 180, 210, 250, 220, 230, 240, 260, 270, 290, 310, 330]

# Plotting the area chart
plt.figure(figsize=(14, 7))
plt.fill_between(months, books_sold, color='#1f77b4')

# Adding labels and title
plt.title('Monthly Book Sales Over a Year', pad=20)
plt.xlabel('Month')
plt.ylabel('Books Sold')

# Customizing the grid
plt.grid(True, color='#e6e6e6', linestyle='-', linewidth=0.7, which='both')

# Adjusting the x-axis labels to fit properly
plt.xticks(rotation=45)

# Adding annotations
for i, txt in enumerate(books_sold):
    plt.annotate(txt, (months[i], books_sold[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Show the plot
plt.tight_layout()
plt.show()