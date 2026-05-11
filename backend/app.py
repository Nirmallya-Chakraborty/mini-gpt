from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.chat import router as chat_router
from routes.github import router as github_router   # ADD THIS

# =========================
# APP INIT
# =========================
app = FastAPI(
    title="Mini GPT",
    version="1.0.0"
)

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# ROUTES
# =========================
app.include_router(chat_router, prefix="/api")
app.include_router(github_router)  # webhook root route

# =========================
# ROOT
# =========================
@app.get("/")
def root():
    return {"status": "ok"}