import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")


# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df.loc[netflix_df["type"] == "Movie"]


# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only.loc[:,[ "title", "country", "genre", "release_year", "duration"]]

# Print the first five rows of the new DataFrame
#print(netflix_movies_col_subset[0:5])


# Create a figure and increase the figure size
#fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
#plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"])

# Create a title
#plt.title("Movie Duration by Year of Release")

# Show the plot
#plt.show()


# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]


# Print the first 20 rows of short_movies
#print(short_movies.head(15))


# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for label, row in netflix_movies_col_subset.iterrows() :
    if row["genre"] == "Children" :
        colors.append("red")
    elif row["genre"] == "Documentaries" :
        colors.append("blue")
    elif row["genre"] == "Stand-Up" :
        colors.append("green")
    else:
        colors.append("black")
        
# Inspect the first 10 values in your list        
print(colors[0:9])

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c=colors)

# Create a title and axis labels
plt.title("Movie Duration by Year of Release")
plt.xlabel("Duration (min) ")
plt.ylabel("Release Year")

# Show the plot
plt.show()