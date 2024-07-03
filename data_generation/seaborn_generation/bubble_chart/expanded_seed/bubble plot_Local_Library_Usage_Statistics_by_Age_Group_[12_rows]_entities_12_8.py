
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = [
    {'Age Group': '0-12', 'Month': 'January', 'Checkouts': 120, 'Visits': 80, 'Computer Usage (hours)': 25},
    {'Age Group': '0-12', 'Month': 'February', 'Checkouts': 115, 'Visits': 82, 'Computer Usage (hours)': 30},
    {'Age Group': '13-18', 'Month': 'January', 'Checkouts': 110, 'Visits': 120, 'Computer Usage (hours)': 45},
    {'Age Group': '13-18', 'Month': 'February', 'Checkouts': 105, 'Visits': 125, 'Computer Usage (hours)': 50},
    {'Age Group': '19-25', 'Month': 'January', 'Checkouts': 200, 'Visits': 150, 'Computer Usage (hours)': 70},
    {'Age Group': '19-25', 'Month': 'February', 'Checkouts': 190, 'Visits': 160, 'Computer Usage (hours)': 75},
    {'Age Group': '26-35', 'Month': 'January', 'Checkouts': 180, 'Visits': 140, 'Computer Usage (hours)': 60},
    {'Age Group': '26-35', 'Month': 'February', 'Checkouts': 175, 'Visits': 145, 'Computer Usage (hours)': 65},
    {'Age Group': '36-50', 'Month': 'January', 'Checkouts': 160, 'Visits': 130, 'Computer Usage (hours)': 55},
    {'Age Group': '36-50', 'Month': 'February', 'Checkouts': 155, 'Visits': 135, 'Computer Usage (hours)': 58},
    {'Age Group': '51+', 'Month': 'January', 'Checkouts': 120, 'Visits': 110, 'Computer Usage (hours)': 40},
    {'Age Group': '51+', 'Month': 'February', 'Checkouts': 115, 'Visits': 112, 'Computer Usage (hours)': 42}
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 8))
bubbleplot = sns.scatterplot(
    data=df,
    x="Month", 
    y="Age Group", 
    size="Checkouts", 
    hue="Computer Usage (hours)", 
    sizes=(100, 1000), # Vary sizes from 100 to 1000
    hue_norm=(0, 100), # Normalize the hue to the range of computer usage
    legend="full" 
)

# Adjust legend for sizes
handles, labels = bubbleplot.get_legend_handles_labels()
h_legend = handles[0:2] + handles[3:]  # remove the handle for 'Checkouts'
l_legend = labels[0:2] + labels[3:]   # remove the label for 'Checkouts'
bubbleplot.legend(h_legend, l_legend, loc="upper right", title="Bubble Size: Checkouts\nBubble Color Intensity: Comp. Usage (hours)")

# Additional aesthetic settings
plt.title('Bubble Chart of Library Metrics')
plt.xlabel('Month')
plt.ylabel('Age Group')
plt.tight_layout()
plt.show()