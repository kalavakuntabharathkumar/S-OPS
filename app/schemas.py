from pydantic import BaseModel, Field

class TicketCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=5)
    category: str = 'general'
    priority: str = 'medium'
    requester: str = 'internal-user'
    channel: str = 'portal'
    assignee: str = 'support-engineer'

class TicketUpdate(BaseModel):
    status: str | None = None
    priority: str | None = None
    assignee: str | None = None
    resolution: str | None = None

class TicketOut(BaseModel):
    id: int
    title: str
    description: str
    category: str
    priority: str
    severity: str
    status: str
    requester: str
    channel: str
    assignee: str
    diagnosis: str
    resolution: str
    customer_response: str

    class Config:
        from_attributes = True
