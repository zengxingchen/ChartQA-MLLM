
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Age Group': '18-24', ' Caffeine Intake (mg)': 85},
    {'Age Group': '25-34', ' Caffeine Intake (mg)': 110},
    {'Age Group': '35-44', ' Caffeine Intake (mg)': 105},
    {'Age Group': '45-54', ' Caffeine Intake (mg)': 99},
    {'Age Group': '55-64', ' Caffeine Intake (mg)': 150},
    {'Age Group': '65-74', ' Caffeine Intake (mg)': 70},
    {'Age Group': '75+', ' Caffeine Intake (mg)': 45},
    {'Age Group': '18-24', ' Caffeine Intake (mg)': 120},
    {'Age Group': '25-34', ' Caffeine Intake (mg)': 80},
    {'Age Group': '35-44', ' Caffeine Intake (mg)': 130},
    {'Age Group': '45-54', ' Caffeine Intake (mg)': 95},
    {'Age Group': '55-64', ' Caffeine Intake (mg)': 100},
    {'Age Group': '65-74', ' Caffeine Intake (mg)': 85},
    {'Age Group': '75+', ' Caffeine Intake (mg)': 40},
    {'Age Group': '18-24', ' Caffeine Intake (mg)': 90}
]

# Preprocess the data to sum up caffeine intake for each age group
intake_sums = {}
for entry in data:
    age_group = entry['Age Group']
    intake = entry[' Caffeine Intake (mg)']
    if age_group in intake_sums:
        intake_sums[age_group] += intake
    else:
        intake_sums[age_group] = intake

# Sort the age groups and intakes for consistent plotting
sorted_age_groups = sorted(intake_sums)
sorted_intakes = [intake_sums[age_group] for age_group in sorted_age_groups]

# Creating the histogram
plt.figure(figsize=(10, 7))
bars = plt.bar(sorted_age_groups, sorted_intakes, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'])

# Adding some flair to the plot
plt.title('Total Caffeine Intake by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Caffeine Intake (mg)')
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Adding the data values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

# Show the plot
plt.show()