from config.dbconfig import pg_config
import psycopg2


class ToolDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllTools(self):
        cursor = self.conn.cursor()
        query = "select tool_id, tool_name from tools;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolById(self, tool_id):
        cursor = self.conn.cursor()
        query = "select tool_id, tool_name from tools where tool_id = %s;"
        cursor.execute(query, (tool_id,))
        result = cursor.fetchone()
        return result

    def getToolByName(self, tool_name):
        cursor = self.conn.cursor()
        query = "select * from tools where tool_name = %s;"
        cursor.execute(query, (tool_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolByLocation(self, resr_location):
        cursor = self.conn.cursor()
        query = "select * from tools natural inner join Resources where resr_location = %s;"
        cursor.execute(query, (resr_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolConfirmed(self, confirmation_status):
        cursor = self.conn.cursor()
        query = "select * from tools natural inner join Resources natural inner join Confirmation where confirmation_status = %s;"
        cursor.execute(query, (confirmation_status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from tools natural inner join Resources natural inner join Provides natural inner join supplier where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolPurchased(self):
        cursor = self.conn.cursor()
        query = "select * from tools natural inner join Purchases;"
        cursor.execute(query, ())
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, tool_name, resr_id):
        cursor = self.conn.cursor()
        query = "insert into tools(tool_name, resr_id) values (%s, %s) returning tool_id;"
        cursor.execute(query, (tool_name, resr_id))
        tid = cursor.fetchone()[0]
        self.conn.commit()
        return tid

    def delete(self, tool_id):
        cursor = self.conn.cursor()
        query = "delete from tools where tool_id = %s;"
        cursor.execute(query, (tool_id,))
        self.conn.commit()
        return tool_id

    def update(self, tool_id, tool_name):
        cursor = self.conn.cursor()
        query = "update tools set tool_name = %s where tool_id = %s;"
        cursor.execute(query, (tool_id, tool_name))
        self.conn.commit()
        return tool_id