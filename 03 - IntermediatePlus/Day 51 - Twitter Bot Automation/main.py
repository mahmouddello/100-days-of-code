from twitter_bot import InternetSpeedTwitterBot

PROMISED_UPLOAD = 5
PROMISED_DOWNLOAD = 24

bot = InternetSpeedTwitterBot(upload=PROMISED_UPLOAD, download=PROMISED_DOWNLOAD)

actual_upload, actual_download = bot.get_internet_speed()

print(f"Download: {actual_download}\nUpload: {actual_upload}")

if actual_download < PROMISED_DOWNLOAD or actual_upload < PROMISED_UPLOAD:
    bot.tweet_at_provider(
        promised_download=PROMISED_DOWNLOAD,
        promised_upload=PROMISED_UPLOAD,
        upload=actual_upload,
        download=actual_download
    )
