# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach


DBNAME = "forum"

def get_posts():
    try:
        """Return all posts from the 'database', most recent first."""
        DB = psycopg2.connect("dbname=forum")
        c = DB.cursor()
        c.execute("SELECT time, content FROM posts ORDER BY time DESC")
        #c.execute("UPDATE posts SET content = 'cheese' WHERE content LIKE '%spam%';")
        '''Get all the posts from the database, sorted with the newest first.
        
        Returns:
        A list of dictionaries, where each dictionary has a 'content' key
        pointing to the post content, and 'time' key pointing to the time
        it was posted.
        '''
        posts = ({'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall())
        #for row in c.fetchall())
        #posts.sort(key=lambda row: row['time'], reverse=True)
        DB.close()
        return posts
    except Exception as e:
        print("There is something wrong",e)

def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    cleaned = bleach.clean(content, strip = True)
    c.execute("insert into posts values(%s)", (cleaned,))
    db.commit()
    db.close()
  
  