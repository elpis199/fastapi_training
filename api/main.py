from fastapi import FastAPI

from routers import task, done

app = FastAPI(root_path="/api")
app.include_router(task.router)
app.include_router(done.router)