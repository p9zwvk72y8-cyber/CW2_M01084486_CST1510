from app.db import get_connection
from app.cyber_incidents import get_user
name = 'ken23'

id,name,hash = get_user(get_connection(),name)
print(id,name,hash)


