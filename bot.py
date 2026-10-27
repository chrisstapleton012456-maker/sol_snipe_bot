import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

MY_SOL = "EWnAGRkwm91ewT3N8MVZV9ypD7Neb4tXvbBdNP4z3wAo"
MY_BTC = "bc1q9gmrxha3yqd2kjzjmdclc7h73qwutsc6g63ctn"
BOT_TOKEN = "8944369323:AAGyXKJ8Re3HXcGA55xinF7pCMZOPhbWvWY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Sol Sniper Active! @sol_sniper_00ms_bot\n\n/deposit\n/balance\n/snipe_on\n/demo")

async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💰 DEPOSIT:\n\nSOL:\n`{MY_SOL}`\n\nBTC:\n`{MY_BTC}`", parse_mode='Markdown')

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 DEMO BALANCE:\nSOL: 1.25 SOL\nBTC: 0.0021 BTC\nReady to snipe!")
async def snipe_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 SNIPER ON! Watching new coins...")
async def demo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧪 DEMO: Go to faucet.solana.com and paste your SOL address to get free test SOL")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("deposit", deposit))
app.add_handler(CommandHandler("balance", balance))
app.add_handler(CommandHandler("snipe_on", snipe_on))
app.add_handler(CommandHandler("demo", demo))
app.run_polling()
