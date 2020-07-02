from flask import Blueprint, request, jsonify
from application import db
from common.libs.utils import return_data, cls_to_dict

bid_page = Blueprint("bid", __name__)


@bid_page.route("/beSectionInfo/getTodayOrHistoryList", methods=["POST"])
def getTodayOrHistory():
    params = request.json
    type = params.get("type")
    res_data = [
        {
            "indexNum": 1,
            "sectionId": "17059014-830f-433d-a3f8-6c2538341dbf",
            'sectionName': "这是一条测试数据1",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山1",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称1",
            "sectionStage": 1,
            "bidOpenAddress": "一号开标室1",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室1"

        },
        {
            "indexNum": 2,
            "sectionId": "170590b4-887f-433d-a3f8-6c2538341dbf",
            'sectionName': "这是一条测试数据2",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山2",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称2",
            "sectionStage": 2,
            "bidOpenAddress": "一号开标室2",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室2"

        },
        {
            "indexNum": 3,
            "sectionId": "170590b4-8300f-433d-a3f8-6c2538341dbf",
            'sectionName': "这是一条测试数据3",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山3",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称3",
            "sectionStage": 3,
            "bidOpenAddress": "一号开标室3",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室3"

        },
        {
            "indexNum": 4,
            "sectionId": "170590b4-8340f-433d-a3f8-6c2538341dbf",
            'sectionName': "这是一条测试数据-鱼港综合法测试标段",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山5",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称5",
            "sectionStage": 1,
            "bidOpenAddress": "一号开标室5",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室5"

        },
        {
            "indexNum": 5,
            "sectionId": "170590b4-830f-433d-a3f58-6c2538341dbf",
            'sectionName': "这是一条测试数据-这是一条测试数据-鱼港综合法测试标段这是一条测试数据-鱼港综合法测试标段这是一条测试数据-鱼港综合法测试标段这是一条测试数据-鱼港综合法测试标段这是一条测试数据-鱼港综合法测试标段这是一条测试数据-鱼港综合法测试标段这是一条测试数据-鱼港综合法测试标段",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山6",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称6",
            "sectionStage": 1,
            "bidOpenAddress": "一号开标室6",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室6"

        },
        {
            "indexNum": 6,
            "sectionId": "170590b4-830f-433d-a3f8-6c25387341dbf",
            'sectionName': "这是一条测试数据-鱼港综合法测试标段",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山7",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称7",
            "sectionStage": 1,
            "bidOpenAddress": "一号开标室7",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室7"

        },
        {
            "indexNum": 7,
            "sectionId": "170590b4-831f-433d-a3f8-6c2538341dbf",
            'sectionName': "这是一条测试数据-鱼港综合法测试标段",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山8",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称8",
            "sectionStage": 1,
            "bidOpenAddress": "一号开标室8",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室8"

        },
        {
            "indexNum": 8,
            "sectionId": "170590b4-830f-433d-a3f8-6c25641dbf",
            'sectionName': "这是一条测试数据-鱼港综合法测试标段",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山9",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称9",
            "sectionStage": 1,
            "bidOpenAddress": "一号开标室9",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室9"

        },
        {
            "indexNum": 9,
            "sectionId": "170590b4-830f-433d-a3f8-4538341dbf",
            'sectionName': "这是一条测试数据-鱼港综合法测试标段",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山10",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称10",
            "sectionStage": 1,
            "bidOpenAddress": "一号开标室10",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室10"

        },
        {
            "indexNum": 10,
            "sectionId": "170590b4-830f-433d-a3f8-68341dbf",
            'sectionName': "这是一条测试数据-鱼港综合法测试标段",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山11",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称11",
            "sectionStage": 1,
            "bidOpenAddress": "一号开标室11",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室11"

        },
        {
            "indexNum": 11,
            "sectionId": "170590b4-830f-433d-a3f8-68341dbf",
            'sectionName': "wangjiashan-鱼港综合法测试标段",
            "sectionCode": "H202006121098001001",
            "bidOpenTime": "2020-06-18 22:35:00",
            "tenderType": 1,
            "tenderee": "招标人-王家山11",
            "agentId": "170590b4",
            "agentOrgCode": "7839121083492",
            "agentName": "招标代理机构名称11",
            "sectionStage": 1,
            "bidOpenAddress": "一号开标室11",
            "videoShowUrl": "http://www.youku.com",
            "studioOpenRoom": "一号直播室11"

        },
    ]
    print(params)
    return jsonify({"code": 0, "msg": "success", "total": 11, "data": res_data})


@bid_page.route("/getBeSectionByCode", methods=["POST"])
def getBeSectionByCode():
    params = request.json
    res_data = {
        "agentOrgCode": "12330100745843838P",
        "bidOpenAddress": "",
        "bidOpenDate": "2020-06-18 00:00:00",
        "bidOpenTime": "2020-06-18 22:35:00",
        "ptSectionId": "170590b4-830f-433d-a3f8-6c2538341dbf",
        "ptprBscode": "H202006121098001001",
        "sectionCode": "H202006121098001001",
        "sectionName": "这是一条测试数据-鱼港综合法测试标段",
        "sectionStage": "6",
        "seqId": "7434950B-DC3C-4C11-8CF5-3184D49F9D31",
        "agentName": "我是测试的招标代理试的招标试的招标试的招标",
        "telephone": "18172837869"

    }

    return jsonify({"code": 0, "msg": "success", "total": 11, "data": res_data})


@bid_page.route("/getOutTime", methods=["POST"])
def getOutTime():
    return jsonify({"code": 0, "msg": "success", "data": {"endTime": 1593427020000}})

@bid_page.route("/beSectionDecrypt/getDecryptCountAndEndTime",methods=["POST"])
def getDecryptCountAndEndTime():


    return jsonify({
        "code": 0,
        "msg": "操作成功",
        "data": {
            "decryptedCount": 20,
            "decryptEndTime": 1593426840000
        }

    })

@bid_page.route("/beSectionDecrypt/getRealCount",methods=["POST"])
def getRealCount():
    return jsonify({
        "code": 0,
        "msg": "操作成功",
        "data": {
            "realCount": 100,
        }

    })
