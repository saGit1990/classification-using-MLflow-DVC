import shutil

class CopyModel:
    def __init__(self, old_path, new_path):
        self.old_path = old_path
        self.new_path = new_path
        
    def model_copier(self):
        try:
            shutil.copy(self.old_path, self.new_path)
        except Exception as e:
            raise e