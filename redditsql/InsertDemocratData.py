import pandas as pd

from sqlalchemy import create_engine

# MySQL database connection parameters
db_host = "localhost"  # Replace with your host
db_user = "your_username"  # Replace with your MySQL username
db_password = "your_password"  # Replace with your MySQL password
db_name = "your_database"  # Replace with your target database name
table_name = "reddit_opinion"  # Name of the table to insert data into

# File path for the CSV
csv_file_pathDems = r"\csv\reddit_opinion_democrats.csv"
csv_file_pathReps = r"\csv\reddit_opinion_republican.csv"

# Create database engine using SQLAlchemy (recommended for Pandas)
engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}")

# Read the CSV in chunks
chunksize = 500  # Adjust the size of each chunk as needed

try:
    for chunk in pd.read_csv(csv_file_path, chunksize=chunksize):


    print("Data insertion complete!")

except Exception as e:
    print(f"An error occurred: {e}")