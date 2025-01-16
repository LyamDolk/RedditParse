import pandas as pd


def saveWokepost(username:str, post:list, postdate:str, subreddit:str)->None:
    print("Woke Post", username, post, postdate, subreddit)
    

def saveNoneWokepost(username:str, postwordcount:int, postdate:str , subreddit:str)->None:
    print("nonWoke Post: ", username,postwordcount,postdate,subreddit)



def parseCSVs()->None:
    csvs = ["C:/Users/lyamd/Downloads/reddit_opinion_republican.csv","C:/Users/lyamd/Downloads/reddit_opinion_democrats.csv"]
    for csv in csvs:
        print(f"Processing file: {csv}")
        if "republican" in csv:
            source_reddit = "r"
        if "democrat" in csv:
            source_reddit = "d"
        chunksize = 1000
        row_count = 0
        limiter:int = 10
        for chunk in pd.read_csv(csv, chunksize=chunksize):
            if row_count == 0:
                print("CSV Header:", chunk.columns.tolist())
            for index, row in chunk.iterrows():
                if row_count >= limiter:
                    break
                post:str = row["self_text"].replace('\n', ' ')
                
                post_contains_woke:bool = "woke" in post.lower()
                subreddit:str = row["subreddit"]
                
                if post_contains_woke:
                    print("*******author:", row["author_name"],"***************** Reddit :", row["subreddit"], "****")
                    print(post)
                    post_tokens = row["self_text"].split()
                    # saveToDatabase(
                    #         comment_id=row["comment_id"], 
                    #         score=row["score"],
                    #         self_text=row["self_text"], 
                    #         subreddit=row["subreddit"],
                    #         created_time=row["created_time"], 
                    #         post_id=row["post_id"],
                    #         author_name=row["author_name"], 
                    #         controversiality=row["controversiality"],
                    #         ups=row["ups"], 
                    #         downs=row["downs"], 
                    #         post_score=row["post_score"], 
                    #         post_self_text=row["post_self_text"],
                    #         post_title=row["post_title"], 
                    #         post_upvote_ratio=row["post_upvote_ratio"],
                    #         post_created_time=row["post_created_time"],
                    #         post_wordcount=len(post_tokens),
                    #         post_contains_woke=post_contains_woke,
                    #         post_tokens="",
                    #         gramatical_category_vector=row["gramatical_category_vector"]
                    #     )
                row_count += 1
            if row_count >= limiter:
                break


   
def printcsvheaders():
    csvs = ["C:/Users/lyamd/Downloads/reddit_opinion_republican.csv","C:/Users/lyamd/Downloads/reddit_opinion_democrats.csv"]
    for csv in csvs:
        print(f"Processing file: {csv}")
        chunksize = 1000
        row_count = 0
        limiter:int = 1000
        for chunk in pd.read_csv(csv, chunksize=chunksize):
            if row_count == 0:
                print("CSV Header:", chunk.columns.tolist())
            row_count += 1
            if row_count >= limiter:
                break       
            

if __name__ == "__main__":
    #printcsvheaders()
    #parseCSVs()
    
    
     
