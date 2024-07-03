
import matplotlib.pyplot as plt

data = {
    'Category': ["Electric Vehicles", "Renewable Energy", "AI Research", "Quantum Computing", "Biotech",
                 "Robotics", "Space Exploration", "Blockchain", "Cybersecurity", "5G Technology", 
                 "Nanotechnology", "Green Construction", "Advanced Materials", "Autonomous Vehicles",
                 "Smart Cities", "Wearable Tech", "Genomics", "Edge Computing", "3D Printing", "IoT",
                 "Synthetic Biology", "VR/AR", "Agritech", "Precision Medicine", "Energy Storage"],
    'Funding Amount ($M)': [300, 250, 500, 400, 350, 200, 450, 150, 100, 180, 220, 270, 310, 380, 240, 130, 360, 190, 210, 260, 330, 140, 230, 280, 320],
    'Success Rate (%)': [85, 88, 92, 80, 87, 75, 90, 65, 72, 78, 85, 83, 89, 80, 82, 70, 90, 77, 75, 82, 88, 65, 84, 92, 86],
    'Duration (years)': [5, 6, 7, 8, 7, 4, 9, 3, 5, 4, 6, 6, 7, 8, 5, 3, 7, 4, 5, 6, 7, 4, 6, 7, 7]
}

size = [value * 2 for value in data['Funding Amount ($M)']]

plt.figure(figsize=(18, 12))

scatter = plt.scatter(data['Success Rate (%)'], data['Duration (years)'],
                      s=size, alpha=0.6, 
                      c=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', '#FF8F33', 
                         '#33FFD7', '#FF3333', '#33FF8F', '#8F33FF', '#FF5733', '#33FFA1', '#FF338F',
                         '#A1FF33', '#FF5733', '#338FFF', '#FFA133', '#33FF57', '#FF338F', '#33A1FF',
                         '#FF57A1', '#33FFA1', '#FF3333', '#57FF33'])

plt.title('Funding and Success Rate of Future Technologies', pad=20)
plt.xlabel('Success Rate (%)')
plt.ylabel('Duration (years)')

for index, category in enumerate(data['Category']):
    plt.text(data['Success Rate (%)'][index], data['Duration (years)'][index],
             category, fontsize=9, ha='center', va='center')

plt.grid(True)
plt.show()