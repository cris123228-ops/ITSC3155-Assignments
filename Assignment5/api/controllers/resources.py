from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..models import models, schemas


def create(db: Session, request: schemas.ResourceCreate):
    resource = models.Resource(**request.model_dump())

    try:
        db.add(resource)
        db.commit()
        db.refresh(resource)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A resource with that name already exists."
        )

    return resource


def read_all(db: Session):
    return db.query(models.Resource).all()


def read_one(db: Session, resource_id: int):
    resource = (
        db.query(models.Resource)
        .filter(models.Resource.id == resource_id)
        .first()
    )

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="Resource not found."
        )

    return resource


def update(
    db: Session,
    resource_id: int,
    request: schemas.ResourceUpdate
):
    resource = read_one(db, resource_id)
    changes = request.model_dump(exclude_unset=True)

    if any(value is None for value in changes.values()):
        raise HTTPException(
            status_code=422,
            detail="Item and amount cannot be null."
        )

    for field, value in changes.items():
        setattr(resource, field, value)

    try:
        db.commit()
        db.refresh(resource)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A resource with that name already exists."
        )

    return resource


def delete(db: Session, resource_id: int):
    resource = read_one(db, resource_id)

    if resource.recipes:
        raise HTTPException(
            status_code=409,
            detail="Remove related recipes first."
        )

    db.delete(resource)
    db.commit()

    return {"message": "Resource deleted successfully."}