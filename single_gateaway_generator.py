import mcschematic as mcs
import os
# up there all I did was import all the necessary packages

# create a schematic
schem = mcs.MCSchematic()

# function


def single_gateway(position_in_schematic, out):

    # unpack position in schematic list
    x, y, z = position_in_schematic
    # set up the nbt tag
    nbt_tag = "minecraft:end_gateway{Age:180,ExactTeleport:1,ExitPortal:{X:" + x + ",Y:" + y + ",Z:" + z + "}}"
    print(nbt_tag)
    # place the blocks
    schem.setBlock(out, nbt_tag)


# get coords from user
X = input("X : ")
Y = input("Y : ")
Z = input("Z : ")
portal_out = X, Y, Z

xpos = int(input("X position : "))
ypos = int(input("Y position : "))
zpos = int(input("Z position : "))
rel_pos = xpos, ypos, zpos

# use the function for this example program
single_gateway(portal_out, rel_pos)

# time to save
rootpath = os.path.expanduser('~')
print(f"your rootpath is {rootpath}")

savepath = r"\AppData\Roaming\.minecraft\config\worldedit\schematics"
print(f"your save path is {savepath}")

savepath = os.path.join(rootpath + savepath)
print(f"saving to {savepath}")

# time to write the save
schem.save("", "_most recent",
           mcs.Version.JE_1_18_2)
# now to WE folder
try:
    schem.save(savepath, "_most_recent_gateway", mcs.Version.JE_1_18_2)
    print("success! saved to your World Edit schematics folder and to the folder this program is running from")
    
except all:  # if the World Edit schematics folder isn't found

    print("looks like you don't have a World Edit schematics folder but don't worry the generated .schem file was still"
          "saved to the folder this program is running from")
