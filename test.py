import jenkins
import time
import json

server = jenkins.Jenkins('http://localhost:8080', username='test', password='test')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
# jobs = server.get_jobs()
# print(jobs)
# print(server.get_all_jobs())
for num in range(0,len(server.get_all_jobs())):
      job_name = server.get_all_jobs()[num]['fullname']
      print(json.dumps(server.get_job_info(job_name)))
      try:
        lastCompletedBuild_num = server.get_job_info(job_name)['lastCompletedBuild']['number']
      except:
        continue
    #获取最后一次完成构建的时间戳，单位由毫秒转换为秒
      info = server.get_build_info(job_name,lastCompletedBuild_num)
      print(json.dumps(info))
      lastCompletedBuild_timestamp = server.get_build_info(job_name,lastCompletedBuild_num)['timestamp'] / 1000
      #将时间先由秒转化为元组在转化为字符串并取到天数
      lastCompletedBuild_date = time.strftime("%Y%m%d",time.localtime(lastCompletedBuild_timestamp))
      now=time.localtime( time.time() )
      print(lastCompletedBuild_date)
      print(now)
      print(time.time()-lastCompletedBuild_timestamp)
    #   server.disable_job(job_name)
    #   server.delete_job(job_name)

# from jenkinsapi.jenkins import Jenkins

# def get_server_instance():
#     jenkins_url = 'http://localhost:8080'
#     server = Jenkins(jenkins_url, username='test', password='test')
#     return server

# def get_job_details():
#     # Refer Example #1 for definition of function 'get_server_instance'
#     server = get_server_instance()
#     for job_name, job_instance in server.get_jobs():
#         print('Job Name:%s' % (job_instance.name))
#         print('Job Description:%s' % (job_instance.get_description()))
#         print('Is Job running:%s' % (job_instance.is_running()))
#         print('Is Job enabled:%s' % (job_instance.is_enabled()))


# if __name__ == '__main__':
#     print(get_server_instance().version)