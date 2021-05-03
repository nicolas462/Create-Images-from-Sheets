from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from GenerarCupon import generar

sched = BlockingScheduler()

sched.add_job(generar, 'interval', hours=12)

sched.start()