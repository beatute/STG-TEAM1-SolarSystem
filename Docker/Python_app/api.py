import db_data
from flask import make_response


def read_all():
    return db_data.get_all_planet(), 200


def create_planet(planet):
    planet, status_code = db_data.create_new_planet(planet)
    return planet, status_code


def read_one_planet(name):
    return db_data.get_one_planet(name), 200


def delete_planet(name):
    rows_affected = db_data.delete_planet(name)

    if rows_affected > 0:
        return make_response(f"{name} planet successfully deleted", 200)
    else:
        return make_response(f"Deletion of {name} failed. Planet not found.", 404)


def update_planet(name, planet):
    return db_data.update_planet(name, planet), 200
