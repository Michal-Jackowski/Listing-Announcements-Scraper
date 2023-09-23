from telethon.sync import TelegramClient
import datetime
import telegram_config
import pandas as pd
import path

api_id = telegram_config.api_id
api_hash = telegram_config.api_hash
chats = [telegram_config.test_user_input_channel]

client = TelegramClient('Me', api_id, api_hash)
df = pd.DataFrame()

for chat in chats:
    with TelegramClient('test', api_id, api_hash) as client:
        for message in client.iter_messages(chat, reverse=True):
            data = {"date" : message.date, "text" : message.text,}
            temp_df = pd.DataFrame(data, index=[1])
            df = df._append(temp_df)
                
df['date'] = df['date'].dt.tz_localize(None)
writer = pd.ExcelWriter(path.scraped_data_from_telegram.format(datetime.date.today()), engine='xlsxwriter')
df.to_excel(writer, sheet_name="MySheet", index=False)

workbook = writer.book
worksheet = writer.sheets['MySheet']

for i, col in enumerate(df.columns):
    width = max(df[col].apply(lambda x: len(str(x))).max(), len(col))
    worksheet.set_column(i, i, width)

writer._save()