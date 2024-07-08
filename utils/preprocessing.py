from typing import Tuple
import pandas as pd


def preprocess_member(df: pd.DataFrame) -> pd.DataFrame:

    def replace_county_name(cell: Tuple[str, str]) -> str:
        # 台北市沒有南屯區，然後鼓山區在高雄...
        county_name, city_name = cell
        res = county_name
        if city_name == '南屯區':
            res = '台中市'
        if city_name == '鼓山區':
            res = '高雄市'
        return res

    # Remove missing values
    df = df[
        df['Gender'].notna() & \
        df['SignupChannle'].notna()
    ].copy()
    # Extract Age and SignupDuration
    now = pd.Timestamp.now()
    df['Birthday'] = pd.to_datetime(df['Birthday'], format='%Y-%m-%d')
    df['Age'] = (now - df['Birthday']).apply(lambda x: x.days) // 365
    df['SignupDate'] = df['SignupDate'].str.extract(r'(\d{4}-\d{2}-\d{2})')[0]
    df['SignupDate'] = pd.to_datetime(df['SignupDate'], format='%Y-%m-%d', errors='coerce')
    df['SignupDuration'] = (now - df['SignupDate']).dt.days
    # Replace CountyName
    # 有一筆 'New Taipei City'在CountyName裏面
    df.loc[:, 'CountyName'] = df['CountyName'] \
                                .str.replace('New Taipei City', '新北市')
    # 龍潭是鄉不是區
    df.loc[:, 'CityName'] = df['CityName'] \
                                 .str.replace('龍潭鄉', '龍潭區')
    df.loc[:, 'CountyName'] = df[['CountyName', 'CityName']] \
                                 .apply(replace_county_name, axis=1)
    df.loc[:, 'Address'] = df['CountyName'] + df['CityName']
    return df


def preprocess_master(df: pd.DataFrame) -> pd.DataFrame:
    df.loc[:, 'OrderDate'] = pd.to_datetime(df['OrderDate'], format='%Y-%m-%d')
    df = df[df['TicketSales'] > 0]
    return df


def preprocess_detail(df: pd.DataFrame) -> pd.DataFrame:
    df.loc[:, 'ProductPrice'] = df['Sales'] / df['Quantity']
    df = df[df['ProductPrice'] > 0]
    return df
