from flask import jsonify
from dao.water import WaterDAO


class WaterHandler:

    def build_wt_dict(self, row):
        result = {}
        result['h2O_id'] = row[0]
        result['h2O_volume'] = row[1]
        return result

    def build_wt_attr(self, h2O_id, h2O_volume):
        result = {}
        result['h2O_id'] = h2O_id
        result['h2O_volume'] = h2O_volume
        return result

    def getAllWater(self):
        dao = WaterDAO()
        wt_list = dao.getAllWater()
        result_list = []
        for row in wt_list:
            result = self.build_wt_dict(row)
            result_list.append(result)
        return jsonify(Water=result_list)

    def getWaterById(self, h2O_id):
        dao = WaterDAO()
        row = dao.getWaterById(h2O_id)
        if not row:
            return jsonify(Error="Water not found"), 404
        else:
            wt = self.build_wt_dict(row)
        return jsonify(Water=wt)

    def searchWater(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            wt = args.get("water")
            if wt:
                dao = WaterDAO()
                wt_list = dao.getWaterByVolume(wt)
                result_list = []
                for row in wt_list:
                    result = self.build_wt_dict(row)
                    result_list.append(result)
                return jsonify(Water=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertWater(self, form):
        if form and len(form) == 2:
            h2O_volume = form['h2O_volume']
            resr_id = form['resr_id']
            if h2O_volume:
                dao = WaterDAO()
                h2O_id = dao.insert(h2O_volume, resr_id)
                result = self.build_wt_attr(h2O_id, h2O_volume)
                return jsonify(Water=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteWater(self, h2O_id):
        dao = WaterDAO()
        if not dao.getWaterById(h2O_id):
            return jsonify(Error="Water not found"), 404
        else:
            dao.delete(h2O_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateWater(self, h2O_id, form):
        dao = WaterDAO()
        if not dao.getWaterById(h2O_id):
            return jsonify(Error="Water not found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                h2O_volume = form['h2O_volume']
                if h2O_volume:
                    dao.update(h2O_id, h2O_volume)
                    result = self.build_wt_attr(h2O_id, h2O_volume)
                    return jsonify(Water=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
