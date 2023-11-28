# Import pandas for data manipulation and matplotlib for data visualization.
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file into a pandas DataFrame.
# The dataset is named 'Train.csv' and should be located in the same directory as the script.
data = pd.read_csv('Train.csv')

# Perform gender analysis by grouping the data by the 'Gender' column.
# Aggregate functions are applied to calculate the mean (average) values for cost, discount offered,
# prior purchases, and customer rating for each gender.
gender_analysis = data.groupby('Gender').agg({
    'Cost_of_the_Product': 'mean',  # Average cost of the product by gender
    'Discount_offered': 'mean',     # Average discount offered by gender
    'Prior_purchases': 'mean',      # Average number of prior purchases by gender
    'Customer_rating': 'mean'       # Average customer rating by gender
}).reset_index()

# Plot the results of the gender analysis using a bar chart for better visualization.
# The index is set to 'Gender' so that gender categories are displayed on the x-axis.
gender_analysis.set_index('Gender').plot(kind='bar')
plt.title('Gender Analysis on Purchasing Habits and Satisfaction')  # Title of the plot
plt.ylabel('Average Values')  # Label for the y-axis
plt.show()  # Display the plot

# Proceed to analyze customer loyalty based on the number of prior purchases.
# A new column 'Customer_Type' is created in the DataFrame, marking customers as 'New' or 'Repeat'.
# This is determined by whether they have only one prior purchase ('New') or more ('Repeat').
data['Customer_Type'] = data['Prior_purchases'].apply(lambda x: 'New' if x == 1 else 'Repeat')

# Group the data by the new 'Customer_Type' column to compare the average customer rating
# and the average on-time delivery rate for new versus repeat customers.
loyalty_analysis = data.groupby('Customer_Type').agg({
    'Customer_rating': 'mean',  # Average customer rating by customer type
    'Reached.on.Time_Y.N': 'mean'  # Average on-time delivery rate by customer type
}).reset_index()

# Plot the results of the loyalty analysis using a bar chart to show the differences.
# 'Customer_Type' is set as the index for the x-axis.
loyalty_analysis.set_index('Customer_Type').plot(kind='bar', figsize=(10, 5))
plt.title('Customer Loyalty Analysis')  # Title of the plot
plt.ylabel('Average Rating and On-Time Delivery Rate')  # Label for the y-axis
plt.show()  # Display the plot
