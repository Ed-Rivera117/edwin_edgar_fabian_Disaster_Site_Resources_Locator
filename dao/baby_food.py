from config.dbconfig import pg_config
import psycopg2

class Baby_FoodDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllBabyFood(self):
        cursor = self.conn.cursor()
        query = "select bb_id, bb_expDate, bb_flavor from babyfood;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBabyFoodById(self, bb_id):
        cursor = self.conn.cursor()
        query = "select bb_id, bb_expDate, bb_flavor from babyfood where bb_id = %s;"
        cursor.execute(query, (bb_id,))
        result = cursor.fetchone()
        return result

    def getBabyFoodByFlavor(self, bb_flavor):
        cursor = self.conn.cursor()
        query = "select * from babyfood where bb_flavor = %s;"
        cursor.execute(query, (bb_flavor,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBabyFoodByExpDate(self, bb_expDate):
        cursor = self.conn.cursor()
        query = "select * from babyfood where bb_expDate = %s;"
        cursor.execute(query, (bb_expDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBabyFoodByFlavorAndExpDate(self, bb_flavor, bb_expDate):
        cursor = self.conn.cursor()
        query = "select * from babyfood where bb_flavor = %s and bb_expDate = %s;"
        cursor.execute(query, (bb_flavor, bb_expDate))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBabyFoodByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from babyfood natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBabyFoodConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from babyfood natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBabyFoodPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from babyfood natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBabyFoodBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from babyfood natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, bb_expDate, bb_flavor, resr_id):
        cursor = self.conn.cursor()
        query = "insert into babyfood(bb_expDate, bb_flavor, resr_id) values (%s, %s, %s) returning bb_id;"
        cursor.execute(query, (bb_expDate, bb_flavor, resr_id,))
        bbid = cursor.fetchone()[0]
        self.conn.commit()
        return bbid

    def delete(self, bb_id):
        cursor = self.conn.cursor()
        query = "delete from babyfood where bb_id = %s;"
        cursor.execute(query, (bb_id,))
        self.conn.commit()
        return bb_id

    def update(self, bb_id, bb_expDate, bb_flavor):
        cursor = self.conn.cursor()
        query = "update babyfood set bb_expDate = %s, bb_flavor = %s where bb_id = %s;"
        cursor.execute(query, (bb_id, bb_expDate, bb_flavor))
        self.conn.commit()
        return bb_id