import arcpy

arcpy.env.workspace = r"D:\_TANJUM\Layer Count According to Name\Bhairab_Bazar.gdb"

suffixes = ["_LG", "_NG", "_SG", "_PG", "_MG"]
counts = {s: 0 for s in suffixes}

for fc in arcpy.ListFeatureClasses():
    for s in suffixes:
        if fc.endswith(s):
            counts[s] += 1

for s, c in counts.items():
    print("Feature classes ending with {}: {}".format(s, c))
