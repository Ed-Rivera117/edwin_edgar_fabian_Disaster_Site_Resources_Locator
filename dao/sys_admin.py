from config.dbconfig import pg_config
import psycopg2


class Sys_adminDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSys_admin(self):
        cursor = self.conn.cursor()
        query = "select sa_id, sa_user, sa_password from sys_admin;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSys_adminById(self, sa_id):
        cursor = self.conn.cursor()
        query = "select sa_id, sa_user, sa_password  from sys_admin where sa_id = %s;"
        cursor.execute(query, (sa_id,))
        result = cursor.fetchone()
        return result

    def getSys_adminByUser(self, sa_usr):
        cursor = self.conn.cursor()
        query = "select * from sys_admin where sa_user = %s;"
        cursor.execute(query, (sa_usr,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, sa_user, sa_password):
        cursor = self.conn.cursor()
        query = "insert into sys_admin(sa_user, sa_password) values (%s, %s) returning sa_id;"
        cursor.execute(query, (sa_user, sa_password,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "delete from sys_admin where sa_id = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

    def update(self, sa_id, sa_user, sa_password):
        cursor = self.conn.cursor()
        query = "update sys_admin set sa_usr = %s, sa_password = %s where sa_id = %s;"
        cursor.execute(query, (sa_user, sa_password, sa_id,))
        self.conn.commit()
        return sa_id
