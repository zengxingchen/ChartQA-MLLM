
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the given data
data = {
    'University': ['Harvard', 'MIT', 'Stanford', 'UC Berkeley', 'Oxford', 'Cambridge', 'Columbia', 'Princeton', 'Yale', 'UCLA', 'Imperial College', 'University of Chicago', 'UPenn', 'Caltech', 'NYU', 'University of Toronto', 'ETH Zurich'],
    'Enrollments': [21, 12, 15, 40, 24, 20, 30, 8, 10, 45, 18, 11, 25, 6, 50, 70, 16],
    'AverageTuitionFee': [50000, 53000, 48000, 36000, 41000, 42000, 49000, 47000, 46000, 34000, 43000, 51000, 45000, 55000, 44000, 39000, 42000],
    'InternationalStudentPercentage': [20, 30, 25, 15, 45, 40, 35, 22, 28, 12, 50, 32, 27, 33, 38, 48, 42]
}
df = pd.DataFrame(data)

# Plot the bubble chart
plt.figure(figsize=(16, 9))
bubble_chart = sns.scatterplot(data=df, x='Enrollments', y='AverageTuitionFee', size='InternationalStudentPercentage', sizes=(20, 500), hue='University', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#FFC300', '#DAF7A6', '#900C3F', '#C70039', '#581845', '#C0C0C0', '#808080', '#800000', '#808000', '#00FF00', '#00FFFF', '#000080', '#FF00FF'])

# Customizing the plot
plt.title('University Enrollments and Tuition Fees', fontsize=20)
plt.xlabel('Enrollments (in thousands)', fontsize=14)
plt.ylabel('Average Tuition Fee (in USD)', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Show the plot
plt.tight_layout()
plt.show()