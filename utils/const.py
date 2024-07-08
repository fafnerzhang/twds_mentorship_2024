import os 
import sys
from pathlib import Path


ROOT = Path(os.path.abspath(__file__)).parent.parent

SAMPLE_DATA_DETAIL_PATH = f'{ROOT}/storage/raw/sample_data_detail.csv'
SAMPLE_DATA_MASTER_PATH = f'{ROOT}/storage/raw/sample_data_master.csv'
SAMPLE_DATA_MEMBER_PATH = f'{ROOT}/storage/raw/sample_data_member.csv'
GEOLOCATION_PATH = f'{ROOT}/storage/external/geolocation.csv'
