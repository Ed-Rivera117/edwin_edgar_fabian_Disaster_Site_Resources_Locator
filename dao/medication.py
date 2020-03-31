from config.dbconfig import pg_config
import psycopg2


class MedicationDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMed(self):
        cursor = self.conn.cursor()
        query = "select med_id, med_name from medicine;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedById(self, med_id):
        cursor = self.conn.cursor()
        query = "select med_id, med_name from medicine where med_id = %s;"
        cursor.execute(query, (med_id,))
        result = cursor.fetchone()
        return result

    def getMedByName(self, med_name):
        cursor = self.conn.cursor()
        query = "select * from medicine where med_name = %s;"
        cursor.execute(query, (med_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from medicine natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from medicine natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from medicine natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from medicine natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, med_name, resr_id):
        cursor = self.conn.cursor()
        query = "insert into medicine(med_name, resr_id) values (%s, %s) returning med_id;"
        cursor.execute(query, (med_name, resr_id,))
        medid = cursor.fetchone()[0]
        self.conn.commit()
        return medid

    def delete(self, med_id):
        cursor = self.conn.cursor()
        query = "delete from medicine where med_id = %s;"
        cursor.execute(query, (med_id,))
        self.conn.commit()
        return med_id

    def update(self, med_id, med_name):
        cursor = self.conn.cursor()
        query = "update medicine set med_name = %s where med_id = %s;"
        cursor.execute(query, (med_id, med_name,))
        self.conn.commit()
        return med_id