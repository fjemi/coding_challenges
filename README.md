# Password Generator
A Pyhon script that generates a random password of a defined length and 
character type.


## Usage
### Script/CL
Run the following commands to execute the script
```
$ git clone https://github.com/fjemi/$ python_password_generator.git 
passwordgenerator
$ cd passwordgenerator
$ python password_generator.py <length> "[<character_types>]"
```
where length is a positive ```integer``` and ```character_types``` can be a 
combination of ```'number'```, ```'lowercase'```, ```'uppercase'```, or 
```'special'```.

## Docker Image
Run the following commands to build and run a docker image of the script
```
$ docker build -t passwordgenerator .
$sudo docker run --rm passwordgenerator -l '<length>' -c "[<character_types>]"
```


## Tech Stack
[Python](https://pyhon.org)

[Docker](https://docker.com)
