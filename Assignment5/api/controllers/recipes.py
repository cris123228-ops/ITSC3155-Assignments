from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..models import models, schemas


def check_references(db, sandwich_id, resource_id):
    if db.get(models.Sandwich, sandwich_id) is None:
        raise HTTPException(404, "Sandwich not found.")

    if db.get(models.Resource, resource_id) is None:
        raise HTTPException(404, "Resource not found.")


def create(db: Session, request: schemas.RecipeCreate):
    check_references(db, request.sandwich_id, request.resource_id)

    recipe = models.Recipe(**request.model_dump())
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe


def read_all(db: Session):
    return db.query(models.Recipe).all()


def read_one(db: Session, recipe_id: int):
    recipe = db.get(models.Recipe, recipe_id)

    if recipe is None:
        raise HTTPException(404, "Recipe not found.")

    return recipe


def update(
    db: Session,
    recipe_id: int,
    request: schemas.RecipeUpdate,
):
    recipe = read_one(db, recipe_id)
    changes = request.model_dump(exclude_unset=True)

    if any(value is None for value in changes.values()):
        raise HTTPException(422, "Recipe fields cannot be null.")

    check_references(
        db,
        changes.get("sandwich_id", recipe.sandwich_id),
        changes.get("resource_id", recipe.resource_id),
    )

    for field, value in changes.items():
        setattr(recipe, field, value)

    db.commit()
    db.refresh(recipe)
    return recipe


def delete(db: Session, recipe_id: int):
    recipe = read_one(db, recipe_id)
    db.delete(recipe)
    db.commit()
    return {"message": "Recipe deleted successfully."}