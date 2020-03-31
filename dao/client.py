from config.dbconfig import pg_config
import psycopg2


class ClientDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllClients(self):
        cursor = self.conn.cursor()
        query = "select c_id, c_usr, c_password, usr_fname, usr_lname, usr_email from client natural inner join usr;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClientById(self, c_id):
        cursor = self.conn.cursor()
        query = "select c_id, c_usr, c_password from client where c_id = %s;"
        cursor.execute(query, (c_id,))
        result = cursor.fetchone()
        return result

    def getClientByUser(self, c_usr):
        cursor = self.conn.cursor()
        query = "select * from client where c_usr = %s;"
        cursor.execute(query, (c_usr,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClientByName(self, usr_fname, usr_lname):
        cursor = self.conn.cursor()
        query = "select * from client natural inner join usr where usr_fname = %s and usr_lname = %s;"
        cursor.execute(query, (usr_fname, usr_lname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, c_usr, c_password, usr_id):
        cursor = self.conn.cursor()
        query = "insert into client(c_usr, c_password, usr_id) values (%s, %s, %s) returning c_id;"
        cursor.execute(query, (c_usr, c_password, usr_id))
        cid = cursor.fetchone()[0]
        self.conn.commit()
        return cid

    def delete(self, c_id):
        cursor = self.conn.cursor()
        query = "delete from client where c_id = %s;"
        cursor.execute(query, (c_id,))
        self.conn.commit()
        return c_id

    def update(self, c_id, c_usr, c_password):
        cursor = self.conn.cursor()
        query = "update client set c_usr = %s, c_password = %s where c_id = %s;"
        cursor.execute(query, (c_usr, c_password, c_id,))
        self.conn.commit()
        return c_id
