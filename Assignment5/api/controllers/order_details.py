from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..models import models, schemas


def check_references(db, order_id, sandwich_id):
    if db.get(models.Order, order_id) is None:
        raise HTTPException(status_code=404, detail="Order not found")

    if db.get(models.Sandwich, sandwich_id) is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")


def create(db: Session, request: schemas.OrderDetailCreate):
    check_references(db, request.order_id, request.sandwich_id)

    detail = models.OrderDetail(**request.model_dump())
    db.add(detail)
    db.commit()
    db.refresh(detail)
    return detail


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, detail_id: int):
    detail = db.get(models.OrderDetail, detail_id)

    if detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")

    return detail


def update(
    db: Session,
    detail_id: int,
    request: schemas.OrderDetailUpdate,
):
    detail = read_one(db, detail_id)
    changes = request.model_dump(exclude_unset=True)

    if any(value is None for value in changes.values()):
        raise HTTPException(
            status_code=422,
            detail="Order detail fields cannot be null",
        )

    check_references(
        db,
        changes.get("order_id", detail.order_id),
        changes.get("sandwich_id", detail.sandwich_id),
    )

    for field, value in changes.items():
        setattr(detail, field, value)

    db.commit()
    db.refresh(detail)
    return detail


def delete(db: Session, detail_id: int):
    detail = read_one(db, detail_id)
    db.delete(detail)
    db.commit()
    return {"message": "Order detail deleted successfully"}