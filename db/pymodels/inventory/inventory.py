from typing import List, Optional
from pydantic import BaseModel

class CreateInventory(BaseModel):
    title: str
    description: str
    image: str
    stock: int
    amount: int
    info: List[str]

class InventoryUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    stock: Optional[int] = None
    amount: Optional[int] = None
    info: Optional[List[str]] = None
    
class InventoryStockUpdate(BaseModel):
    stock: int
