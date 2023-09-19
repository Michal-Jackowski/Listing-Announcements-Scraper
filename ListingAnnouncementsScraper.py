from telethon.sync import TelegramClient
import datetime
import telegram_config
#import pandas as pd

# Insert api id here
api_id = telegram_config.api_id
# Insert api_hash here
api_hash = telegram_config.api_hash

#chats = ['...'] # Insert chats or channels here, legit one
#chats = [telegram_config.user_input_channel]
# Insert chats or channels here, just for testing purpose
chats = [telegram_config.test_user_input_channel]

client = TelegramClient('None', api_id, api_hash)

#df = pd.DataFrame()

print("Waiting for Announcements...")
while True:
    for chat in chats:
        with TelegramClient('test', api_id, api_hash) as client:
            for message in client.iter_messages(chat, offset_date=datetime.date.today(), reverse=True):
                print(message.message)
                #print(message.date)
                print(message)
                #data = { "group" : chat, "sender" : message.sender_id, "text" : message.text, "date" : message.date}
                #temp_df = pd.DataFrame(data, index=[1])
                #df = df._append(temp_df)
                
#df['date'] = df['date'].dt.tz_localize(None)
#df.to_excel("...".format(datetime.date.today()), index=False)