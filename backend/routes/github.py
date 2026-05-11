from fastapi import APIRouter, Request

router = APIRouter()  # ?? NO PREFIX

@router.post("/github-webhook/")
async def github_webhook(request: Request):
    payload = await request.json()
    print("GitHub Event Received:", payload)
    return {"status": "received"}