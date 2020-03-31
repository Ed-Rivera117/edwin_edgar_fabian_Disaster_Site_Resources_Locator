from flask import jsonify
from dao.reservation import ReservationDAO


class ReservationHandler:

    def build_rs_dict(self, row):
        result = {}
        result['rs_id'] = row[0]
        result['rs_date'] = row[1]
        return result

    def build_rs_attr(self, rs_id, rs_date):
        result = {}
        result['rs_id'] = rs_id
        result['rs_date'] = rs_date
        return result

    def getAllReservations(self):
        dao = ReservationDAO()
        rs_list = dao.getAllReservations()
        result_list = []
        for row in rs_list:
            result = self.build_rs_dict(row)
            result_list.append(result)
        return jsonify(Reservations=result_list)

    def getReservationsById(self, rs_id):
        dao = ReservationDAO()
        row = dao.getReservationById(rs_id)
        if not row:
            return jsonify(Error="Reservation not found"), 404
        else:
            rs = self.build_rs_dict(row)
        return jsonify(Reservation=rs)

    def searchReservation(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            rs = args.get("date")
            if rs:
                dao = ReservationDAO()
                rs_list = dao.getReservationByDate(rs)
                result_list = []
                for row in rs_list:
                    result = self.build_rs_dict(row)
                    result_list.append(result)
                return jsonify(Reservation=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertReservation(self, form):
        if form and len(form) == 1:
            rs_date = form['rs_date']
            if rs_date:
                dao = ReservationDAO()
                rs_id = dao.insert(rs_date)
                result = self.build_rs_attr(rs_id, rs_date)
                return jsonify(Reservation=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteReservation(self, rs_id):
        dao = ReservationDAO()
        if not dao.getReservationById(rs_id):
            return jsonify(Error="Reservation not found"), 404
        else:
            dao.delete(rs_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateReservation(self, rs_id, form):
        dao = ReservationDAO()
        if not dao.getReservationById(rs_id):
            return jsonify(Error="Reservation not found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                rs_date = form['rs_date']
                if rs_date:
                    dao.update(rs_id, rs_date)
                    result = self.build_rs_attr(rs_id, rs_date)
                    return jsonify(Reservation=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
