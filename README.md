# Azure Image Resize Function

This project contains an Azure Function that resizes images uploaded to an Azure Blob Storage container.

## Prerequisites

- Azure subscription
- Azure Storage Account
- Python 3.8 or later
- Azure Functions Core Tools

## Setup

1. **Create Azure Resources:**

   - Create a storage account in the Azure portal.
   - Create two blob containers: `input-images` and `output-images`.

2. **Deploy the Function:**

   - Install the Azure Functions Core Tools: [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)
   - Install the Azure CLI: [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

   ```bash
   # Clone the repository
   git clone https://github.com/vishwadnya123/azure-image-resize.git
   cd azure-image-resize/function_app

   # Create a virtual environment and activate it
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

   # Install dependencies
   pip install -r ImageResizeFunction/requirements.txt

   # Deploy the function app
   func azure functionapp publish <your-function-app-name>
