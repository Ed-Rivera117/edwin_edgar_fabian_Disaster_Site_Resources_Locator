from flask import jsonify
from dao.medical_devices import Medical_DevicesDAO


class MedicalDeviceHandler:

    def build_md_dict(self, row):
        result = {}
        result['mdev_id'] = row[0]
        result['mdev_name'] = row[1]
        result['mdev_description'] = row[2]
        return result

    def build_md_attr(self, mdev_id, mdev_name, mdev_description):
        result = {}
        result['mdev_id'] = mdev_id
        result['mdev_name'] = mdev_name
        result['mdev_description'] = mdev_description
        return result

    def getAllMD(self):
        dao = Medical_DevicesDAO()
        med_list = dao.getAllMedicalDevices()
        result_list = []
        for row in med_list:
            result = self.build_md_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevices=result_list)

    def getMDById(self, mdev_id):
        dao = Medical_DevicesDAO()
        row = dao.getMedicalDevicesById(mdev_id)
        if not row:
            return jsonify(Error="Medical Devices not found"), 404
        else:
            md = self.build_md_dict(row)
        return jsonify(MedicalDevice=md)

    def searchMD(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            md = args.get("medical")
            if md:
                dao = Medical_DevicesDAO()
                med_list = dao.getMedicalDeviceByName(md)
                result_list = []
                for row in med_list:
                    result = self.build_md_dict(row)
                    result_list.append(result)
                return jsonify(MedicalDevice=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertMD(self, form):
        if form and len(form) == 3:
            mdev_name = form['mdev_name']
            mdev_description = form['mdev_description']
            resr_id = form['resr_id']
            if mdev_name and mdev_description:
                dao = Medical_DevicesDAO()
                mdev_id = dao.insert(mdev_name, mdev_description, resr_id)
                result = self.build_md_attr(mdev_id, mdev_name, mdev_description)
                return jsonify(MedicalDevice=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteMD(self, mdev_id):
        dao = Medical_DevicesDAO()
        if not dao.getMedicalDevicesById(mdev_id):
            return jsonify(Error="Medical Device not found"), 404
        else:
            dao.delete(mdev_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateMD(self, mdev_id, form):
        dao = Medical_DevicesDAO()
        if not dao.getMedicalDevicesById(mdev_id):
            return jsonify(Error="Medical Device not found"), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                mdev_name = form['mdev_name']
                mdev_description = form['mdev_description']
                if mdev_name and mdev_description:
                    dao.update(mdev_id, mdev_name, mdev_description)
                    result = self.build_md_attr(mdev_id, mdev_name, mdev_description)
                    return jsonify(MedicalDevice=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
