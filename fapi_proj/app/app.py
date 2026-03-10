from fastapi import FastAPI, HTTPException

# Create a FastAPI instance
app = FastAPI()


@app.get("/helloworld")
def helloworld():
    return {"message": "World"}


posts = {"1": {"title": "First Post", "content": "This is the first post"},

         "2": {"title": "Second Post", "content": "This is the second post"},
         "3": {"title": "Third Post", "content": "This is the third post"},
         "4": {"title": "Fourth Post", "content": "This is the fourth post"},
         "5": {"title": "Fifth Post", "content": "This is the fifth post"},
         "6": {"title": "Sixth Post", "content": "This is the sixth post"},
         "7": {"title": "Seventh Post", "content": "This is the seventh post"},
         "8": {"title": "Eighth Post", "content": "This is the eighth post"},
         "9": {"title": "Ninth Post", "content": "This is the ninth post"}, }


@app.get("/posts")
def get_limited_posts(limit: str = None):
    if limit:
        return list(posts.values())[:int(limit)]
    return posts


@app.get("/posts/{id}")
def get_posts(id: int):
    if id not in posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts.get(id)
