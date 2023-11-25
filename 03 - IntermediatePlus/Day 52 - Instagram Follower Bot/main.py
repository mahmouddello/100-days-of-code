from instagram_bot import InstagramFollowerBot

bot = InstagramFollowerBot()

if __name__ == '__main__':
    bot.login()
    bot.find_followers()
