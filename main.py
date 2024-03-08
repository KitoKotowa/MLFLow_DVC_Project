from src.MLProject import logger
from MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f'--- Stage {STAGE_NAME} started ---')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'--- Stage {STAGE_NAME} completed ---')

except Exception as e:
    logger.exception(e)
    raise 

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f"--- Stage {STAGE_NAME} started ---")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"--- Stage {STAGE_NAME} completed ---")

except Exception as e:
    logger.exception(e)
    raise e