from telethon import TelegramClient, sync
from config import *
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime, timezone, timedelta
from utils import *
from time import sleep

def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now(timezone(timedelta(hours=3)))) != prev_time

client = TelegramClient('<sess>', api_id, api_hash, proxy=proxy)
client.start()
print('Sess started')

prev_update_time = ""

while True:
    if time_has_changed(prev_update_time):
        print('>Update..')
        prev_update_time = convert_time_to_string(datetime.now(timezone(timedelta(hours=3))))
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"img/{prev_update_time}.png")
        print(f'>Get img/{prev_update_time}.png')
        client(UploadProfilePhotoRequest(file))
        print('>Updated')
        sleep(1)