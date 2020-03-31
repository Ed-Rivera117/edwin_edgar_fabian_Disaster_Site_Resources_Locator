from config.dbconfig import pg_config
import psycopg2

class FuelDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        cursor = self.conn.cursor()
        query = "select fuel_id, fuel_type from fuel;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelById(self, fuel_id):
        cursor = self.conn.cursor()
        query = "select fuel_id, fuel_type from fuel where fuel_id = %s;"
        cursor.execute(query, (fuel_id,))
        result = cursor.fetchone()
        return result

    def getFuelByType(self, fuel_type):
        cursor = self.conn.cursor()
        query = "select * from fuel where fuel_type = %s;"
        cursor.execute(query, (fuel_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, fuel_type, resr_id):
        cursor = self.conn.cursor()
        query = "insert into fuel(fuel_type, resr_id) values (%s, %s) returning fuel_id;"
        cursor.execute(query, (fuel_type, resr_id,))
        fid = cursor.fetchone()[0]
        self.conn.commit()
        return fid

    def delete(self, fuel_id):
        cursor = self.conn.cursor()
        query = "delete from fuel where fuel_id = %s;"
        cursor.execute(query, (fuel_id,))
        self.conn.commit()
        return fuel_id

    def update(self, fuel_id, fuel_type):
        cursor = self.conn.cursor()
        query = "update fuel set fuel_type = %s where fuel_id = %s;"
        cursor.execute(query, (fuel_id, fuel_type))
        self.conn.commit()
        return fuel_id