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

**To deply to Azure**
- All of the above
- An active Azure subscription (free to create)
- Install the Azure [Command-line Interface](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)

\* You don't have to use Visual Studio Code but it has some tools that I find make the deployment process run a bit smoother

With these things in place we can now begin development of our Azure Function.

# Create and test a function locally

You can create, run and test a Python Azure Function locally without an Azure subscription, so you can carry out the majority of the process without the worry of incurring any costs. The instructions given here assume you are using the Visual Studio Code IDE.

## Install the Azure Functions extension in VS Code

The Azure Functions extension in VS Code provides some functionality that automates some of the tasks, such as creating an Azure Functions project and Azure Function templates.

<img src="https://github.com/AndBooth/leeds-ds-meetup/blob/master/Misc/Images/azurefunctionsextension.PNG" width="450" height="200">

## Create an Azure Functions project

Once installed we can get straight into creating our first locally deployed Azure Function. The first thing to do is to create an Azure Functions project. If you select the two buttons in the image below you will then be prompted to choose a directory where your function app will be stored and asked to choose a language, choose a folder and then choose Python.

<img src="https://github.com/AndBooth/leeds-ds-meetup/blob/master/Misc/Images/setupazfun.PNG">

Setup of the project will take a little while, once complete you will see that a new folder structure has been created and some files added to the directory that you chose earlier. These files are important but are mostly outside of the context of this guide so we won't worry too much about them here (see the links provided above for more detail).

## Create an Azure Function

We can now create our first Azure Function. This is very easy; the Azure Functions extension provides templates that provide everything we need. In this guide I am just going to show how to create and run one of these template functions but look out for updates when I will show how to do it for our own function, servicing a machine learning model.

<img src="https://github.com/AndBooth/leeds-ds-meetup/blob/master/Misc/Images/createazfun.PNG">

You will be prompted to
1. Choose the location of the Function App - this is where the code will be created
2. Choose a trigger template - choose HttpTrigger
3. Choose a name for the function

Once this is done you will see that a new folder has been created with the name you chose in step 3 above. Look inside and you will see a file called **\_\_init\_\_.py**. This file contains the code for your function and is actually fully ready to be deployed, whether locally or in Azure.

## Deploy locally

Open Command Prompt and change your current directory to the one that was created when you created the Azure Functions project (the directory above the one containing the **\_\_init.py\_\_** file created in the last step).

You will need to create a Python virtual environment to work in and then activate, which is done as follows in Command Prompt

```
py -3.6 -m venv .env
.env\scripts\activate
```

For the final part to work, the deployment, you must have the Azure Functions Core Tools installed. If they are it should now simply be a case of running the command below to test the function locally

```
func host start
```

If successful you should see the following output to your Command Prompt window.

<img src="https://github.com/AndBooth/leeds-ds-meetup/blob/master/Misc/Images/azfunslocal1.PNG">

<img src="https://github.com/AndBooth/leeds-ds-meetup/blob/master/Misc/Images/azfunslocal2.PNG">

You can test a function by entering the URL in your browser. If you've used the HttpTrigger template function you'll want to enter something such as 

```
http://localhost:7071/api/newfunction?name=World
```
which should give you the response
```
Hello World!
```

# Deploy to the cloud

Now for the interesting bit! By deploying our function locally we've been able to test that it actually works, but now we want to deploy it to the cloud so that other people can use it. How do we do that?

## Create an Azure function app in Azure

The function app provides an environment for executing the function code and makes it easier to manage and deploy them as a unit. Within a function app you can have multiple individual functions.

To carry out these steps you will need to have the Azure CLI installed and an active Azure subscription. 

From the command line you will need to run the following set of commands.

If you have more than one Azure subscription that you can work with, set to the one that you want to deply to.

```
az account set -s <subscription_id>
```
Create a resource group under which you'll create the resources required to get you function deployed.
```
az group create --name myResourceGroup --location westeurope
```
You will need a storage account that stores information about your functions. Give a unique name `<storage_name>` and assign to your previously created resource group.
```
az storage account create --name <storage_name> --location westeurope --resource-group myResourceGroup --sku Standard_LRS
```

```
az functionapp create --resource-group myResourceGroup --os-type Linux \
--consumption-plan-location westeurope  --runtime python \
--name <app_name> --storage-account  <storage_name>
```


