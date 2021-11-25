# DDW 2D Bonus Submission 
SC05 Group 6- Chirag Shivakumar, Ethan Pang, Lin Xi, Nicole Shuan, Nguyen Bao Long Tran

## Setup

### Install Git

You need to have Git to do the project. Download and install the software according to your OS:
- Windows: [Git for Windows](https://git-scm.com/download/win)
- Mac OS: [Git for MacOS](https://git-scm.com/download/mac)

### Downloading Repository
Clone the mini project repository from Github. On your terminal or Git Bash, type the following:

```shell
$ cd Downloads
$ git clone https://github.com/chiragshiva99/DDW_2d_bonus.git 
```

### Go to ddw-2d-bonus Folder

Once you have downloaded the repository, you can go to the repository and to the folder called `DDW_2d_bonus` for this mini project.

```shell
$ cd DDW_2d_bonus
$ ls
```

The last command should output the following:

```shell
app
application.py
config.py
requirements.txt
```

## Create Virtual Environment (Windows)

**You should open Anaconda Prompt to do the following steps.**

In the following steps, the Windows prompt will be represented by:
```shell
>
```
Go to the root folder `DDW_2d_bonus`.
```shell
> cd %USERPROFILE%\Downloads\DDW_2d_bonus
```
From the root folder, i.e. `DDW_2d_bonus`, create virtual environment called `virtenv`.

```shell
> python -m venv virtenv
```

A folder called `virtenv` will be created. Now, activate the virtual environment.
```shell
> virtenv\Scripts\activate
```

You should see the word `virtenv` in your prompt something like:
```shell
(virtenv) folder>
```

_To exit the virtual environment at the end of this mini project, simply type:_
```shell
> deactivate
```

## Create Virtual Environment (MacOS/Linux)


In the following steps, the MacOS/Linux prompt will be represented by:
```shell
$
```

Go to the root folder `DDW_2d_bonus`. 
```shell
$ cd ~/Downloads/DDW_2d_bonus
```

From the root folder, i.e. `DDW_2d_bonus`, create virtual environment called `virtenv`.

```shell
$ python -m venv virtenv
```

A folder called `virtenv` will be created. Now, activate the virtual environment. 

```shell
$ source virtenv/bin/activate
```

You should see the word `virtenv` in your prompt something like:
```shell
(virtenv) user$
```

_To exit the virtual environment at the end of this mini project, simply type:_
```shell
$ deactivate
```
## Combined (Windows/Mac/Linux)

### Install Python Packages

Install the necessary packages for this mini project. From the root folder, i.e. `DDW_2d_bonus`, type the following:

For Windows:
```shell
> python -m pip install -U --force-reinstall -r requirements.txt
```

For MacOS/Linux: (For Linux, you might need to type pip3 instead)
```shell
$ python -m pip install -U --force-reinstall -r requirements.txt
```

### Brief Overview of Project Structure
Templates- Home, About, Task-1, Task-2

### Run Flask

Now you are ready to run your web app in your local computer. 
You should see `application.py` in this root folder. 

#### Vocareum
If you use Vocareum terminal to run your Flask application, you can do so by running the `runflaskvoc.sh` script. Before running this script, make sure the `voc=True` is set true in the following line inside `DDW_2d_bonus/app/__init__.py`.

```python
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=True)
```

Now, make sure you are inside the `DDW_2d_bonus` folder  by using the `pwd` command. 

```shell
> pwd
```

Use `ls` to ensure that you see the `runflaskvoc.sh` in the current folder.

```shell
> ls
```

Make sure that the script is executable by running the following command. 

```shell
> chmod a+x ./runflaskvoc.sh
```
The above script is to change the file to be executable for all users, group and owner.

To run the script, type the following.

```shell
> ./runflaskvoc.sh
```

Once it is running, you can open another tab in your browser and type the following url: [`https://myserver.vocareum.com/`](https://myserver.vocareum.com/).

To stop the web app type `CTRL+C`. 

#### Local Computer

If you are using your own computer, make sure to change the flag `voc=False` in the following line inside `DDW_2d_bonus/app/__init__.py`.

```python
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=False)
```

Now, you can run Flask by typing:

```shell
> flask run
```

You should see that some output will be thrown out, which one of them would be:

```shell
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
To stop the web app type `CTRL+C`. 

### Home.html - Overview of Design Thinking Project 3
### About.html - Content from our HASS Presentation (Has Covid 19 divided society?)
### Task-1.html- Data for Model 1
DDW and MU Task 1- Input Data for Population Density (100 - 500), Human Development Index (0.85 - 0.99) and Monthly Cases (100 - 30,000)
![](https://www.dropbox.com/sh/3wbod28ze5n6gtn/AABap0Bp56PHXeD_sHJWwePpa?dl=0)
![]()
![]()

### Task-2.html- Data for Model 2
Input Data for Mental Illness Percentage (1 - 100), Number of Fast food restaurants per 100 000 people (1 - 100) and Hypertension Percentage (1 - 100)
![]()
![]()
![]()
