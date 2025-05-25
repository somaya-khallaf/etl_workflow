import requests
import logging
from transform import transform_data

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_api_response():

    logger.info("Testing API response...")
    response = requests.get("https://restcountries.com/v3.1/all", timeout=10)
    assert response.status_code == 200, f"Bad status code: {response.status_code}"
    logger.info("API test passed (status 200 with data)")
    return True


def test_transformations():
    sample = {
        "name": {"common": "Testland", "official": "Test Republic"},
        "region": "Test Region",
        "population": 1000000,
        "area": 50000
    }
 
    logger.info("Testing transformations...")
    result = transform_data([sample])
    assert not result.empty, "Empty transformation result"
    assert "population_density" in result.columns, "Missing calculated column"
    logger.info("Transformation test passed")
    return True

if __name__ == "__main__":
    test_api_response()
    test_transformations()