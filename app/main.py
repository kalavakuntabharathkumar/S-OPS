from pathlib import Path
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import Ticket
from .schemas import TicketCreate, TicketOut, TicketUpdate
from .troubleshooting import diagnose, response_is_consistent

Base.metadata.create_all(bind=engine)
app = FastAPI(title='SupportOps API', version='2.0.0')
STATIC_DIR = Path(__file__).resolve().parent.parent / 'static'
app.mount('/static', StaticFiles(directory=STATIC_DIR), name='static')

@app.get('/', include_in_schema=False)
def home():
    return FileResponse(STATIC_DIR / 'index.html')

@app.get('/api/tickets', response_model=list[TicketOut])
def list_tickets(status: str | None = None, priority: str | None = None, db: Session = Depends(get_db)):
    query = select(Ticket).order_by(Ticket.id.desc())
    if status:
        query = query.where(Ticket.status == status)
    if priority:
        query = query.where(Ticket.priority == priority)
    return db.scalars(query).all()

@app.post('/api/tickets', response_model=TicketOut)
def create_ticket(payload: TicketCreate, db: Session = Depends(get_db)):
    r = diagnose(payload.title, payload.description, payload.category)
    t = Ticket(
        title=payload.title,
        description=payload.description,
        category=r.category,
        priority=payload.priority,
        severity=r.severity,
        requester=payload.requester,
        channel=payload.channel,
        assignee=payload.assignee,
        diagnosis=r.diagnosis,
        resolution=r.resolution,
        customer_response=r.customer_response,
    )
    db.add(t)
    db.commit()
    db.refresh(t)
    return t

@app.patch('/api/tickets/{ticket_id}', response_model=TicketOut)
def update_ticket(ticket_id: int, payload: TicketUpdate, db: Session = Depends(get_db)):
    t = db.get(Ticket, ticket_id)
    if not t:
        raise HTTPException(404, 'Ticket not found')
    for field in ('status', 'priority', 'assignee', 'resolution'):
        value = getattr(payload, field)
        if value is not None:
            setattr(t, field, value)
    db.commit()
    db.refresh(t)
    return t

@app.post('/api/tickets/{ticket_id}/resolve', response_model=TicketOut)
def resolve_ticket(ticket_id: int, db: Session = Depends(get_db)):
    t = db.get(Ticket, ticket_id)
    if not t:
        raise HTTPException(404, 'Ticket not found')
    if not response_is_consistent(diagnose(t.title, t.description, t.category)):
        raise HTTPException(422, 'Required troubleshooting fields incomplete')
    t.status = 'resolved'
    db.commit()
    db.refresh(t)
    return t

@app.get('/api/metrics')
def metrics(db: Session = Depends(get_db)):
    ts = db.scalars(select(Ticket)).all()
    n = len(ts)
    resolved = sum(t.status == 'resolved' for t in ts)
    complete = sum(bool(t.diagnosis and t.resolution and t.customer_response) for t in ts)
    return {
        'total_tickets': n,
        'resolved_tickets': resolved,
        'open_tickets': sum(t.status == 'open' for t in ts),
        'high_priority_tickets': sum(t.priority == 'high' for t in ts),
        'resolution_rate_percent': round(resolved / n * 100, 2) if n else 0,
        'first_response_consistency_percent': round(complete / n * 100, 2) if n else 0,
    }
