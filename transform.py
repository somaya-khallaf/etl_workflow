import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def transform_data(data):

    if not data:
        logger.error("No data provided for transformation")
        return None
    
    try:
        logger.info("Starting data transformation")
        
        # Initialize list to store transformed data
        transformed = []
        
        for country in data:
            try:
                transformed.append({
                    'name': country.get('name', {}).get('common', 'N/A'),
                    'official_name': country.get('name', {}).get('official', 'N/A'),
                    'region': country.get('region', 'N/A'),
                    'subregion': country.get('subregion', 'N/A'),
                    'population': country.get('population', 0),
                    'area': country.get('area', 0),
                    'languages': ', '.join(country.get('languages', {}).values()) if country.get('languages') else 'N/A',
                    'capital': ', '.join(country.get('capital', ['N/A']))
                })
            except Exception as e:
                logger.warning(f"Error processing country: {str(e)}")
                continue
        
        # Create DataFrame
        df = pd.DataFrame(transformed)
        
        # Add derived columns
        df['population_density'] = df['population'] / df['area']
        df['population_density'] = df['population_density'].round(2)
        
        logger.info(f"Successfully transformed {len(df)} records")
        return df
        
    except Exception as e:
        logger.error(f"Error during data transformation: {str(e)}")
        return None

if __name__ == "__main__":
    # For testing purposes
    sample_data = [{
        'name': {'common': 'Testland', 'official': 'Republic of Testland'},
        'region': 'Test Region',
        'population': 1000000,
        'area': 50000
    }]
    
    transformed = transform_data(sample_data)
    if transformed is not None:
        logger.info("Transformation test completed successfully")
        print(transformed.head())