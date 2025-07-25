from dagster import SensorDefinition, RunRequest
from pathlib import Path
from .jobs import etl_job
from .config import ops

# Example: trigger ETL job if raw_input_data.json changes


def etl_sensor_fn(context):
    raw_data_path = Path("example_input_files_resource/raw_input_data.json")
    if raw_data_path.exists():
        mtime = raw_data_path.stat().st_mtime
        last_mtime = context.instance_storage.get_value("raw_data_mtime")
        if last_mtime != mtime:
            context.instance_storage.set_value("raw_data_mtime", mtime)
            yield RunRequest(
                run_key=str(mtime),
                job_name=etl_job.name,
                run_config={"ops": ops},
            )


etl_sensor = SensorDefinition(
    name="etl_sensor",
    evaluation_fn=etl_sensor_fn,
)
