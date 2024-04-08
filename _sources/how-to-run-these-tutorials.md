# How to run these tutorials

The tutorials are in the form of [Jupyter notebooks](https://jupyter.org/). You will not need to install any software as there are a number of free cloud-based services to create, edit, run and export Jupyter notebooks such as these. At the top of each tutorial you will find links to a selection of such cloud-based services to run the tutorial. These may include the following:

|                               Binder                               |                                            Kaggle                                             |                                                  Colab                                                   |
| :----------------------------------------------------------------: | :-------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/) |
|      Binder may take some time to load, so please be patient!      |   Requires (free) registration with Kaggle. Once in, "switch on the internet" via settings    |   Requires Google account, and installation of some libraries, such as Cartopy `!pip install cartopy`    |

```{warning}
These free cloud-based services are not supported by ECMWF
```
##### Binder

1. Click on the Binder badge
2. Wait for the Binder environment to load.
3. Once loaded, navigate to the desired notebook and click on it to open and interact with it.

##### Kaggle

1. Click on the Kaggle badge
2. If you're not logged in to Kaggle, sign in or create a free account.
3. After signing in, you'll be redirected to the Kaggle notebook interface with the option to open the notebook. Click on it to proceed.

##### Colab

1. Click on the Colab badge
2. If prompted, sign in to your Google account.
3. Once signed in, the notebook will open in Google Colab. You can then interact with and run the notebook in the Colab environment.


#### WEKEO

[WEKEO](https://www.wekeo.eu/) is the EU Copernicus DIAS reference service for environmental data, virtual processing environments, and skilled user support. It is a platform for all audiences. This is our official platform for accessing the notebooks. You can access every notebook by clicking on the WEkEO link, which will redirect you to our official website. From there, you can open the notebook directly in JupyterHub. You need to be [signed up](https://www.wekeo.eu/register) to access the notebooks.

If you don't have Jupyter installed, here is a guide on how to install JupyterLab and open notebooks.

#### Run the notebooks locally
```{tip}
If you would like to run this notebook in your own environment, we suggest you install [Anaconda](https://docs.anaconda.com/anaconda/install/), which contains most of the libraries you will need. You will also need to install [Xarray](http://xarray.pydata.org/en/stable/) for working with multidimensional data in netcdf files, and the ADS API (`pip install cdsapi`) for downloading data programatically from the ADS.
```
In order to visualize and execute the notebooks, we recommend downloading JupyterLab, a a versatile web-based interactive development environment. You can see and play with our notebooks in that environment locally.

1. Download JupyterLab:
   1. Visit the JupyterLab website in your web browser.
   2. Go to the "Install" section and follow the instructions to download and install JupyterLab according to your operating system (Windows, macOS, or Linux).

2. Launch JupyterLab:
   1. After installing JupyterLab, open your terminal or command prompt.
   2. Type jupyter lab and press Enter to launch JupyterLab. This will start a local server and open JupyterLab in your default web browser.

3. Access JupyterLab Interface:
Once JupyterLab is launched, you will see the JupyterLab interface in your web browser. It consists of a file browser on the left and a main work area on the right.

4. Open a Notebook:
   1. You can download every notebook by clicking on the download button at the top of the webpage.
    2. Navigate to the directory where your notebook is located using the file browser on the left.
    3. Click on the notebook file (usually with a .ipynb extension) to open it in JupyterLab.
    4. The notebook will open in a new tab within the main work area of JupyterLab.

6. Interact with the Notebook:
You can now interact with the notebook by running code cells, editing text, and executing various commands.
To run a code cell, select it and either click the "Run" button in the toolbar or press Shift + Enter.
Explore the different features of JupyterLab to customize your workflow and make the most out of your notebook experience.


```{note}
These tutorials provide practical guides on how to work with atmospheric composition data. They can be run without need for installation, and can be fully adapted to suit your needs!
```
