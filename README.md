
# SpaceX Launch Program

If taking about the project, i have created this  as a coding assigment by TechDome. 

This project will list the all the Space program from 2007 to 2020 by SpaceX.It has different filters on sidebar where user can filter the data based on particular year, successfull launch and successfull land.
# Methodology

I used flask framework to do this project. Along with html and js to make page responsive and to prevent it from reload when filter applied.

It is using python 3.11.0 version.

Initially, when we start the project, the home page container the combination of various program by SpaceX without filter. Page is render from flask server at server side with url('/').

Whenver, any filter will apply, i have added 'onclick(fun())' method which is define in <script> function fun(){}</script>.

It will access the button value and send post request to flask server using  XMLHttpRequest()  with given button value.

XMLHttpRequest helps to update the webpage content without reload the site.
Server will send api request to given api link by Techdom with filter.

Server will return data into json formate. First, screen_container.innerHtml=''.

Then creating new Elements using javascript and appending new child to it with updated data sent by server.





## NOTE

As flask server is sending json file of data, i am updating the url to filter value, like (Filter_by_year_2007 or filter_by_launch_true).

These urls are define at server site which return json data as we hit request. I am using javascript to display json data into html. 

So, if you direct run browser url, it will send request to server which returns json data and you will see json data instead of webpage.

So, to avoid this say at default url and navigate using given filter button. 


## API Reference

#### Get all items

```http
https://api.spaceXdata.com/v3/lau
nches?limit=100
```

#### Launch Success Filter: 

```http
https://api.spaceXdata.com/v3/launches?limit=100&launch_success=true
```


#### Launch Success Filter: 
```http
https://api.spaceXdata.com/v3/launches?limit=100&launch_success=true&lan
d_success=true
```
#### Filter by year: 
```http
https://api.spaceXdata.com/v3/launches?limit=100&launch_success=true&lan
d_success=true&launch_year=2014
```



## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Open it with any IDE and run command in cmd

```bash
  python app.py
```



## Features

- Fully responsive as descriped in Assginment Problem 
- 1 Column view for mobile
- 2 column view for tablate
- 4 column view for desktop
- No reload when filter will be applied.

