from flask import jsonify
from dao.client import ClientDAO


class ClientHandler:

    def build_client_dict(self, row):
        result = {}
        result['c_id'] = row[0]
        result['c_usr'] = row[1]
        result['c_password'] = row[2]
        return result

    def build_client_attr(self, c_id, c_usr, c_password):
        result = {}
        result['c_id'] = c_id
        result['c_usr'] = c_usr
        result['c_password'] = c_password
        return result

    def getAllClients(self):
        dao = ClientDAO()
        clients_list = dao.getAllClients()
        result_list = []
        for row in clients_list:
            result = self.build_client_dict(row)
            result_list.append(result)
        return jsonify(Clients=result_list)

    def getClientById(self, c_id):
        dao = ClientDAO()
        row = dao.getClientById(c_id)
        if not row:
            return jsonify(Error="Client not found"), 404
        else:
            client = self.build_client_dict(row)
        return jsonify(Client = client)

    def searchClients(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            usr = args.get("user")
            if usr:
                dao = ClientDAO()
                client_list = dao.getClientByUser(usr)
                result_list = []
                for row in client_list:
                    result = self.build_client_dict(row)
                    result_list.append(result)
                return jsonify(Clients=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertClient(self, form):
        if form and len(form) == 2:
            c_usr = form['c_usr']
            c_password = form['c_password']
            if c_usr and c_password:
                dao = ClientDAO()
                c_id = dao.insert(c_usr, c_password)
                result = self.build_client_attr(c_id, c_usr, c_password)
                return jsonify(Client=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteClient(self, c_id):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client not found"), 404
        else:
            dao.delete(c_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateClient(self, c_id, form):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client not found"), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                c_usr = form['c_usr']
                c_password = form['c_password']
                if c_usr and c_password:
                    dao.update(c_id, c_usr, c_password)
                    result = self.build_client_attr(c_id, c_usr, c_password)
                    return jsonify(Client=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
