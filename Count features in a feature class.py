import arcpy

arcpy.env.workspace = r"D:\_TANJUM\Count features in a feature class.py\Bhairab_Bazar.gdb"

for fc in arcpy.ListFeatureClasses():
    count = int(arcpy.GetCount_management(fc)[0])
    print("{} {}".format(fc, count))


