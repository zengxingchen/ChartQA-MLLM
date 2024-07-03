
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Income data ranging from 0 to 100000 with varied counts
income_list = list(range(0, 100001, 1000))
data = pd.DataFrame({"income": income_list})

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Set the size of the figure
plt.figure(figsize=(16, 10))

# Create the histogram with modified aesthetics
sns.histplot(data, y='income', bins=50, color='#FF5733', binwidth=2500)

# Set the title of the histogram and labels
plt.title('Income Distribution Analysis', fontsize=22, pad=20)
plt.xlabel('Frequency', fontsize=15)
plt.ylabel('Income', fontsize=15)

# Show the plot
plt.show()