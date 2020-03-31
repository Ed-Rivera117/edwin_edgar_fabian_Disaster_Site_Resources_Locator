from flask import jsonify
from dao.clothing import ClothingDAO


class ClothingHandler:

    def build_clothing_dict(self, row):
        result = {}
        result['cl_id'] = row[0]
        result['cl_size'] = row[1]
        result['cl_color'] = row[2]
        result['cl_material'] = row[3]
        return result

    def build_clothing_attr(self, cl_id, cl_size, cl_color, cl_material):
        result = {}
        result['cl_id'] = cl_id
        result['cl_size'] = cl_size
        result['cl_color'] = cl_color
        result['cl_material'] = cl_material
        return result

    def getAllClothing(self):
        dao = ClothingDAO()
        cl_list = dao.getAllClothing()
        result_list = []
        for row in cl_list:
            result = self.build_clothing_dict(row)
            result_list.append(result)
        return jsonify(Clothing=result_list)

    def getClothingById(self, cl_id):
        dao = ClothingDAO()
        row = dao.getClothingById(cl_id)
        if not row:
            return jsonify(Error="Clothing not found"), 404
        else:
            clothing = self.build_clothing_dict(row)
        return jsonify(Clothing=clothing)

    def searchClothing(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            size = args.get("size")
            if size:
                dao = ClothingDAO()
                cl_list = dao.getClothingBySize(size)
                result_list = []
                for row in cl_list:
                    result = self.build_clothing_dict(row)
                    result_list.append(result)
                return jsonify(Clothing=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertClothing(self, form):
        if form and len(form) == 4:
            cl_size = form['cl_size']
            cl_color = form['cl_color']
            cl_material = form['cl_material']
            resr_id = form['resr_id']
            if cl_size and cl_color and cl_material:
                dao = ClothingDAO()
                cl_id = dao.insert(cl_size, cl_color, cl_material, resr_id)
                result = self.build_clothing_attr(cl_id, cl_size, cl_color, cl_material)
                return jsonify(Clothing=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteClothing(self, cl_id):
        dao = ClothingDAO()
        if not dao.getClothingById(cl_id):
            return jsonify(Error="Clothing not found"), 404
        else:
            dao.delete(cl_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateClothing(self, cl_id, form):
        dao = ClothingDAO()
        if not dao.getClothingById(cl_id):
            return jsonify(Error="Clothing not found"), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                cl_size = form['cl_size']
                cl_color = form['cl_color']
                cl_material = form['cl_material']
                if cl_size and cl_color and cl_material:
                    dao.update(cl_id, cl_size, cl_color, cl_material)
                    result = self.build_clothing_attr(cl_id, cl_size, cl_color, cl_material)
                    return jsonify(Clothing=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
