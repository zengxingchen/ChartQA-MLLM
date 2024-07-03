
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# CSV data
csv_data = """Day,Steps Walked
1,12000
2,11500
3,13000
4,12500
5,13500
6,14000
7,14500
8,15000
9,16000
10,15500
11,16500
12,17000
13,17500
14,18000
15,18500
16,19000
17,19500
18,20000
19,20500
20,21000
21,21500
22,22000
23,22500
24,23000
25,23500
26,24000
27,24500
28,25000
29,25500
30,26000
31,26500"""

# Read data into a pandas DataFrame
data = pd.read_csv(StringIO(csv_data))

# Create figure and plot
fig, ax = plt.subplots(figsize=(14, 7))

# Fill area under the line
ax.fill_between(data['Day'], data['Steps Walked'], color="#76C1FA", alpha=0.7, label='Steps Walked')

# Labels and Titles
ax.set_xlabel('Day of the Month', fontsize=14)
ax.set_ylabel('Number of Steps', fontsize=14)
ax.set_title('Daily Steps Walked Over a Month', fontsize=18, pad=20)

# Annotations
for i in range(0, len(data), 5):
    ax.text(data['Day'][i], data['Steps Walked'][i], str(data['Steps Walked'][i]), fontsize=10, verticalalignment='bottom')

# Legend
ax.legend(loc='upper left')

# Display
plt.show()