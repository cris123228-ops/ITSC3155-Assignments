from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .models import models, schemas
from .controllers import (
    orders,
    sandwiches,
    resources,
    recipes,
    order_details,
)
from .dependencies.database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ORDERS

@app.post(
    "/orders/",
    response_model=schemas.Order,
    status_code=201,
    tags=["Orders"],
)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
):
    return orders.create(db=db, order=order)


@app.get(
    "/orders/",
    response_model=list[schemas.Order],
    tags=["Orders"],
)
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get(
    "/orders/{order_id}",
    response_model=schemas.Order,
    tags=["Orders"],
)
def read_one_order(
    order_id: int,
    db: Session = Depends(get_db),
):
    order = orders.read_one(db, order_id=order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return order


@app.put(
    "/orders/{order_id}",
    response_model=schemas.Order,
    tags=["Orders"],
)
def update_one_order(
    order_id: int,
    order: schemas.OrderUpdate,
    db: Session = Depends(get_db),
):
    order_db = orders.read_one(db, order_id=order_id)

    if order_db is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return orders.update(
        db=db,
        order=order,
        order_id=order_id,
    )


@app.delete(
    "/orders/{order_id}",
    tags=["Orders"],
)
def delete_one_order(
    order_id: int,
    db: Session = Depends(get_db),
):
    order = orders.read_one(db, order_id=order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return orders.delete(db=db, order_id=order_id)


# SANDWICHES

@app.post(
    "/sandwiches/",
    response_model=schemas.Sandwich,
    status_code=201,
    tags=["Sandwiches"],
)
def create_sandwich(
    sandwich: schemas.SandwichCreate,
    db: Session = Depends(get_db),
):
    return sandwiches.create(db=db, request=sandwich)


@app.get(
    "/sandwiches/",
    response_model=list[schemas.Sandwich],
    tags=["Sandwiches"],
)
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)


@app.get(
    "/sandwiches/{sandwich_id}",
    response_model=schemas.Sandwich,
    tags=["Sandwiches"],
)
def read_one_sandwich(
    sandwich_id: int,
    db: Session = Depends(get_db),
):
    return sandwiches.read_one(
        db=db,
        sandwich_id=sandwich_id,
    )


@app.put(
    "/sandwiches/{sandwich_id}",
    response_model=schemas.Sandwich,
    tags=["Sandwiches"],
)
def update_sandwich(
    sandwich_id: int,
    sandwich: schemas.SandwichUpdate,
    db: Session = Depends(get_db),
):
    return sandwiches.update(
        db=db,
        sandwich_id=sandwich_id,
        request=sandwich,
    )


@app.delete(
    "/sandwiches/{sandwich_id}",
    tags=["Sandwiches"],
)
def delete_sandwich(
    sandwich_id: int,
    db: Session = Depends(get_db),
):
    return sandwiches.delete(
        db=db,
        sandwich_id=sandwich_id,
    )


# RESOURCES

@app.post(
    "/resources/",
    response_model=schemas.Resource,
    status_code=201,
    tags=["Resources"],
)
def create_resource(
    resource: schemas.ResourceCreate,
    db: Session = Depends(get_db),
):
    return resources.create(db=db, request=resource)


@app.get(
    "/resources/",
    response_model=list[schemas.Resource],
    tags=["Resources"],
)
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)


@app.get(
    "/resources/{resource_id}",
    response_model=schemas.Resource,
    tags=["Resources"],
)
def read_one_resource(
    resource_id: int,
    db: Session = Depends(get_db),
):
    return resources.read_one(
        db=db,
        resource_id=resource_id,
    )


@app.put(
    "/resources/{resource_id}",
    response_model=schemas.Resource,
    tags=["Resources"],
)
def update_resource(
    resource_id: int,
    resource: schemas.ResourceUpdate,
    db: Session = Depends(get_db),
):
    return resources.update(
        db=db,
        resource_id=resource_id,
        request=resource,
    )


@app.delete(
    "/resources/{resource_id}",
    tags=["Resources"],
)
def delete_resource(
    resource_id: int,
    db: Session = Depends(get_db),
):
    return resources.delete(
        db=db,
        resource_id=resource_id,
    )


# RECIPES

@app.post(
    "/recipes/",
    response_model=schemas.Recipe,
    status_code=201,
    tags=["Recipes"],
)
def create_recipe(
    recipe: schemas.RecipeCreate,
    db: Session = Depends(get_db),
):
    return recipes.create(db=db, request=recipe)


@app.get(
    "/recipes/",
    response_model=list[schemas.Recipe],
    tags=["Recipes"],
)
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)


@app.get(
    "/recipes/{recipe_id}",
    response_model=schemas.Recipe,
    tags=["Recipes"],
)
def read_one_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
):
    return recipes.read_one(
        db=db,
        recipe_id=recipe_id,
    )


@app.put(
    "/recipes/{recipe_id}",
    response_model=schemas.Recipe,
    tags=["Recipes"],
)
def update_recipe(
    recipe_id: int,
    recipe: schemas.RecipeUpdate,
    db: Session = Depends(get_db),
):
    return recipes.update(
        db=db,
        recipe_id=recipe_id,
        request=recipe,
    )


@app.delete(
    "/recipes/{recipe_id}",
    tags=["Recipes"],
)
def delete_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
):
    return recipes.delete(
        db=db,
        recipe_id=recipe_id,
    )


# ORDER DETAILS

@app.post(
    "/order_details/",
    response_model=schemas.OrderDetail,
    status_code=201,
    tags=["Order Details"],
)
def create_order_detail(
    detail: schemas.OrderDetailCreate,
    db: Session = Depends(get_db),
):
    return order_details.create(db=db, request=detail)


@app.get(
    "/order_details/",
    response_model=list[schemas.OrderDetail],
    tags=["Order Details"],
)
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)


@app.get(
    "/order_details/{detail_id}",
    response_model=schemas.OrderDetail,
    tags=["Order Details"],
)
def read_one_order_detail(
    detail_id: int,
    db: Session = Depends(get_db),
):
    return order_details.read_one(
        db=db,
        detail_id=detail_id,
    )


@app.put(
    "/order_details/{detail_id}",
    response_model=schemas.OrderDetail,
    tags=["Order Details"],
)
def update_order_detail(
    detail_id: int,
    detail: schemas.OrderDetailUpdate,
    db: Session = Depends(get_db),
):
    return order_details.update(
        db=db,
        detail_id=detail_id,
        request=detail,
    )


@app.delete(
    "/order_details/{detail_id}",
    tags=["Order Details"],
)
def delete_order_detail(
    detail_id: int,
    db: Session = Depends(get_db),
):
    return order_details.delete(
        db=db,
        detail_id=detail_id,
    )