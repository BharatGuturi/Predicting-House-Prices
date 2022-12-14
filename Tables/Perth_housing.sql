-- Table: public.Perth_housing

-- DROP TABLE IF EXISTS public."Perth_housing";

CREATE TABLE IF NOT EXISTS public."Perth_housing"
(
    "ADDRESS" text COLLATE pg_catalog."default",
    "SUBURB" text COLLATE pg_catalog."default",
    "PRICE" bigint,
    "BEDROOMS" bigint,
    "BATHROOMS" bigint,
    "GARAGE" double precision,
    "LAND_AREA" bigint,
    "FLOOR_AREA" bigint,
    "BUILD_YEAR" double precision,
    "CBD_DIST" bigint,
    "NEAREST_STN" text COLLATE pg_catalog."default",
    "NEAREST_STN_DIST" bigint,
    "DATE_SOLD" text COLLATE pg_catalog."default",
    "POSTCODE" bigint,
    "LATITUDE" double precision,
    "LONGITUDE" double precision,
    "NEAREST_SCH" text COLLATE pg_catalog."default",
    "NEAREST_SCH_DIST" double precision,
    "NEAREST_SCH_RANK" double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Perth_housing"
    OWNER to postgres;