import time
import schedule

import schedule_job
from msgs import start_msg


def main():
    start_msg()
    schedule_job.schedule_job_interval(1, 'seconds')
    # schedule_job.schedule_job_interval(0, 'days', '10:30')
    while True:
        schedule.run_pending()
        time.sleep(3)


if __name__ == '__main__':
    main()
