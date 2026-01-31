Description: 
These Python codes are simple GIS automation script that is used on features, feature classes based on their geometry type and different name within a specified geodatabase.
It is used in ArcGIS Desktop and ArcGIS Pro where ArcPy is available. Applied for data management, quality control, database auditing, and project documentation to understand and varify the spatial database without any delay. 


  Count Feature classes according to their type, Output example:
Point: 5  
Polyline: 12  
Polygon: 8


  Count Feature classes according to their name, Output example:
Feature classes ending with _PG: 9
Feature classes ending with _MG: 9
Feature classes ending with _NG: 9
Feature classes ending with _SG: 3
Feature classes ending with _LG: 9


  Count Total Feature Classes and List, Expected Output and Example: 
Counts the feature classes and list all of them stored within a specified geodatabase. The output shows the total number of feature classes followed by a list of their names as text in the same kernel. 

Total feature classes: 4

DHA_KIS_BHA_001_001_RS_LG
DHA_KIS_BHA_001_001_RS_MG
DHA_KIS_BHA_001_001_RS_NG
DHA_KIS_BHA_001_001_RS_PG


  Count features in a feature class, Expected Output and Example:
The script lists all feature classes in it, and prints each feature class name along with the number of features it contains.

DHA_KIS_BHA_001_005_RS_LG 8780
DHA_KIS_BHA_001_005_RS_MG 2981
DHA_KIS_BHA_001_005_RS_NG 2981


  Difference between 2 same type feature class, Output Example:
Values only in FeatureClass_1:
888881
Values only in FeatureClass_2:
889500 


  Import feature classes with the same name to another gdb, Expected Output and Example:
Identifies the feature classes ending with "_MG" within an input file geodatabase and copy them directly into a newly created output geodatabase. Alongside, it connects the data to the ArcMap/MXD being used to run the code and if the gdb is not created earlier, then it would create one.  

Copied: DHA_KIS_BHA_001_001_RS_MG
Copied: DHA_KIS_BHA_001_002_RS_MG
Done.


  Rename Feature Classes, Expected Outpu and Example: 
Identifies the feature classes ending with _LD, _MD, _ND, _PD, _SD, within an input file geodatabase and rename them directly into the same geodatabase according to _LG, _MG, _NG, _PG, _SG.

Renamed: DHA_TAN_MIR_045_000_RS_LD -> DHA_TAN_MIR_045_000_RS_LG
Renamed: DHA_TAN_MIR_045_000_RS_MD -> DHA_TAN_MIR_045_000_RS_MG
Renamed: DHA_TAN_MIR_045_000_RS_ND -> DHA_TAN_MIR_045_000_RS_NG
Renamed: DHA_TAN_MIR_045_000_RS_PD -> DHA_TAN_MIR_045_000_RS_PG
Renamed: DHA_TAN_MIR_045_000_RS_SD -> DHA_TAN_MIR_045_000_RS_SG
Done.







