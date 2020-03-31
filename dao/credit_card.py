from config.dbconfig import pg_config
import psycopg2

class Credit_CardDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCreditCards(self):
        cursor = self.conn.cursor()
        query = "select cc_id, cc_nameOnCard, cc_number, cc_expDate, cc_cvc from creditcard natural inner join CreditCardNumber;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardById(self, cc_id):
        cursor = self.conn.cursor()
        query = "select cc_id, cc_nameOnCard, cc_number, cc_expDate, cc_cvc from creditcard natural inner join CreditCardNumber where cc_id = %s;"
        cursor.execute(query, (cc_id,))
        result = cursor.fetchone()
        return result

    def getCreditCardByName(self, cc_nameOnCard):
        cursor = self.conn.cursor()
        query = "select * from creditcard where cc_nameOnCard = %s;"
        cursor.execute(query, (cc_nameOnCard,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardByNumber(self, cc_number):
        cursor = self.conn.cursor()
        query = "select * from creditcard natural inner join CreditCardNumber where cc_number = %s;"
        cursor.execute(query, (cc_number,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, cc_nameOnCard, cc_expDate, cc_cvc):
        cursor = self.conn.cursor()
        query = "insert into creditcard(cc_nameOnCard, cc_expDate, cc_cvc) values (%s, %s, %d) returning cc_id;"
        cursor.execute(query, (cc_nameOnCard, cc_expDate, cc_cvc,))
        ccid = cursor.fetchone()[0]
        self.conn.commit()
        return ccid

    def delete(self, cc_id):
        cursor = self.conn.cursor()
        query = "delete from creditcard where cc_id = %s;"
        cursor.execute(query, (cc_id,))
        self.conn.commit()
        return cc_id

    def update(self, cc_id, cc_nameOnCard, cc_expDate, cc_cvc):
        cursor = self.conn.cursor()
        query = "update creditcard set cc_nameOnCard = %s, cc_expDate = %s, cc_cvc = %d where cc_id = %s;"
        cursor.execute(query, (cc_id, cc_nameOnCard, cc_expDate, cc_cvc,))
        self.conn.commit()
        return cc_id