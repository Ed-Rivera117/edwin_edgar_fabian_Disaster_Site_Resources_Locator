from flask import jsonify
from dao.baby_food import Baby_FoodDAO


class BabyFoodHandler:

    def build_bbfood_dict(self, row):
        result = {}
        result['bb_id'] = row[0]
        result['bb_flavor'] = row[1]
        result['bb_expDate'] = row[2]
        return result

    def build_bbfood_attr(self, bb_id, bb_flavor, bb_expDate):
        result = {}
        result['bb_id'] = bb_id
        result['bb_flavor'] = bb_flavor
        result['bb_expDate'] = bb_expDate
        return result

    def getAllBabyFood(self):
        dao = Baby_FoodDAO()
        bbfood_list = dao.getAllBabyFood()
        result_list = []
        for row in bbfood_list:
            result = self.build_bbfood_dict(row)
            result_list.append(result)
        return jsonify(BabyFood=result_list)

    def getBabyFoodById(self, bb_id):
        dao = Baby_FoodDAO()
        row = dao.getBabyFoodById(bb_id)
        if not row:
            return jsonify(Error="Baby Food not found"), 404
        else:
            bbfood = self.build_bbfood_dict(row)
        return jsonify(BabyFood=bbfood)

    def searchBabyFood(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            flavor = args.get("flavor")
            if (len(args) == 1) and flavor:
                dao = Baby_FoodDAO()
                bbfood_list = dao.getBabyFoodByFlavor(flavor)
                result_list = []
                for row in bbfood_list:
                    result = self.build_bbfood_dict(row)
                    result_list.append(result)
                return jsonify(BabyFood=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertBabyFood(self, form):
        if form and len(form) == 3:
            bb_flavor = form['bb_flavor']
            bb_expDate = form['bb_expDate']
            resr_id = form['resr_id']
            if bb_flavor and bb_expDate:
                dao = Baby_FoodDAO()
                bb_id = dao.insert(bb_flavor, bb_expDate, resr_id)
                result = self.build_bbfood_attr(bb_id, bb_flavor, bb_expDate)
                return jsonify(BabyFood=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteBabyFood(self, bb_id):
        dao = Baby_FoodDAO()
        if not dao.getBabyFoodById(bb_id):
            return jsonify(Error="Baby Food not found"), 404
        else:
            dao.delete(bb_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateBabyFood(self, bb_id, form):
        dao = Baby_FoodDAO()
        if not dao.getBabyFoodById(bb_id):
            return jsonify(Error="Baby Food not found"), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                bb_flavor = form['bb_flavor']
                bb_expDate = form['bb_expDate']
                if bb_flavor and bb_expDate:
                    dao.update(bb_id, bb_flavor, bb_expDate)
                    result = self.build_bbfood_attr(bb_id, bb_flavor, bb_expDate)
                    return jsonify(BabyFood=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
