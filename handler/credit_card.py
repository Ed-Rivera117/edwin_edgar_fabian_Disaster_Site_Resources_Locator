from flask import jsonify
from dao.credit_card import Credit_CardDAO


class CreditCardHandler:

    def build_cc_dict(self, row):
        result = {}
        result['cc_id'] = row[0]
        result['cc_nameOnCard'] = row[1]
        result['cc_number'] = row[2]
        result['cc_expDate'] = row[3]
        result['cc_cvc'] = row[4]
        return result

    def build_cc_attr(self, cc_id, cc_nameOnCard, cc_expDate, cc_cvc):
        result = {}
        result['cc_id'] = cc_id
        result['cc_nameOnCard'] = cc_nameOnCard
        result['cc_expDate'] = cc_expDate
        result['cc_cvc'] = cc_cvc
        return result

    def getAllCreditCard(self):
        dao = Credit_CardDAO()
        cc_list = dao.getAllCreditCards()
        result_list = []
        for row in cc_list:
            result = self.build_cc_dict(row)
            result_list.append(result)
        return jsonify(CreditCards=result_list)

    def getCreditCardById(self, cc_id):
        dao = Credit_CardDAO()
        row = dao.getCreditCardById(cc_id)
        if not row:
            return jsonify(Error="Credit Card not found"), 404
        else:
            cc = self.build_cc_dict(row)
        return jsonify(CreditCard=cc)

    def searchCC(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            name = args.get("name")
            if name:
                dao = Credit_CardDAO()
                cc_list = dao.getCreditCardByName(name)
                result_list = []
                for row in cc_list:
                    result = self.build_cc_dict(row)
                    result_list.append(result)
                return jsonify(CreditCard=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertCC(self, form):
        if form and len(form) == 3:
            cc_nameOnCard = form['cc_nameOnCard']
            cc_expDate = form['cc_expDate']
            cc_cvc = form['cc_cvc']
            if cc_nameOnCard and cc_expDate and cc_cvc:
                dao = Credit_CardDAO()
                cc_id = dao.insert(cc_nameOnCard, cc_expDate, cc_cvc)
                result = self.build_cc_attr(cc_id, cc_nameOnCard, cc_expDate, cc_cvc)
                return jsonify(CreditCard=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteCC(self, cc_id):
        dao = Credit_CardDAO()
        if not dao.getCreditCardById(cc_id):
            return jsonify(Error="Credit Card not found"), 404
        else:
            dao.delete(cc_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateCC(self, cc_id, form):
        dao = Credit_CardDAO()
        if not dao.getCreditCardById(cc_id):
            return jsonify(Error="Credit Card not found"), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                cc_nameOnCard = form['cc_nameOnCard']
                cc_expDate = form['cc_expDate']
                cc_cvc = form['cc_cvc']
                if cc_nameOnCard and cc_expDate and cc_cvc:
                    dao.update(cc_id, cc_nameOnCard, cc_expDate, cc_cvc)
                    result = self.build_cc_attr(cc_id, cc_nameOnCard, cc_expDate, cc_cvc)
                    return jsonify(CreditCard=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
