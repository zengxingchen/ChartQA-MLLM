
import matplotlib.pyplot as plt
import numpy as np

# Your table data
data = [
    {'Age Group': '0-12', 'January': 0, 'Adult Section': 120, 'January.1': 0, "Children's Section": 140, 'February': np.nan, 'Adult Section.1': np.nan, 'February.1': np.nan, "Children's Section.1": np.nan},
    {'Age Group': '13-17', 'January': 40, 'Adult Section': 80, 'January.1': 45, "Children's Section": 90, 'February': np.nan, 'Adult Section.1': np.nan, 'February.1': np.nan, "Children's Section.1": np.nan},
    # ... other data rows
]

# Extracting data
age_groups = [d['Age Group'] for d in data]
january_adults = np.nan_to_num([d['Adult Section'] for d in data])
january_children = np.nan_to_num([d["Children's Section"] for d in data])

# Setting up the figure size
plt.figure(figsize=(10, 6))

# Stacking bars: first the Adult section, then the Children's on top
plt.bar(age_groups, january_adults, label='Adult Section')
plt.bar(age_groups, january_children, bottom=january_adults, label="Children's Section")

# Adding title and labels
plt.title('Visitor Counts in January (by Age Group)')
plt.xlabel('Age Group')
plt.ylabel('Number of Visitors')

# Adding a legend
plt.legend()

# Showing the final plot
plt.show()