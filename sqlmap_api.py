import requests 
import json
import time

def sqlmapapi(url):
    headers = {
        'Content-Type':'application/json'
    }#指纹头
    data={
        'url':url
    }#扫描地址
    task_new_url = 'http://127.0.0.1:8775/task/new'
    responce = requests.get(task_new_url)#得到json
    taskid = responce.json()['taskid']#json方法，取taskid的值
    #print(responce.content.decode('utf-8'))
    if 'success' in responce.content.decode('utf-8'):
        print('sqlmap_api_task create success')
        task_set_url = 'http://127.0.0.1:8775/option/'+taskid+'/set'
        task_set_responce = requests.post(task_set_url,data=json.dumps(data),headers=headers)
        #print(task_set_responce.content.decode('utf-8'))
        if 'success' in task_set_responce.content.decode('utf-8'):
            print('sqlmap_api_task set success')
            task_start_url = 'http://127.0.0.1:8775/scan/' + taskid +'/start'
            task_start_responce = requests.post(task_start_url,data=json.dumps(data),headers=headers)
            #print(task_start_responce.content.decode('utf-8')) 
            if 'success' in task_start_responce.content.decode('utf-8'):
                print('sqlmap_api_task start success')
                while 1:
                    task_status_url = 'http://127.0.0.1:8775/scan/'+taskid+'/status'
                    task_status_responce = requests.get(task_status_url)
                    #print(task_status_responce.url.decode('utf-8'))
                    if 'running' in task_status_responce.content.decode('utf-8'):
                        print(url+'->'+'sqlmap_api_task scanning')
                        pass
                    else:
                        task_data_url = 'http://127.0.0.1:8775/scan/'+taskid+'/data'
                        task_data_responce = requests.get(task_data_url)
                        print(task_data_responce.content.decode('utf-8'))
                        with open(r'scan_result.txt','a+') as f:
                            f.write(url+'\n')
                            f.write(task_data_responce.content.decode('utf-8')+'\n')
                            f.write("\n========by yuanjiu======\n")
                        break
                    time.sleep(0.01)
if __name__ == '__main__':
    for url in open('url.txt'):
        url = url.replace('\n','')
        sqlmapapi(url)

