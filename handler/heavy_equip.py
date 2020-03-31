from flask import jsonify
from dao.heavy_equip import Heavy_EquipmentDAO


class HeavyEquipHandler:

    def build_heq_dict(self, row):
        result = {}
        result['heq_id'] = row[0]
        result['heq_type'] = row[1]
        return result

    def build_heq_attr(self, heq_id, heq_type):
        result = {}
        result['heq_id'] = heq_id
        result['heq_type'] = heq_type
        return result

    def getAllHE(self):
        dao = Heavy_EquipmentDAO()
        heq_list = dao.getAllHeavyEquip()
        result_list = []
        for row in heq_list:
            result = self.build_heq_dict(row)
            result_list.append(result)
        return jsonify(HeavyEquipment=result_list)

    def getHEById(self, heq_id):
        dao = Heavy_EquipmentDAO()
        row = dao.getHeavyEquipById(heq_id)
        if not row:
            return jsonify(Error="Heavy Equipment not found"), 404
        else:
            heq = self.build_heq_dict(row)
        return jsonify(HeavyEquipment=heq)

    def searchHE(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            heq = args.get("heq")
            if heq:
                dao = Heavy_EquipmentDAO()
                heq_list = dao.getHeavyEquipByType(heq)
                result_list = []
                for row in heq_list:
                    result = self.build_heq_dict(row)
                    result_list.append(result)
                return jsonify(HeavyEquipment=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertHE(self, form):
        if form and len(form) == 2:
            heq_type = form['heq_type']
            resr_id = form['resr_id']
            if heq_type:
                dao = Heavy_EquipmentDAO()
                heq_id = dao.insert(heq_type, resr_id)
                result = self.build_heq_attr(heq_id, heq_type)
                return jsonify(HeavyEquipment=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteHE(self, heq_id):
        dao = Heavy_EquipmentDAO()
        if not dao.getHeavyEquipById(heq_id):
            return jsonify(Error="Heavy Equipment not found"), 404
        else:
            dao.delete(heq_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateHE(self, heq_id, form):
        dao = Heavy_EquipmentDAO()
        if not dao.getHeavyEquipById(heq_id):
            return jsonify(Error="Heavy Equipment not found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                heq_type = form['heq_type']
                if heq_type:
                    dao.update(heq_id, heq_type)
                    result = self.build_heq_attr(heq_id, heq_type)
                    return jsonify(HeavyEquipment=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
