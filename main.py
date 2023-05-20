import time
import schedule
# my functions
import messages
import file_manipulations
import schedule_job


def main():
    messages.start_msg()
    file_manipulations.create_file_to_price()
    schedule_job.schedule_job_interval(1, 'seconds')
    #schedule_job.schedule_job_interval(0, 'days', '10:30')
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
