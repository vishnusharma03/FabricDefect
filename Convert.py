import os
from PIL import Image
import json
import base64


def convert_images_to_binary_and_save_as_json(image_folder, label_folder, output_file):
    # Get the list of image files
    image_files = os.listdir(image_folder)

    # Create an empty list to store image data and labels
    data_list = []

    for image_file in image_files:
        # Construct the paths for images and labels
        image_path = os.path.join(image_folder, image_file)
        label_path = os.path.join(label_folder, image_file.replace(".jpg",
                                                                   ".txt"))  # Assuming labels have the same name with .txt extension

        # Check if the label file exists
        if os.path.exists(label_path):
            # Open and read the image file as binary
            with open(image_path, "rb") as image_files:
                image_data = base64.b64encode(image_files.read()).decode('utf-8')

            # Read labels from the label file
            with open(label_path, "r") as label_file:
                labels = label_file.read().strip()

            # Create a dictionary with image data and labels
            data_dict = {"image_data": image_data, "labels": labels}

            # Append the dictionary to the list
            data_list.append(data_dict)

    # Write the list to a JSON file
    with open(output_file, "w") as output_files:
        json.dump(data_list, output_files)


if __name__ == "__main__":
    image_folder = "data/test/images"
    label_folder = "data/test/labels"
    output_file = "test_data.json"

    convert_images_to_binary_and_save_as_json(image_folder, label_folder, output_file)

# import os
# from PIL import Image
# import json
# import base64
#
#
# def convert_images_to_binary_and_save_as_json(image_folder, label_folder, output_folder):
#     # Create output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)
#
#     # Get the list of image files
#     image_files = os.listdir(image_folder)
#
#     for image_file in image_files:
#         # Construct the paths for images and labels
#         image_path = os.path.join(image_folder, image_file)
#         label_path = os.path.join(label_folder, image_file.replace(".jpg",
#                                                                    ".txt"))  # Assuming labels have the same name with .txt extension
#
#         # Check if the label file exists
#         if os.path.exists(label_path):
#             # Open and read the image file as binary
#             with open(image_path, "rb") as image_files:
#                 image_data = base64.b64encode(image_files.read()).decode('utf-8')
#
#             # Read labels from the label file
#             with open(label_path, "r") as label_file:
#                 labels = label_file.read().strip()
#
#             # Create a dictionary with image data and labels
#             data_dict = {"image_data": image_data, "labels": labels}
#
#             # Convert the dictionary to JSON
#             json_data = json.dumps(data_dict)
#
#             # Construct the output file path
#             output_path = os.path.join(output_folder, image_file.replace(".jpg", ".json"))
#
#             # Write the JSON data to the output file
#             with open(output_path, "w") as output_file:
#                 output_file.write(json_data)
#
#
# if __name__ == "__main__":
#     image_folder = "data/train/images"
#     label_folder = "data/train/labels"
#     output_folder = "output_json"
#
#     convert_images_to_binary_and_save_as_json(image_folder, label_folder, output_folder)
