from flask import jsonify
from dao.tools import ToolDAO


class ToolHandler:

    def build_tool_dict(self, row):
        result = {}
        result['tool_id'] = row[0]
        result['tool_name'] = row[1]
        return result

    def build_tool_attr(self, tool_id, tool_name):
        result = {}
        result['tool_id'] = tool_id
        result['tool_name'] = tool_name
        return result

    def getAllTools(self):
        dao = ToolDAO()
        tool_list = dao.getAllTools()
        result_list = []
        for row in tool_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)

    def getToolsById(self, tool_id):
        dao = ToolDAO()
        row = dao.getToolById(tool_id)
        if not row:
            return jsonify(Error="Tool not found"), 404
        else:
            tool = self.build_tool_dict(row)
        return jsonify(Tool=tool)

    def searchTool(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string"), 400
        else:
            tool = args.get("tool")
            if tool:
                dao = ToolDAO()
                tool_list = dao.getToolByName(tool)
                result_list = []
                for row in tool_list:
                    result = self.build_tool_dict(row)
                    result_list.append(result)
                return jsonify(Tool=result_list)
            else:
                return jsonify(Error="Malformed search string"), 400

    def insertTool(self, form):
        if form and len(form) == 2:
            tool_name = form['tool_name']
            resr_id = form['resr_id']
            if tool_name:
                dao = ToolDAO()
                tool_id = dao.insert(tool_name, resr_id)
                result = self.build_tool_attr(tool_id, tool_name)
                return jsonify(Tool=result), 201
            else:
                return jsonify(Error="Malformed post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400

    def deleteTool(self, tool_id):
        dao = ToolDAO()
        if not dao.getToolById(tool_id):
            return jsonify(Error="Tool not found"), 404
        else:
            dao.delete(tool_id)
            return jsonify(DeleteStatus="OK"), 200

    def updateTool(self, tool_id, form):
        dao = ToolDAO()
        if not dao.getToolById(tool_id):
            return jsonify(Error="Tool not found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                tool_name = form['tool_name']
                if tool_name:
                    dao.update(tool_id, tool_name)
                    result = self.build_tool_attr(tool_id, tool_name)
                    return jsonify(Tool=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
