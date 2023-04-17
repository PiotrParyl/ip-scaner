# Server Menager

-----------------------------------------------------------
## Table of contents
* [About Project](#about-project)
* [Set up](#set-up)
* [Technologies](#technologies)
* [Docker](#docker)

-----------------------------------------------------------
# About Project

The task of the project is to monitor the activity of remote servers. If any stops working we will get information which one and at what time on SMS and email. The project may seem simple but it is the first in which I used (or at least there was such an attempt) OOP (the objects are servers in this case). This is a very early version, and not exact. Rather, the goal is to collect some specific feedback on how to create such projects, create a repo, probably a component, mainly how to improve to make it better !!! 

The general principle of the program at the moment is as follows. At the entrance we give the IP addresses of our servers. After adding servers, we have a small preview of what servers we added and if they are online/offline. After firing "monitoring" the program runs in the background (so we can, for example: go back to the main menu and scan the LAN for ourselves :) addition for fun)

The next step will be to create a user account so that our servers are saved in the DB. Now anyone will be able to download the program, register and monitor the added servers :) 

An interesting addition will be the ability to write with other users from within the program hmm . .

-----------------------------------------------------------
# Set up

Before running the program, you need to install the necessary libraries, they can be found in requaierments.txt files. To install the package you should:
``` pip install -r requirements.txt ```

After installing the packages, you can run up the program: 
```python main.py```

## Technologies
-----------------------------------------------------------
Technologies Used
The following technologies have been used in this project:

* Python 3
* MySQL database
* Linux Ubuntu OS
* AWS



## Docker
-- Not Ready Yet --

























