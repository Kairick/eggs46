from sqlalchemy import inspect
from collections import Iterable
from datetime import datetime, date
import time


def map_sql_objects_fields(obj_array, max_depth=None):
    """ маппинг результата запроса к базе в массив словарей
    :param obj_array: выборка из базы
    :return:  массив словарей (для фронта json)
    """

    if obj_array is None:
        return None

    result_members = []

    try:
        test = inspect(obj_array[0]).mapper.column_attrs
        is_mapped = True
    except Exception:
        is_mapped = False

    try:
        if is_mapped:
            for item in obj_array:
                # https://stackoverflow.com/a/37350445 - пока наиболее адекватное решение

                res = {c.key: getattr(item, c.key)
                       for c in inspect(item).mapper.column_attrs}

                if max_depth is None:
                    current_depth = None
                else:
                    current_depth = max_depth - 1
                if current_depth is None or current_depth > 0:
                    rellations = [c for c in inspect(item).mapper.relationships]

                    for r in rellations:
                        arr = getattr(item, r.key)
                        if isinstance(arr, Iterable):
                            res[r.key] = map_sql_objects_fields(arr, current_depth)
                        else:
                            res[r.key] = single_object_map(arr, current_depth)

                result_members.append(res)
        else:
            for item in obj_array:
                res = {_key: getattr(item, _key) for _key in item.keys()}
                result_members.append(res)

    except Exception as ex:
        # print("Ошибка подготовки сущностей базы для json response" + str(ex))
        result_members = None

    return result_members


def single_object_map(obj: object, max_depth = None):
    """ маппинг объекта базы в словарь
    :param obj: единичный объект выборка из базы
    :return:  словарей (для фронта json)
    """

    if obj is None:
        return None

    res = {c.key: getattr(obj, c.key)
           for c in inspect(obj).mapper.column_attrs}

    if max_depth is None:
        current_depth = None
    else:
        current_depth = max_depth - 1
    if current_depth is None or current_depth > 0:

        rellations = [c for c in inspect(obj).mapper.relationships]

        for r in rellations:
            arr = getattr(obj, r.key)
            if isinstance(arr, Iterable):
                res[r.key] = map_sql_objects_fields(arr, current_depth)
            else:
                res[r.key] = single_object_map(arr, current_depth)

    return res


def convert_date(data):
    """
    Convert date from datetime to epoch
    :param data:
    :return:
    """
    for item in data:
        if not item:
            return []
        for key, value in item.items():
            if isinstance(value, datetime):
                item[key] = float(value.timestamp())
            elif isinstance(value, date):
                item[key] = float(time.mktime(value.timetuple()))

    return data
