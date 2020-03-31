from config.dbconfig import pg_config
import psycopg2


class SupplierDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select s_id, s_usr, s_password, s_location, s_resources from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, s_id):
        cursor = self.conn.cursor()
        query = "select s_id, s_usr, s_password, s_location, s_resources from supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = cursor.fetchone()
        return result

    def getSupplierByUser(self, s_usr):
        cursor = self.conn.cursor()
        query = "select * from supplier where s_usr = %s;"
        cursor.execute(query, (s_usr,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByLocation(self, s_location):
        cursor = self.conn.cursor()
        query = "select * from supplier where s_location = %s;"
        cursor.execute(query, (s_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByFirstAndLastName(self, usr_fname, usr_lname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join usr where usr_fname = %s and usr_lname = %s;"
        cursor.execute(query, (usr_fname, usr_lname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, s_usr, s_password, s_location, s_resources, usr_id):
        cursor = self.conn.cursor()
        query = "insert into supplier(s_usr, s_password, s_location, s_resources, usr_id) values (%s, %s, %s, %s, %s) returning s_id;"
        cursor.execute(query, (s_usr, s_password, s_location, s_resources, usr_id,))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid

    def delete(self, s_id):
        cursor = self.conn.cursor()
        query = "delete from supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        self.conn.commit()
        return s_id

    def update(self, s_id, s_usr, s_password, s_location, s_resources):
        cursor = self.conn.cursor()
        query = "update supplier set s_usr = %s, s_password = %s, s_location = %s, s_resources = %s where s_id = %s;"
        cursor.execute(query, (s_usr, s_password, s_location, s_resources, s_id,))
        self.conn.commit()
        return s_id