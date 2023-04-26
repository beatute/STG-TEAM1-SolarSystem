import db_connect as db

def get_all_planet():
    planet_list = []
    with db.create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT name, orbital_period_days, average_speed_kms, satellites, mean_radius, temperature_c FROM planets")
            for planet in cursor.fetchall():
                planet_dict = {
                    'name': planet[0],
                    'orbital_period_days': planet[1],
                    'average_speed_kms': planet[2],
                    'satellites': planet[3],
                    'mean_radius': planet[4],
                    'temperature_c': planet[5]
                }
                planet_list.append(planet_dict)
    return planet_list

def create_new_planet(planet):
    existing_planet = get_one_planet(planet['name'])
    if existing_planet:
        return {'error': f" Planets with name {planet['name']} already exists"}, 409

    with db.create_connection() as connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO planets (name, orbital_period_days, average_speed_kms, satellites, mean_radius, temperature_c) VALUES (%s, %s, %s, %s, %s, %s);"
            values = (planet['name'], planet['orbital_period_days'], planet['average_speed_kms'], planet['satellites'], planet['mean_radius'], planet['temperature_c'])
            cursor.execute(query, values)
            connection.commit()
    return planet, 201


def get_one_planet(name):
    with db.create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT name, orbital_period_days, average_speed_kms, satellites, mean_radius, temperature_c FROM planets WHERE name ='" + name + "'")
            planet = cursor.fetchone()
            if planet is not None:
                return {
                    'name': planet[0],
                    'orbital_period_days': planet[1],
                    'average_speed_kms': planet[2],
                    'satellites': planet[3],
                    'mean_radius': planet[4],
                    'temperature_c': planet[5]
                }
            else:
                return None


def delete_planet(name):
    with db.create_connection() as conn:
        with conn.cursor() as cursor:
            delete_query = "DELETE FROM planets WHERE name ='" + name + "'"
            cursor.execute(delete_query)
            conn.commit()
            return cursor.rowcount


def update_planet(name, planet):
    with db.create_connection() as conn:
        with conn.cursor() as cursor:
            update_query = "UPDATE planets SET orbital_period_days = %s, average_speed_kms = %s, satellites = %s, mean_radius = %s, temperature_c = %s WHERE name = %s"
            values = (planet['orbital_period_days'], planet['average_speed_kms'], planet['satellites'], planet['mean_radius'], planet['temperature_c'], name)
            cursor.execute(update_query, values)
            conn.commit()
        return planet
