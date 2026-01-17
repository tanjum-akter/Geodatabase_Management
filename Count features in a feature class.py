import arcpy

arcpy.env.workspace = r"D:\_TANJUM\Difference between 2 same type feature class\EdgM.gdb"

fc1 = "FeatureClass_1"   # first feature class
fc2 = "FeatureClass_2"   # second feature class
field = "ID"             # common attribute field

# Read values from both feature classes
vals_fc1 = set(row[0] for row in arcpy.da.SearchCursor(fc1, [field]))
vals_fc2 = set(row[0] for row in arcpy.da.SearchCursor(fc2, [field]))

# Differences
only_in_fc1 = vals_fc1 - vals_fc2
only_in_fc2 = vals_fc2 - vals_fc1

print("Values only in {}:".format(fc1))
for v in only_in_fc1:
    print(v)

print("\nValues only in {}:".format(fc2))
for v in only_in_fc2:
    print(v)
