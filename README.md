# MassMutual Data Viz Recruitment

This project is intended to evaluate MassMutual data visualization engineering candidates. The project contains three sub-projects. Each sub-project provides a starting point for using python, R or web, to build data visualizations.

## Instructions

Your goal, as a data visualization engineering candidate, is to build interesting data visualizations for a target audience of an insurance agent or marketing manager. These visualizations should enable these users to locate and understand potential new markets or customers for the purpose of selling life insurance.

The visualizations you construct should reveal insights about the data and follow visualization best practices. Best practices include presenting multivariate data, enabling comparisons, and providing descriptive titles and labels.

You will recieve points for every visualization you construct. For instance, every python or R chart you create you will recieve 1 point and for every web visualization you create you will recieve 3 points. Finally, you will recieve an extra 2 points for each different technology you use.

Please feel free to contact the recruiter if you have any questions.

### Point Breakdown
* R visualization +1
* Python visualization +1
* Web visualization +3
* Use only R +2
* or use R and Python +4
* or use R, Python and Web +6


## Getting Started

Make sure python is installed on your system:
`python --version`

If not, you can download python here:
(https://www.python.org/downloads/)

Make sure R is installed on your system, if not, you can download R here:
(https://cran.r-project.org/mirrors.html)

Install the python tool **virtualenv** in order to be able to set up a python virtual environment.
`pip install virtualenv`

## Data
This project contains an SQLite database, **recruit.db**. This database is pre-populated with data and should be utilized in each project to produce data visualizations.

### Data Dictionary
#### customer table
* id - primary key
* race_code - foreign key to race table
* education_id - foreign key to educaton table
* home_owner - Home Owner / Renter, O = Home Owner, R = Renter
* state - state location in the United States
* is_smoker - whether customer is a smoker, 1 = Yes
* is_exerciser - whether customer excercises, 1 = Yes
* has_insurance - Life Insurance Policy Owner, 1 = True
* income - Income By The Thousands
* travel_spending - Amount spent by customer on Travel
* sports_leisure_spending - Amount spent by customer on Sports & Leisure
* economic_stability - 01 = Most Likely Economically Stable, 30 = Least Likely Economically Stable
* insurance_segment_id - foreign key to insurance_segment table
* youtube_user_rank - Propensity to use YouTube, 01 (Most Likely) through 20 (Least Likely)
* facebook_user_rank - Propensity to use Facebook, 01 (Most Likely) through 20 (Least Likely)
* gender - M = Male, F = Female


## Project recruit-viz/python

Use python pandas and matplotlib to visualize data.

Start here: start.py

Create a python virtual environment for the **python** project:
`virtualenv venv`

Then set up the new virtual environment with the required dependancies:
`./venv/bin/pip install -r requirements.txt`

Run the python start file to verfiy everything is setup:
`./venv/bin/python start.py`

### Instructions
Use the start.py file as a starting place for building python data visualizatons driven by the data found in **recruit.db**.


## Project recruit-viz/R

Use R dataframes and ggplot to visualize data.

Start here: start.R

### Instructions
Use the start.R file as a starting place for building R data visualizatons driven by the data found in **recruit.db**.


## Project recruit-viz/web

Use a python Flask rest api and the D3.js JavaScript library to visualize data.

Start here: start.py

### Setup
Create a python virtual environment for the **web** project:
`virtualenv venv`

Then set up the new virtual environment with the required dependancies:
`./venv/bin/pip install -r requirements.txt`

Start the web application:
`./venv/bin/python start.py`

### Instructions
Use the start.py file and templates/index.html as a starting place for building web based data visualizatons driven by the data found in **recruit.db**.

# recruit-viz-prj
