需求
----
该任务主要抓取国家专利网站的的专利数据， 框架采用Scrapy, 数据库使用Mongo

抓取来源
----
1：发明专利： http://epub.sipo.gov.cn/index.action

2：发明授权： http://epub.sipo.gov.cn/index.action

3：实用新型： http://epub.sipo.gov.cn/index.action

4：外观设计： http://epub.sipo.gov.cn/index.action


数据存储：
--------
192.168.100.20的py_crawl库 patent 表

说明：
---
可以基于专利各种条件的选择(http://epub.sipo.gov.cn/gjcx.jsp)需要不同的值， 可根据此链接选择

部署情况：
-------
l: 部署位置：192.168.205.207：/opt/scrapyer

2：使用screen -ls(patent那个即是)

3：定时调度程序位置：patent/aps.py(python patent/aps.py)

4：抓取程序在：patent/patent目录下， 调度程序在patent/aps.py

备注：具体问题以代码为准。