# OverWatch
Project OverviewThis project is a tracking pipeline that processes data from an external XML source and displays it on an HTML dashboard.

Data Source (satellite_feed.xml): An XML file simulating location and biometric metrics sent from field transceivers via satellite relay.

Backend Engine (app.py): A Python Flask application that reads the local XML file, parses the elements, and exposes the structured data as a JSON API endpoint.

Overwatch Console (templates/index.html): A monospace HTML interface that queries the JSON endpoint every 3000ms using the JavaScript Fetch API to update asset positions without a page refresh.

The application serves as a full-stack data pipeline (XML $\rightarrow$ JSON $\rightarrow$ HTML DOM) built with Python and Vanilla JavaScript inside a uv managed environment.
