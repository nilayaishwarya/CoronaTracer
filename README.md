# CoronaTracer
This is a web platform to track COVID Cases in India and also provide a robust approach to track symptoms in localities and generating health risk scoring.

This application get's user feedback on symptops, past disease history, local history, travel history and more to determine personal risk factor.
This individual factor with location is pooled to generate locality risk factor.
Presently provide- Symtomatic health index, Past-Disease risk factor, Inventory Preparedness Index

Along with this the plaform also provides a continous self updating tracking of active, total, recovered and deceased cases in India across all states and cities.

Check out the LIVE VERSION:
https://coronatracer.pythonanywhere.com/Dashboard

Tech Stack used:

---DASHBOARD---
UI(Frontend) - HTML, CSS, JS, JS Addons- Interactive Chart and Tables
Backend - Flask(Py), Apscheduler, MongoDB client
Analytics -  Numpy, Pandas, Seaborn and more
DB - MongoDB cluster

---DATA COLLECTION---
Google form integrated to UI
-Service: Google App Script application to communicate with Mongo Stitch Service
-MongoDB Cluster through Mongo Stitch Service


