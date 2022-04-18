import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,"rb") 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BF8c-xDKDHj-bOc8uiz5tXWkUW00KKpbhAA5PULP71eDV3oCQU00gBqmVtSH7L_xx1ASnfx_XdUKhoNg4ARue4f702pwaXfo9qZaqdYMl8RUvfLx-6wlIW-u1adJIrstE1YQEYbbMfTY'
    transferData = TransferData(access_token)

    file_from = input("Enter the file name to transfer : ")
    file_to = input("Enter the file path in dropbox : ") 

     # The full path to upload the file to, including the file name
    

    # API v2
    transferData.upload_file(file_from, file_to)
    print ("File has been uploaded")

main()