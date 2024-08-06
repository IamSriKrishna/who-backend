from db.pymodels.inventory.inventory import CreateInventory, InventoryStockUpdate
from db.models.inventory.inventory import Inventory
from dependencies.dependencies import db_dependency
from starlette import status
from fastapi import HTTPException
from util.content import (status as st, success, data, inventoryNotFound, length)

def create_inventory(inventory: CreateInventory, db: db_dependency):
    try:
        inventory_model = Inventory(
            title=inventory.title,
            description=inventory.description,
            image=inventory.image,
            stock=inventory.stock,
            info=inventory.info,
            amount=inventory.amount
        )
        db.add(inventory_model)
        db.commit()
        db.refresh(inventory_model)

        return {
            st: success,
            data: inventory_model
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def get_inventory_byID(id: int, db: db_dependency):
    try:
        inventory_model = db.query(Inventory).filter(Inventory.id == id).first()
        if not inventory_model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=inventoryNotFound)
        db.refresh(inventory_model)
        return {
            st: success,
            data: inventory_model
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def delete_inventory_byID(id: int, db: db_dependency):
    try:
        inventory_model = db.query(Inventory).filter(Inventory.id == id).first()
        if not inventory_model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=inventoryNotFound)
        db.delete(inventory_model)
        db.commit()
        return {
            st: success
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def get_all(db:db_dependency):
    try:
        inventory_model = db.query(Inventory).all()
        return {
            st: success,
            length: len(inventory_model),
            data:inventory_model
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def update_stock(id:int,inventory: InventoryStockUpdate, db:db_dependency):
    try:
        inventory_model = db.query(Inventory).filter(Inventory.id == id).first()
        if not inventory_model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=inventoryNotFound)
        inventory_model.stock = inventory.stock
        db.commit()
        db.refresh(inventory_model)

        return {
            st: success,
            data:inventory_model
        }
    except Exception as e: 
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))