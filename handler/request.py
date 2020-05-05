from flask import jsonify
from dao.request import RequestDAO


class RequestHandler:

    def build_rq_dict(self, row):
        result = {}
        result['rq_id'] = row[0]
        result['rq_date'] = row[1]
        return result

    def build_rq_attr(self, rq_id, rq_date):
        result = {}
        result['rq_id'] = rq_id
        result['rq_date'] = rq_date
        return result

    def getAllRequests(self):
        dao = RequestDAO()
        rq_list = dao.getAllRequests()
        result_list = []
        for row in rq_list:
            result = self.build_rq_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestsById(self, rq_id):
        dao = RequestDAO()
        row = dao.getRequestById(rq_id)
        if not row:
            return jsonify(Error="Request not found"), 404
        else:
            rq = self.build_rq_dict(row)
        return jsonify(Request=rq)

    def getRequestByUsrId(self, usr_id):
        dao = RequestDAO()
        row = dao.getRequestByUsrId(usr_id)
        if not row:
            return jsonify(Error="Request not found"), 404
        else:
            rq = self.build_rq_dict(row)
        return jsonify(Request=row)

    def searchRequest(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            rq = args.get("date")
            if rq:
                dao = RequestDAO()
                rq_list = dao.getRequestByDate(rq)
                result_list = []
                for row in rq_list:
                    result = self.build_rq_dict(row)
                    result_list.append(result)
                return jsonify(Request=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertRequest(self, form):
        if form and len(form) == 1:
            rq_date = form['rq_date']
            if rq_date:
                dao = RequestDAO()
                rq_id = dao.insert(rq_date)
                result = self.build_rq_attr(rq_id, rq_date)
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteRequest(self, rq_id):
        dao = RequestDAO()
        if not dao.getRequestById(rq_id):
            return jsonify(Error="Request not found"), 404
        else:
            dao.delete(rq_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateRequest(self, rq_id, form):
        dao = RequestDAO()
        if not dao.getRequestById(rq_id):
            return jsonify(Error="Request not found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                rq_date = form['rq_date']
                if rq_date:
                    dao.update(rq_id, rq_date)
                    result = self.build_rq_attr(rq_id, rq_date)
                    return jsonify(Request=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
