
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Assume 'ages_list' contains the full range of ages 0-100 with varied counts for each age
ages_list = [0] + [1]*2 + [2]*3 + [3]*4 + [4]*5 + list(range(5, 99)) * 6 + [98]*2 + [99]*3 + [100]
data = pd.DataFrame({"age": ages_list})

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Set the size of the figure
plt.figure(figsize=(14, 8))

# Create the histogram with modified aesthetics
sns.histplot(data, x='age', bins=40, color='#3366CC', binwidth=2.5)

# Set the title of the histogram and labels
plt.title('Population Age Distribution', fontsize=20)
plt.xlabel('Age', fontsize=15)
plt.ylabel('Frequency', fontsize=15)

# Show the plot
plt.show()