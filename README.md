# Team 74, Don't React

## Problem Statement
Building a mentor-mentee matching mechanism for high school students to engage in peer-to-peer learning. CLAYLAB is looking for a flexible online platform that can fulfill the mentee's requirements. Career choices, gender preferences, interests, geography, and language are all factors taken into account when pairing a mentor and mentee. 

## Solution
We built an intuitive web application which allows mentors and mentees to sign up year round while integrating that data which is passed to a custom built machine learning model to predict and assign the most suitable mentor for a mentee in the most optimised manner keeping into consideration the requirements of each individual mentee. 

## Tech Stack
* React
* Python
* Flask
* SQLite

## Working
We have developed different routes for the sign up and the login page with the help of API's using Flask and routing through ReactJS. The match making algorithm is based on the content based filtering. The database is present inside the models and all routes are present in the resources.

##### The code ("Code") in this repository was created solely by the student teams during a coding competition hosted by JPMorgan Chase Bank, N.A. ("JPMC").						JPMC did not create or contribute to the development of the Code.  This Code is provided AS IS and JPMC makes no warranty of any kind, express or implied, as to the Code,						including but not limited to, merchantability, satisfactory quality, non-infringement, title or fitness for a particular purpose or use.