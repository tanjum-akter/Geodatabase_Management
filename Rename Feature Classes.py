import arcpy

arcpy.env.addOutputsToMap = False  # Prevents adding outputs to MXD

gdb = r"D:\_TANJUM\Import_MG_to_GDB\Bhairab_Bazar.gdb"
arcpy.env.workspace = gdb

suffix_map = {
    "_LD": "_LG",
    "_MD": "_MG",
    "_ND": "_NG",
    "_SD": "_SG",
    "_PD": "_PG"
}

for fc in arcpy.ListFeatureClasses():
    for old_sfx, new_sfx in suffix_map.items():
        if fc.endswith(old_sfx):
            new_name = fc[:-len(old_sfx)] + new_sfx
            arcpy.Rename_management(fc, new_name)
            print("Renamed: {0} -> {1}".format(fc, new_name))
            break

print("Done.")
