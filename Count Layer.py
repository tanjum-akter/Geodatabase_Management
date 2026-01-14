import arcpy
arcpy.env.workspace = r"D:\_TANJUM\Layer Count According to Type\Bhairab_Bazar.gdb"
counts = {"Point":0,"Polyline":0,"Polygon":0}
for fc in arcpy.ListFeatureClasses():
    t = arcpy.Describe(fc).shapeType
    if t in counts: counts[t] += 1

for k,v in counts.items():
    print("{}: {}".format(k, v))
