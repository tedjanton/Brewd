<!-- ABOUT THE PROJECT -->
## About The Project

[Click here to view Brewd live on the web!](https://brewd-app.herokuapp.com/)
<br>
</br>


### Built With

* [JavaScript]()
* [Python]()
* [React]()
* [Redux]()
* [Flask]()
* [SQLAlchemy]()
* [Docker]()
* [CSS]()



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Here is everything we need you to do to get started with Brewd.

  * npm
  ```sh
  npm install npm@latest -g
  ```
  * pipenv
  ```
  pipenv install 
  ```
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/tedjanton/Brewd
   ```
2. Install NPM packages in the React App
   ```sh
   npm install
   ```
3. Install Dependencies
   ```bash
   pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
   ```
      
4. Add a '.env' with your environment variables to the root of your local directory

5. Create a postgreSQL user
    ```sh
    CREATE USERS <<your username>> WITH PASSWORD <<your password>> CREATEDB
    ```
6. Create your database
    ```sh
   CREATE DATABASE <<database name>> WITH OWNER <<your username>>
    ```
7. Start a pipenv virtual environment
   ```bash
   pipenv shell
   ```
8. Migrate and seed your database
    ```sh
    flask db migrate
    ```
    ```bash
   flask db upgrade
   ```
   ```bash
   flask seed all
   ```
   ```bash
   flask run
   ```
9. Start your local development server in the React App
   ```bash
   npm start
   ```
## Obstacles

### SQLAlchemy Querying

We ran into issues when trying to query our database because of interdependent relationships. We had to define specific relationships between tables, and create new methods that allowed us to return information pertaining to multiple tables without running into major conflicts. 


### Likes

We had issues with React updating and rendering the state of a like without refreshing our entire page. Through hours of debugging and collaboration, we realized we overcomplicated the issue from the start. 


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/tedjanton/Brewd/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact & Acknowledgements

* Ted Anton - [LinkedIn](https://www.linkedin.com/in/ted-anton/) - [GitHub](https://github.com/tedjanton)
* Olivia Young - [LinkedIn](https://www.linkedin.com/in/olivia-young-2437ba1b9/) - [GitHub](https://github.com/olivianicole)
* Lauren Chambers - [LinkedIn] (https://www.linkedin.com/in/lauren-chambers94/) - [Github] (https://github.com/laurenchambers)
* Rajiv Hudek - [LinkedIn] (https://www.linkedin.com/in/raj-hudek-026b051b1/) - [Github] (https://github.com/LifeJunkieRaj)

Project Link: [https://github.com/tedjanton/Brewd](https://github.com/tedjanton/Brewd)


<!-- ACKNOWLEDGEMENTS -->
