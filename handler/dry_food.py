from flask import jsonify
from dao.dry_food import Dry_FoodDAO


class DryFoodHandler:

    def build_df_dict(self, row):
        result = {}
        result['df_id'] = row[0]
        result['df_name'] = row[1]
        result['df_expDate'] = row[2]
        return result

    def build_df_attr(self, df_id, df_name, df_expDate):
        result = {}
        result['df_id'] = df_id
        result['df_name'] = df_name
        result['df_expDate'] = df_expDate
        return result

    def getAllDF(self):
        dao = Dry_FoodDAO()
        df_list = dao.getAllDryFood()
        result_list = []
        for row in df_list:
            result = self.build_df_dict(row)
            result_list.append(result)
        return jsonify(DryFood=result_list)

    def getDFById(self, df_id):
        dao = Dry_FoodDAO()
        row = dao.getDryFoodById(df_id)
        if not row:
            return jsonify(Error="Dry Food not found"), 404
        else:
            df = self.build_df_dict(row)
        return jsonify(DryFood=df)

    def searchDF(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            food = args.get("food")
            if food:
                dao = Dry_FoodDAO()
                df_list = dao.getDryFoodByName(food)
                result_list = []
                for row in df_list:
                    result = self.build_df_dict(row)
                    result_list.append(result)
                return jsonify(DryFood=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertDF(self, form):
        if form and len(form) == 3:
            df_name = form['df_name']
            df_expDate = form['df_expDate']
            resr_id = form['resr_id']
            if df_expDate and df_name:
                dao = Dry_FoodDAO()
                df_id = dao.insert(df_expDate, df_name, resr_id)
                result = self.build_df_attr(df_id, df_name, df_expDate)
                return jsonify(DryFood=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteDF(self, df_id):
        dao = Dry_FoodDAO()
        if not dao.getDryFoodById(df_id):
            return jsonify(Error="Dry Food not found"), 404
        else:
            dao.delete(df_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateDF(self, df_id, form):
        dao = Dry_FoodDAO()
        if not dao.getDryFoodById(df_id):
            return jsonify(Error="Dry Food not found"), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                df_name = form['df_name']
                df_expDate = form['df_expDate']
                if df_name and df_expDate:
                    dao.update(df_id, df_name, df_expDate)
                    result = self.build_df_attr(df_id, df_name, df_expDate)
                    return jsonify(DryFood=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
