import hashlib, datetime


def cls_to_dict(cls_list):
    '''
    将数据库查询出来的实例对象列表进行统一的转换
    :param cls_list: 待转换的class 实例对象列表
    :return: 字典列表
    '''
    dict_list = []
    for item in cls_list:
        dict_list.append(item.to_json())
    return dict_list


def return_data(code, msg, data=None):
    if data is not None:
        return {
            "code": code,
            "msg": msg,
            "data": data
        }
    else:
        return {
            "code": code,
            "msg": msg
        }


def get_md5(data):
    '''
    获取md5,并转成小写
    :param data:
    :return:
    '''
    md5 = hashlib.md5()
    md5.update(data.encode(encoding='utf-8'))
    sign = md5.hexdigest()
    return sign.lower()


def formatDateTime():
    curr_date_time = datetime.datetime.now()
    curr_year = curr_date_time.year
    curr_month = curr_date_time.month
    curr_day = curr_date_time.day
    curr_hour = curr_date_time.hour
    curr_minute = curr_date_time.minute
    curr_second = curr_date_time.second
    format_data = curr_date_time.strftime('%Y-%m-%d %H:%M:%S')
    print(format_data)
    return format_data
