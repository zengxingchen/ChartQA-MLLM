
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Data in CSV format
csv_data = """Listening Hours
2
5
5
6
7
8
8
9
10
11
12
12
13
14
14
15
16
17
18
18
19
20
21
21
22
23
24
25
25
26
27
28
29
30
31
31
32
33
34
35
36
37
38
38
39
40
41
42
43
44
45
46
47
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
"""

# Reading data into a pandas DataFrame
data = pd.read_csv(StringIO(csv_data))

# Set figure size
plt.figure(figsize=(10, 8))

# Create a vertical histogram
sns.histplot(data['Listening Hours'], 
             color="#8A2BE2", 
             binwidth=3, 
             binrange=(0, 90),
             orientation='vertical')

# Additional modifications for aesthetics
plt.title('Distribution of Listening Hours per Week')
plt.xlabel('Listening Hours')
plt.ylabel('Frequency')
sns.despine()

# Display the plot
plt.show()