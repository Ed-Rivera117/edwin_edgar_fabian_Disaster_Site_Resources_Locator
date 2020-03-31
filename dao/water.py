from config.dbconfig import pg_config
import psycopg2


class WaterDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllWater(self):
        cursor = self.conn.cursor()
        query = "select h2O_id, h2O_volume from water;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterById(self, h2O_id):
        cursor = self.conn.cursor()
        query = "select h2O_id, h2O_volume from water where h2O_id = %s;"
        cursor.execute(query, (h2O_id,))
        result = cursor.fetchone()
        return result

    def getWaterByVolume(self, h2O_volume):
        cursor = self.conn.cursor()
        query = "select * from water where h2O_volume = %s;"
        cursor.execute(query, (h2O_volume,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, h2O_volume, resr_id):
        cursor = self.conn.cursor()
        query = "insert into water(h2O_volume, resr_id) values (%s, %s) returning h2O_id;"
        cursor.execute(query, (h2O_volume, resr_id))
        wid = cursor.fetchone()[0]
        self.conn.commit()
        return wid

    def delete(self, h2O_id):
        cursor = self.conn.cursor()
        query = "delete from water where h2O_id = %s;"
        cursor.execute(query, (h2O_id,))
        self.conn.commit()
        return h2O_id

    def update(self, h2O_id, h2O_volume):
        cursor = self.conn.cursor()
        query = "update water set h2O_volume = %s where h2O_id = %s;"
        cursor.execute(query, (h2O_id, h2O_volume,))
        self.conn.commit()
        return h2O_id