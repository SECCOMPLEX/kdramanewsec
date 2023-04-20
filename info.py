import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/183b228dec64900497caa.jpg https://telegra.ph/file/a46c93054d23bde4117a3.jpg https://telegra.ph/file/0ac502481d96ae40877b9.jpg https://telegra.ph/file/71d4a58daaceaef3dbdee.jpg https://telegra.ph/file/a5b5a3f2302b438fd864d.jpg https://telegra.ph/file/f6ce57c82abe38c5fe26e.jpg https://telegra.ph/file/c869fe5190d12262c467b.jpg https://telegra.ph/file/62196aea6754a9173319e.jpg https://telegra.ph/file/4544a4b4ba4f93f0b1a53.jpg https://telegra.ph/file/09b8eb980ceba0121c7ab.jpg https://telegra.ph/file/a5a68b2b805cd20ddd736.jpg https://telegra.ph/file/518da5ca9e47854d322d1.jpg https://telegra.ph/file/9ec559909eef6d7a025d2.jpg https://telegra.ph/file/00475ad2f322cecc967fa.jpg https://telegra.ph/file/fc9bd776459007036b3fe.jpg https://telegra.ph/file/c72e0c26896e77b6180bd.jpg https://telegra.ph/file/9c630576a13a10278a6fc.jpg https://telegra.ph/file/ecbacd1677d59f82b7531.jpg https://telegra.ph/file/48baba62cb65804b43f58.jpg https://telegra.ph/file/05c4262412819b3195c13.jpg https://telegra.ph/file/367f543bb8bbe98963e60.jpg https://telegra.ph/file/6eaf4e5c8e4041276778d.jpg https://telegra.ph/file/ed97063c727c67c89788f.jpg https://telegra.ph/file/3cf618f94e719c0ed8362.jpg https://telegra.ph/file/1d28a6a303e9954d60b6e.jpg https://telegra.ph/file/bb5a0456baab033855aaf.jpg https://telegra.ph/file/a05dd47a0adfd4f46c402.jpg https://telegra.ph/file/21b7a7163b3db45c32159.jpg https://telegra.ph/file/c4442f57d791a25692c2e.jpg https://telegra.ph/file/62e4efd365146610ce016.jpg https://telegra.ph/file/a05da87b4d9d0c6565b97.jpg https://telegra.ph/file/35d58f3fe4bd974438c2a.jpg https://telegra.ph/file/4cf5991c0d92c7e5a73d5.jpg https://telegra.ph/file/ca88fb2c4acc276dd9393.jpg https://telegra.ph/file/eefb564da3d882bcc672a.jpg https://telegra.ph/file/b38cf8df6a95e1859debf.jpg https://telegra.ph/file/6626ca2b0222025d69e79.jpg https://telegra.ph/file/a293538a67dd4c379e61b.jpg https://telegra.ph/file/bfa1f4703102c65ccf8e1.jpghttps://telegra.ph/file/14422dc751fc2f517f89e.jpg https://telegra.ph/file/4fa992935b6377b1a9ca2.jpg https://telegra.ph/file/bedaa0cc61e1cc5ec592b.jpg https://telegra.ph/file/a6741a5d2e9e0eaeb1ff7.jpg https://telegra.ph/file/70a23bb047f28c529acdd.jpg https://telegra.ph/file/3c12d8d8af26eb46a8ba4.jpg https://telegra.ph/file/e0538d30bdb95c68e2ceb.jpg https://telegra.ph/file/c59378bf570ca415e2d3f.jpg https://telegra.ph/file/0e727f11d4c1c7a1902ea.jpg https://telegra.ph/file/d84ea124b32e5b56296eb.jpg https://telegra.ph/file/5222743bd3ca5d2507cff.jpg https://telegra.ph/file/35af9791e33172250c40b.jpg https://telegra.ph/file/e9d3f0b13452a704cf16e.jpg https://telegra.ph/file/4189d167823f65316b529.jpg https://telegra.ph/file/cb33b9fe933a0ff408c4c.jpg https://telegra.ph/file/ef33f0592f64f64d5ef14.jpg https://telegra.ph/file/7b86b314eff38f982a4ef.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'SECL4u')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🪄 𝚀𝚞𝚎𝚛𝚢 ➠ {query}</b>\n\n <b>𝚃𝚒𝚝𝚕𝚎 ➠ <a href={url}>{title}</a> ({year})</b>\n <b>{release_date} • {runtime}min</b> \n\n <b>𝙶𝚎𝚗𝚛𝚎 ➠ {genres}</b> \n <b>𝚁𝚊𝚝𝚒𝚗𝚐 ⭐️ ➠ {rating}/10 ({votes})</b> \n <b>𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎 ➠ {languages}</b> \n\n <b><a href='https://t.me/SECLK'>®️ sᴇᴄ ʙᴏᴛs</a></b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", '20')
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
