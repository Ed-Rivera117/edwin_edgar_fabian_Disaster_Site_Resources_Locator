from flask import jsonify
from dao.ice import IceDAO


class IceHandler:

    def build_ice_dict(self, row):
        result = {}
        result['ice_id'] = row[0]
        result['ice_bagSize'] = row[1]
        return result

    def build_ice_attr(self, ice_id, ice_bagSize):
        result = {}
        result['ice_id'] = ice_id
        result['ice_bagSize'] = ice_bagSize
        return result

    def getAllIce(self):
        dao = IceDAO()
        ice_list = dao.getAllIce()
        result_list = []
        for row in ice_list:
            result = self.build_ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    def getIceById(self, ice_id):
        dao = IceDAO()
        row = dao.getIceById(ice_id)
        if not row:
            return jsonify(Error="Ice not found"), 404
        else:
            ice = self.build_ice_dict(row)
        return jsonify(Ice=ice)

    def searchIce(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            ice = args.get("ice")
            if ice:
                dao = IceDAO()
                ice_list = dao.getIceByBagSize(ice)
                result_list = []
                for row in ice_list:
                    result = self.build_ice_dict(row)
                    result_list.append(result)
                return jsonify(Ice=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertIce(self, form):
        if form and len(form) == 2:
            ice_bagSize = form['ice_bagSize']
            resr_id = form['resr_id']
            if ice_bagSize:
                dao = IceDAO()
                ice_id = dao.insert(ice_bagSize, resr_id)
                result = self.build_ice_attr(ice_id, ice_bagSize)
                return jsonify(Ice=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteIce(self, ice_id):
        dao = IceDAO()
        if not dao.getIceById(ice_id):
            return jsonify(Error="Ice not found"), 404
        else:
            dao.delete(ice_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateIce(self, ice_id, form):
        dao = IceDAO()
        if not dao.getIceById(ice_id):
            return jsonify(Error="Ice not found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                ice_bagSize = form['ice_bagSize']
                if ice_bagSize:
                    dao.update(ice_id, ice_bagSize)
                    result = self.build_ice_attr(ice_id, ice_bagSize)
                    return jsonify(Ice=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
