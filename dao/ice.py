from config.dbconfig import pg_config
import psycopg2

class IceDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllIce(self):
        cursor = self.conn.cursor()
        query = "select ice_id, ice_bagSize from ice;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceById(self, ice_id):
        cursor = self.conn.cursor()
        query = "select ice_id, ice_bagSize from ice where ice_id = %s;"
        cursor.execute(query, (ice_id,))
        result = cursor.fetchone()
        return result

    def getIceByBagSize(self, ice_bagSize):
        cursor = self.conn.cursor()
        query = "select * from ice where ice_bagSize = %s;"
        cursor.execute(query, (ice_bagSize,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from ice natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from ice natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from ice natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIcePurchased(self):
        cursor = self.conn.cursor()
        query = "select * from ice natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, ice_bagSize, resr_id):
        cursor = self.conn.cursor()
        query = "insert into ice(ice_bagSize, resr_id) values (%s, %s) returning ice_id;"
        cursor.execute(query, (ice_bagSize, resr_id,))
        iceid = cursor.fetchone()[0]
        self.conn.commit()
        return iceid

    def delete(self, ice_id):
        cursor = self.conn.cursor()
        query = "delete from ice where ice_id = %s;"
        cursor.execute(query, (ice_id,))
        self.conn.commit()
        return ice_id

    def update(self, ice_id, ice_bagSize):
        cursor = self.conn.cursor()
        query = "update ice set ice_bagSize = %s where ice_id = %s;"
        cursor.execute(query, (ice_id, ice_bagSize,))
        self.conn.commit()
        return ice_id