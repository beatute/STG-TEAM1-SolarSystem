import db_connect as db

def get_all_planets():
    planets_list = []
    with db.create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, `orbital period days`, `average speed kms`, 'satellites', 'mean radius', `temperature c` FROM planets")
            for planets in cursor.fetchall():
                planets_dict = {
                    'id': planets[0],
                    'name': planets[1],
                    'orbital_period_days': planets[2],
                    'average_speed_kms': planets[3],
                    'satellites': planets[4],
                    'mean_radius': planets[5],
                    'temperature_c': planets[6]
                }
                planets_list.append(planets_dict)
    return planets_list

def create_new_planets(planets):
    existing_planets = get_one_planet(planets['id'])
    if existing_planets:
        return {'error': f" Planets with id {planets['id']} already exists"}, 409

    with db.create_connection() as connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO planets (id, name, `orbital period days`, `average speed kms`,'satellites', mean radius, " \
                    "`temperature c`) VALUES (%s, %s, %s, %s, %s, %s, %s;);"
            values = (planets['id'], planets['name'], planets['orbital period days'],  planets['average speed kms'], planets['satelittes'], planets['mean radius'], planets['temperature c'])
            cursor.execute(query, values)
            connection.commit()
    return planets, 201


def get_one_planet(id):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, `orbital period days`, `average speed kms`, satellites,  mean radius, "
                           "`temperature c`"
                           "FROM planets WHERE id ='" + id + "'")
            planets = cursor.fetchone()
            if planets is not None:
                return {
                    'id': planets[0],
                    'name': planets[1],
                    'orbital_period_days': planets[2],
                    'average_speed_kms': planets[3],
                    'satellites':planets[4],
                    'mean radius': planets[5],
                    'temperature_c': planets[6]
                }
            else:
                return None


def delete_planets(id):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            delete_query = "DELETE FROM planets WHERE id ='" + id + "'"
            cursor.execute(delete_query)
            conn.commit()
            return cursor.rowcount


def update_planets(id, planets):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            update_query = "UPDATE planets SET id = %s, name = %s, orbital_period_days = %s, average_speed_kms = %s, satellites = %s," \
                           "mean radius = %s, temperature = %s WHERE id = %s"
            values = (planets['name'], planets['orbital_period_days'], planets['average_speed_kms'], planets['satellites'], planets['mean radius'], planets['temperature_c'], id)
            cursor.execute(update_query, values)
            conn.commit()
        return planets
