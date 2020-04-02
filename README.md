# ReadyRecipe
## Web App Development 2 - University of Glasgow
- Team: Lab 1 Team D
- Andreas Vrachimis, George Flouris, Kai Hu
## Instructions to run locally:
- Download the repository
- Download and install pip. Version 19.3.1 was used for this web application.
- Create and activate the virtual enviroment 
> conda create -n rango python=3.7.2 <br>
> conda activate rango
- Install all the packages required in the requirements.txt
> pip install -r requirements.txt
- Apply migrations
> python manage.py makemigrations <br>
> python manage.py migrate
- Create objects
>python population_script.py
- Run the server
>python manage.py runserver
