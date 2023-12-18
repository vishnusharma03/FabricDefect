from ingest_data import MongoDBDataset
from torch.utils.data import DataLoader

class MongoDataLoader:
    def __init__(self, db_url, db_name, batch_size=64, num_workers=0):
        self.db_url = db_url
        self.db_name = db_name
        self.batch_size = batch_size
        self.num_workers = num_workers

    def get_loader(self, collection_name, shuffle):
        dataset = MongoDBDataset(self.db_url, self.db_name, collection_name)
        return DataLoader(dataset, batch_size=self.batch_size, shuffle=shuffle, num_workers=self.num_workers)

    def get_train_loader(self):
        return self.get_loader('train', shuffle=True)

    def get_validation_loader(self):
        return self.get_loader('valid', shuffle=False)

    def get_test_loader(self):
        return self.get_loader('test', shuffle=False)



# Usage
# db_url = "mongodb+srv://vishnusharma7:mongodb20@clusters3.bp4facb.mongodb.net/?retryWrites=true&w=majority"
# db_name = "TildaBD"
#
# data_loader = MongoDataLoader(db_url, db_name)
#
# train_loader = data_loader.get_train_loader()
# val_loader = data_loader.get_validation_loader()
# test_loader = data_loader.get_test_loader()



#
#
# db_url = "mongodb+srv://vishnusharma7:mongodb20@clusters3.bp4facb.mongodb.net/?retryWrites=true&w=majority"
# db_name = "TildaBD"
#
# # Training dataset
# train_dataset = MongoDBDataset(db_url, db_name, 'train')
#
# train_loader = DataLoader(train_dataset, batch_size=64,
#                           shuffle=True, num_workers=0)
#
# # Validation dataset
# val_dataset = MongoDBDataset(db_url, db_name, 'valid')
#
# val_loader = DataLoader(val_dataset, batch_size=64,
#                         shuffle=False, num_workers=0)
#
# # Test dataset
# test_dataset = MongoDBDataset(db_url, db_name, 'test')
#
# test_loader = DataLoader(test_dataset, batch_size=64,
#                          shuffle=False, num_workers=0)


# # Usage
#
# collection_name = "test"
# dataset = MongoDBDataset(db_url, db_name, collection_name)
#
# s = dataset.__getitem__(0)
# print(s)




# import os
# import torch
# from torchvision import transforms
# from torch.utils.data import Dataset, DataLoader
# from PIL import Image
# from torchvision.datasets.utils import list_files
# from ingest_data import IngestData
#
# data_loader = IngestData(
#     "mongodb+srv://vishnusharma7:mongodb20@clusters3.bp4facb.mongodb.net/?retryWrites=true&w=majority", "TildaBD")
#
#
# # Normalize means and stds
# mean = [0.485, 0.456, 0.406]
# std = [0.229, 0.224, 0.225]
#
# # Define transforms
# train_transforms = transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Normalize(mean, std)
# ])
#
#
# # Custom dataset
# class CustomDataset(Dataset):
#     def __init__(self, root_dir, transform=None):
#         self.root_dir = root_dir
#         self.transform = transform
#         self.images = list_files(root_dir)
#
#     def __len__(self):
#         return len(self.images)
#
#     def __getitem__(self, idx):
#         img_path = os.path.join(self.root_dir, self.images[idx])
#         image = Image.open(img_path).convert("RGB")
#
#         if self.transform:
#             image = self.transform(image)
#
#         return image


# # Prepare train set
# train_set = CustomDataset('/path/to/train',
#                           transform=train_transforms)
#
# train_loader = DataLoader(train_set,
#                           batch_size=16,
#                           shuffle=True)

