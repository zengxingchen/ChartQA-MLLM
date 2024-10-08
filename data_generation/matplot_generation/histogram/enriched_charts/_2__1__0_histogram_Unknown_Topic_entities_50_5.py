
import matplotlib.pyplot as plt

# Data: Calorie content in food items
calories = [52, 102, 158, 210, 265, 302, 358, 402, 459, 506, 552, 609, 658, 703, 754, 807, 852, 903, 951, 1004, 1062, 1115, 1162, 1215, 1267, 1315, 1368, 1420, 1470, 1526,1572, 1628, 1678, 1730, 1786, 1833, 1887, 1941, 1984, 2035, 2082, 2138, 2183, 2240, 2292, 2338, 2385, 2439, 2486, 2535, 2582, 2635, 2687, 2741, 2790, 2841, 2890, 2945, 2998, 3056, 3101, 3159, 3210, 3261, 3318, 3363, 3411, 3466, 3513, 3562, 3615, 3664, 3711, 3766, 3813, 3864, 3912, 3967, 4016, 4069, 4125, 4171, 4228, 4270, 4330, 4382, 4428, 4477, 4532, 4576, 4635, 4681, 4729, 4785, 4826, 4884, 4930, 4977]

# Create the histogram with the specified modifications
plt.figure(figsize=(12, 6))  # Adjusted size for a horizontal chart
n, bins, patches = plt.hist(calories, bins=20, color='#2E8B57', rwidth=0.8, orientation='horizontal')  # Color scheme & horizontal bars

# Customize histogram
for i, patch in enumerate(patches):
    patch.set_facecolor("#%06x" % ((i * 543210) % 0xFFFFFF))  # Varied colors for each bar

plt.title('Distribution of Calorie Content in Food Items', pad=20)  # Changed topic & title with appropriate padding
plt.ylabel('Calorie Range')  # Adjust for the horizontal histogram
plt.xlabel('Frequency')  # Adjust for the horizontal histogram

# Display the plot
plt.show()