-- Table: public.Perth_housing_filtered

-- DROP TABLE IF EXISTS public."Perth_housing_filtered";

CREATE TABLE IF NOT EXISTS public."Perth_housing_filtered"
(
    "PRICE" bigint,
    "BEDROOMS" bigint,
    "BATHROOMS" bigint,
    "GARAGE" double precision,
    "LAND_AREA" bigint,
    "FLOOR_AREA" bigint,
    "BUILD_YEAR" double precision,
    "CBD_DIST" bigint,
    "NEAREST_STN_DIST" bigint,
    "POSTCODE" bigint,
    "LATITUDE" double precision,
    "LONGITUDE" double precision,
    "NEAREST_SCH_DIST" double precision,
    "NEAREST_SCH_RANK" double precision,
    "MONTH_SOLD" integer,
    "YEAR_SOLD" integer
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Perth_housing_filtered"
    OWNER to postgres;