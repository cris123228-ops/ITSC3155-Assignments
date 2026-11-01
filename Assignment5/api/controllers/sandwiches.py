from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..models import models, schemas


def create(db: Session, request: schemas.SandwichCreate):
    sandwich = models.Sandwich(**request.model_dump())

    try:
        db.add(sandwich)
        db.commit()
        db.refresh(sandwich)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A sandwich with that name already exists."
        )

    return sandwich


def read_all(db: Session):
    return db.query(models.Sandwich).all()


def read_one(db: Session, sandwich_id: int):
    sandwich = (
        db.query(models.Sandwich)
        .filter(models.Sandwich.id == sandwich_id)
        .first()
    )

    if sandwich is None:
        raise HTTPException(
            status_code=404,
            detail="Sandwich not found."
        )

    return sandwich


def update(
    db: Session,
    sandwich_id: int,
    request: schemas.SandwichUpdate
):
    sandwich = read_one(db, sandwich_id)
    changes = request.model_dump(exclude_unset=True)

    if any(value is None for value in changes.values()):
        raise HTTPException(
            status_code=422,
            detail="Sandwich name and price cannot be null."
        )

    for field, value in changes.items():
        setattr(sandwich, field, value)

    try:
        db.commit()
        db.refresh(sandwich)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A sandwich with that name already exists."
        )

    return sandwich


def delete(db: Session, sandwich_id: int):
    sandwich = read_one(db, sandwich_id)

    if sandwich.recipes or sandwich.order_details:
        raise HTTPException(
            status_code=409,
            detail="Remove related recipes and order details first."
        )

    db.delete(sandwich)
    db.commit()

    return {"message": "Sandwich deleted successfully."}