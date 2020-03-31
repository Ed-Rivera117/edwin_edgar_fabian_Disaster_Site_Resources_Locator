from config.dbconfig import pg_config
import psycopg2


class Heavy_EquipmentDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllHeavyEquip(self):
        cursor = self.conn.cursor()
        query = "select heq_id, heq_type from heavyequip;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquipById(self, heq_id):
        cursor = self.conn.cursor()
        query = "select heq_id, heq_type from heavyequip where heq_id = %s;"
        cursor.execute(query, (heq_id,))
        result = cursor.fetchone()
        return result

    def getHeavyEquipByType(self, heq_type):
        cursor = self.conn.cursor()
        query = "select * from heavyequip where heq_type = %s;"
        cursor.execute(query, (heq_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquipByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from heavyequip natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquipConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from heavyequip natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquipBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from heavyequip natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquipPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from heavyequip natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, heq_type, resr_id):
        cursor = self.conn.cursor()
        query = "insert into heavyequip(heq_type, resr_id) values (%s, %s) returning heq_id;"
        cursor.execute(query, (heq_type, resr_id,))
        heqid = cursor.fetchone()[0]
        self.conn.commit()
        return heqid

    def delete(self, heq_id):
        cursor = self.conn.cursor()
        query = "delete from heavyequip where heq_id = %s;"
        cursor.execute(query, (heq_id,))
        self.conn.commit()
        return heq_id

    def update(self, heq_id, heq_type):
        cursor = self.conn.cursor()
        query = "update heavyequip set heq_type = %s where heq_id = %s;"
        cursor.execute(query, (heq_id, heq_type))
        self.conn.commit()
        return heq_id