import base64
from pymongo import MongoClient
from PIL import Image
from io import BytesIO
from torch.utils.data import Dataset
from torchvision import transforms


class MongoDBDataset(Dataset):
    def __init__(self, db_url, db_name, collection):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection]

    def __getitem__(self, idx):
        sample = self.collection.find()[idx]
        # sample = self.collection.find({}).skip(idx).limit(1).next()
        # cursor = self.collection.find({})
        # sample = cursor.skip(idx).limit(1).next()
        img = sample['image_data']
        img_bytes = base64.b64decode(img)
        img = BytesIO(img_bytes)
        img = Image.open(img).convert("RGB")
        label = sample['labels']

        # Normalize means and stds
        mean = [0.65036837, 0.65036837, 0.65036837]
        std = [0.11331617, 0.11331617, 0.11331617]

        # Transform
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean, std)
        ])
        img = transform(img)
        return img, label

    def __len__(self):
        return self.collection.estimated_document_count()


# # Usage
# dataset = MongoDBDataset(db_url, db_name, collection_name)



# import pymongo
#
# class IngestData:
#
#     def __init__(self, uri, db_name):
#         self.client = pymongo.MongoClient(uri)
#         self.db = self.client[db_name]
#
#     def load_data(self, collection_name):
#
#         if collection_name == "train":
#             collection = self.db['train']
#         elif collection_name == "test":
#             collection = self.db['test']
#         elif collection_name == "valid":
#             collection = self.db['valid']
#         else:
#             print("Invalid collection name")
#             return
#         images = list(collection.find({}, {'image_data': 1}))
#         labels = list(collection.find({}, {'label': 1}))
#
#         return images, labels


# # Usage
# data_loader = IngestData(
#     "mongodb+srv://vishnusharma7:mongodb20@clusters3.bp4facb.mongodb.net/?retryWrites=true&w=majority", "TildaBD")
#
# collection_name = "test"
# images, labels = data_loader.load_data(collection_name)