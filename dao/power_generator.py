from config.dbconfig import pg_config
import psycopg2


class Power_GeneratorDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPowerGenerator(self):
        cursor = self.conn.cursor()
        query = "select pg_id, pg_wattage, pg_fuelType from powergenerator;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPowerGeneratorById(self, pg_id):
        cursor = self.conn.cursor()
        query = "select pg_id, pg_wattage, pg_fuelType from powergenerator where pg_id = %s;"
        cursor.execute(query, (pg_id,))
        result = cursor.fetchone()
        return result

    def getPowerGeneratorByWattage(self, pg_wattage):
        cursor = self.conn.cursor()
        query = "select * from powergenerator where pg_wattage = %s;"
        cursor.execute(query, (pg_wattage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPowerGeneratorByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from powergenerator natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPowerGeneratorConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from powergenerator natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPowerGeneratorBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from powergenerator natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBPowerGeneratorPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from powergenerator natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, pg_wattage, pg_fuelType, resr_id):
        cursor = self.conn.cursor()
        query = "insert into powergenerator(pg_wattage, pg_fuelType, resr_id) values (%s, %s, %s) returning pg_id;"
        cursor.execute(query, (pg_wattage, pg_fuelType, resr_id,))
        pqid = cursor.fetchone()[0]
        self.conn.commit()
        return pqid

    def delete(self, pg_id):
        cursor = self.conn.cursor()
        query = "delete from powergenerator where pg_id = %s;"
        cursor.execute(query, (pg_id,))
        self.conn.commit()
        return pg_id

    def update(self, pg_id, pg_wattage, pg_fuelType):
        cursor = self.conn.cursor()
        query = "update powergenerator set pg_wattage = %s, pg_fuelType = %s where pg_id = %s;"
        cursor.execute(query, (pg_id, pg_wattage, pg_fuelType))
        self.conn.commit()
        return pg_id