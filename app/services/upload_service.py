import os, string, random
import shutil

class UploadService:
    def random_string(self, ):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    async def store_file(self, file):
        os.makedirs('uploads', exist_ok=True)
        extension = os.path.splitext(file.filename)[1]
        newname = self.random_string() + extension
        with open(os.path.join('uploads', newname), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return newname


    def remove_file(self, filename):
        try:
            os.remove(os.path.join('app/uploads', filename))
        except:
            print('file already Deleted')