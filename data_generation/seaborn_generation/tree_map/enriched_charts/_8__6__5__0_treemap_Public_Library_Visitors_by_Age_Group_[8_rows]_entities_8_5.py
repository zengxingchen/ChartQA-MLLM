
import matplotlib.pyplot as plt
import squarify

conditions = [
    "Heart_Disease", "Diabetes", "Cancer", "Stroke", "Chronic_Respiratory_Disease",
    "Alzheimer's_Disease", "Kidney_Disease", "Septicemia", "Liver_Disease", "Hypertension",
    "Osteoporosis", "Parkinson's_Disease", "Asthma", "Arthritis", "Epilepsy",
    "Migraine", "Depression", "Anxiety", "Obesity", "HIV/AIDS",
    "Tuberculosis", "Malaria", "Hepatitis", "Influenza", "Pneumonia", "Chickenpox"
]

prevalence = [
    1500, 1300, 1100, 900, 800, 700, 600, 500, 400, 350,
    300, 250, 220, 200, 180, 160, 140, 120, 100, 90,
    80, 70, 60, 50, 40, 30
]

color_palette = [
    '#FF4500', '#32CD32', '#4682B4', '#FFD700', '#8A2BE2', '#FF69B4', '#7FFFD4',
    '#FF6347', '#40E0D0', '#EE82EE', '#8B0000', '#00FA9A', '#1E90FF', '#D2691E',
    '#FF00FF', '#00BFFF', '#ADFF2F', '#DC143C', '#FF1493', '#7CFC00',
    '#FF8C00', '#9932CC', '#00CED1', '#FF4500', '#DA70D6', '#B22222'
]

plt.figure(figsize=(22, 14))

squarify.plot(sizes=prevalence, label=conditions, color=color_palette, alpha=0.8)

plt.title('Prevalence of Various Health Conditions', fontsize=26, fontweight='bold', pad=30)
plt.axis('off')

plt.show()