import connect
from pymongo.collection import Collection
from connect.connect import ConnectToRpi4
from main import CafeteriaDataBase


db = ConnectToRpi4(
    user_name="ufo",
    user_passwd="pempiai234",
    host="192.168.1.81",
    port=27017,
    db_name="cafeteria",
    collection_name="customer",
)
