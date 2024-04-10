# How to run these tutorials

The tutorials are in the form of [Jupyter notebooks](https://jupyter.org/). You will not need to install any software as there are a number of free cloud-based services to create, edit, run and export Jupyter notebooks such as these. At the top of each tutorial you will find links to a selection of such cloud-based services to run the tutorial. These may include the following:

|                               Binder                               |                                            Kaggle                                             |                                                  Colab                                                   |
| :----------------------------------------------------------------: | :-------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/) |
|      Binder may take some time to load, so please be patient!      |   Requires (free) registration with Kaggle. Once in, "switch on the internet" via settings    |   Requires Google account, and installation of some libraries, such as Cartopy `!pip install cartopy`    |

<hr>

#### WEKEO

[WEKEO](https://www.wekeo.eu/) is the EU Copernicus DIAS reference service for environmental data, virtual processing environments, and skilled user support. It is a platform for all audiences. This is our official platform for accessing the notebooks. You can access every notebook by clicking on the WEkEO link, which will redirect you to our official website. From there, you can open the notebook directly in JupyterHub. You need to be [signed up](https://www.wekeo.eu/register) to access the notebooks.

<hr>

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

<hr>

#### Run the notebooks locally

```{tip}
If you would like to run this notebook in your own environment, we suggest you install [Anaconda](https://docs.anaconda.com/anaconda/install/), which contains most of the libraries you will need. You will also need to install [Xarray](http://xarray.pydata.org/en/stable/) for working with multidimensional data in netcdf files, and the ADS API (`pip install cdsapi`) for downloading data programatically from the ADS.
```

To visualize and execute the notebooks, we recommend downloading [JupyterLab](https://jupyter.org/), a versatile web-based interactive development environment. You can interact with our notebooks in this environment locally.

1. **Download JupyterLab**:

   - Visit the [JupyterLab installation website](https://jupyter.org/install) in your web browser.
   - Navigate to the "Install" section and follow the instructions to download and install JupyterLab for your operating system (Windows, macOS, or Linux).

   ![Jupyter Lab install screenshot](jupyter-lab-install.png)

2. **Launch JupyterLab**:

   - After installing JupyterLab, open your terminal or command prompt.
   - Type `jupyter lab` and press Enter to launch JupyterLab. This will start a local server and open JupyterLab in your default web browser.

3. **Access JupyterLab Interface**:

   - Once JupyterLab is launched, you will see the JupyterLab interface in your web browser. It consists of a file browser on the left and a main work area on the right.

   ![Jupyter Lab Interface](jupyter-lab-interface.png)

4. **Open a Notebook**:

   - You can download every notebook by clicking on the download button at the top of the webpage.
   - Navigate to the directory where your notebook is located using the file browser on the left.
   - Click on the notebook file (usually with a `.ipynb` extension) to open it in JupyterLab.
   - The notebook will open in a new tab within the main work area of JupyterLab.

5. **Interact with the Notebook**:
   - You can now interact with the notebook by running code cells, editing text, and executing various commands.
   - To run a code cell, select it and either click the "Run" button in the toolbar or press Shift + Enter.
   - Explore the different features of JupyterLab to customize your workflow and make the most out of your notebook experience.

```{note}
These tutorials provide practical guides on how to work with atmospheric composition data. They can be run without need for installation, and can be fully adapted to suit your needs!
```
