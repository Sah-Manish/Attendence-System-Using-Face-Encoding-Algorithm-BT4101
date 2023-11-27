class SendAlert:
    def __init__(self, msg):
        import requests
        apiToken = '6717954189:AAFb7PDYJ3_pqTPsnYrf30O8R2r-CuU_KUM'
        chatID = '-1002031478342'
        apiURLMSG = f'https://api.telegram.org/bot{apiToken}/sendMessage'
        apiURLImg = f'https://api.telegram.org/bot{apiToken}/sendPhoto'

        try:
            response = requests.post(apiURLMSG, json={'chat_id': chatID, 'text': msg})
            # response = requests.post(apiURLImg, json={'chat_id': chatID, 'photo': img})
            img="Extra7.jpeg"
            files = {'photo': open(img, 'rb')}
            data = {'chat_id': chatID}
            response = requests.post(apiURLImg, files=files, data=data)
            # print(response.text)
        except Exception as e:
            print(e)
# SendAlert("Test message by Extra7, \nPlease ignore this","Extra7.jpeg")
