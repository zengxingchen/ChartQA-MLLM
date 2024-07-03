
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data as a list of dictionaries
data = [
    {'Product': 'Espresso', 'Customer Age Group': '18-25', 'Average Rating (out of 5)': 4.5},
    {'Product': 'Espresso', 'Customer Age Group': '26-35', 'Average Rating (out of 5)': 4.0},
    {'Product': 'Espresso', 'Customer Age Group': '36-50', 'Average Rating (out of 5)': 4.3},
    {'Product': 'Latte', 'Customer Age Group': '18-25', 'Average Rating (out of 5)': 4.7},
    {'Product': 'Latte', 'Customer Age Group': '26-35', 'Average Rating (out of 5)': 4.5},
    {'Product': 'Latte', 'Customer Age Group': '36-50', 'Average Rating (out of 5)': 4.6},
    {'Product': 'Cappuccino', 'Customer Age Group': '18-25', 'Average Rating (out of 5)': 4.4},
    {'Product': 'Cappuccino', 'Customer Age Group': '26-35', 'Average Rating (out of 5)': 4.2},
    {'Product': 'Cappuccino', 'Customer Age Group': '36-50', 'Average Rating (out of 5)': 4.3},
    {'Product': 'Mocha', 'Customer Age Group': '18-25', 'Average Rating (out of 5)': 4.8},
    {'Product': 'Mocha', 'Customer Age Group': '26-35', 'Average Rating (out of 5)': 4.6},
    {'Product': 'Mocha', 'Customer Age Group': '36-50', 'Average Rating (out of 5)': 4.4}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Set up the markers for each age group
markers = {"18-25": "o", "26-35": "s", "36-50": "X"}

# Create a scatter plot
sns.scatterplot(data=df, x='Product', y='Average Rating (out of 5)', 
                style='Customer Age Group', hue='Customer Age Group', 
                palette='deep', markers=markers, s=100)

# Enhance the plot to make it more readable
plt.title('Average Product Rating by Age Group')
plt.xlabel('Product')
plt.ylabel('Average Rating (out of 5)')
plt.legend(title='Customer Age Group', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels

# Show the plot
plt.show()