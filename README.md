# POWERPLANT CODING CHALLENGE SOLUTION
https://github.com/gem-spaas/powerplant-coding-challenge

## CONSIDERATIONS 

This repository includes a complete development environment based on Docker, the objective of it is to eliminate any setup problem of the project whatever the complexity that can reach, deploying both the contributed code of the solution and any service that the developer may need in The performance of your work.



### REQUIREMENTS
To operate the development environment you will only need to have a functional Docker and Docker-Compose in your system and nothing else!

Whatever your host operating system, you will find various installation mechanisms that may give good result.

In addition your host system must have the ability to run SHELL scripts that will provide you with the use of this environment. In most cases Linux-based operating systems, and Mac do not have an inconvenience for this, in the case of Windows we strongly recommend the use of WSDL2 with what you will not have any problem.

### How use a full Docker Development Environment (recomended)

In the BIN directory you will find a series of scripts that will provide you with the operation of this environment.


#### make migrate operations and admin user creation (only need a first time)
> ./bin/install 

para construir o reconstruir las imagenes necesarias, esto solo es requerido la primera vez, aunque puedes usar este script para regenerar las imagenes cuando te interese.
#### clean context, launch all services and connect to log output. ( allways before coding)

> ./bin/start 

#### hard clean containers context

> ./bin/cleanup

#### reconect to log output

> ./bin/logs

#### create and access to container shell for check and made pip or phyton operations

> ./bin/utils


### Using native python install 


if you dont use a full docker environment, inside source folder you can access to native source code for deploy using your local hosted python resources.

access to api folder

> pip install --no-cache-dir -r requirements.txt
> python manage.py runserver



### INCLUDED SERVICES

#### API

Built with Django using Django-Rest-Framework, logic has been divided into a REST resource architecture, which you will find in the "Services" folder, within which each resource handles its own routes, views, and serializers,

The development environment displays a container with this service called Django-API, this is exposed in port 8000 of your host machine

The development environment detects the changes produced in the code by performing the necessary operations so that it is not necessary to restart the service

Business logic and calculation engines are segregated from REST architecture in the "Logic" folder organized by thematic blocks

> http://localhost:8000


##### resources and endpoints

http://localhost:8000/productionplan/ [POST]