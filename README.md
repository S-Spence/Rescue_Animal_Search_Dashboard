<h1>Rescue Animal Search Dashboard</h1>

This application generates a user dashboard for Grazioso Salvare’s users to search for rescue animals 
based on the rescue type. Grazioso Salvare trains dogs for three rescue types, water, mountain, and disaster. Certain breeds, genders, and ages are better for each rescue type. 
The table below describes the characteristics of dogs that train for each rescue type.
</br>
<img src="README_Images/Breeds_Table.png" width="400" height="400", class="center" />
</br>
The user dashboard contains a table that allows users to filter rescue animals by their compatible rescue type. 
The dashboard also includes a geolocation chart and a pie chart to update dynamically with filter options. 
The screencasts below provides a demonstration of the dashboard’s filter options.
</br>
<img src="Dashboard_Screencast_Part1.gif" width="800" height="400" />
<img src="Dashboard_Screencast_Part2.gif" width="800" height="400" />
</br>
<h2>Motivation</h2>
The project exists to simplify searching for rescue animals. Non-technical users can easily query the mongo database for rescue dogs. 
The widgets show the percentage of rescue dogs belonging to each breed. The geolocation chart shows the dog’s name and location. 
The user dashboard allows users to quickly find trained rescue animals for water, mountain, and disaster rescue. 
</br>
<h2>Tools and Installation</h2>
Tools and Installation

Install MongoDB if the database is not running. The database will not be continuously running since this is a school project. 
A non-relational database was great for this project to allow Grazioso Salvare to change the data type associated with animal information. 
Non-relational databases also enhance search performance (MongoDB, 2021). MongoDB will also enable scalability as the business grows. 
MongoDB was a good option for use with Python due to the pymongo module discussed below. 
</br>
1. <a href="1.	Install MongoDB at https://docs.mongodb.com/manual/installation/ ">Install MongoDB</a>
</br>
Next, install dash dependencies. Dash is an open-source Python framework used primarily for building analytical web applications (Tutorialpoint, 2021). Dash was a powerful, user-friendly option for developing this data-driven application. Dash enabled the development of data visualizations and interactivity in Grazioso Salvare’s dashboard. 
</br>
2. Install Dash and its dependencies with the following commands:
<ul>
  <li><code>pip install dash</code></li>
  <li><code>pip install jupyter-dash</code></li>
  <li><code>pip install jupyter-plotly-dash</code></li>
  <li><code>pip install dash-leaflet</code></li>
  <li><code>pip install pandas</code></li>
</ul>  
</body>
</html>
</br>
Next, install pymongo. The pymongo module provides user-friendly compatibility between Python and MongoDB. 
The pymongo module allows users to establish database connections, work with collections and documents, work with encryption, and manipulate MongoDB cursor objects.
</br>
3. <code>pip install pymongo</code>
</br>
Finally, install jupyter to load and execute jupyter notebooks. 
</br>
4. <code>pip install jupyterlab</code> 
