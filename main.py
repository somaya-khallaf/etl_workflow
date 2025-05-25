# pipeline.py - Core ETL pipeline
import logging
from extract import extract_data
from transform import transform_data
from load import load_data

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_pipeline():

    # Extract
    logger.info("Starting ETL pipeline")
    raw_data = extract_data()
    
    # Transform
    processed_data = transform_data(raw_data)
    
    # Load
    load_data(processed_data)

    logger.info("Pipeline completed successfully")
    return True
        
if __name__ == "__main__":
    run_pipeline()