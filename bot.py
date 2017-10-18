import config
import telebot
import psycopg2
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	slovo= message.text
	conn = psycopg2.connect(
		host='localhost', port='5432', database='klimanych',
		user='klimanych', password='Pezhishe1')
	cur = conn.cursor()
	sql_fam=("select fam from kursanty where jeton =%s")
	sql_im=("select im from kursanty where jeton =%s")
	sql_vzv=("select vzv from kursanty where jeton =%s")
	cur.execute(sql_fam,(slovo,))
	fam=str(cur.fetchall())
	cur.execute(sql_im,(slovo,))
	im=str(cur.fetchall())
	cur.execute(sql_vzv,(slovo,))
	vzv=str(cur.fetchall())
	answer=fam[3:(len(fam)-4)]+" "+im[3:(len(im)-4)]
	conn.close()
	bot.send_message(message.chat.id,answer)
bot.polling()
