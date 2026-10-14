import random


# أمر إعطاء إشارة الطيارة
@bot.message_handler(commands=['signal', 'aviator'])
def send_aviator_signal(message):
  multiplier = round(random.uniform(1.10, 4.00), 2)

  response = (
      f"✈️ **إشارة لعبة الطيارة (Aviator)**\n\n"
      f"🎯 المضاعف المتوقع: **{multiplier}x**\n"
      f"⚠️ العب بحذر ولا تغامر بكل رصيدك!"
  )

  bot.reply_to(message, response, parse_mode='Markdown')
    
