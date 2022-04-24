"""
A simple script to periodically check Gmail for specific sender.
If received mail from sender, send Telegram message with subject.
"""

from imap_tools import MailBox
from telethon.sync import TelegramClient
from config import api_config, gmail_config

# Configure this as you like!
sender = "abfuhrkalender@srhh.de"

# Config stuff
imap_url = "imap.gmail.com"
user = gmail_config()["user"]
password = gmail_config()["password"]
api_id = api_config()["api_id"]
api_hash = api_config()["api_hash"]
phone = api_config()["phone"]


def main():
    # Login to Gmail
    mailbox = MailBox(imap_url).login(user, password)
    # Get mail from server, pass if None
    print("Getting mail...")
    mail = None
    try:
        mail = list(mailbox.fetch(f'FROM "{sender}"'))[0]
    except IndexError:
        pass
    if mail is None:
        return "No mail from sender found!"
    # Send subject to specified number
    print("Sending Telegram message...")
    with TelegramClient('session', api_id, api_hash) as client:
        client.send_message('me', mail.subject)
    # Move mail to trash
    print("Moving mail to trash...")
    mailbox.move([msg.uid for msg in mailbox.fetch(f'FROM "{sender}"')], "[Google Mail]/Trash")
    # Logout from Gmail
    mailbox.logout()
    # Sleep for x seconds
    return "All done!"


if __name__ == "__main__":
    print(main())
