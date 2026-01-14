import arcpy

arcpy.env.workspace = r"D:\_TANJUM\Total Layer Count and list\Bhairab_Bazar.gdb"

fc_list = arcpy.ListFeatureClasses()

print("Total number of feature classes: {}".format(len(fc_list)))
print("\nFeature classes:")
for fc in fc_list:
    print(fc)
