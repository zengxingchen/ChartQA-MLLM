
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# CSV data as provided
csv_data = """Day,City A,City B
1,16,14
2,17,14
3,19,15
4,21,17
5,20,16
6,22,18
7,23,17
8,25,19
9,26,22
10,27,22
11,24,20
12,23,21
13,25,22
14,24,21
15,26,23
16,28,22
17,27,24
18,26,23
19,28,25
20,29,26
21,30,27
22,29,26
23,28,27
24,27,25
25,26,24
26,28,25
27,29,27
28,31,28
29,30,28
30,28,26
31,27,25"""

# Read data into a pandas DataFrame
data = pd.read_csv(StringIO(csv_data))

# Create figure and plot
fig, ax = plt.subplots(figsize=(12, 6))

# Fill areas under the lines
ax.fill_between(data['Day'], data['City A'], color="#FF5733", alpha=0.5, label='City A Avg Temp')
ax.fill_between(data['Day'], data['City B'], color="#33D7FF", alpha=0.5, label='City B Avg Temp')

# Labels and Titles
ax.set_xlabel('Day of the Month', fontsize=12)
ax.set_ylabel('Average Daily Temperature (°C)', fontsize=12)
ax.set_title('Average Daily Temperatures in City A and City B Over a Month', fontsize=16)

# Legend
ax.legend()

# Display
plt.show()