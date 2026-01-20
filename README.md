Description: 
These Python codes are simple GIS automation script that is used to count features, feature classes based on their geometry type and different name within a specified geodatabase.
It is used in ArcGIS Desktop and ArcGIS Pro where ArcPy is available. Applied for data management, quality control, database auditing, and project documentation to understand and varify the spatial database without any delay. 


  Count layer, Output example:
Point: 5  
Polyline: 12  
Polygon: 8


  Count Feature Class, Output example:
Total number of feature classes: 39
Feature classes:
DHA_KIS_BHA_001_009_RS_PG
DHA_KIS_BHA_001_001_RS_LG
DHA_KIS_BHA_001_001_RS_MG
DHA_KIS_BHA_001_001_RS_NG


  Count Layer according to trair name, Output example:
Feature classes ending with _PG: 9
Feature classes ending with _MG: 9
Feature classes ending with _NG: 9
Feature classes ending with _SG: 3
Feature classes ending with _LG: 9


  Count total features a feature class, Output example:

DHA_KIS_BHA_001_003_RS_SG 8
DHA_KIS_BHA_002_001_RS_LG 15
DHA_KIS_BHA_010_004_RS_PG 3


  Difference between 2 same type feature class, Output example:
Values only in FeatureClass_1:
888881
Values only in FeatureClass_2:
889500 


  Import feature classes with the same name to another gdb, Expected Output and Example:
Identifies the feature classes ending with "_MG" within an input file geodatabase and copy them directly into a newly created output geodatabase. Alongside, it connects the data to the ArcMap/MXD being used to run the code and if the gdb is not created earlier, then it would create one.  

Copied: DHA_KIS_BHA_001_001_RS_MG
Copied: DHA_KIS_BHA_001_002_RS_MG
Done.


