import os
from azure.storage.blob import BlobServiceClient

# Replace with your Azure Storage connection string
CONNECTION_STRING = "Your_Azure_Storage_Connection_String"
RESTORE_FOLDER = "restored_data"

def restore_files():
    try:
        os.makedirs(RESTORE_FOLDER, exist_ok=True)

        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        print("Starting restore process...\n")

        blob_list = container_client.list_blobs()

        for blob in blob_list:
            file_name = blob.name.split("_", 2)[-1]  # remove timestamp part
            download_path = os.path.join(RESTORE_FOLDER, file_name)

            with open(download_path, "wb") as file:
                download_data = container_client.download_blob(blob.name)
                file.write(download_data.readall())

            print(f"Restored: {blob.name} -> {download_path}")

        print("\nRestore completed successfully!")

    except Exception as e:
        print(f"Error during restore: {e}")

if __name__ == "__main__":
    restore_files()