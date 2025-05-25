import pandas as pd
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_data(df, filename='data/output.csv'):
    if df is None or df.empty:
        logger.error("No data provided for loading")
        return False
    
    try:
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Save to CSV
        df.to_csv(filename, index=False)
        logger.info(f"Data successfully saved to {filename}")
        return True
        
    except Exception as e:
        logger.error(f"Error during data loading: {str(e)}")
        return False

if __name__ == "__main__":
    # For testing purposes
    import pandas as pd
    test_df = pd.DataFrame({
        'name': ['Testland'],
        'population': [1000000]
    })
    
    if load_data(test_df, 'data/test_output.csv'):
        logger.info("Load test completed successfully")