from fastapi import APIRouter
from starlette import status
from db.pymodels.inventory.inventory import CreateInventory, InventoryStockUpdate
from dependencies.dependencies import db_dependency
from controller.inventory.inventory import (
    create_inventory as create_func, 
    get_inventory_byID as get_id_func, 
    delete_inventory_byID as delete_id_func, 
    get_all as get_func,
    update_stock as update_stock_func
    )
router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_inventory(inventory:CreateInventory,db:db_dependency):
    return create_func(inventory,db)


@router.get("/{id}",status_code=status.HTTP_200_OK)
async def get_byID(id:int,db:db_dependency):
    return get_id_func(id=id,db=db)


@router.delete("/{id}",status_code=status.HTTP_200_OK)
async def delete_Inventory(id:int,db:db_dependency):
    return delete_id_func(id=id,db=db)


@router.get("/",status_code=status.HTTP_200_OK)
async def get_allInventory(db:db_dependency):
    return get_func(db=db)

@router.put("/{id}",status_code=status.HTTP_200_OK)
async def update_stock(id:int, inventory:InventoryStockUpdate, db:db_dependency):
    return update_stock_func(id=id,inventory=inventory,db=db)