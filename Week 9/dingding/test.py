# __Author__: Han
# __Date__: 2019/5/29

import requests
import json

appkey = "dingujadqlmq5q1qioa5"
appsecret = "58rA8onCXPvkvyAdrjTWmazNT5iRsEclJUlVQo9Py1oyGuySirqDGfrU24OFhXLe"


def getToken():
    url = 'https://oapi.dingtalk.com/gettoken?appkey='+appkey+'&appsecret='+appsecret
    response = requests.get(url=url)
    result = response.json()
    errmsg = result['errmsg']
    print('获取密钥是否成功：',errmsg)
    try:
        access_token = result['access_token']
    except Exception as e:
        print(e)
        access_token = ''
    return access_token
access_token = getToken()

#------在钉钉考勤应用中，设置考勤组规则后，会生成每天的排班信息，包括工作日、周末、节假日等。如果企业想查询某天的排班情况，可使用此接口查询某天的考勤排班全量信息。注：固定班制只能查到未来15天的排班信息。
url = 'https://oapi.dingtalk.com/topapi/attendance/listschedule?access_token='+access_token
# url = 'https: // oapi.dingtalk.com / topapi / processinstance / create?access_token = ' + getToken
payload = {
    'workDate':'2019-03-09 11:11:11'
}
_data = json.dumps(payload)
response = requests.post(url=url, data=_data)
print(response.json())

#------在钉钉考勤应用中，考勤组是一类具有相同的班次、考勤位置等考勤规则的人或部门的组合，企业可根据实际业务设置多个考勤组。如果企业想获取企业的考勤组与企业业务系统对接，可使用此接口查询所有的考勤组详情信息。
url = 'https://oapi.dingtalk.com/topapi/attendance/getsimplegroups?access_token='+access_token
response = requests.post(url=url)
print(response.json())

#------该接口用于返回企业内员工的实际打卡记录。比如，企业给一个员工设定的排班是上午9点和下午6点各打一次卡，但是员工在这期间打了多次，该接口会把所有的打卡记录都返回。如果只要获取打卡结果数据，不需要详情数据，可使用获取打卡结果接口。
url = 'https://oapi.dingtalk.com/attendance/listRecord?access_token='+access_token
payload = {
    'userIds':['用户ID'],
    'checkDateFrom':'2019-05-14 00:00:00',
    'checkDateTo':'2019-05-14 18:00:00',
    'isI18n':'false'

}
_data = json.dumps(payload)
response = requests.post(url=url, data=_data)
print(response.json())

#------该接口用于返回企业内员工的实际打卡结果。比如，企业给一个员工设定的排班是上午9点和下午6点各打一次卡，即使员工在这期间打了多次，该接口也只会返回两条记录，包括上午的打卡结果和下午的打卡结果。如果要获取打卡详细数据，比如打卡位置，可使用获取打卡详情接口。
url = 'https://oapi.dingtalk.com/attendance/list?access_token='+access_token
payload = {
    'workDateFrom':'2019-05-14 00:00:00',
    'workDateTo':'2019-05-14 18:00:00',
    'userIdList':["userIdList"],
    'offset':0,
    'limit':5,
    'isI18n':'false'

}
_data = json.dumps(payload)
response = requests.post(url=url, data=_data)
print(response.json())


#------该接口用于返回企业内员工的实际打卡结果。比如，企业给一个员工设定的排班是上午9点和下午6点各打一次卡，即使员工在这期间打了多次，该接口也只会返回两条记录，包括上午的打卡结果和下午的打卡结果。如果要获取打卡详细数据，比如打卡位置，可使用获取打卡详情接口。
url = 'https://oapi.dingtalk.com/topapi/attendance/getleaveapproveduration?access_token='+access_token
payload = {
    'userid':"userid",
    'from_date':"2018-01-01 09:00:00",
    'to_date':"2019-01-01 18:00:00",

}
_data = json.dumps(payload)
response = requests.post(url=url, data=_data)
print(response.json())


#------该接口用于查询指定企业下的指定用户在指定时间段内的请假状态。
url = 'https://oapi.dingtalk.com/topapi/attendance/getleavestatus?access_token='+access_token
payload = {
    'userid_list':"userid_list",
    'start_time':"1546304400000",
    'end_time':"1557795600000",
    'offset':0,
    'size':20,

}
_data = json.dumps(payload)
response = requests.post(url=url, data=_data)
print(response.json())


#------在钉钉考勤应用中，考勤组是一类具有相同的班次、考勤位置等考勤规则的人或部门的组合，一个企业中的一个人只能属于一个考勤组。如果您的企业使用了钉钉考勤并希望获取员工的考勤组信息，可选择使用此接口。
url = 'https://oapi.dingtalk.com/topapi/attendance/getusergroup?access_token='+access_token
payload = {
    'userid':"userid",
}
_data = json.dumps(payload)
response = requests.post(url=url, data=_data)
print(response.json())



















