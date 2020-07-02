from flask import Blueprint, request, jsonify
from application import db
from common.libs.utils import return_data, cls_to_dict

index_page = Blueprint("index", __name__)


@index_page.route("/logout", methods=["POST"])
def logout():
    params = request.json
    return jsonify(return_data(1, "success"))


@index_page.route("/getBeSectionListPaging", methods=["POST"])
def getBeSectionListPaging():
    params = request.json
    # type = params.get("type")
    type = 1
    if type == 1:
        res_dat = {
            "code": 0,
            "msg": "success",
            "data": {
                list: [
                    {
                        "agentOrgCode": "12330100745843838P",
                        "bidOpenAddress": "",
                        "bidOpenDate": "2020-06-18 00:00:00",
                        "bidOpenTime": "2020-06-18 22:35:00",
                        "ptSectionId": "170590b4-830f-433d-a3f8-6c2538341dbf",
                        "ptprBscode": "H202006121098001001",
                        "sectionCode": "H202006121098001001",
                        "sectionName": "这是一条测试数据-鱼港综合法测试标段",
                        "sectionStage": "6",
                        "seqId": "7434950B-DC3C-4C11-8CF5-3184D49F9D31"
                    },
                    {
                        "agentOrgCode": "12330100745843838P",
                        "bidOpenAddress": "",
                        "bidOpenDate": "2020-06-18 00:00:00",
                        "bidOpenTime": "2020-06-18 22:35:00",
                        "ptSectionId": "170590b4-830f-433d-a3f8-6c2538341dbf",
                        "ptprBscode": "H202006121098001001",
                        "sectionCode": "H202006121098001001",
                        "sectionName": "这是一条测试数据-鱼港综合法测试标段",
                        "sectionStage": "6",
                        "seqId": "7434950B-DC3C-4C11-8CF5-3184D49F9D31"
                    },
                    {
                        "agentOrgCode": "12330100745843838P",
                        "bidOpenAddress": "",
                        "bidOpenDate": "2020-06-18 00:00:00",
                        "bidOpenTime": "2020-06-18 22:35:00",
                        "ptSectionId": "170590b4-830f-433d-a3f8-6c2538341dbf",
                        "ptprBscode": "H202006121098001001",
                        "sectionCode": "H202006121098001001",
                        "sectionName": "这是一条测试数据-鱼港综合法测试标段",
                        "sectionStage": "6",
                        "seqId": "7434950B-DC3C-4C11-8CF5-3184D49F9D31"
                    },
                ],
                "count": 37,
                "total": 37
            }
        }
    return jsonify(res_dat)




@index_page.route("/test")
def test():
    return "hello world"
