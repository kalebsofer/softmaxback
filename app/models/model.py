from pydantic import BaseModel


class DashboardRequest(BaseModel):
    dataset: str


class DashboardResponse(BaseModel):
    dashboard: dict
