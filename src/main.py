from time import sleep
from config import mailboxes, sleep_time
from functions import filter_mailbox, create_folders, imap_connect, imap_disconnect
import logging

logging.basicConfig(format="[%(asctime)s - %(funcName)s - %(levelname)s] %(message)s", level=logging.INFO)

# Connect to the imap server, ensure the needed
# mailboxes are present and then disconnect
imap = imap_connect()
create_folders(imap)
imap_disconnect(imap)

# Loop indefinetly
while True:
    # Connect to the imap server using the credentials found in config.py
    imap = imap_connect()

    # Loop through all the required mailboxes and filter them
    for mailbox in mailboxes:
        logging.info('Filtering started on ' + mailbox)
        if filter_mailbox(imap, mailbox) == 0:
            logging.info('There was nothing to do.')

    # Disconnect from the imap server
    imap_disconnect(imap)

    # Sleep for as many seconds as indicated in the config.py file
    logging.debug(f'Filtering done. Rerunning in {sleep_time} seconds.')
    sleep(sleep_time)
    logging.debug('Filtering triggered by timer.')
