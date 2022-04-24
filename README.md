# Prerequisites:
- Python installation (see [Link](https://wiki.python.org/moin/BeginnersGuide/Download))
- Pip installation (should come with the latest Python version, 
otherwise, see [Link](https://pip.pypa.io/en/stable/installation/))

# Initial Setup:
- Run `pip install -r requirements.txt`
- Modify `config_ex.ini` with your mail data and recipient phone number and remove the `_ex` from the file name. 
- For Gmail, set up an app password (see https://support.google.com/accounts/answer/185833?hl=en for help)
- Specify the sender address you want to listen to and the interval to check for new mails in seconds
- Finally, run the script using `python main.py`
