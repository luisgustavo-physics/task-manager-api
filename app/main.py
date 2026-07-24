from fastapi import FastAPI

app = FastAPI(
    title = "Task Manager API",
    version = "1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Task Manager API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/users")
def get_users():
    users = []
    return users


@app.post("/users")
def create_user(user: dict):
    users = []
    users.append(user)
    return user