
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Data in CSV format
csv_data = """Daily Exercise Minutes
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
100
105
110
115
120
125
130
135
140
145
150
155
160
165
170
175
180
185
190
195
200
205
210
215
220
225
230
235
240
245
250
255
260
265
270
275
280
285
290
295
300
"""

# Reading data into a pandas DataFrame
data = pd.read_csv(StringIO(csv_data))

# Set figure size
plt.figure(figsize=(12, 6))

# Create a horizontal histogram
sns.histplot(data['Daily Exercise Minutes'], 
             color="#1E90FF", 
             binwidth=10, 
             binrange=(0, 300),
             orientation='horizontal')

# Additional modifications for aesthetics
plt.title('Distribution of Daily Exercise Minutes')
plt.xlabel('Frequency')
plt.ylabel('Daily Exercise Minutes')
sns.despine()

# Display the plot
plt.show()