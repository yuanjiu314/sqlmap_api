'''
https://www.freebuf.com/articles/web/204875.html
1.创建新任务记录任务 ID @get("/task/new")
2.设置任务 ID 扫描信息 @post("/option/<taskid>/set ")
3.开始扫描对应 ID 任务 @post("/scan/<taskid>/start")
4.读取扫描状态判断结果 @get("/scan/<taskid>/status")
5.如果结束删除 ID 并获取结果 @get("/task/<taskid>/delete")
6.扫描结果查看@get("/scan/<taskid>/data")
'''
import requests 
import json
#创建任务ID
task_new_url = 'http://127.0.0.1:8775/task/new'
responce = requests.get(task_new_url)#得到json
taskid = responce.json()['taskid']#json方法，取taskid的值

#设置任务ID的配置信息（扫描信息）
headers = {
    'Content-Type':'application/json'
}#指纹头
data={
    'url':'http://127.0.0.1/sqli-labs-master/'
}#扫描地址
task_set_url = 'http://127.0.0.1:8775/option/'+taskid+'/set'
task_set_responce = requests.post(task_set_url,data=json.dumps(data),headers=headers)
print(task_set_responce.content.decode('utf-8'))
#启动对应ID的扫描任务
task_start_url = 'http://127.0.0.1:8775/scan/' + taskid +'/start'
task_start_responce = requests.post(task_start_url,data=json.dumps(data),headers=headers)
print(task_start_responce.content.decode('utf-8'))

#获取对应ID的扫描状态
task_status_url = 'http://127.0.0.1:8775/option/'+taskid+'/status'
task_status_responce = requests.get(task_status_url)
print(task_start_responce.content.decode('utf-8'))



