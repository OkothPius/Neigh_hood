# Neigh_Hood

A web application that allows you to be in the loop about everything happening in your neighborhood.

### Prerequisites

What things you need to install the software and how to install them

```
sudo apt-get install python3.6.
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
pip install virtualenv
```

Then activate

```
source virtual/bin/activate
```
Install pip

```
sudo apt install python3-pip
```

```
pip install django==1.11
```

```
cd to the dir you cloned the repository
```

## Bugs
 I got the following bugs during deployment

 * The vote button failed to function after deployment
 * The site responsiveness in small devices also failed


## Deployment

In order to deploy the following files must be created assuming you have set heroku:

* Add a `procfile` in the project root.
* Add `requirement.txt` file with all the requirements in the project root;
* Add `Gunicorn` to `requirements.txt`;
* A `runtime.txt` to specify the correct Python version in the project root;
* Configure `whitenoise` to serve static files.


## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Python3.6](https://docs.python.org/3/) - Dependency Language
* [Postgres](https://www.postgresql.org/docs/10/tutorial-inheritance.html) - Used to store data
* [Heroku](https://devcenter.heroku.com/categories/reference) - To deploy the application
* [API](https://moringaschool.instructure.com/courses/20/pages/monday-restful-api?module_item_id=350) - To allow users use my data


## Authors

* **Oruko Pius** 


## License

This project is licensed under the MIT License - see the [license.md](license.md) file for details

## Acknowledgments

* Used LMS for the sole reference
* StackOverflow
