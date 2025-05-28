# dalys.py

# Pseudocode:
# BEGIN
#   // 1. Import necessary libraries
#   Import os for file and directory operations
#   Import pandas for data manipulation and analysis
#   Import matplotlib.pyplot for plotting
#   Import numpy for numerical operations (though not directly used, it's good practice for data science scripts)

#   // 2. Set up environment and load data
#   (Optional: Change current working directory if CSV is in a subdirectory)
#   Load the "dalys-rate-from-all-causes.csv" file into a pandas DataFrame called dalys_data
#   Verify successful loading by printing current working directory and listing files (optional, for debugging)

#   // 3. Initial data exploration (as per Practical Guide & Portfolio)
#   Display the first 5 rows of dalys_data using head()
#   Display concise summary of dalys_data using info()
#   Display descriptive statistics of dalys_data using describe()
#   Add comments based on describe() output (Max DALYs, Min DALYs, First Year, Last Year)

#   // 4. Specific data extraction using iloc and loc (as per Practical Guide & Portfolio)
#   Display the value at the first row, fourth column using iloc[0,3]
#   Display row at index 2, all columns using iloc[2,:]
#   Display first 2 rows, all columns using iloc[0:2,:]
#   Display rows 0 to 9 (exclusive), step 2; all columns using iloc[0:10:2,:]
#   (Portfolio) Display the third column (Year) for the first 10 rows (inclusive) using iloc[0:10, 2]
#   (Portfolio) Find and comment on the 10th year DALYs were recorded for Afghanistan
#   (Optional example) Demonstrate iloc with a boolean list for column selection
#   (Optional example) Demonstrate loc for selecting specific rows and a named column (e.g., dalys_data.loc[2:4, "Year"])

#   // 5. Answer specific questions (as per Practical Guide & Portfolio)
#   (Portfolio) Extract DALYs for all countries in the year 1990 using loc and boolean indexing
#   Print these 1990 DALYs values

#   // 6. Compare DALYs between the UK and France
#   Extract data for "United Kingdom" (DALYs and Year columns) into a new DataFrame 'uk'
#   Extract data for "France" (DALYs and Year columns) into a new DataFrame 'france'
#   Calculate the mean DALYs for 'uk'
#   Calculate the mean DALYs for 'france'
#   Print both mean DALYs
#   (Portfolio) Add a comment/print statement comparing if UK's mean DALYs is greater/smaller than France's

#   // 7. Visualize UK DALYs over time
#   Create a plot of UK DALYs (uk.DALYs) against Year (uk.Year)
#   Use blue star markers ('b*') for the plot
#   Rotate x-axis (Year) labels for better readability
#   Set appropriate xlabel, ylabel, and title for the plot
#   Add a legend
#   Display the plot
#   (Optional: Save the plot to a file)

#   // 8. Address a custom question (as per Practical Guide & Portfolio)
#   Define a custom question (e.g., "Which countries had DALYs > 100,000 in 1990?")
#   Filter dalys_data to find rows matching the criteria for the custom question
#   Print the resulting data (e.g., Entity and DALYs for these countries)
#   Create a plot (e.g., bar chart) to visualize the answer to the custom question
#   Set appropriate labels, title for the plot
#   Display the plot
#   (Optional: Save the plot to a file)
#   (Remember to create question.txt file separately)
# END


# 1. Import necessary libraries
import os                          # For interacting with the operating system (e.g., changing directory, listing files)
import pandas as pd                # For data manipulation and analysis, especially DataFrames
import matplotlib.pyplot as plt      # For creating static, interactive, and animated visualizations
import numpy as np                 # For numerical operations (often used by pandas and matplotlib under the hood)

# 2. Set up environment and load data
# It's generally better to ensure your script and CSV are in the same directory,
# or to use full paths if they are not. os.chdir can make scripts less portable.
# However, following the practical's suggestion if you've placed the CSV in a specific subdirectory:
try:
    # Attempt to change to the directory where the CSV is expected to be
    # Adjust "Practical-10" if your directory structure is different
    # or if the script itself is already in "Practical-10"
    if "Practical-10" not in os.getcwd(): # Check if not already in the target directory
        os.chdir("Practical-10")
    print(f"Changed working directory to: {os.getcwd()}")
except FileNotFoundError:
    print(f"Error: Could not change directory to 'Practical-10'. Make sure it exists relative to script location: {os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()}")
    exit() # Exit if directory change fails

# Verify the working environment (optional, for debugging)
print(f"Current Working Directory: {os.getcwd()}")
print(f"Files in CWD: {os.listdir('.')}") # List files in the current directory

# Load the dataset
csv_file_name = "dalys-rate-from-all-causes.csv"
try:
    dalys_data = pd.read_csv(csv_file_name)
    print(f"\nSuccessfully loaded '{csv_file_name}'")
except FileNotFoundError:
    print(f"\nError: The file '{csv_file_name}' was not found in the directory '{os.getcwd()}'.")
    print("Please make sure the CSV file is in the correct location or update the path.")
    exit() # Exit if file loading fails

# 3. Initial data exploration
print("\n--- Initial Data Exploration ---")
# Display the first 5 rows of the DataFrame
print("\nFirst 5 rows of the dataset (dalys_data.head()):")
print(dalys_data.head(5))

# Display DataFrame info (column names, data types, non-null counts, memory usage)
print("\nDataFrame Info (dalys_data.info()):")
dalys_data.info()

# Display statistical summary of numerical columns
print("\nStatistical Summary (dalys_data.describe()):")
print(dalys_data.describe())
# Portfolio-related comments based on describe() output:
# After running, observe the output of dalys_data.describe()
# Max DALYs: [Inspect 'max' row for 'DALYs' column from describe() output and fill in]
# Min DALYs: [Inspect 'min' row for 'DALYs' column from describe() output and fill in]
# First Year DALYs recorded: [Inspect 'min' row for 'Year' column from describe() output and fill in]
# Last Year DALYs recorded: [Inspect 'max' row for 'Year' column from describe() output and fill in]

# 4. Specific data extraction using iloc and loc
print("\n--- Specific Data Extraction ---")
# Display the value at the first row, fourth column (0-indexed column 3 is DALYs)
print("\nValue at first row, fourth column (dalys_data.iloc[0,3]):")
print(dalys_data.iloc[0,3]) # This is the DALYs value for Afghanistan in 1990.

# Display row at index 2 (third row), all columns (0 to 3, as there are 4 columns)
print("\nRow at index 2, all columns (dalys_data.iloc[2,:]):")
print(dalys_data.iloc[2,:]) # Shows 'Entity', 'Code', 'Year', 'DALYs' for the 3rd entry

# Display first 2 rows, all columns
print("\nFirst 2 rows, all columns (dalys_data.iloc[0:2,:]):")
print(dalys_data.iloc[0:2,:])

# Display rows 0 to 9 (exclusive of 10), every second row; columns 0 to 4 (exclusive of 5)
# Since there are 4 columns (0,1,2,3), let's show all of them.
print("\nRows 0, 2, 4, 6, 8; all columns (dalys_data.iloc[0:10:2,:]):")
print(dalys_data.iloc[0:10:2,:])

# Portfolio Requirement: Show the third column (the year) for the first 10 rows (inclusive).
# The 'Year' column is the 3rd column, so index 2. Rows 0 to 9 (inclusive).
print("\nThird column (Year) for the first 10 rows (dalys_data.iloc[0:10, 2]):")
year_first_10_rows = dalys_data.iloc[0:10, 2]
print(year_first_10_rows)

# Portfolio Requirement: Comment stating what was the 10th year with DALYs data recorded in Afghanistan.
afghanistan_data = dalys_data[dalys_data['Entity'] == 'Afghanistan'] # Filter for Afghanistan
if len(afghanistan_data) >= 10:
    # The 10th record for Afghanistan is at iloc index 9
    tenth_year_afghanistan_dalys = afghanistan_data.iloc[9]['Year']
    print(f"\nThe 10th year for which DALYs were recorded in Afghanistan is: {tenth_year_afghanistan_dalys}")
    # Comment for portfolio: The 10th year with DALYs data recorded in Afghanistan is 1999.
else:
    print("\nAfghanistan has fewer than 10 DALYs records in this dataset.")

# Example of using iloc with a Boolean list (from practical guide)
print("\nUsing iloc with Boolean list for columns (first 3 rows, columns 'Entity', 'Code', 'DALYs'):")
# Assuming columns are: Entity, Code, Year, DALYs
my_columns_boolean = [True, True, False, True] # Select Entity, Code, DALYs (skip Year)
if len(dalys_data.columns) == len(my_columns_boolean):
    print(dalys_data.iloc[0:3, my_columns_boolean])
else:
    print(f"Boolean list length ({len(my_columns_boolean)}) does not match number of columns ({len(dalys_data.columns)}). Skipping boolean iloc example.")

# Example of using loc for specific column names (rows with index label 2 to 4, for 'Year' column)
print("\nUsing loc - Rows with index label 2 to 4, 'Year' column (dalys_data.loc[2:4, 'Year']):")
# Note: .loc includes the end label in slices, so 2:4 means rows with index labels 2, 3, and 4.
print(dalys_data.loc[2:4, "Year"])


# 5. Answer specific questions (Portfolio: DALYs for all countries in 1990)
print("\n--- Answering Specific Questions ---")
# Portfolio Requirement: Successfully used a Boolean to show DALYs for all countries in 1990.
print("\nDALYs for all countries in 1990:")
dalys_1990_boolean_filter = dalys_data['Year'] == 1990 # Create the boolean Series
dalys_in_1990 = dalys_data.loc[dalys_1990_boolean_filter, "DALYs"] # Apply boolean filter and select DALYs column
print(dalys_in_1990)


# 6. Compare DALYs between the UK and France
print("\n--- Comparing DALYs: UK vs France ---")
# Extract data for "United Kingdom" (DALYs and Year columns)
uk_data = dalys_data.loc[dalys_data['Entity'] == "United Kingdom", ["DALYs", "Year"]]
# Extract data for "France" (DALYs and Year columns)
france_data = dalys_data.loc[dalys_data['Entity'] == "France", ["DALYs", "Year"]]

if not uk_data.empty and not france_data.empty:
    # Calculate the mean DALYs for the UK
    uk_mean_dalys = uk_data["DALYs"].mean()
    # Calculate the mean DALYs for France
    france_mean_dalys = france_data["DALYs"].mean()

    print(f"UK mean DALYs over the period: {uk_mean_dalys:.2f}")
    print(f"France mean DALYs over the period: {france_mean_dalys:.2f}")

    # Portfolio Requirement: Comment stating whether the mean DALYs in the UK was greater or smaller than France.
    if uk_mean_dalys > france_mean_dalys:
        print("The mean DALYs for the UK is greater than for France over the recorded period.")
        # Comment for portfolio: The mean DALYs in the UK was greater than for France.
    elif uk_mean_dalys < france_mean_dalys:
        print("The mean DALYs for the UK is smaller than for France over the recorded period.")
        # Comment for portfolio: The mean DALYs in the UK was smaller than for France.
    else:
        print("The mean DALYs for the UK is equal to that of France over the recorded period.")
        # Comment for portfolio: The mean DALYs in the UK was equal to that of France.
else:
    print("Could not find data for both UK and France to compare mean DALYs.")

# 7. Visualize UK DALYs over time
print("\n--- Visualizing UK DALYs Over Time ---")
if not uk_data.empty:
    plt.figure(figsize=(10, 6)) # Create a new figure for this plot
    plt.plot(uk_data['Year'], uk_data['DALYs'], 'b*', label="United Kingdom DALYs") # Plot UK DALYs with blue star markers
    # plt.xticks(uk_data['Year'], rotation=-90) # Rotating all years can make x-axis too crowded.
    # Better to let matplotlib decide or select fewer ticks if needed.
    # If rotation is desired for many ticks:
    # unique_years_uk = sorted(uk_data['Year'].unique())
    # plt.xticks(ticks=unique_years_uk, rotation=-90, ha='left') # ha='left' for better alignment with rotated ticks
    plt.xlabel("Year")
    plt.ylabel("DALYs (Disability-Adjusted Life Years)")
    plt.title("DALYs in the United Kingdom Over Time")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("uk_dalys_over_time.png") # Save the plot
    plt.show()
else:
    print("No data for UK to plot.")


# 8. Address a custom question (Portfolio: Question in question.txt)
# This section's code should correspond to the question you state in question.txt
# Example custom question: "Which countries had DALYs greater than 100,000 in the year 1990?"
# The line number for this section in dalys.py will be part of question.txt

print("\n--- Custom Question Analysis ---")
# (Line number for question.txt starts here for this example)
question_line_start = "This line number (or the next actual code line) for question.txt" # Placeholder for line number tracking

# Custom question: Which countries had DALYs greater than 100,000 in 1990?
# Filter data for the year 1990 and DALYs > 100,000
high_daly_countries_1990 = dalys_data.loc[(dalys_data["Year"] == 1990) & (dalys_data["DALYs"] > 100000), ["Entity", "DALYs"]]

if not high_daly_countries_1990.empty:
    print("\nCountries with DALYs > 100,000 in 1990:")
    print(high_daly_countries_1990.sort_values(by="DALYs", ascending=False)) # Sort for better presentation

    # Visualize the result for the custom question
    plt.figure(figsize=(12, 7)) # Create a new figure
    plt.bar(high_daly_countries_1990["Entity"], high_daly_countries_1990["DALYs"], color='skyblue')
    plt.xlabel("Country/Region")
    plt.ylabel("DALYs (Disability-Adjusted Life Years)")
    plt.title("Countries with DALYs > 100,000 in 1990")
    plt.xticks(rotation=45, ha="right") # Rotate x-axis labels for readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("high_daly_countries_1990.png") # Save the plot
    plt.show()
    # Discussion for question.txt:
    # e.g., "The countries identified with DALYs > 100,000 in 1990 are [list some].
    # This might be expected for countries with large populations or specific health challenges at the time.
    # For example, [mention a country] might have high DALYs due to [possible reason]."
else:
    print("\nNo countries found with DALYs > 100,000 in 1990 for the custom question.")

print("\n--- Script End ---")