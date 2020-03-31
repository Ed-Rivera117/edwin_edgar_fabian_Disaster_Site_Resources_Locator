from config.dbconfig import pg_config
import psycopg2

class Canned_FoodDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCannedFood(self):
        cursor = self.conn.cursor()
        query = "select cf_id, cf_expDate, cf_name from cannedfood;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCannedFoodById(self, cf_id):
        cursor = self.conn.cursor()
        query = "select cf_id, cf_expDate, cf_name from cannedfood where cf_id = %s;"
        cursor.execute(query, (cf_id,))
        result = cursor.fetchone()
        return result

    def getCannedFoodByName(self, cf_name):
        cursor = self.conn.cursor()
        query = "select * from cannedfood where cf_name = %s;"
        cursor.execute(query, (cf_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCannedFoodByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from cannedfood natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCannedFoodConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from cannedfood natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCannedFoodBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from cannedFood natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCannedFoodPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from cannedfood natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, cf_expDate, cf_name, resr_id):
        cursor = self.conn.cursor()
        query = "insert into cannedfood(cf_expDate, cf_name, resr_id) values (%s, %s, %s) returning cf_id;"
        cursor.execute(query, (cf_expDate, cf_name, resr_id,))
        cfid = cursor.fetchone()[0]
        self.conn.commit()
        return cfid

    def delete(self, cf_id):
        cursor = self.conn.cursor()
        query = "delete from cannedfood where cf_id = %s;"
        cursor.execute(query, (cf_id,))
        self.conn.commit()
        return cf_id

    def update(self, cf_id, cf_expDate, cf_name):
        cursor = self.conn.cursor()
        query = "update cannedfood set cf_expDate = %s, cf_name = %s where cf_id = %s;"
        cursor.execute(query, (cf_id, cf_expDate, cf_name))
        self.conn.commit()
        return cf_id