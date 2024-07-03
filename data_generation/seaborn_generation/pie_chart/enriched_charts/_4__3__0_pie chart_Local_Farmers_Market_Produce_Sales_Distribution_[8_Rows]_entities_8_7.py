
import matplotlib.pyplot as plt

# Data
mental_health_services = ["Counseling", "Therapy", "Medication", "Support Groups", "Workshops", "Online Resources", "Crisis Intervention", "Rehabilitation", "Consultations"]
expenditure = [150, 100, 70, 60, 40, 30, 50, 20, 25]

# Colors
colors = [
    "#5DA5DA",  # Counseling
    "#FAA43A",  # Therapy
    "#60BD68",  # Medication
    "#F17CB0",  # Support Groups
    "#B2912F",  # Workshops
    "#B276B2",  # Online Resources
    "#DECF3F",  # Crisis Intervention
    "#F15854",  # Rehabilitation
    "#4D4D4D",  # Consultations
]

# Create pie chart
plt.figure(figsize=(12, 10))  # width and height in inches
plt.pie(expenditure, labels=mental_health_services, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Expenditure on Mental Health Services in 2023', pad=30)

# Show plot
plt.show()