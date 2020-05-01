from flask import jsonify
from dao.resources import ResourcesDAO


class ResourcesHandler:

    def build_resr_dict(self, row):
        result = {}
        result['resr_id'] = row[0]
        result['resr_price'] = row[1]
        result['resr_location'] = row[2]
        result['resr_category'] = row[3]
        result['stock'] = row[4]
        return result

    def build_resr_attr(self, resr_id, resr_price, resr_location, resr_category, stock):
        result = {}
        result['resr_id'] = resr_id
        result['resr_price'] = resr_price
        result['resr_location'] = resr_location
        result['resr_category'] = resr_category
        result['stock'] = stock
        return result

    def getAllResource(self):
        dao = ResourcesDAO()
        resr_list = dao.getAllResources()
        result_list = []
        for row in resr_list:
            result = self.build_resr_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def getResourceById(self, resr_id):
        dao = ResourcesDAO()
        row = dao.getResourcesById(resr_id)
        if not row:
            return jsonify(Error="Resource not found"), 404
        else:
            sa = self.build_resr_dict(row)
        return jsonify(Resource=sa)

    def getResourcesRequested(self):
        dao = ResourcesDAO()
        resr_list = dao.getResourcesRequested()
        result_list = []
        for row in resr_list:
            result = self.build_resr_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)
    
    def getResourcesAvailable(self):
        dao = ResourcesDAO()
        resr_list = dao.getResourcesAvailable()
        result_list = []
        for row in resr_list:
            result = self.build_resr_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def searchResource(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            location = args.get("location")
            category = args.get("category")
            if location:
                dao = ResourcesDAO()
                resr_list = dao.getResourceByLocation(location)
                result_list = []
                for row in resr_list:
                    result = self.build_resr_dict(row)
                    result_list.append(result)
                return jsonify(Resource=result_list)
            elif category:
                dao = ResourcesDAO()
                resr_list = dao.getResourceByLocation(category)
                result_list = []
                for row in resr_list:
                    result = self.build_resr_dict(row)
                    result_list.append(result)
                return jsonify(Resource=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertResource(self, form):
        if form and len(form) == 4:
            resr_price = form['resr_price']
            resr_location = form['resr_location']
            resr_category = form['resr_category']
            stock = form['stock']
            if resr_price and resr_location and resr_category and stock:
                dao = ResourcesDAO()
                resr_id = dao.insert(resr_price, resr_location, resr_category, stock)
                result = self.build_resr_attr(resr_id, resr_price, resr_location, resr_category, stock)
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteResource(self, resr_id):
        dao = ResourcesDAO()
        if not dao.getResourcesById(resr_id):
            return jsonify(Error="Resource not found"), 404
        else:
            dao.delete(resr_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateResource(self, resr_id, form):
        dao = ResourcesDAO()
        if not dao.getResourcesById(resr_id):
            return jsonify(Error="Resource not found"), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                resr_price = form['resr_price']
                resr_location = form['resr_location']
                resr_category = form['resr_category']
                if resr_price and resr_location:
                    dao.update(resr_id, resr_price, resr_location, resr_category)
                    result = self.build_resr_attr(resr_id, resr_price, resr_location, resr_category)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
