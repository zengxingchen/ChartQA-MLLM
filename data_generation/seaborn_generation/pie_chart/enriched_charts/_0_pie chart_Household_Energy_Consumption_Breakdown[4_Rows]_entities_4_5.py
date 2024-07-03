
import matplotlib.pyplot as plt
import seaborn as sns

# Data for the pie chart
data = {
    'Programming Language': [
        'Python', 'Java', 'JavaScript', 'C#', 'PHP',
        'C++', 'TypeScript', 'Ruby', 'Swift', 'Objective-C',
        'Kotlin', 'Rust', 'Dart', 'Scala', 'Perl'
    ],
    'Usage Percentage': [
        30.3, 17.6, 8.2, 7.3, 5.8,
        5.5, 4.5, 3.3, 3.1, 2.9,
        2.6, 2.5, 2.3, 1.3, 1.2
    ]
}

# Colors for the pie chart
colors = [
    '#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF66B2',
    '#C4C4C4', '#FFD700', '#C0C0C0', '#FFA500', '#87CEEB',
    '#DA70D6', '#32CD32', '#6495ED', '#FF4500', '#D2691E'
]

# Create a pie chart
plt.figure(figsize=(10, 8))
plt.pie(data['Usage Percentage'], labels=data['Programming Language'], colors=colors, autopct='%1.1f%%')

# Set the chart title and axis equal to have a perfect circle
plt.title('Programming Language Usage Percentage', pad=20)
plt.axis('equal')

# Show the plot
plt.show()