# Import necessary libraries for data handling and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a pandas DataFrame
# The CSV file 'Train.csv' is expected to be in the same directory as this script, or the path needs to be provided.
data = pd.read_csv('Train.csv')

# Calculate and print the correlation matrix for selected features.
# This matrix will show how 'Customer_rating', 'Cost_of_the_Product', 'Discount_offered', and 'Customer_care_calls'
# correlate with each other, with values ranging from -1 (perfect negative correlation) to 1 (perfect positive correlation).
correlation_matrix = data[['Customer_rating', 'Cost_of_the_Product', 'Discount_offered', 'Customer_care_calls']].corr()
print(correlation_matrix)

# Create pairplot visualizations to see the relationships between the selected features.
# Pairplot will plot scatter plots for each pair of variables in the list, along with a histogram for each individual variable.
# This visual aid is a powerful tool for spotting trends, correlations, and outliers in the dataset.
sns.pairplot(data, vars=['Customer_rating', 'Cost_of_the_Product', 'Discount_offered', 'Customer_care_calls'])

# Display the pairplot using matplotlib's show function.
# This line is required to display the plot when using certain Python environments or if the plot does not show automatically.
plt.show()
