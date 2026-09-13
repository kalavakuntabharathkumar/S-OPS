from pydantic import BaseModel,Field
class TicketCreate(BaseModel):
    title:str=Field(min_length=3,max_length=200)
    description:str=Field(min_length=5)
    category:str='general'
class TicketOut(BaseModel):
    id:int; title:str; description:str; category:str; severity:str; status:str; diagnosis:str; resolution:str; customer_response:str
    class Config: from_attributes=True
