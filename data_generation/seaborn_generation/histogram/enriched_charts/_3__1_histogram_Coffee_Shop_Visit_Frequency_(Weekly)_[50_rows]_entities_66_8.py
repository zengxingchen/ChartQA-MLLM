
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points for the new topic "Age of Historical Figures at Death"
age_data = [2, 2, 3, 3, 5, 5, 6, 7, 8, 9, 11, 12, 15, 17, 19, 21, 24, 26, 28, 30, 32, 
            35, 37, 40, 42, 45, 47, 50, 52, 55, 57, 60, 62, 65, 67, 70, 72, 75, 77, 
            80, 82, 85, 87, 90, 92, 95, 97, 100]

# Create the DataFrame
df = pd.DataFrame(age_data, columns=['Age'])

# Set the style
sns.set_style('darkgrid')

# Create the histogram
plt.figure(figsize=(14, 8))
sns.histplot(df['Age'], bins=15, color="#ff6347", binwidth=10, kde=True, element="step")

# Customize the plot with title and labels
plt.title('Age of Historical Figures at Death', fontsize=20, pad=20)
plt.xlabel('Age', fontsize=15)
plt.ylabel('Frequency', fontsize=15)

# Show the plot
plt.show()