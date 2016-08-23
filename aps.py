import os
import time
from os.path import dirname, abspath

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor


def create_sqlite():
    sqlite_path = dirname(abspath(__file__))
    for sql_path in os.listdir(sqlite_path):
        if sql_path.endswith('.db'):
            os.remove(os.path.join(sqlite_path, sql_path))

create_sqlite()


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.db')
}

# using ThreadPoolExecutor as default other than ProcessPoolExecutor(not work) to executors
executors = {
    'default': ThreadPoolExecutor(4),
    # 'default': ProcessPoolExecutor(4),
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

app = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)


def run_patent():
    rtypes = ['fmgb', 'fmsq', 'syxx', 'wgsj']

    for rtype in rtypes:
        cmd = 'scrapy crawl sipo -a rtype=%s -a start=1 -a end=50' % rtype
        os.system(cmd)
        time.sleep(60)


# app.add_job(run_patent, trigger='cron', horu='9-18', minute='*/15')
# app.start()

run_patent()
