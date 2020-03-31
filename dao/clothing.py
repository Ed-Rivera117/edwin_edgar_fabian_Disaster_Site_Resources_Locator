from config.dbconfig import pg_config
import psycopg2


class ClothingDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllClothing(self):
        cursor = self.conn.cursor()
        query = "select cl_id, cl_size, cl_color, cl_material from clothing;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingById(self, cl_id):
        cursor = self.conn.cursor()
        query = "select cl_id, cl_size, cl_color, cl_material from clothing where cl_id = %s;"
        cursor.execute(query, (cl_id,))
        result = cursor.fetchone()
        return result

    def getClothingBySize(self, cl_size):
        cursor = self.conn.cursor()
        query = "select * from clothing where cl_size = %s;"
        cursor.execute(query, (cl_size,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from clothing natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from clothing natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from clothing natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from clothing natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, cl_size, cl_color, cl_material, resr_id):
        cursor = self.conn.cursor()
        query = "insert into clothing(cl_size, cl_color, cl_material, resr_id) values (%s, %s, %s, %s) returning cl_id;"
        cursor.execute(query, (cl_size, cl_color, cl_material, resr_id,))
        clid = cursor.fetchone()[0]
        self.conn.commit()
        return clid

    def delete(self, cl_id):
        cursor = self.conn.cursor()
        query = "delete from clothing where cl_id = %s;"
        cursor.execute(query, (cl_id,))
        self.conn.commit()
        return cl_id

    def update(self, cl_id, cl_color, cl_size, cl_material):
        cursor = self.conn.cursor()
        query = "update clothing set cl_size = %s, cl_color = %s, cl_material = %s where cl_id = %s;"
        cursor.execute(query, (cl_id, cl_size, cl_color, cl_material))
        self.conn.commit()
        return cl_id