from config.dbconfig import pg_config
import psycopg2

class Dry_FoodDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllDryFood(self):
        cursor = self.conn.cursor()
        query = "select df_id, df_expDate, df_name from dryfood;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDryFoodById(self, df_id):
        cursor = self.conn.cursor()
        query = "select df_id, df_expDate, df_name from dryfood where df_id = %s;"
        cursor.execute(query, (df_id,))
        result = cursor.fetchone()
        return result

    def getDryFoodByName(self, df_name):
        cursor = self.conn.cursor()
        query = "select * from dryfood where df_name = %s;"
        cursor.execute(query, (df_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDryFoodByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from dryfood natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDryFoodConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from dryfood natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDryFoodBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from dryfood natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDryFoodPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from dryfood natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, df_expDate, df_name, resr_id):
        cursor = self.conn.cursor()
        query = "insert into dryfood(df_expDate, df_name, resr_id) values (%s, %s, %s) returning df_id;"
        cursor.execute(query, (df_expDate, df_name, resr_id,))
        dfid = cursor.fetchone()[0]
        self.conn.commit()
        return dfid

    def delete(self, df_id):
        cursor = self.conn.cursor()
        query = "delete from dryfood where df_id = %s;"
        cursor.execute(query, (df_id,))
        self.conn.commit()
        return df_id

    def update(self, df_id, df_expDate, df_name):
        cursor = self.conn.cursor()
        query = "update dryfood set df_expDate = %s, df_name = %s where df_id = %s;"
        cursor.execute(query, (df_id, df_expDate, df_name))
        self.conn.commit()
        return df_id