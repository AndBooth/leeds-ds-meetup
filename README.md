# Leeds Data Science
Repository for code and documents from Leeds Data Science meetup talk

# Productionise Python ML models with Azure Functions how-to guide

We can use Azure Functions to deploy a machine learning model that has been developed in Python as an API. Once the API is created we can ask the model to make predictions on new data by sending it a request.

I have found that the main difficulty in getting this to work lies in ensuring that the steps required to get everything set up have been followed correctly. The documentation to get it working does exist, but can be tricky to piece together. I have written this document with the intention of it being a guide that will allow anyone to get to the point where they have successfully created a machine learning API.

However, it is not intended as a guide to creating full production, enterprise ready software, so it should not be used with that intention.

## Sources

This how-to guide is a collated and abridged version of multiple sources, including Microsoft documentation and the Github repos of one of the developers of the Python Azure Functions worker. For further reading and information you can find these at the following links

- [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Create you first Python function in Azure](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python#create-a-function)
- [Create your first function using Visual Studio Code](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code)
- [Asavari Tayal's github](https://github.com/asavaritayal?utf8=%E2%9C%93&tab=repositories&q=&type=&language=python)

# Prerequisites

To follow this guide you will need to have the following in place

**To create and test functions locally**
- Installation of Python 3.6
- Install [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2)
- Visual Studio Code IDE (you don't actually *need* this)*

* 
