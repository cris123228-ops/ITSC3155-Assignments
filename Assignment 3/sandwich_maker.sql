-- Cristian Flores
-- Assignment 3: Ham Sandwich Maker Database
-- Oracle FreeSQL version: uses the provided personal schema.

CREATE TABLE resources (
    item VARCHAR2(50),
    amount INT
);

CREATE TABLE sandwiches (
    sandwich_size VARCHAR2(50),
    price DECIMAL(5,2)
);

CREATE TABLE recipes (
    sandwich_size VARCHAR2(50),
    item VARCHAR2(50),
    amount INT
);

-- Resources
INSERT INTO resources (item, amount) VALUES ('bread', 12);
INSERT INTO resources (item, amount) VALUES ('ham', 18);
INSERT INTO resources (item, amount) VALUES ('cheese', 24);

-- Sandwich prices
INSERT INTO sandwiches (sandwich_size, price) VALUES ('small', 1.75);
INSERT INTO sandwiches (sandwich_size, price) VALUES ('medium', 3.25);
INSERT INTO sandwiches (sandwich_size, price) VALUES ('large', 5.50);

-- Small sandwich recipe
INSERT INTO recipes (sandwich_size, item, amount)
VALUES ('small', 'bread', 2);

INSERT INTO recipes (sandwich_size, item, amount)
VALUES ('small', 'ham', 4);

INSERT INTO recipes (sandwich_size, item, amount)
VALUES ('small', 'cheese', 4);

-- Medium sandwich recipe
INSERT INTO recipes (sandwich_size, item, amount)
VALUES ('medium', 'bread', 4);

INSERT INTO recipes (sandwich_size, item, amount)
VALUES ('medium', 'ham', 6);

INSERT INTO recipes (sandwich_size, item, amount)
VALUES ('medium', 'cheese', 8);

-- Large sandwich recipe
INSERT INTO recipes (sandwich_size, item, amount)
VALUES ('large', 'bread', 6);

INSERT INTO recipes (sandwich_size, item, amount)
VALUES ('large', 'ham', 8);

INSERT INTO recipes (sandwich_size, item, amount)
VALUES ('large', 'cheese', 12);

COMMIT;

-- Display each table
SELECT * FROM resources;
SELECT * FROM sandwiches;
SELECT * FROM recipes;