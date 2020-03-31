from flask import jsonify
from dao.canned_food import Canned_FoodDAO


class CannedFoodHandler:

    def build_cf_dict(self, row):
        result = {}
        result['cf_id'] = row[0]
        result['cf_name'] = row[1]
        result['cf_expDate'] = row[2]
        return result

    def build_cf_attr(self, cf_id, cf_name, cf_expDate):
        result = {}
        result['cf_id'] = cf_id
        result['cf_name'] = cf_name
        result['cf_expDate'] = cf_expDate
        return result

    def getAllCF(self):
        dao = Canned_FoodDAO()
        cf_list = dao.getAllCannedFood()
        result_list = []
        for row in cf_list:
            result = self.build_cf_dict(row)
            result_list.append(result)
        return jsonify(CannedFood=result_list)

    def getCFById(self, cf_id):
        dao = Canned_FoodDAO()
        row = dao.getCannedFoodById(cf_id)
        if not row:
            return jsonify(Error="Canned Food not found"), 404
        else:
            cffood = self.build_cf_dict(row)
        return jsonify(CannedFood=cffood)

    def searchCF(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            name = args.get("name")
            if name:
                dao = Canned_FoodDAO()
                cffood_list = dao.getCannedFoodByName(name)
                result_list = []
                for row in cffood_list:
                    result = self.build_cf_dict(row)
                    result_list.append(result)
                return jsonify(CannedFood=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertCF(self, form):
        if form and len(form) == 3:
            cf_name = form['cf_name']
            cf_expDate = form['cf_expDate']
            resr_id = form['resr_id']
            if cf_name and cf_expDate:
                dao = Canned_FoodDAO()
                cf_id = dao.insert(cf_name, cf_expDate, resr_id)
                result = self.build_cf_attr(cf_id, cf_name, cf_expDate)
                return jsonify(CannedFood=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteCF(self, cf_id):
        dao = Canned_FoodDAO()
        if not dao.getCannedFoodById(cf_id):
            return jsonify(Error="Canned Food not found"), 404
        else:
            dao.delete(cf_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateCF(self, cf_id, form):
        dao = Canned_FoodDAO()
        if not dao.getCannedFoodById(cf_id):
            return jsonify(Error="Canned Food not found"), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                cf_name = form['cf_name']
                cf_expDate = form['cf_expDate']
                if cf_expDate and cf_name:
                    dao.update(cf_id, cf_name, cf_expDate)
                    result = self.build_cf_attr(cf_id, cf_name, cf_expDate)
                    return jsonify(CannedFood=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
