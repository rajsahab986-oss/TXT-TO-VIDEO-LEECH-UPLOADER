

from os import environ

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "hellloooxxy")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "hellloooxxy")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "7170328188").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "7170328188"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





