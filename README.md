Description: 
This Python code is a simple GIS automation script that counts feature classes based on their geometry type—Point, Polyline, and Polygon within a specified geodatabase.
It is used in ArcGIS Desktop where ArcPy is available. This is applied for data management, quality control, database auditing, and project documentation to understand the spatial datasets without any delay. 
The script sets the workspace to a geodatabase, loops through all feature classes inside it, identifies each feature class’s geometry type using arcpy.Describe(), and increments a counter for each type. Finally, it prints the total number of point, polyline, and polygon feature classes in the geodatabase.

Output example:
Point: 5  
Polyline: 12  
Polygon: 8
