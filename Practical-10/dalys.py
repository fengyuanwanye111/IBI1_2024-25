# // 1. Import necessary libraries
# Import os for file and directory operations
# Import pandas for data manipulation and analysis
# Import matplotlib.pyplot for plotting
# Import numpy for numerical operations

# Import libraries for file operations, data analysis, plotting, and numerical computations
import os              # For interacting with the operating system (e.g., file paths)
import pandas as pd    # For data manipulation and analysis (e.g., DataFrames)
import matplotlib.pyplot as plt  # For creating visualizations (e.g., plots, bar charts)
import numpy as np     # For numerical operations (used indirectly by pandas/matplotlib)

# // 2. Verify working directory and files
# Print current working directory
# Print list of files in the directory

# Verify the working environment
print(os.getcwd())     # Print the current working directory to confirm the path
print(os.listdir())    # List all files in the directory to ensure the CSV file exists

# // 3. Load and explore the dataset
# Load CSV file "dalys-rate-from-all-causes.csv" into a DataFrame
# Display the first 5 rows of the DataFrame
# Display DataFrame info (column names, data types, row count)
# Display statistical summary of numerical columns
# Extract and display the "Year" column for the first 10 rows
# Extract DALYs for the year 1990 and display them

# Extract DALYs for the year 1990
dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]  # Filter rows where Year is 1990, extract DALYs
print(dalys_1990)  # Display the DALYs values for 1990

# // 4. Compare DALYs between the UK and France
# Extract UK data (DALYs and Year) from the DataFrame
# Extract France data (DALYs and Year) from the DataFrame
# Calculate the mean DALYs for the UK
# Calculate the mean DALYs for France
# Print the mean DALYs for both countries

# Compare DALYs between the UK and France
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]  # Extract UK data (DALYs and Year)
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]]  # Extract France data (DALYs and Year)
uk_mean = uk["DALYs"].mean()  # Calculate the mean DALYs for the UK
france_mean = france["DALYs"].mean()  # Calculate the mean DALYs for France
print(f"UK mean DALYs: {uk_mean}, France mean DALYs: {france_mean}")  # Print the mean DALYs for both countries

# // 5. Visualize UK DALYs over time
# Plot a line graph of UK DALYs over years with blue star markers
# Rotate x-axis labels by 90 degrees
# Set x-axis label as "Year"
# Set y-axis label as "DALYs"
# Set plot title as "DALYs in the United Kingdom Over Time"
# Add a legend to the plot
# Display the plot

# Visualize UK DALYs over time
plt.plot(uk.Year, uk.DALYs, 'b*', label="United Kingdom")  # Plot UK DALYs as a line with blue star markers
plt.xticks(uk.Year, rotation=-90)  # Rotate x-axis labels (years) by 90 degrees to avoid overlap
plt.xlabel("Year")  # Set x-axis label
plt.ylabel("DALYs")  # Set y-axis label
plt.title("DALYs in the United Kingdom Over Time")  # Set the plot title
plt.legend()  # Add a legend to show "United Kingdom" label
plt.show()  # Display the plot

# // 6. Custom question: Find countries with DALYs > 100,000 in 1990
# Extract rows where Year is 1990 and DALYs > 100,000, keeping Entity and DALYs columns
# Print the filtered data
# Plot a bar chart of countries with DALYs > 100,000 in 1990
# Rotate x-axis labels by 90 degrees
# Set x-axis label as "Country/Region"
# Set y-axis label as "DALYs"
# Set plot title as "Countries with DALYs > 100,000 in 1990"
# Adjust layout to prevent label cutoff
# Display the plot

# Custom question: Which countries had more than 100,000 DALYs in 1990?
high_daly_1990 = dalys_data.loc[(dalys_data["Year"] == 1990) & (dalys_data["DALYs"] > 100000), ["Entity", "DALYs"]]  # Filter rows for 1990 with DALYs > 100,000
print(high_daly_1990)  # Display the filtered data (countries and their DALYs)
# Visualize the result
plt.bar(high_daly_1990["Entity"], high_daly_1990["DALYs"])  # Create a bar chart of countries vs DALYs
plt.xticks(rotation=-90)  # Rotate x-axis labels (country names) by 90 degrees to avoid overlap
plt.xlabel("Country/Region")  # Set x-axis label
plt.ylabel("DALYs")  # Set y-axis label
plt.title("Countries with DALYs > 100,000 in 1990")  # Set the plot title
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()  # Display the bar chart