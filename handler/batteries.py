from flask import jsonify
from dao.batteries import BatteriesDAO


class BatteriesHandler:

    def build_batteries_dict(self, row):
        result = {}
        result['batt_id'] = row[0]
        result['batt_type'] = row[1]
        return result

    def build_batteries_attr(self, batt_id, batt_type):
        result = {}
        result['batt_id'] = batt_id
        result['batt_type'] = batt_type
        return result

    def getAllBatteries(self):
        dao = BatteriesDAO()
        batteries_list = dao.getAllBatteries()
        result_list = []
        for row in batteries_list:
            result = self.build_batteries_dict(row)
            result_list.append(result)
        return jsonify(Batteries=result_list)

    def getBatteriesById(self, batt_id):
        dao = BatteriesDAO()
        row = dao.getBatteriesById(batt_id)
        if not row:
            return jsonify(Error="Batteries not found"), 404
        else:
            batteries = self.build_batteries_dict(row)
        return jsonify(Batteries=batteries)

    def searchBatteries(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            type = args.get("type")
            if type:
                dao = BatteriesDAO()
                batteries_list = dao.getBatteriesByType(type)
                result_list = []
                for row in batteries_list:
                    result = self.build_batteries_dict(row)
                    result_list.append(result)
                return jsonify(Batteries=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertBatteries(self, form):
        if form and len(form) == 2:
            batt_type = form['batt_type']
            resr_id = form['resr_id']
            if batt_type:
                dao = BatteriesDAO()
                batt_id = dao.insert(batt_type, resr_id)
                result = self.build_batteries_attr(batt_id, batt_type)
                return jsonify(Batteries=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteBatteries(self, batt_id):
        dao = BatteriesDAO()
        if not dao.getBatteriesById(batt_id):
            return jsonify(Error="Batteries not found"), 404
        else:
            dao.delete(batt_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateBatteries(self, batt_id, form):
        dao = BatteriesDAO()
        if not dao.getBatteriesById(batt_id):
            return jsonify(Error="Batteries not found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                batt_type = form['batt_type']
                if batt_type:
                    dao.update(batt_id, batt_type)
                    result = self.build_batteries_attr(batt_id, batt_type)
                    return jsonify(Batteries=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
