# cthulhualtar-api
API service for the Cthulhu altar

# Development Environment
1. Codespace on VS Code
1. 8 core 16 GB RAM

# Links
- Local : [http://127.0.0.1:5001/api/check_alive](http://127.0.0.1:8000/api/check_alive)
- Azure : [https://cthulhualtarapi-d6ekechrece6beb8.centralus-01.azurewebsites.net:8181/api/check_alive](https://cthulhualtarapi-d6ekechrece6beb8.centralus-01.azurewebsites.net/api/check_alive)

# Azure Setup Notes 
## Get values needed for pipeline setup 
To retrieve the details for AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET, and AZURE_SUBSCRIPTION_ID in the Azure Portal, follow these steps:

1. AZURE_CLIENT_ID (Application (client) ID)
This is the unique identifier for your Azure Service Principal (or registered app).
Navigate to Azure Active Directory in the Azure portal.
Under Manage, go to App registrations.
Select the application (service principal) you created (or any registered app).
On the Overview page of the selected app, you'll see the Application (client) ID. This is your AZURE_CLIENT_ID.
1. AZURE_TENANT_ID (Directory (tenant) ID)
This is the ID of your Azure Active Directory (AAD) tenant.
In the same App registrations section where you found the Application (client) ID, you can also find the Directory (tenant) ID under the Overview page. This is your AZURE_TENANT_ID.
1. AZURE_CLIENT_SECRET
The client secret is a key used to authenticate your Service Principal.
Go to the Certificates & secrets tab on the App registrations page for your application.
Under the Client secrets section, click New client secret.
Add a description and choose an expiration period.
Click Add, and the secret value will be shown. Copy the secret immediately, as it won't be visible again after you leave this page. This value is your AZURE_CLIENT_SECRET.
1. AZURE_SUBSCRIPTION_ID
This is the ID of your Azure subscription, which is necessary for your Service Principal to have access to deploy resources.

Navigate to Subscriptions in the Azure portal (search for "Subscriptions" in the search bar).
Select the subscription that you want your Service Principal to have access to.
On the Overview page of the selected subscription, you'll see the Subscription ID. This is your AZURE_SUBSCRIPTION_ID.

## Set up Azure credentials using Service Principal
