from config.dbconfig import pg_config
import psycopg2


class ReservationDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReservations(self):
        cursor = self.conn.cursor()
        query = "select rs_id, rs_date from reservation;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationById(self, rs_id):
        cursor = self.conn.cursor()
        query = "select rs_id, rs_date from reservation where rs_id = %s;"
        cursor.execute(query, (rs_id,))
        result = cursor.fetchone()
        return result

    def getReservationByDate(self, rs_date):
        cursor = self.conn.cursor()
        query = "select * from reservation where rs_date = %s;"
        cursor.execute(query, (rs_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationByClient(self, c_usr):
        cursor = self.conn.cursor()
        query = "select * from reservation natural inner join Makes natural inner join client where c_usr = %s;"
        cursor.execute(query, (c_usr,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rs_date):
        cursor = self.conn.cursor()
        query = "insert into reservation(rs_date) values (%s) returning rs_id;"
        cursor.execute(query, (rs_date,))
        rsid = cursor.fetchone()[0]
        self.conn.commit()
        return rsid

    def delete(self, rs_id):
        cursor = self.conn.cursor()
        query = "delete from reservation where rs_id = %s;"
        cursor.execute(query, (rs_id,))
        self.conn.commit()
        return rs_id

    def update(self, rs_id, rs_date):
        cursor = self.conn.cursor()
        query = "update reservation set rs_date = %s where rs_id = %s;"
        cursor.execute(query, (rs_id, rs_date,))
        self.conn.commit()
        return rs_id