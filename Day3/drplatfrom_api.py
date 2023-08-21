'''
Author: hongbinyang
LastEditTime: 2023-03-23 17:24:29
FilePath: /practise/Days3/drplatfrom_api.py
'''
import requests
import json
import pandas as pd
from pandas import DataFrame
import pandasql as ps

class DrPlatformAPI(object):
    def __init__(self):
        pass

    def authority(self):
        pass

    def load_trips(self):
        url = "https://drplatform.deeproute.cn/dr-pipeline/trip/query"
        trips_param = json.dumps({
            "condition": {
                "end_time": {"le": 1678291199000},
                "start_time": {"ge": 1678204800000},
                "tester": {
                    "eq": ["yili03","xiaolonghuang","jiangweitan"
                        ]
                }
            },
            "page": 0,
            "size": 1000,
            "orderBys": []
        })
        
        headers = {
            'Authorization': '{{Authorization}}',
            'Content-Type': 'application/json'
            }
        response = requests.request("POST", url, headers=headers, data=trips_param)
        #Data Manipulation
        response_data = response.json()
        new_response = response_data["body"]

        data_frame=pd.DataFrame(new_response).fillna('null')
        # print(data_frame)
        timestamp_cols = ['startTime', 'endTime']
        convert_func = lambda x: pd.to_datetime(x, unit='ms', errors='coerce'
                                                ) + pd.Timedelta('08:00:00')
        for col in timestamp_cols:
            data_frame[col] = data_frame[col].apply(convert_func)

        data_frame["duration"] = data_frame.endTime - data_frame.startTime
        data_frame["hour"] = data_frame.duration.map(lambda x:x.seconds/3600)

        data_frame = data_frame[["tester","vehicleId","location","taskType","startTime","hour"]]
        # return data_frame
        sql_platform = """
        SELECT tester AS 测试工程师 , vehicleId AS Car_ID , location AS 城市 , DATE(startTime) AS 日期 , SUM(hour) AS 测试时间（h）
        FROM data_frame
        GROUP BY tester
        """
        sql_platform_result = ps.sqldf(sql_platform, locals())
        return sql_platform_result

if __name__=='__main__':
    dpa = DrPlatformAPI()
    r = dpa.load_trips()
    print(r)