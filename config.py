
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3,os
from dotenv import load_dotenv


load_dotenv()

host =  os.getenv("HOST")
region = os.getenv("REGION") 
service = os.getenv("SERVICE") 
access_key = os.getenv("ACCESS")
secret_key = os.getenv("SECRET")
awsauth = AWS4Auth(access_key, secret_key, region, service)
es = Elasticsearch(
        hosts = [{'host': host, 'port': 443}],
        http_auth = awsauth,
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
    )
def elastic():
    return es