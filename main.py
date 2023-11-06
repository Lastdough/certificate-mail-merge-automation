from modules.certificate_sender.sender import Sender

sender = Sender(folder_id='1DfBMvowZcaO9ShrZlCd-ZhnysNmcmQOz',
                client_secret_path='secrets/client_secret.json')

sender.generate_all()
sender.send_all()
