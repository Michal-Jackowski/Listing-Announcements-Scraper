from telethon.sync import TelegramClient
import datetime
import telegram_config
import pandas as pd
import path
import xlsxwriter

api_id = telegram_config.api_id
api_hash = telegram_config.api_hash
chats = [telegram_config.test_user_input_channel]

client = TelegramClient('Me', api_id, api_hash)
df = pd.DataFrame()

for chat in chats:
    with TelegramClient('test', api_id, api_hash) as client:
        #for message in client.iter_messages(chat, offset_date=datetime.date.today(), reverse=True):
        for message in client.iter_messages(chat, reverse=True):
            #print(message.message)
            #print(message.date)
            #print(message)
            #data = { "text" : message.text, "date" : message.date}
            data = {"date" : message.date, "text" : message.text,}
            #df["date"] = pd.to_datetime(df["date"], format='%Y-%m-%d')
            temp_df = pd.DataFrame(data, index=[1])
            #print(temp_df)
            df = df._append(temp_df)
                
#df['date'] = df['date'].dt.tz_localize(None)
df['date'] = df['date'].dt.tz_localize(None)
#df['text'] = pd.to_timedelta(df['text'])
#writer = pd.ExcelWriter(path.scraped_data_from_telegram, engine='xlsxwriter', datetime_format='dd/mm/yy')
#df.to_excel(writer, index=False)
df.to_excel(path.scraped_data_from_telegram.format(datetime.date.today()), index=False)

#DaveX then you would do my_df[time_columns] = my_df[time_columns].dt.tz_localize(None) where time_columns is a list of column names that have datetime dtype