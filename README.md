# Simple Machine Learning Project 
![image info](./frontend/src/Images/image.png)

### Requirements:
* Python3 
* Node.JS
* Pipenv 
* npm 

## Frameworks and packages used

- [Material-UI](https://material-ui.com/)
- [react-bootstrap](https://react-bootstrap.github.io/getting-started/introduction/)
- [react-carbon-component](https://carbon-components-svelte.onrender.com)
- [react-router-dom][https://v5.reactrouter.com/web/guides/quick-start]
- ... and more!

# How clone and start the code 
## Software Requirements

- <b>Python3</b>: Click [Here](https://www.python.org/downloads/) to download Python
- <b>Node.js</b>: Click [Here](https://nodejs.org/en/download/) to download node.js

# Windows Setup Guide
1. <b>Search 'Power Shell' in search box, and open the Power Shell. </b>
2. cd \Desktop\
2. git clone https://github.com/Sameam/machine_learning
3. cd .\machine_learning
4. pip install --upgrade pip
5. python -m venv venv
6. Set-ExecutionPolicy Unrestricted -Scope Process
7. venv\Scripts\activate
8. cd .\backend
9. pip install -r .\Python_File\requirements.txt
10. flask run 
11. open another new terminal, change directory to .\frontend
12. npm install
13. npm start **(This will start the web run on your Machine Local Host)**

# MacOS Setup Guide
1. <b>Hold 'command + space' and search for 'Terminal', and open the Terminal </b>
2. cd ~/Desktop
3. git clone https://github.com/Sameam/machine_learning
4. cd ./machine_learning
5. pip3 install --upgrade pip3
6. python3 -m venv venv 
7. source venv/bin/activate
8. cd ./backend
9. pip3 install -r ./Python_File/requirements.txt
10. flask run 
11. open another new terminal, change directory to ./frontend
12. npm install
13. npm start **(This will start the web run on your Machine Local Host)**

# Linux Setup Guide
1. <b>Open the Terminal </b>
2. cd ~/Desktop
3. git clone https://github.com/Sameam/machine_learning 
4. cd machine_learning 
**Step 4 and 5 is needed if you Linux system is not update with the newest package yet**

5. sudo apt-get update
6. sudo apt-get upgrade
7. sudo apt-get install python3.8
8. pip3 install --upgrade pip3
9. python3 -m venv venv 
10. source venv/bin/activate
11. cd ./backend
12. pip3 install -r ./Python_File/requirements.txt
13. flask run 
11. open another new terminal, change directory to ./frontend
12. sudo apt install nodejs
13. sudo apt install npm
14. npm install
15. npm start **(This will start the web run on your Machine Local Host)**

# Future start after follow the step above 
**Make sure you are in machine_learning directory**
1. cd ./backend
2. flask run
3. open another terminal 
4. cd ./frontend
5. npm start
