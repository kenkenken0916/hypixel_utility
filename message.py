#url https://discordapp.com/api/webhooks/1387844439938175007/uwyc40CjLs-_Dve_CpsodpjEdCWPEh4EuDQ2D_VUGjPcT_Kdf0ElEahJflGSBbW1RXbw
#nme doom
from discord_webhook import DiscordWebhook
import time

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1387844439938175007/uwyc40CjLs-_Dve_CpsodpjEdCWPEh4EuDQ2D_VUGjPcT_Kdf0ElEahJflGSBbW1RXbw"

def send_discord_message():
    webhook = DiscordWebhook(url=WEBHOOK_URL, content="fuck u ken fix this")
    webhook.execute()

send_discord_message()