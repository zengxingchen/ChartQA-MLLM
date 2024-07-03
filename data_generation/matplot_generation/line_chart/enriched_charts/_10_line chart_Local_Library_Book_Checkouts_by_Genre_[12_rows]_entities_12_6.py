
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Month': 'January', 'VR Headsets': 400, 'Smartphones': 780, 'Tablets': 560, 'Smartwatches': 420, 'AR Glasses': 200},
    {'Month': 'February', 'VR Headsets': 380, 'Smartphones': 750, 'Tablets': 540, 'Smartwatches': 410, 'AR Glasses': 190},
    {'Month': 'March', 'VR Headsets': 390, 'Smartphones': 770, 'Tablets': 555, 'Smartwatches': 430, 'AR Glasses': 195},
    {'Month': 'April', 'VR Headsets': 410, 'Smartphones': 800, 'Tablets': 575, 'Smartwatches': 450, 'AR Glasses': 205},
    {'Month': 'May', 'VR Headsets': 420, 'Smartphones': 820, 'Tablets': 590, 'Smartwatches': 470, 'AR Glasses': 215},
    {'Month': 'June', 'VR Headsets': 415, 'Smartphones': 815, 'Tablets': 585, 'Smartwatches': 465, 'AR Glasses': 210},
    {'Month': 'July', 'VR Headsets': 430, 'Smartphones': 830, 'Tablets': 600, 'Smartwatches': 480, 'AR Glasses': 220},
    {'Month': 'August', 'VR Headsets': 440, 'Smartphones': 845, 'Tablets': 610, 'Smartwatches': 490, 'AR Glasses': 225},
    {'Month': 'September', 'VR Headsets': 450, 'Smartphones': 860, 'Tablets': 620, 'Smartwatches': 500, 'AR Glasses': 230},
    {'Month': 'October', 'VR Headsets': 460, 'Smartphones': 870, 'Tablets': 630, 'Smartwatches': 510, 'AR Glasses': 235},
    {'Month': 'November', 'VR Headsets': 455, 'Smartphones': 865, 'Tablets': 625, 'Smartwatches': 505, 'AR Glasses': 232},
    {'Month': 'December', 'VR Headsets': 470, 'Smartphones': 880, 'Tablets': 640, 'Smartwatches': 520, 'AR Glasses': 240}
]

# Extracting months
months = [record['Month'] for record in data]

# Extracting data for each technology
vr_headsets = [record['VR Headsets'] for record in data]
smartphones = [record['Smartphones'] for record in data]
tablets = [record['Tablets'] for record in data]
smartwatches = [record['Smartwatches'] for record in data]
ar_glasses = [record['AR Glasses'] for record in data]

# Start plotting
plt.figure(figsize=(14, 9))

# Plotting each technology
plt.plot(months, vr_headsets, label='VR Headsets', marker='o', linestyle='-', color='#1f77b4')
plt.plot(months, smartphones, label='Smartphones', marker='X', linestyle='--', color='#ff7f0e')
plt.plot(months, tablets, label='Tablets', marker='^', linestyle='-.', color='#2ca02c')
plt.plot(months, smartwatches, label='Smartwatches', marker='s', linestyle=':', color='#d62728')
plt.plot(months, ar_glasses, label='AR Glasses', marker='D', linestyle='-', color='#9467bd')

# Adding titles and labels
plt.title('Monthly Sales of Emerging Technologies', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales (Units)')

# Add a legend
plt.legend(loc='upper left')

# Annotate a specific data point
plt.annotate('Peak Sales', xy=('December', 880), xytext=('November', 900),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()