# Asbuilt_Trax
A simplified prototype for an as-built tracking database with API

The purpose of this project is to:
  1) Model a database that tracks construction as-builts, GIS contributers, GIS data, and construction crew leaders all in one place
  2) Publish an API that provides access to that data
  3) Use Jupyter Notebook to analyze and visualize the data


  
## API Reference:

| Endpoint path | Method | Parameter | Description |
| ------------- | ------ | --------- | ----------- |
| http://localhost:5000/asbuilts/[ID] | GET | asbuilt.ID | Returns data for specified as-built |
| http://localhost:5000/asbuilts/[ID] | PUT | asbuilt.ID | Updates specified as-built |
| http://localhost:5000/asbuilts | GET | None | Returns data for all as-builts |
| http://localhost:5000/asbuilts | POST | (JSON) gis_user_id, work_order, crew_leader_id, install_date | Creates new record in asbuilts table |
| http://localhost:5000/asbuilts/[ID] | DELETE | asbuilt.ID | Deletes specified as-built record |


## Project evolution
Asbuilt_Trax began as a way to practice PostgreSQL database design, construction, and maintenance by implementing a simplified records management database based on a utilities mapping workflow. What it provides is a solution to the problem of being able to lookup and manage records in an efficient way, leveraging the power of a database to serve the data up via API, and visualize the data in using Jupyter Notebook.

## ORM
With a reasonable footing in SQL, I chose to build the API with Flask-SQLAlchemy in order to practice using the ORM and the framework it provides.

## Future devlopments
Currently the API only provides for basic query and post/ delete operations. So I am looking forward to expanding those capabilities to return more comprehensive data from the database, including GIS records, creating and updating user tables, and SQL triggers to automate data management. I'd also like to implement more data visualization tools in the associated Jupyter Notebook.
