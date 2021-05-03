import dropbox

__accessToken__ = dbxAccessToken
__dbx__ = dropbox.Dropbox(__accessToken__)
__dropboxPath__ = dbxPath

#dbx.files_create_folder('/..', autorename=False)

def getFolderValues():
    for entry in __dbx__.files_list_folder(__dropboxPath__).entries:
        print(entry.name)

#upload file
def saveFile(image, name):
    destination =  __dropboxPath__+'/'+name
    __dbx__.files_upload(image,destination, mode=dropbox.files.WriteMode('overwrite', None), autorename=True, client_modified=None, mute=False, property_groups=None, strict_conflict=False)
