from fastapi import FastAPI
from db.database import engine
from db.models.user import user
from router.auth import auth
from router.inventory import inventory

app = FastAPI()

user.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(inventory.router)