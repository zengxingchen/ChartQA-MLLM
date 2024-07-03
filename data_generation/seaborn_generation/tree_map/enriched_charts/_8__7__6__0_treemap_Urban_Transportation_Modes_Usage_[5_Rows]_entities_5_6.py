
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Category': ['Mental Health', 'Physical Fitness', 'Nutrition', 'Medical Research', 'Healthcare Services', 
                 'Therapy and Counseling', 'Preventive Care', 'Wellness Programs', 'Pharmaceuticals', 'Public Health', 
                 'Alternative Medicine', 'Healthcare Technology', 'Chronic Disease Management', 'Health Insurance', 
                 'Rehabilitation', 'Personal Health Devices', 'Emergency Services', 'Home Health Care', 'Elderly Care', 
                 'Vaccination Programs', 'Sleep Science', 'Digital Health', 'Health Education', 'Telemedicine', 
                 'Occupational Health', 'Patient Advocacy', 'Disease Prevention', 'Clinical Trials', 'Addiction Treatment', 
                 'Health Policy', 'Medical Equipment'],
    'Investment': [400, 390, 380, 370, 360, 350, 340, 330, 320, 310, 300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 
                   200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100]
})

# Custom colors for the treemap
colors = ['#FF4500', '#FFD700', '#00FA9A', '#1E90FF', '#FF69B4', '#8A2BE2', '#00CED1', '#FF6347', '#ADFF2F', '#FF1493',
          '#7FFF00', '#7B68EE', '#FF7F50', '#4682B4', '#DDA0DD', '#32CD32', '#FF00FF', '#EE82EE', '#00FF7F', '#6A5ACD',
          '#8B0000', '#FFFF00', '#008000', '#00BFFF', '#FF00FF', '#4B0082', '#20B2AA', '#FF4500', '#9ACD32', '#FF6347',
          '#6B8E23']

# Create a figure and a set of subplots
plt.figure(figsize=(24, 14))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Investment'], label=df['Category'], color=colors, alpha=0.8)

plt.title("Investment Distribution in Health & Psychology", fontsize=26, fontweight='bold', y=1.05)
plt.axis('off')  # Disable the axis

plt.show()