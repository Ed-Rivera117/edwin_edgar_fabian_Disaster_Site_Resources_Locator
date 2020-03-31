from config.dbconfig import pg_config
import psycopg2


class UsrDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsr(self):
        cursor = self.conn.cursor()
        query = "select usr_id, usr_fname, usr_lname, usr_email, usr_phone from usr natural inner join phone;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsrById(self, usr_id):
        cursor = self.conn.cursor()
        query = "select usr_id, usr_fname, usr_lname, usr_email, usr_phone from usr natural inner join phone where usr_id = %s;"
        cursor.execute(query, (usr_id,))
        result = cursor.fetchone()
        return result

    def getUsrByFirstName(self, fname):
        cursor = self.conn.cursor()
        query = "select * from usr where usr_fname = %s;"
        cursor.execute(query, (fname,))
        result = []
        for row in cursor:
            result.append(row)
        return

    def getUsrByLastName(self, lname):
        cursor = self.conn.cursor()
        query = "select * from usr where usr_lname = %s;"
        cursor.execute(query, (lname,))
        result = []
        for row in cursor:
            result.append(row)
        return

    def getUsrByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select * from usr where usr_email = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return

    def getUsrByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "select * from usr natural inner join phone where usr_phone = %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return

    def insert(self, usr_fname, usr_lname, usr_email):
        cursor = self.conn.cursor()
        query = "insert into usr(usr_fname, usr_lname, usr_email) values (%s, %s, %s) returning usr_id;"
        cursor.execute(query, (usr_fname, usr_lname, usr_email,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "delete from usr where usr_id = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

    def update(self, usr_id, usr_fname, usr_lname, usr_email):
        cursor = self.conn.cursor()
        query = "update usr set usr_fname = %s, usr_lname = %s, usr_email = %s where usr_id = %s;"
        cursor.execute(query, (usr_fname, usr_lname, usr_email,  usr_id,))
        self.conn.commit()
        return usr_id

