import os
from azure.storage.blob import BlobServiceClient
from datetime import datetime

# Replace with your Azure Storage connection string
CONNECTION_STRING = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
LOCAL_FOLDER = "sample_data"

def upload_files():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        print("Starting backup process...\n")

        for file_name in os.listdir(LOCAL_FOLDER):
            file_path = os.path.join(LOCAL_FOLDER, file_name)

            if os.path.isfile(file_path):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                blob_name = f"{timestamp}_{file_name}"

                with open(file_path, "rb") as data:
                    container_client.upload_blob(name=blob_name, data=data, overwrite=True)

                print(f"Uploaded: {file_name} -> Blob: {blob_name}")

        print("\nBackup completed successfully!")

    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    upload_files()