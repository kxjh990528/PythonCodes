# 下面是一个email邮件格式的字符串，将其中的任务ID,任务名称,执行时间,执行耗时,执行状态等值由用户引导输入嵌入到该模板中
"""<html>
<head>
   <meta charset="utf-8">
</head>
<body>
Hello，定时任务出错了：
<p style="font-size:16px;">任务执行详情：</p>
<p style="display:block; padding:10px; background:#efefef;border:1px solid #e4e4e4">
    任务 ID：1001<br/>
    任务名称：定时检测订单<br/>
    执行时间：2012-12-12<br/>
    执行耗时：15秒<br/>
    执行状态：开启
</p>
<br/>
<p>-----------------------------------------------------------------<br/>
    本邮件由CronJob定时系统自动发出，请勿回复<br/>
    如果要取消邮件通知，请登录到系统进行设置<br/>
</p>
</body>
</html>"""

# 引导用户输入
mission_id = input("请输入任务ID：")
mission_name = input("请输入任务名称：")
run_date = input("请输入执行时间：")
run_time = input("请输入执行耗时：")
run_state = input("请输入执行状态：")

# 将输入内容镶嵌进模板内
ret = f"""
任务 ID：{mission_id}
任务名称：{mission_name}
执行时间：{run_date}
执行耗时：{run_time}
执行状态：{run_state}
"""

# 打印模板内容
print(ret)
