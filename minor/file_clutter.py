import os


def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

if __name__ == "__main__":

    files = os.listdir()
    files.remove("main.py")
    print(files)


    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')
    createIfNotExist('Zips')

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    docExts = [".txt", ".docx", ".doc", ".pdf"]
    documents = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    mediaExts = [".mp4", ".mp3", ".flv"]
    mediafiles = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    zipext = [".zip"]
    zipfiles = [file for file in files if os.path.splitext(file)[1].lower() in zipext]

    others = []

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)

    print(others)

    move("Images", images)
    move("Docs", documents)
    move("Media", mediafiles)
    move("Zips", zipfiles)
    move("Others", others)