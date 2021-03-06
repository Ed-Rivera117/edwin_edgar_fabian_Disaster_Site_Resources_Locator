from config.dbconfig import pg_config
import psycopg2


class ResourcesDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesById(self, resr_id):
        cursor = self.conn.cursor()
        query = "select * from resources where resr_id = %s;"
        cursor.execute(query, (resr_id,))
        result = cursor.fetchone()
        return result

    def getResourceByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Purchases natural inner join request " \
                "where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceReservedByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Confirmation natural inner join reservation " \
                "where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceAvailableByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources " \
                "where stock > 0 and resr_location = %s" \
                "except select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Purchases natural inner join request " \
                "except select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Confirmation natural inner join reservation;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByCategory(self, resr_category):
        cursor = self.conn.cursor()
        query = "select * from resources where resr_category = %s;"
        cursor.execute(query, (resr_category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceRequestedByCategory(self, resr_category):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Purchases natural inner join request " \
                "where resr_category = %s;"
        cursor.execute(query, (resr_category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceReservedByCategory(self, resr_category):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Confirmation natural inner join reservation " \
                "where resr_category = %s;"
        cursor.execute(query, (resr_category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceAvailableByCategory(self, resr_category):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources " \
                "where stock > 0 and resr_category = %s" \
                "except select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Purchases natural inner join request " \
                "except select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Confirmation natural inner join reservation;"
        cursor.execute(query, (resr_category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRequest(self, rq_id):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock "\
                "from resources natural inner join Purchases natural inner join request where rq_id = %s;"
        cursor.execute(query, (rq_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByReservation(self, rs_id):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock "\
                "from resources natural inner join Confirmation natural inner join reservation where rs_id = %s;"
        cursor.execute(query, (rs_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequested(self):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Purchases natural inner join request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesReserved(self):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Confirmation natural inner join reservation where confirmation_status = 'confirmed';"

        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvailable(self):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources " \
                "where stock > 0 " \
                "except select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Purchases natural inner join request " \
                "except select resr_id, resr_price, resr_location, resr_category, stock " \
                "from resources natural inner join Confirmation natural inner join reservation;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasesByUsrId(self, usr_id):
        cursor = self.conn.cursor()
        query = "select resr_id, resr_price, resr_location, resr_category, stock  " \
                "from resources natural inner join Purchases natural inner join request " \
                "natural inner join Transaction natural inner join creditcard " \
                "natural inner join client " \
                "where usr_id = %s;"
        cursor.execute(query, (usr_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join Confirmation  where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, resr_price, resr_location, resr_category, stock):
        cursor = self.conn.cursor()
        query = "insert into resources(resr_price, resr_location, resr_category, stock) values (%s, %s, %s, %s) returning resr_id;"
        cursor.execute(query, (resr_price, resr_location, resr_category, stock))
        resrid = cursor.fetchone()[0]
        self.conn.commit()
        return resrid

    def delete(self, resr_id):
        cursor = self.conn.cursor()
        query = "delete from resources where resr_id = %s;"
        cursor.execute(query, (resr_id,))
        self.conn.commit()
        return resr_id

    def update(self, resr_id, resr_price, resr_location, resr_category, stock):
        cursor = self.conn.cursor()
        query = "update resources set resr_price = %s, resr_location = %s, resr_category = %s, stock = %s where resr_id = %s;"
        cursor.execute(query, (resr_id, resr_price, resr_location, resr_category, stock))
        self.conn.commit()
        return resr_id
