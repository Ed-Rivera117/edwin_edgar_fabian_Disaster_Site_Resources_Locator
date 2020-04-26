from flask import Flask, jsonify, request
from handler.usr import UsrHandler
from handler.client import ClientHandler
from handler.supplier import SupplierHandler
from handler.sys_admin import SysAdminHandler
from handler.request import RequestHandler
from handler.reservation import ReservationHandler
from handler.resources import ResourcesHandler
from handler.credit_card import CreditCardHandler
from handler.baby_food import BabyFoodHandler
from handler.batteries import BatteriesHandler
from handler.canned_food import CannedFoodHandler
from handler.clothing import ClothingHandler
from handler.dry_food import DryFoodHandler
from handler.fuel import FuelHandler
from handler.heavy_equip import HeavyEquipHandler
from handler.ice import IceHandler
from handler.medical_devices import MedicalDeviceHandler
from handler.medication import MedicationHandler
from handler.power_generator import PowerGeneratorHandler
from handler.tools import ToolHandler
from handler.water import WaterHandler

from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello this is Edwin, Edgar and Fabian`s DB App!'


@app.route('/DBApp/users', methods=['GET', 'POST'])
def getAllUsr():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UsrHandler().insertUser(request.json)
    else:
        if not request.args:
            return UsrHandler().getAllUser()
        else:
            return UsrHandler().searchUser(request.args)


@app.route('/DBApp/users/<int:usr_id>', methods=['GET', 'PUT', 'DELETE'])
def getUsrById(usr_id):
    if request.method == 'GET':
        return UsrHandler().getUserById(usr_id)
    elif request.method == 'PUT':
        return UsrHandler().updateUser(usr_id, request.form)
    elif request.method == 'DELETE':
        return UsrHandler().deleteUser(usr_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Clients
@app.route('/DBApp/clients', methods=['GET', 'POST'])
def getAllClients():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ClientHandler().insertClient(request.json)
    else:
        if not request.args:
            return ClientHandler().getAllClients()
        else:
            return ClientHandler().searchClients(request.args)


@app.route('/DBApp/clients/<int:c_id>', methods=['GET', 'PUT', 'DELETE'])
def getClientById(c_id):
    if request.method == 'GET':
        return ClientHandler().getClientById(c_id)
    elif request.method == 'PUT':
        return ClientHandler().updateClient(c_id, request.form)
    elif request.method == 'DELETE':
        return ClientHandler().deleteClient(c_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Supplier
@app.route('/DBApp/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return SupplierHandler().insertSupplier(request.json)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)


@app.route('/DBApp/suppliers/<int:s_id>', methods=['GET', 'PUT', 'DELETE'])
def getSuppliersById(s_id):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(s_id)
    elif request.method == 'PUT':
        return SupplierHandler().updateSupplier(s_id, request.form)
    elif request.method == 'DELETE':
        return SupplierHandler().deleteSupplier(s_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# SysAdmin
@app.route('/DBApp/SysAdmin', methods=['GET', 'POST'])
def getAllSysAdmin():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return SysAdminHandler().insertSysAdmin(request.json)
    else:
        if not request.args:
            return SysAdminHandler().getAllSysAdmin()
        else:
            return SysAdminHandler().searchSysAdmin(request.args)


@app.route('/DBApp/SysAdmin/<int:sa_id>', methods=['GET', 'PUT', 'DELETE'])
def getSysAdminById(sa_id):
    if request.method == 'GET':
        return SysAdminHandler().getSysAdminById(sa_id)
    elif request.method == 'PUT':
        return SysAdminHandler().updateSysAdmin(sa_id, request.form)
    elif request.method == 'DELETE':
        return SysAdminHandler().deleteSysAdmin(sa_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Request
@app.route('/DBApp/request', methods=['GET', 'POST'])
def getAllRequest():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return RequestHandler().insertRequest(request.json)
    else:
        if not request.args:
            return RequestHandler().getAllRequests()
        else:
            return RequestHandler().searchRequest(request.args)


@app.route('/DBApp/requests/<int:rq_id>', methods=['GET', 'PUT', 'DELETE'])
def getRequestById(rq_id):
    if request.method == 'GET':
        return RequestHandler().getRequestsById(rq_id)
    elif request.method == 'PUT':
        return RequestHandler().updateRequest(rq_id, request.form)
    elif request.method == 'DELETE':
        return RequestHandler().deleteRequest(rq_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Reservation
@app.route('/DBApp/reservations', methods=['GET', 'POST'])
def getAllReservations():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ReservationHandler().insertReservation(request.json)
    else:
        if not request.args:
            return ReservationHandler().getAllReservations()
        else:
            return ReservationHandler().searchReservation(request.json)


@app.route('/DBApp/reservations/<int:rs_id>', methods=['GET', 'PUT', 'DELETE'])
def getReservationsById(rs_id):
    if request.method == 'GET':
        return ReservationHandler().getReservationsById(rs_id)
    elif request.method == 'PUT':
        return ReservationHandler().updateReservation(rs_id, request.form)
    elif request.method == 'DELETE':
        return ReservationHandler().deleteReservation(rs_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Resources
@app.route('/DBApp/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ResourcesHandler().insertResource(request.json)
    else:
        if not request.args:
            return ResourcesHandler().getAllResource()
        else:
            return ResourcesHandler().searchResource(request.args)


@app.route('/DBApp/resources/<int:resr_id>', methods=['GET', 'PUT', 'DELETE'])
def getResourcesById(resr_id):
    if request.method == 'GET':
        return ResourcesHandler().getResourceById(resr_id)
    elif request.method == 'PUT':
        return ResourcesHandler().updateResource(resr_id, request.form)
    elif request.method == 'DELETE':
        return ResourcesHandler().deleteResource(resr_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DBApp/requested', methods=['GET'])
def getResourcesRequested():
    return ResourcesHandler().getResourcesRequested()

@app.route('/DBApp/available', methods=['GET'])
def getResourcesAvailable():
    return ResourcesHandler().getResourcesAvailable()

# CreditCard
@app.route('/DBApp/creditcards', methods=['GET', 'POST'])
def getAllCreditCards():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CreditCardHandler().insertCC(request.json)
    else:
        if not request.args:
            return CreditCardHandler().getAllCreditCard()
        else:
            return CreditCardHandler().searchCC(request.args)


@app.route('/DBApp/creditcards/<int:cc_id>', methods=['GET', 'PUT', 'DELETE'])
def getCreditCardById(cc_id):
    if request.method == 'GET':
        return CreditCardHandler().getCreditCardById(cc_id)
    elif request.method == 'PUT':
        return CreditCardHandler().updateCC(cc_id, request.form)
    elif request.method == 'DELETE':
        return CreditCardHandler().deleteCC(cc_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# BabyFood
@app.route('/DBApp/babyfood', methods=['GET', 'POST'])
def getAllBabyFood():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return BabyFoodHandler().insertBabyFood(request.json)
    else:
        if not request.args:
            return BabyFoodHandler().getAllBabyFood()
        else:
            return BabyFoodHandler().searchBabyFood(request.args)


@app.route('/DBApp/babyfood/<int:bb_id>', methods=['GET', 'PUT', 'DELETE'])
def getBabyFoodById(bb_id):
    if request.method == 'GET':
        return BabyFoodHandler().getBabyFoodById(bb_id)
    elif request.method == 'PUT':
        return BabyFoodHandler().updateBabyFood(bb_id, request.form)
    elif request.method == 'DELETE':
        return BabyFoodHandler().deleteBabyFood(bb_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Batteries
@app.route('/DBApp/batteries', methods=['GET', 'POST'])
def getAllBatteries():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return BatteriesHandler().insertBatteries(request.json)
    else:
        if not request.args:
            return BatteriesHandler().getAllBatteries()
        else:
            return BatteriesHandler().searchBatteries(request.args)


@app.route('/DBApp/batteries/<int:batt_id>', methods=['GET', 'PUT', 'DELETE'])
def getBatteriesById(batt_id):
    if request.method == 'GET':
        return BatteriesHandler().getBatteriesById(batt_id)
    elif request.method == 'PUT':
        return BatteriesHandler().updateBatteries(batt_id, request.form)
    elif request.method == 'DELETE':
        return BatteriesHandler().deleteBatteries(batt_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Canned Food
@app.route('/DBApp/cannedfood', methods=['GET', 'POST'])
def getAllCannedFoods():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CannedFoodHandler().insertCF(request.json)
    else:
        if not request.args:
            return CannedFoodHandler().getAllCF()
        else:
            return CannedFoodHandler().searchCF(request.args)


@app.route('/DBApp/cannedfoods/<int:cf_id>', methods=['GET', 'PUT', 'DELETE'])
def getCannedFoodsById(cf_id):
    if request.method == 'GET':
        return CannedFoodHandler().getCFById(cf_id)
    elif request.method == 'PUT':
        return CannedFoodHandler().updateCF(cf_id, request.form)
    elif request.method == 'DELETE':
        return CannedFoodHandler().deleteCF(cf_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Clothing
@app.route('/DBApp/clothing', methods=['GET', 'POST'])
def getAllClothing():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ClothingHandler().insertClothing(request.json)
    else:
        if not request.args:
            return ClothingHandler().getAllClothing()
        else:
            return ClothingHandler().searchClothing(request.args)


@app.route('/DBApp/clothing/<int:cl_id>', methods=['GET', 'PUT', 'DELETE'])
def getClothingById(cl_id):
    if request.method == 'GET':
        return ClothingHandler().getClothingById(cl_id)
    elif request.method == 'PUT':
        return ClothingHandler().updateClothing(cl_id, request.form)
    elif request.method == 'DELETE':
        return ClothingHandler().deleteClothing(cl_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# DryFood
@app.route('/DBApp/dryfood', methods=['GET', 'POST'])
def getAllDryFoods():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return DryFoodHandler().insertDF(request.json)
    else:
        if not request.args:
            return DryFoodHandler().getAllDF()
        else:
            return DryFoodHandler().searchDF(request.args)


@app.route('/DBApp/dryfood/<int:df_id>', methods=['GET', 'PUT', 'DELETE'])
def getDryFoodsById(df_id):
    if request.method == 'GET':
        return DryFoodHandler().getDFById(df_id)

    elif request.method == 'PUT':
        return DryFoodHandler().updateDF(df_id, request.form)
    elif request.method == 'DELETE':
        return DryFoodHandler().deleteDF(df_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Fuel
@app.route('/DBApp/fuel', methods=['GET', 'POST'])
def getAllFuel():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FuelHandler().insertFuel(request.json)
    else:
        if not request.args:
            return FuelHandler().getAllFuel()
        else:
            return FuelHandler().searchFuel(request.args)


@app.route('/DBApp/fuel/<int:fuel_id>', methods=['GET', 'PUT', 'DELETE'])
def getFuelById(fuel_id):
    if request.method == 'GET':
        return FuelHandler().getFuelById(fuel_id)
    elif request.method == 'PUT':
        return FuelHandler().updateFuel(fuel_id, request.form)
    elif request.method == 'DELETE':
        return FuelHandler().deleteFuel(fuel_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# HeavyEquipment
@app.route('/DBApp/heavyequipment', methods=['GET', 'POST'])
def getAllHeavyEquipments():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return HeavyEquipHandler().insertHE(request.json)
    else:
        if not request.args:
            return HeavyEquipHandler().getAllHE()
        else:
            return HeavyEquipHandler().searchHE(request.args)


@app.route('/DBApp/heavyequipment/<int:heq_id>', methods=['GET', 'PUT', 'DELETE'])
def geHeavyEquipmentById(heq_id):
    if request.method == 'GET':
        return HeavyEquipHandler().getHEById(heq_id)
    elif request.method == 'PUT':
        return HeavyEquipHandler().updateHE(heq_id, request.form)
    elif request.method == 'DELETE':
        return HeavyEquipHandler().deleteHE(heq_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Ice
@app.route('/DBApp/ice', methods=['GET', 'POST'])
def getAllIce():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return IceHandler().insertIce(request.json)
    else:
        if not request.args:
            return IceHandler().getAllIce()
        else:
            return IceHandler().searchIce(request.args)


@app.route('/DBApp/ice/<int:ice_id>', methods=['GET', 'PUT', 'DELETE'])
def getIceById(ice_id):
    if request.method == 'GET':
        return IceHandler().getIceById(ice_id)
    elif request.method == 'PUT':
        return IceHandler().updateIce(ice_id, request.form)
    elif request.method == 'DELETE':
        return IceHandler().deleteIce(ice_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Medical Devices
@app.route('/DBApp/medicaldevices', methods=['GET', 'POST'])
def getAllMedicalDevices():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MedicalDeviceHandler().insertMD(request.json)
    else:
        if not request.args:
            return MedicalDeviceHandler().getAllMD()
        else:
            return MedicalDeviceHandler().searchMD(request.args)


@app.route('/DBApp/medicaldevices/<int:mdev_id>', methods=['GET', 'PUT', 'DELETE'])
def getMedicalDevicesById(mdev_id):
    if request.method == 'GET':
        return MedicalDeviceHandler().getMDById(mdev_id)
    elif request.method == 'PUT':
        return MedicalDeviceHandler().updateMD(mdev_id, request.form)
    elif request.method == 'DELETE':
        return MedicalDeviceHandler().deleteMD(mdev_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Medication
@app.route('/DBApp/medications', methods=['GET', 'POST'])
def getAllMedication():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MedicationHandler().insertMD(request.json)
    else:
        if not request.args:
            return MedicationHandler().getAllMed()
        else:
            return MedicationHandler().searchMD(request.args)


@app.route('/DBApp/medications/<int:med_id>', methods=['GET', 'PUT', 'DELETE'])
def getMedicationById(med_id):
    if request.method == 'GET':
        return MedicationHandler().getMedById(med_id)
    elif request.method == 'PUT':
        return MedicationHandler().updateMD(med_id, request.form)
    elif request.method == 'DELETE':
        return MedicationHandler().deleteMD(med_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Power Generator
@app.route('/DBApp/powergenerator', methods=['GET', 'POST'])
def getAllPowerGenerators():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PowerGeneratorHandler().insertPG(request.json)
    else:
        if not request.args:
            return PowerGeneratorHandler().getAllPG()
        else:
            return PowerGeneratorHandler().searchPG(request.args)


@app.route('/DBApp/powergenerator/<int:pg_id>', methods=['GET', 'PUT', 'DELETE'])
def getPowerGeneratorById(pg_id):
    if request.method == 'GET':
        return PowerGeneratorHandler().getPGById(pg_id)
    elif request.method == 'PUT':
        return PowerGeneratorHandler().updatePG(pg_id, request.form)
    elif request.method == 'DELETE':
        return PowerGeneratorHandler().deletePG(pg_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Tools
@app.route('/DBApp/tools', methods=['GET', 'POST'])
def getAllTools():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ToolHandler().insertTool(request.json)
    else:
        if not request.args:
            return ToolHandler().getAllTools()
        else:
            return ToolHandler().searchTool(request.args)


@app.route('/DBApp/tools/<int:tool_id>', methods=['GET', 'PUT', 'DELETE'])
def getToolsById(tool_id):
    if request.method == 'GET':
        return ToolHandler().getToolsById(tool_id)
    elif request.method == 'PUT':
        return ToolHandler().updateTool(tool_id, request.form)
    elif request.method == 'DELETE':
        return ToolHandler().deleteTool(tool_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# Water
@app.route('/DBApp/water', methods=['GET', 'POST'])
def getAllWater():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return WaterHandler().insertWater(request.json)
    else:
        if not request.args:
            return WaterHandler().getAllWater()
        else:
            return WaterHandler().searchWater(request.args)


@app.route('/DBApp/water/<int:h2O_id>', methods=['GET', 'PUT', 'DELETE'])
def getWaterById(h2O_id):
    if request.method == 'GET':
        return WaterHandler().getWaterById(h2O_id)
    elif request.method == 'PUT':
        return WaterHandler().updateWater(h2O_id, request.form)
    elif request.method == 'DELETE':
        return WaterHandler().deleteWater(h2O_id)
    else:
        return jsonify(Error="Method not allowed."), 405


if __name__ == '_main__':
    app.run()
