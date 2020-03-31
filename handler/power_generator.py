from flask import jsonify
from dao.power_generator import Power_GeneratorDAO


class PowerGeneratorHandler:

    def build_pg_dict(self, row):
        result = {}
        result['pg_id'] = row[0]
        result['pg_wattage'] = row[1]
        result['pg_fuelType'] = row[2]
        return result

    def build_pg_attr(self, pg_id, pg_wattage, pg_fuelType):
        result = {}
        result['pg_id'] = pg_id
        result['pg_wattage'] = pg_wattage
        result['pg_fuelType'] = pg_fuelType
        return result

    def getAllPG(self):
        dao = Power_GeneratorDAO()
        pg_list = dao.getAllPowerGenerator()
        result_list = []
        for row in pg_list:
            result = self.build_pg_dict(row)
            result_list.append(result)
        return jsonify(PowerGenerator=result_list)

    def getPGById(self, pg_id):
        dao = Power_GeneratorDAO()
        row = dao.getPowerGeneratorById(pg_id)
        if not row:
            return jsonify(Error="Medical Devices not found"), 404
        else:
            pg = self.build_pg_dict(row)
        return jsonify(PowerGenerator=pg)

    def searchPG(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            pg = args.get("power")
            if pg:
                dao = Power_GeneratorDAO()
                pg_list = dao.getPowerGeneratorByWattage(pg)
                result_list = []
                for row in pg_list:
                    result = self.build_pg_dict(row)
                    result_list.append(result)
                return jsonify(PowerGenerator=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertPG(self, form):
        if form and len(form) == 3:
            pg_wattage = form['pg_wattage']
            pg_fuelType = form['pg_fuelType']
            resr_id = form['resr_id']
            if pg_wattage and pg_fuelType:
                dao = Power_GeneratorDAO()
                pg_id = dao.insert(pg_wattage, pg_fuelType, resr_id)
                result = self.build_pg_attr(pg_id, pg_wattage, pg_fuelType)
                return jsonify(PowerGenerator=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deletePG(self, pg_id):
        dao = Power_GeneratorDAO()
        if not dao.getPowerGeneratorById(pg_id):
            return jsonify(Error="Medical Device not found"), 404
        else:
            dao.delete(pg_id)
            return jsonify(DeleteStatus="OK"), 200

    def updatePG(self, pg_id, form):
        dao = Power_GeneratorDAO()
        if not dao.getPowerGeneratorById(pg_id):
            return jsonify(Error="Medical Device not found"), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                pg_wattage = form['pg_wattage']
                pg_fuelType = form['pg_fuelType']
                if pg_wattage and pg_fuelType:
                    dao.update(pg_id, pg_wattage, pg_fuelType)
                    result = self.build_pg_attr(pg_id, pg_wattage, pg_fuelType)
                    return jsonify(PowerGenerator=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
