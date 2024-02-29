import poplib
from email.parser import Parser
from email.header import decode_header

# 邮箱配置
email = 'liuperson304@126.com'
password = 'NCFGDQFUCLREFWNG'
pop3_server = 'pop.126.com'
subject_to_search = 'Number of submissions'

# 连接到 POP3 服务器
mail_server = poplib.POP3_SSL(pop3_server, 995)
mail_server.user(email)
mail_server.pass_(password)

# 搜索符合特定主题的邮件
num_messages = len(mail_server.list()[1])
for i in range(num_messages, 0, -1):
    raw_email = b'\n'.join(mail_server.retr(i)[1]).decode('utf-8')
    email_message = Parser().parsestr(raw_email)
    subject = email_message['Subject']
    
    if subject == subject_to_search:
        # 找到主题为"Number of submissions"的邮件
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                content = part.get_payload(decode=True).decode(part.get_content_charset())
                print("邮件正文内容:")
                print(content)
                break

# 关闭连接
mail_server.quit()


