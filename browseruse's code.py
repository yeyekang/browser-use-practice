import json
import matplotlib.pyplot as plt

# Load movie type counts from the JSON file
with open('movie_type_counts.json', 'r', encoding='utf-8') as f:
    movie_type_counts = json.load(f)

# Prepare data for the pie chart
types = list(movie_type_counts.keys())
counts = list(movie_type_counts.values())

# Create the pie chart
plt.figure(figsize=(10, 8))
plt.pie(counts, labels=types, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Movie Types in Douban TOP100')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Save the pie chart as an image file
plt.savefig('movie_type_pie_chart.png')
plt.show()