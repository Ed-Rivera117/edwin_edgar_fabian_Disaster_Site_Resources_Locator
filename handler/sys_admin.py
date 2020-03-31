from flask import jsonify
from dao.sys_admin import Sys_adminDAO


class SysAdminHandler:

    def build_sa_dict(self, row):
        result = {}
        result['sa_id'] = row[0]
        result['sa_usr'] = row[1]
        result['sa_password'] = row[2]
        return result

    def build_sa_attr(self, sa_id, sa_usr, sa_password):
        result = {}
        result['sa_id'] = sa_id
        result['sa_usr'] = sa_usr
        result['sa_password'] = sa_password
        return result

    def getAllSysAdmin(self):
        dao = Sys_adminDAO()
        sa_list = dao.getAllSys_admin()
        result_list = []
        for row in sa_list:
            result = self.build_sa_dict(row)
            result_list.append(result)
        return jsonify(SystemAdministrator=result_list)

    def getSysAdminById(self, sa_id):
        dao = Sys_adminDAO()
        row = dao.getSys_adminById(sa_id)
        if not row:
            return jsonify(Error="System Administrator not found"), 404
        else:
            sa = self.build_sa_dict(row)
        return jsonify(SysAdmin=sa)

    def searchSysAdmin(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            usr = args.get("user")
            if usr:
                dao = Sys_adminDAO()
                sa_list = dao.getSys_adminByUser(usr)
                result_list = []
                for row in sa_list:
                    result = self.build_sa_dict(row)
                    result_list.append(result)
                return jsonify(SystemAdministrator=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertSysAdmin(self, form):
        if form and len(form) == 2:
            sa_usr = form['sa_usr']
            sa_password = form['sa_password']
            if sa_usr and sa_password:
                dao = Sys_adminDAO()
                sa_id = dao.insert(sa_usr, sa_password)
                result = self.build_sa_attr(sa_id, sa_usr, sa_password)
                return jsonify(SystemAdministrator=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteSysAdmin(self, sa_id):
        dao = Sys_adminDAO()
        if not dao.getSys_adminById(sa_id):
            return jsonify(Error="System Administrator not found"), 404
        else:
            dao.delete(sa_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateSysAdmin(self, sa_id, form):
        dao = Sys_adminDAO()
        if not dao.getSys_adminById(sa_id):
            return jsonify(Error="System Administrator not found"), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                sa_usr = form['sa_usr']
                sa_password = form['sa_password']
                if sa_usr and sa_password:
                    dao.update(sa_id, sa_usr, sa_password)
                    result = self.build_sa_attr(sa_id, sa_usr, sa_password)
                    return jsonify(SystemAdministrator=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
