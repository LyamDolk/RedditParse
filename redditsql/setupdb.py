from dotenv import load_dotenv
import os

import mysql.connector

# Database connection
# Load environment variables from .env file
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user="root",
    password=os.getenv("MYSQL_ROOT_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = db.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS reddit_posts (
    comment_id CHAR(255) PRIMARY KEY,
    source CHAR(1), 
    score INT,
    self_text TEXT,
    subreddit VARCHAR(255),
    created_time TIMESTAMP,
    post_id CHAR(255),
    author_name VARCHAR(255),
    controversiality INT,
    ups INT,
    downs INT,
    user_is_verified BOOLEAN,
    user_account_created_time TIMESTAMP,
    user_awardee_karma INT,
    user_awarder_karma INT,
    user_link_karma INT,
    user_comment_karma INT,
    user_total_karma INT,
    post_score INT,
    post_self_text TEXT,
    post_title VARCHAR(255),
    post_upvote_ratio FLOAT,
    post_thumbs_ups INT,
    post_total_awards_received INT,
    post_created_time TIMESTAMP
    )
""")

db.commit()
cursor.close()
db.close()