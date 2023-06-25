import time
import schedule

import messages
import schedule_job


def main():
    messages.start_msg()
    schedule_job.schedule_job_interval(1, 'seconds')
    #schedule_job.schedule_job_interval(0, 'days', '10:30')
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
