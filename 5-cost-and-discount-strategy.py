# Import the necessary libraries for data manipulation and visualization.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a pandas DataFrame from a CSV file named 'Train.csv'.
# This assumes that 'Train.csv' is located in the same directory as the script.
data = pd.read_csv('Train.csv')

# Create a scatter plot to analyze the relationship between the cost of the product and the discount offered.
# The figure size is set to 14 inches wide by 6 inches tall for clarity.
plt.figure(figsize=(14, 6))
# Use seaborn's scatterplot function to plot 'Cost_of_the_Product' on the x-axis and 'Discount_offered' on the y-axis.
# The 'data' parameter specifies the DataFrame to use for plotting.
sns.scatterplot(x='Cost_of_the_Product', y='Discount_offered', data=data)
# Set the title of the scatter plot to 'Relationship Between Cost of Product and Discount Offered'.
plt.title('Relationship Between Cost of Product and Discount Offered')
# Label the x-axis as 'Cost of the Product (USD)'.
plt.xlabel('Cost of the Product (USD)')
# Label the y-axis as 'Discount Offered (%)'.
plt.ylabel('Discount Offered (%)')
# Display the plot. This is necessary for non-interactive environments to render the plot.
plt.show()

# Calculate the Pearson correlation coefficient between 'Discount_offered' and 'Customer_rating'.
# This measures the linear relationship between the discount offered and customer satisfaction rating.
discount_satisfaction_corr = data['Discount_offered'].corr(data['Customer_rating'])

# Calculate the Pearson correlation coefficient between 'Discount_offered' and 'Reached.on.Time_Y.N'.
# This measures the linear relationship between the discount offered and whether the delivery was on time.
discount_delivery_corr = data['Discount_offered'].corr(data['Reached.on.Time_Y.N'])

# Print out the correlation coefficients with an explanatory message.
# This will display how the discount correlates with customer satisfaction and delivery timeliness.
print(f"Correlation between Discount Offered and Customer Satisfaction: {discount_satisfaction_corr}")
print(f"Correlation between Discount Offered and Delivery Timeliness: {discount_delivery_corr}")
