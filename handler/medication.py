from flask import jsonify
from dao.medication import MedicationDAO


class MedicationHandler:

    def build_med_dict(self, row):
        result = {}
        result['med_id'] = row[0]
        result['med_name'] = row[1]
        return result

    def build_med_attr(self, med_id, med_name):
        result = {}
        result['med_id'] = med_id
        result['med_name'] = med_name
        return result

    def getAllMed(self):
        dao = MedicationDAO()
        med_list = dao.getAllMed()
        result_list = []
        for row in med_list:
            result = self.build_med_dict(row)
            result_list.append(result)
        return jsonify(Medication=result_list)

    def getMedById(self, med_id):
        dao = MedicationDAO()
        row = dao.getMedById(med_id)
        if not row:
            return jsonify(Error="Medication not found"), 404
        else:
            md = self.build_med_dict(row)
        return jsonify(Medication=md)

    def searchMD(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            med = args.get("medication")
            if med:
                dao = MedicationDAO()
                med_list = dao.getMedByName(med)
                result_list = []
                for row in med_list:
                    result = self.build_med_dict(row)
                    result_list.append(result)
                return jsonify(Medication=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertMD(self, form):
        if form and len(form) == 2:
            med_name = form['med_name']
            resr_id = form['resr_id']
            if med_name:
                dao = MedicationDAO()
                med_id = dao.insert(med_name, resr_id)
                result = self.build_med_attr(med_id, med_name)
                return jsonify(Medication=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteMD(self, med_id):
        dao = MedicationDAO()
        if not dao.getMedById(med_id):
            return jsonify(Error="Medication not found"), 404
        else:
            dao.delete(med_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateMD(self, med_id, form):
        dao = MedicationDAO()
        if not dao.getMedById(med_id):
            return jsonify(Error="Medication not found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                med_name = form['med_name']
                if med_name:
                    dao.update(med_id, med_name)
                    result = self.build_med_attr(med_id, med_name)
                    return jsonify(Medication=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
