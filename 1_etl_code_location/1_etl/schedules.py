from dagster import ScheduleDefinition
from .jobs import etl_job
from .config import ops

# Run the ETL job every day at midnight
etl_daily_schedule = ScheduleDefinition(
    job=etl_job,
    cron_schedule="0 0 * * *",
    name="etl_daily_schedule",
    run_config={"ops": ops},
)
