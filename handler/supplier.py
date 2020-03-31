from flask import jsonify
from dao.supplier import SupplierDAO

class SupplierHandler:

    def build_supplier_dict(self, row):
        result = {}
        result['s_id'] = row[0]
        result['s_usr'] = row[1]
        result['s_password'] = row[2]
        result['s_location'] = row[3]
        result['s_resources'] = row[4]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['resr_id'] = row[0]
        result['resr_price'] = row[1]
        result['resr_location'] = row[2]
        result['resr_category'] = row[3]
        return result

    def build_supplier_attr(self, s_id, s_usr, s_password, s_location, s_resources):
        result = {}
        result['s_id'] = s_id
        result['s_usr'] = s_usr
        result['s_password'] = s_password
        result['s_location'] = s_location
        result['s_resources'] = s_resources
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        supplier_list = dao.getAllSuppliers()
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, s_id):
        dao = SupplierDAO()
        row = dao.getSupplierById(s_id)
        if not row:
            return jsonify(Error="Supplier not found"), 404
        else:
            supp = self.build_supplier_dict(row)
        return jsonify(Supplier=supp)

    def searchSuppliers(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            location = args.get("location")
            if location:
                dao = SupplierDAO()
                supplier_list = dao.getSupplierByLocation(location)
                result_list = []
                for row in supplier_list:
                    result = self.build_supplier_dict(row)
                    result_list.append(result)
                return jsonify(Suppliers=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertSupplier(self, form):
        if form and len(form) == 4:
            s_usr = form['s_usr']
            s_password = form['s_password']
            s_location = form['s_location']
            s_resources = form['s_resources']
            if s_usr and s_password and s_location and s_resources:
                dao = SupplierDAO()
                s_id = dao.insert(s_usr, s_password, s_location, s_resources)
                result = self.build_supplier_attr(s_id, s_usr, s_password, s_location, s_resources)
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteSupplier(self, s_id):
        dao = SupplierDAO()
        if not dao.getSupplierById():
            return jsonify(Error="Supplier not found"), 404
        else:
            dao.delete(s_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateSupplier(self, s_id, form):
        dao = SupplierDAO()
        if not dao.getSupplierById(s_id):
            return jsonify(Error="Supplier not found"), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                s_usr = form['s_usr']
                s_password = form['s_password']
                s_location = form['s_location']
                s_resources = form['s_resources']
                if s_usr and s_password and s_location and s_resources:
                    dao.update(s_id, s_usr, s_password, s_location, s_resources)
                    result = self.build_supplier_attr(s_id, s_usr, s_password, s_location, s_resources)
                    return jsonify(Supplier=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
