
import matplotlib.pyplot as plt

# Data for scatterplot
methods = ["Radial Velocity", "Transit", "Direct Imaging", "Gravitational Microlensing", 
           "Astrometry", "Pulsar Timing", "Transit Timing Variations", "Orbital Brightness Modulations", 
           "Eclipse Timing Variations", "Variations in Star's Spectrum", "X-ray Eclipse", 
           "Orbital Phase Curve"]
known_exoplanets = [32, 83, 12, 24, 6, 8, 5, 3, 4, 10, 2, 1]
discovery_year = [1995, 2003, 2008, 2004, 2009, 1992, 2011, 2013, 2012, 2010, 2014, 2015]

# Size of each point will be proportional to the known exoplanets
sizes = [exoplanets * 10 for exoplanets in known_exoplanets]

# Different colors for different methods
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', 
          '#f781bf', '#999999', '#66c2a5', '#fc8d62', '#8da0cb']

# Create scatterplot
plt.figure(figsize=(16, 10))  # Adjust width and height for better visual
plt.scatter(methods, discovery_year, s=sizes, c=colors, alpha=0.8)

# Chart details
plt.title('Known Exoplanets and Discovery Years by Method', fontsize=15, pad=20)
plt.xlabel('Discovery Method')
plt.ylabel('Discovery Year')
plt.xticks(rotation=45, ha='right')
plt.grid(True)

# Show the chart
plt.show()