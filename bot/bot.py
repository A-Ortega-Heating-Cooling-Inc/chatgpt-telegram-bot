import config
import telegram
import telegram.ext

async def post_init(application):
    await application.bot.set_my_commands([
        telegram.BotCommand("/new", "Start new dialog"),
        # telegram.BotCommand("/mode", "Select chat mode"),
        # telegram.BotCommand("/retry", "Re-generate response for previous query"),
        # telegram.BotCommand("/balance", "Show balance"),
        # telegram.BotCommand("/settings", "Show settings"),
        # telegram.BotCommand("/help", "Show help message"),
    ])

def run_bot():

    application = (
        telegram.ext.ApplicationBuilder()
        .token(config.telegram_token)
        .concurrent_updates(True)
        .rate_limiter(telegram.ext.AIORateLimiter(5))
        .http_version("1.1")
        .get_updates_http_version("1.1")
        .post_init(post_init)
        .build()
    )

    application.run_polling()

if __name__ == "__main__":
    run_bot()