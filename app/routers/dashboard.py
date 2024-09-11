from fastapi import APIRouter, Depends, HTTPException
from app.services import dashboard_service
from app.models.dashboard import DashboardRequest, DashboardResponse
from utils.rate_limiter import rate_limit

router = APIRouter()


@router.post("/generate-dashboard", response_model=DashboardResponse)
@rate_limit(max_calls=5, time_frame=60)
async def generate_dashboard(request: DashboardRequest):
    try:
        dashboard = dashboard_service.generate_dashboard(request.dataset)
        return DashboardResponse(dashboard=dashboard)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/ask-question")
@rate_limit(max_calls=10, time_frame=60)
async def ask_question(question: str):
    try:
        answer = dashboard_service.ask_chatgpt(question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
