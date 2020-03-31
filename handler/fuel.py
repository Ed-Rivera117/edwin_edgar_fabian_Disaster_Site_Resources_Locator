from flask import jsonify
from dao.fuel import FuelDAO


class FuelHandler:

    def build_fuel_dict(self, row):
        result = {}
        result['fuel_id'] = row[0]
        result['fuel_type'] = row[1]
        return result

    def build_fuel_attr(self, fuel_id, fuel_type):
        result = {}
        result['fuel_id'] = fuel_id
        result['fuel_type'] = fuel_type
        return result

    def getAllFuel(self):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def getFuelById(self, fuel_id):
        dao = FuelDAO()
        row = dao.getFuelById(fuel_id)
        if not row:
            return jsonify(Error="Fuel not found"), 404
        else:
            fuel = self.build_fuel_dict(row)
        return jsonify(Fuel=fuel)

    def searchFuel(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            fuel = args.get("fuel")
            if fuel:
                dao = FuelDAO()
                fuel_list = dao.getFuelByType(fuel)
                result_list = []
                for row in fuel_list:
                    result = self.build_fuel_dict(row)
                    result_list.append(result)
                return jsonify(Fuel=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertFuel(self, form):
        if form and len(form) == 2:
            fuel_type = form['fuel_type']
            resr_id = form['resr_id']
            if fuel_type:
                dao = FuelDAO()
                fuel_id = dao.insert(fuel_type, resr_id)
                result = self.build_fuel_attr(fuel_id, fuel_type)
                return jsonify(Fuel=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteFuel(self, fuel_id):
        dao = FuelDAO()
        if not dao.getFuelById(fuel_id):
            return jsonify(Error="Fuel not found"), 404
        else:
            dao.delete(fuel_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateFuel(self, fuel_id, form):
        dao = FuelDAO()
        if not dao.getFuelById(fuel_id):
            return jsonify(Error="Fuel not found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                fuel_type = form['fuel_type']
                if fuel_type:
                    dao.update(fuel_id, fuel_type)
                    result = self.build_fuel_attr(fuel_id, fuel_type)
                    return jsonify(Fuel=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
