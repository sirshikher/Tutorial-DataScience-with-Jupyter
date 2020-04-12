import os 
import pandas as pd
import csv 
from dotenv import find_dotenv,load_dotenv
import logging


def extract_data(file_path):
        with open(file_path, 'w') as handle:
            response = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")
            response.to_csv(handle)
            
def main(project_dir):
    
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    
    raw_data_path = os.path.join(os.path.pardir,'data','raw')
    train_data_path = os.path.join(raw_data_path,'train.csv')
    test_data_path = os.path.join(raw_data_path,'test.csv')

    extract_data(train_data_path)
    extract_data(test_data_path)
    logger.info('downloaded raw training and test data')
    
if __name__ == '__main__':
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    log_fmt = '%(asctime)s - %(name)s - &(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    
    main(project_dir)