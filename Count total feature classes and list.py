import arcpy

gdb = r"D:\_TANJUM\Count total feature classes and list\Bhairab_Bazar.gdb"
arcpy.env.workspace = gdb

fc_list = arcpy.ListFeatureClasses() or []
for fd in arcpy.ListDatasets(feature_type='Feature') or []:
    fc_list += arcpy.ListFeatureClasses(feature_dataset=fd) or []

print("Total feature classes:", len(fc_list))
print("\nFeature classes list:\n" + "\n".join(fc_list))
