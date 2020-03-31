from config.dbconfig import pg_config
import psycopg2


class Medical_DevicesDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedicalDevices(self):
        cursor = self.conn.cursor()
        query = "select mdev_id, mdev_name, mdev_description from medicaldevices;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicalDevicesById(self, mdev_id):
        cursor = self.conn.cursor()
        query = "select mdev_id, mdev_name, mdev_description from medicaldevices where mdev_id = %s;"
        cursor.execute(query, (mdev_id,))
        result = cursor.fetchone()
        return result

    def getMedicalDeviceByName(self, mdev_name):
        cursor = self.conn.cursor()
        query = "select * from medicaldevices where mdev_name = %s;"
        cursor.execute(query, (mdev_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicalDeviceByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from medicaldevices  natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicalDeviceConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from medicaldevices natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicalDeviceBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from medicaldevices natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicalDevicePurchased(self):
        cursor = self.conn.cursor()
        query = "select * from medicaldevices natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, mdev_name, mdev_description, resr_id):
        cursor = self.conn.cursor()
        query = "insert into medicaldevices(mdev_name, mdev_description, resr_id) values (%s, %s, %s) returning mdev_id;"
        cursor.execute(query, (mdev_name, mdev_description, resr_id))
        mdevid = cursor.fetchone()[0]
        self.conn.commit()
        return mdevid

    def delete(self, mdev_id):
        cursor = self.conn.cursor()
        query = "delete from medicaldevices where mdev_id = %s;"
        cursor.execute(query, (mdev_id,))
        self.conn.commit()
        return mdev_id

    def update(self, mdev_id, mdev_name, mdev_description):
        cursor = self.conn.cursor()
        query = "update medicaldevices set mdev_name = %s, mdev_description = %s where mdev_id = %s;"
        cursor.execute(query, (mdev_id, mdev_name, mdev_description))
        self.conn.commit()
        return mdev_id