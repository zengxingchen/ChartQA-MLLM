
import matplotlib.pyplot as plt

# Data
topics = [
    'Cardiovascular Disease', 'Cancer', 'Respiratory Disease', 'Diabetes', 
    'Mental Health', 'Infectious Diseases', 'Neurological Disorders', 
    'Digestive Disorders', 'Musculoskeletal Disorders', 'Genitourinary Disorders', 
    'Dermatological Disorders', 'Ophthalmic Disorders', 'Hematological Disorders', 
    'Endocrine Disorders', 'Immune Disorders'
]
count = [
    800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100
]

# Create horizontal bar chart
plt.figure(figsize=(12, 8))  # Change width and height of the chart
colors = [
    '#FF6347', '#FFA07A', '#FF4500', '#FF8C00', '#FFD700', '#ADFF2F', 
    '#7FFF00', '#32CD32', '#00FF00', '#00FA9A', '#00FFFF', '#4682B4', 
    '#4169E1', '#8A2BE2', '#9400D3'
]

plt.bar(topics, count, color=colors, width=0.6)  # Change direction of chart and bar width

# Customizing the plot
plt.ylabel('Count (in thousands)')
plt.title('Prevalence of Various Health Conditions (2020)', pad=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits to start from a specific value
plt.ylim(100, 850)

plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()