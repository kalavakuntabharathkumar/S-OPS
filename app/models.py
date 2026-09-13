from datetime import datetime
from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Ticket(Base):
    __tablename__ = 'tickets'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(50), default='general')
    priority: Mapped[str] = mapped_column(String(20), default='medium')
    severity: Mapped[str] = mapped_column(String(20), default='medium')
    status: Mapped[str] = mapped_column(String(30), default='open')
    requester: Mapped[str] = mapped_column(String(120), default='internal-user')
    channel: Mapped[str] = mapped_column(String(30), default='portal')
    assignee: Mapped[str] = mapped_column(String(120), default='support-engineer')
    diagnosis: Mapped[str] = mapped_column(Text, default='')
    resolution: Mapped[str] = mapped_column(Text, default='')
    customer_response: Mapped[str] = mapped_column(Text, default='')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
