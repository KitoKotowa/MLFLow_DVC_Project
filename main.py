from src.MLProject import logger
from MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MLProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f'--- Stage {STAGE_NAME} started ---')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'--- Stage {STAGE_NAME} completed ---\n\n')

except Exception as e:
    logger.exception(e)
    raise 

STAGE_NAME = "Data Validation"

try:
    logger.info(f"--- Stage {STAGE_NAME} started ---")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"--- Stage {STAGE_NAME} completed ---\n\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation"

try:
    logger.info(f'--- Stage {STAGE_NAME} started ---')
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f'--- Stage {STAGE_NAME} completed ---\n\n')
except Exception as e:
    logger.exception(e)
    raise e


# STAGE_NAME = "Data Transformation stage"

# try:
#     logger.info(f"--- Stage {STAGE_NAME} started ---")

#     logger.info(f"--- Stage {STAGE_NAME} completed ---")

# except Exception as e:
#     logger.exception(e)
#     raise e



# STAGE_NAME = "Data Transformation stage"

# try:
#     logger.info(f"--- Stage {STAGE_NAME} started ---")

#     logger.info(f"--- Stage {STAGE_NAME} completed ---")

# except Exception as e:
#     logger.exception(e)
#     raise e