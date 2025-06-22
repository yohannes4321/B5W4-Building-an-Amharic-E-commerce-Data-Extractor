from telethon import TelegramClient
from dotenv import load_dotenv
load_dotenv('.env')
import os
import csv
api_id=os.getenv('api_id')
api_hash=os.getenv('api_hash')
phone=os.getenv('phone')
client=TelegramClient(phone,api_id,api_hash)
async def main():
    await client.start()
    if not await client.is_user_authorized():
        client.send_code_request(phone)
        code=('Enter code here')
        client.sign_in(phone,code)
    async def tellegram_scrapper(client,channel,media_dir,writer):
        entity=await client.get_entity(channel)
        channel_title=entity.title
        channel_username=entity.username
        async for message in client.iter_messages(entity,limit=60):
            media_path=None
            if message.media and hasattr(message.media,'photo'):
                file_name=f'{channel_username}_{message.id}.jpg'
                media_path=os.path.join(media_dir,file_name)
                await client.download_media(message.media,media_path)
            writer.writerow([
                channel_title,
            channel_username,
            message.message if message.message else "",
            message.date,
            media_path if media_path else ""
            ])

    channels=['@ZemenExpress',
              ' @nevacomputer',
              '@meneshayeofficial',
              '@ethio_brand_collection',
              '@Leyueqa'
              ]
    media_dir='photos'
    os.makedirs(media_dir,exist_ok=True)
    with open('telegram_data.csv','w',newline='',encoding='utf-8') as file :
        writer=csv.writer(file)
        writer.writerow(['Channel Title','Channel Username','Message','Date' ,'Media Path'])
        
        for channel in channels:
            await tellegram_scrapper(client,channel,media_dir,writer)
            print(f"scrapped Data from {channel}")

with client:
    client.loop.run_until_complete(main())