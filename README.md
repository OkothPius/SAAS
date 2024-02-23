# Order Service

This repo contains the code that allows a customer to make an order and get an alert. The SMS alert is send using the African's Talking API. 

# Requirements
* Python (3.11.8)
* Azure Account
* Azure Subscription

Please install the dependencies via the `requirements.txt` file using 
```commandline
pip install -r requirements.txt
```
If you don't have Pip installed please follow instructions online on how to do it.

# How To Run the Unit Tests
To run the Unit Tests, from the root of the repo run
```commandline
coverage run -m pytest  -v -s
```

# Configuring OpenID Connect in Azure
Ensure you have created:
* Create an Entra ID application and a service principal.
* Add federated credentials for the Entra ID application.
* Create GitHub secrets for storing Azure configuration.

Make sure to create your `AZURE_CREDENTIALS`, `AZURE_CLIENT_ID`, `AZURE_SUBSCRIPTION_ID`, `AZURE_TENANT_ID`, `RESOURCE_GROUP`, `CLUSTER_NAME`. `REGISTRY_URL`. and `AZURE_CONTAINER_REGISTRY` aecrets in your repository setting.

# CICD
![image](https://github.com/OkothPius/SAAS/assets/47280229/2edc6f9e-4d48-438a-b654-803857501deb)


[![Coverage Status](coverage.svg)](https://github.com/OkothPius/Order-Service)
