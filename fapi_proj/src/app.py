from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()


@app.get("/helloworld")
def helloworld():
    return {"Hello": "World"}
