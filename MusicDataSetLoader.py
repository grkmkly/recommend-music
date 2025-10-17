import pandas as pd
import os


class MusicDatasetLoader:

    def __init__(self, base_path="./recommendation-dataset/"):
        self.base_path = base_path
        self.members = None
        self.sample_submission = None
        self.song_extra_info = None
        self.songs = None
        self.test = None
        self.train = None
        
        self._load_data()

    def _load_data(self):

        print("Csv files are loading")
        try:
            self.members = pd.read_csv(os.path.join(self.base_path, "members.csv"))
            self.sample_submission = pd.read_csv(os.path.join(self.base_path, "sample_submission.csv"))
            self.song_extra_info = pd.read_csv(os.path.join(self.base_path, "song_extra_info.csv"))
            self.songs = pd.read_csv(os.path.join(self.base_path, "songs.csv"))
            self.test = pd.read_csv(os.path.join(self.base_path, "test.csv"))
            self.train = pd.read_csv(os.path.join(self.base_path, "train.csv"))
            print("Csv files had loaded")
        except Exception as e:
            print(f"Csv files can not readed {e}")