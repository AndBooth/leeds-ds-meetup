# leeds-ds-meetup
Repository for code and documents from Leeds Data Science meetup talk

# Productinise Python ML models with Azure Functions how-to guide

We can use Azure Functions to deploy a machine learning model that has been developed in Python as an API. Once the API is created we can ask the model to make predictions on new data by sending it a request.

I have found that the main difficulty in getting this to work lies in ensuring that the steps required to get everything set up have been followed correctly. The documentation to get it working does exist, but can be tricky to piece together. I have written this document with the intention of it being a guide that will allow anyone to get to the point where they have successfully created a machine learning API.

However, it is not intended as a guide to creating full production, enterprise ready software, so it should not be used with that intention.

This how-to guide is a collated and abridged version of multiple sources, including Microsoft documentation and   
