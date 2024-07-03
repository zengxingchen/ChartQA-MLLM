
import matplotlib.pyplot as plt

# Data
therapy_types = [
    "Cognitive Behavioral Therapy (CBT)", 
    "Dialectical Behavior Therapy (DBT)", 
    "Psychodynamic Therapy", 
    "Humanistic Therapy", 
    "Interpersonal Therapy", 
    "Supportive Therapy", 
    "Holistic Therapy", 
    "Existential Therapy", 
    "EMDR Therapy"
]
popularity = [250, 180, 140, 110, 90, 70, 60, 50, 40]

# Colors
colors = [
    "#3498db",  # CBT
    "#e74c3c",  # DBT
    "#f1c40f",  # Psychodynamic
    "#9b59b6",  # Humanistic
    "#2ecc71",  # Interpersonal
    "#e67e22",  # Supportive
    "#1abc9c",  # Holistic
    "#34495e",  # Existential
    "#d35400",  # EMDR
]

# Create pie chart
plt.figure(figsize=(12, 9))  # width and height in inches
plt.pie(popularity, labels=therapy_types, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Popularity of Different Mental Health Therapies in 2023', pad=30)

# Show plot
plt.show()