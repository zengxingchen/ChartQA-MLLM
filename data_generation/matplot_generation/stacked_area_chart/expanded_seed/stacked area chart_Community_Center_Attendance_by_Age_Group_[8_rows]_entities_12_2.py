
import matplotlib.pyplot as plt

# Given data
data = [
    {'Month': 'January', 'Children (0-14)': 400, 'Youth (15-24)': 300, 'Adults (25-64)': 450, 'Seniors (65+)': 200},
    {'Month': 'February', 'Children (0-14)': 350, 'Youth (15-24)': 280, 'Adults (25-64)': 430, 'Seniors (65+)': 180},
    {'Month': 'March', 'Children (0-14)': 450, 'Youth (15-24)': 320, 'Adults (25-64)': 500, 'Seniors (65+)': 210},
    {'Month': 'April', 'Children (0-14)': 500, 'Youth (15-24)': 340, 'Adults (25-64)': 520, 'Seniors (65+)': 220},
    {'Month': 'May', 'Children (0-14)': 550, 'Youth (15-24)': 360, 'Adults (25-64)': 540, 'Seniors (65+)': 230},
    {'Month': 'June', 'Children (0-14)': 580, 'Youth (15-24)': 370, 'Adults (25-64)': 560, 'Seniors (65+)': 240},
    {'Month': 'July', 'Children (0-14)': 600, 'Youth (15-24)': 380, 'Adults (25-64)': 580, 'Seniors (65+)': 250},
    {'Month': 'August', 'Children (0-14)': 620, 'Youth (15-24)': 390, 'Adults (25-64)': 600, 'Seniors (65+)': 260},
    {'Month': 'September', 'Children (0-14)': 500, 'Youth (15-24)': 370, 'Adults (25-64)': 570, 'Seniors (65+)': 240},
    {'Month': 'October', 'Children (0-14)': 480, 'Youth (15-24)': 350, 'Adults (25-64)': 550, 'Seniors (65+)': 230},
    {'Month': 'November', 'Children (0-14)': 460, 'Youth (15-24)': 330, 'Adults (25-64)': 530, 'Seniors (65+)': 220},
    {'Month': 'December', 'Children (0-14)': 420, 'Youth (15-24)': 310, 'Adults (25-64)': 490, 'Seniors (65+)': 210}
]

# Extract data for plotting
months = [item['Month'] for item in data]
children = [item['Children (0-14)'] for item in data]
youth = [item['Youth (15-24)'] for item in data]
adults = [item['Adults (25-64)'] for item in data]
seniors = [item['Seniors (65+)'] for item in data]

# Plotting the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(months, children, youth, adults, seniors, 
              labels=['Children (0-14)', 'Youth (15-24)', 'Adults (25-64)', 'Seniors (65+)'],
              colors=['#ff9999','#66b3ff','#99ff99','#ffd700'], alpha=0.8)

# Add titles and labels
plt.title('Population Distribution by Age Group Over Months', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of People', fontsize=14)

# Add a legend
plt.legend(loc='upper left')

# Improve the aesthetics with a grid
plt.grid(True, linestyle='--', color='grey', alpha=0.5)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()