from config.dbconfig import pg_config
import psycopg2

class BatteriesDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllBatteries(self):
        cursor = self.conn.cursor()
        query = "select batt_id, batt_type from batteries;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesById(self, batt_id):
        cursor = self.conn.cursor()
        query = "select batt_id, batt_type from batteries where batt_id = %s;"
        cursor.execute(query, (batt_id,))
        result = cursor.fetchone()
        return result

    def getBatteriesByType(self, batt_type):
        cursor = self.conn.cursor()
        query = "select * from batteries where batt_type = %s;"
        cursor.execute(query, (batt_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from batteries natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from batteries natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from batteries natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from batteries natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, batt_type, resr_id):
        cursor = self.conn.cursor()
        query = "insert into batteries(batt_type,resr_id) values (%s,%s) returning batt_id;"
        cursor.execute(query, (batt_type, resr_id,))
        battid = cursor.fetchone()[0]
        self.conn.commit()
        return battid

    def delete(self, batt_id):
        cursor = self.conn.cursor()
        query = "delete from batteries where batt_id = %s;"
        cursor.execute(query, (batt_id,))
        self.conn.commit()
        return batt_id

    def update(self, batt_id, batt_type):
        cursor = self.conn.cursor()
        query = "update batteries set batt_type = %s where batt_id = %s;"
        cursor.execute(query, (batt_id, batt_type))
        self.conn.commit()
        return batt_id