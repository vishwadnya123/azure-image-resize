import logging
import os
from PIL import Image
from io import BytesIO
import azure.functions as func
from azure.storage.blob import BlobServiceClient

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(os.environ["AzureWebJobsStorage"])

def main(myblob: func.InputStream):
    logging.info(f"Processing blob: {myblob.name}, Size: {myblob.length} bytes")

    try:
        # Read image from the input blob
        image = Image.open(myblob)
        
        # Resize the image
        resized_image = image.resize((128, 128))

        # Save the resized image to a byte stream
        byte_stream = BytesIO()
        resized_image.save(byte_stream, format="JPEG")
        byte_stream.seek(0)

        # Get the output container client
        output_container_client = blob_service_client.get_container_client("output-images")

        # Upload the resized image
        output_blob_name = f"resized-{os.path.basename(myblob.name)}"
        output_blob_client = output_container_client.get_blob_client(output_blob_name)
        output_blob_client.upload_blob(byte_stream, overwrite=True)

        logging.info(f"Resized image uploaded to output-images/{output_blob_name}")
    except Exception as e:
        logging.error(f"Error processing blob: {e}")
