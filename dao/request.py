from config.dbconfig import pg_config
import psycopg2


class RequestDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select rq_id, rq_date from request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, rq_id):
        cursor = self.conn.cursor()
        query = "select rq_id, rq_date from request where rq_id = %s;"
        cursor.execute(query, (rq_id,))
        result = cursor.fetchone()
        return result

    def getRequestByUsrId(self, usr_id):
        cursor = self.conn.cursor()
        query = "select rq_id, rq_date " \
                "from request natural inner join Places natural inner join client " \
                "where usr_id = %s;"
        cursor.execute(query, (usr_id,))
        result = cursor.fetchone()
        return result

    def getRequestByDate(self, rq_date):
        cursor = self.conn.cursor()
        query = "select * from request where rq_date = %s;"
        cursor.execute(query, (rq_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByClient(self, c_usr):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join Places natural inner join client where c_usr = %s;"
        cursor.execute(query, (c_usr,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByTransaction(self, transaction_num):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join Transaction where transaction_num = %s;"
        cursor.execute(query, (transaction_num,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rq_date):
        cursor = self.conn.cursor()
        query = "insert into request(rq_date) values (%s) returning rq_id;"
        cursor.execute(query, (rq_date,))
        rqid = cursor.fetchone()[0]
        self.conn.commit()
        return rqid

    def delete(self, rq_id):
        cursor = self.conn.cursor()
        query = "delete from request where rq_id = %s;"
        cursor.execute(query, (rq_id,))
        self.conn.commit()
        return rq_id

    def update(self, rq_id, rq_date):
        cursor = self.conn.cursor()
        query = "update request set rq_date = %s where rq_id = %s;"
        cursor.execute(query, (rq_id, rq_date,))
        self.conn.commit()
        return rq_id