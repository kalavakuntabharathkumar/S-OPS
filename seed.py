from app.database import Base,SessionLocal,engine
from app.models import Ticket
from app.troubleshooting import diagnose
Base.metadata.create_all(bind=engine)
samples=[('Checkout requests timing out','Users receive 504 responses and checkout is slow.'),('Access denied to report','Analysts receive 403 forbidden.'),('Server disk full','Logs show no space left on device.'),('Database unavailable','The API cannot establish a database connection.'),('Unknown application error','Users report an intermittent issue without useful error details.')]
db=SessionLocal()
try:
    for title,description in samples:
        r=diagnose(title,description);db.add(Ticket(title=title,description=description,category=r.category,severity=r.severity,diagnosis=r.diagnosis,resolution=r.resolution,customer_response=r.customer_response))
    db.commit()
finally: db.close()
print('Seeded SupportOps sample tickets.')
