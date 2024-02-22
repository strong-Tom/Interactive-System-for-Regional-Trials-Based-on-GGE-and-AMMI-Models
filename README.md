# Interactive-System-for-Regional-Trials-Based-on-GGE-and-AMMI-Models
Convenient for agricultural experts to use GGE and AMMI models more conveniently

The online website for this project is:
http://175.24.133.23/

You can register and log in, or you can directly use existing account and password to log in:

Account: zhuyiqi842@qq.com

Password: zhuyiqi0409

## General introduction
The front-end of this project is completed using Vue and the back-end is completed using DJango.The Python version is 3.7.9, and the Yarn version is 1.22.19，django version is 3.2.12，node version is v16.14.0，pip version is 23.0.

The command for running the Vue project on the front-end is:
```
yarn serve
```
The command for running the django project on the backend is:
```
python manage.py runserver
```
The project includes the requirement file, which contains the required Python package dependencies. The command to install the Python package dependencies for the project using pip is:
```
pip install -r requirements.txt
```
The dependent commands for installing the Vue project using Yarn are:
```
yarn install
```
Install the specified version node:
```
nvm install 16.14.0
```
Use the specified version node:
```
nvm use 16.14.0
```

## Function screenshot
This includes the AMMI model, GGE model, and scatter plot,as shown in the following figure.Users can change various data in the panel according to their preferences.
![image](https://github.com/strong-Tom/Interactive-System-for-Regional-Trials-Based-on-GGE-and-AMMI-Models/assets/54710966/8f4e60c7-9ae6-4bec-9148-8a1cb71ddce0)

![image](https://github.com/strong-Tom/Interactive-System-for-Regional-Trials-Based-on-GGE-and-AMMI-Models/assets/54710966/008fe9e0-e308-44ea-8f78-3ed987be14dd)

![image](https://github.com/strong-Tom/Interactive-System-for-Regional-Trials-Based-on-GGE-and-AMMI-Models/assets/54710966/be59eb9a-03e9-4502-9ece-ca07c919e865)

## Data Format Example
Users can directly download sample data to verify the effect,Or preview the effect of online data onlineas shown in the following figure.

![image](https://github.com/strong-Tom/Interactive-System-for-Regional-Trials-Based-on-GGE-and-AMMI-Models/assets/54710966/27094d64-97d2-491a-a15a-c14cfcf08357)

You can also upload data themselves to verify the effect. If you want to upload data for use, the format of the data is shown in the following figure. Rows represent different varieties, columns represent different locations, and row names are optional. Column names need to be specified to distinguish different locations. The GGE model and AMMI model both use this format of data.

![image](https://github.com/strong-Tom/Interactive-System-for-Regional-Trials-Based-on-GGE-and-AMMI-Models/assets/54710966/3ee4696a-8d2f-4ed2-ae09-eca90ebb8e5f)

The scatter plot function can view the growth of samples of different tree species in different regions. The sample data that needs to be uploaded is shown in the following figure. Users need to upload the location label, variety label, as well as the height and diameter of the sample.

![image](https://github.com/strong-Tom/Interactive-System-for-Regional-Trials-Based-on-GGE-and-AMMI-Models/assets/54710966/e88a44bf-7213-4c93-8b6f-7017b6783de7)

