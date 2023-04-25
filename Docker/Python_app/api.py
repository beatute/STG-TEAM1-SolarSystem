import db_data
from flask import make_response


def read_all():
    return db_data.get_all_planets(), 200


def create_planets(planets):
    status_code = None
    planets, status_code = db_data.create_new_planets(planets)
    return planets, status_code


def read_one_planets(id):
    return db_data.get_one_planet(id), 200


def delete_planets(id):
    rows_affected = db_data.delete_planets(id)

    if rows_affected > 0:
        return make_response(f"{id} planet successfully deleted", 200)
    else:
        return make_response(f"Deletion of {id} failed. Planet not found.", 404)


def update_planets(id, planets):
    return db_data.update_planets(id, planets), 200
