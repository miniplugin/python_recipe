import smtplib # SMTP 서버사용가능한 모듈
from email.mime.text import MIMEText # 메일 내용을 담을 수 있는 모듈
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sendEmail = "네이버 이메일"
recvEmail = "받는 사용자 이메일"
password = "사용자 개인 비번"

# 메일서버정보: https://help.naver.com/support/contents/contents.help?serviceNo=2342&categoryNo=2288
smtpName = "smtp.naver.com" # smtp 서버 주소
smtpPort = 587 # smtp 서비스 포트

# 여러 MIME 를 넣기 위한 MIMEMultipart 객체 생성
msg = MIMEMultipart()

# 본문
text = "파이썬으로 내게 메일 보내기 내용"
msg_content = MIMEText(text) # 편지 봉투 생성
msg.attach(msg_content)

# 파일 추가 with 파일 처리 함수 사용
fileName = 'attach.txt'
with open(fileName, 'rb') as FD: # rb(read binary), FD(File Descriptor)
    msg_attach = MIMEApplication(FD.read())
    # 첨부파일의 정보를 헤더로 추가
    msg_attach.add_header('Content-Disposition','attachment',filename=fileName)
    msg.attach(msg_attach)

msg['Subject'] = "파이썬으로 내게 메일 보내기 제목"
msg['From'] = sendEmail
msg['To'] = recvEmail
# print(msg.as_string())

s = smtplib.SMTP(smtpName, smtpPort)
s.starttls() # TLS 보안 처리
s.login(sendEmail, password) # SMTP 서버 로그인 인증
s.sendmail(sendEmail, recvEmail, msg.as_string()) # 메일 전송 함수사용
s.close() # smtp 서버 연결 종료