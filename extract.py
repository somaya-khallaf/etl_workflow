import requests
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def extract_data():

    url = "https://restcountries.com/v3.1/all"
    
    try:
        logger.info("Starting data extraction from API")
        response = requests.get(url)
        
        # Validate response
        if response.status_code != 200:
            logger.error(f"API request failed with status code: {response.status_code}")
            return None
            
        data = response.json()
        logger.info(f"Successfully extracted data for {len(data)} countries")
        return data
        
    except Exception as e:
        logger.error(f"Error during data extraction: {str(e)}")
        return None

if __name__ == "__main__":
    extracted_data = extract_data()
    if extracted_data:
        logger.info("Data extraction completed successfully")
    else:
        logger.error("Data extraction failed")