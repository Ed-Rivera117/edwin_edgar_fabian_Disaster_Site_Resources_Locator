from flask import jsonify
from dao.usr import UsrDAO


class UsrHandler:

    def build_usr_dict(self, row):
        result = {}
        result['usr_id'] = row[0]
        result['usr_fname'] = row[1]
        result['usr_lname'] = row[2]
        result['usr_email'] = row[3]
        result['usr_phone'] = row[4]
        return result

    def build_usr_attr(self, usr_id, usr_fname, usr_lname, usr_email):
        result = {}
        result['usr_id'] = usr_id
        result['usr_fname'] = usr_fname
        result['usr_lname'] = usr_lname
        result['usr_email'] = usr_email
        return result

    def getAllUser(self):
        dao = UsrDAO()
        usr_list = dao.getAllUsr()
        result_list = []
        for row in usr_list:
            result = self.build_usr_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getUserById(self, usr_id):
        dao = UsrDAO()
        row = dao.getUsrById(usr_id)
        if not row:
            return jsonify(Error="User not found"), 404
        else:
            sa = self.build_usr_dict(row)
        return jsonify(User=sa)

    def searchUser(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            usr = args.get("user")
            if usr:
                dao = UsrDAO()
                usr_list = dao.getUsrByFirstName(usr)
                result_list = []
                for row in usr_list:
                    result = self.build_usr_dict(row)
                    result_list.append(result)
                return jsonify(User=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertUser(self, form):
        if form and len(form) == 3:
            usr_fname = form['usr_fname']
            usr_lname = form['usr_lname']
            usr_email = form['usr_email']
            if usr_fname and usr_lname:
                dao = UsrDAO()
                usr_id = dao.insert(usr_fname, usr_lname, usr_email)
                result = self.build_usr_attr(usr_id, usr_fname, usr_lname, usr_email)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteUser(self, usr_id):
        dao = UsrDAO()
        if not dao.getUsrById(usr_id):
            return jsonify(Error="User not found"), 404
        else:
            dao.delete(usr_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateUser(self, usr_id, form):
        dao = UsrDAO()
        if not dao.getUsrById(usr_id):
            return jsonify(Error="User not found"), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                usr_fname = form['usr_fname']
                usr_lname = form['usr_lname']
                usr_email = form['usr_email']
                if usr_fname and usr_lname:
                    dao.update(usr_id, usr_fname, usr_lname, usr_email)
                    result = self.build_usr_attr(usr_id, usr_fname, usr_lname, usr_email)
                    return jsonify(User=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
