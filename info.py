import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Admins & Channels
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(channel) if re.search('^-100\d+$', channel) else channel for channel in environ['CHANNELS'].split()]

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
𝐇𝐢, 𝐈'𝐦 𝐒𝐭𝐮𝐝𝐲 𝐌𝐚𝐭𝐞𝐫𝐢𝐚𝐥 𝐒𝐞𝐚𝐫𝐜𝐡 𝐛𝐨𝐭 .

𝐻𝑒𝑟𝑒 𝑦𝑜𝑢 𝑐𝑎𝑛 𝑠𝑒𝑎𝑟𝑐ℎ 𝑀𝑎𝑡𝑒𝑟𝑖𝑎𝑙𝑠 𝑖𝑛 𝑖𝑛𝑙𝑖𝑛𝑒 𝑚𝑜𝑑𝑒. 𝐽𝑢𝑠𝑡 𝑝𝑟𝑒𝑠𝑠 𝑓𝑜𝑙𝑙𝑜𝑤𝑖𝑛𝑔 𝑏𝑢𝑡𝑡𝑜𝑛𝑠 𝑎𝑛𝑑 𝑠𝑡𝑎𝑟𝑡 𝑠𝑒𝑎𝑟𝑐ℎ𝑖𝑛𝑔.

Rᴇϙᴜᴇsᴛ Mᴀᴛᴇʀɪᴀʟ/Aᴅᴅ Mᴀᴛᴇʀɪᴀʟ : @matreqqbot .

𝙲𝚛𝚎𝚊𝚝𝚘𝚛 : 𝖪𝗒𝖺 𝗄𝖺𝗋𝗈𝗀𝖾 𝗇𝖺𝖺𝗆 𝗃𝖺𝗇𝗄𝖾 ?


"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching study material'
