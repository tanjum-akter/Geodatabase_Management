import arcpy, os

# Input and output geodatabases
in_gdb  = r"D:\_TANJUM\Import_MG_to_GDB\Bhairab_Bazar.gdb"
out_gdb = r"D:\_TANJUM\Import_MG_to_GDB\Bhairab_Bazar_MG.gdb"

# Set workspace
arcpy.env.workspace = in_gdb

# Create output GDB if it does not exist
if not arcpy.Exists(out_gdb):
    arcpy.CreateFileGDB_management(
        os.path.dirname(out_gdb),
        os.path.basename(out_gdb)
    )

# Copy feature classes ending with _MG
for fc in arcpy.ListFeatureClasses("*_MG"):
    arcpy.CopyFeatures_management(fc, os.path.join(out_gdb, fc))
    print("Copied: {0}".format(fc.encode("utf-8")))

print("Done.")


