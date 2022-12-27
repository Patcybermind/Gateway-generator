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
    nbt_tag = "minecraft:end_gateway{Age:180,ExactTeleport:1,ExitPortal:" \
              "{X:" + str(x) + ",Y:" + str(y) + ",Z:" + str(z) + "}}"
    print(nbt_tag)
    # place the blocks
    schem.setBlock(out, nbt_tag)

# ask the user the mode they will use
print("do you want to enter the coordinates manually or"
      " with copy pasted coordinates from pressing f3 + c? note that you have to paste it raw"
      "c for copy pasted mode and m for manual : ")
autoormanual = input("c for copy pasted mode and m for manual : ")

if autoormanual.lower() == "c":  # if the user chose to copy-paste the coords
    print("copy the coordinates of where you want the gateways to lead to : ")
    pasted_coords = input("Paste your clipboard here : ")
    # /execute in minecraft:overworld run tp @s 173.01 88.39 86.64 162.05 16.95
    # that is the format we will decode

    pasted_coords = pasted_coords.split()

    X = int(round(float(pasted_coords[6])))
    Y = int(round(float(pasted_coords[7])))
    Z = int(round(float(pasted_coords[8])))

    # relative position
    xpos = 0
    ypos = -1
    zpos = 0
elif autoormanual.lower() == "m":  # if the user chose to manually enter the coords
    # get coords from user if the answer was no
    print("target :")
    X = int(input("X : "))
    Y = int(input("Y : "))
    Z = int(input("Z : "))

    print("relative position :")
    xpos = int(input("X position : "))
    ypos = int(input("Y position : "))
    zpos = int(input("Z position : "))


portal_out = X, Y, Z

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
schem.save("", "most recent_gate_way",
           mcs.Version.JE_1_18_2)
# now to WE folder
try:
    schem.save(savepath, "_most_recent_gateway", mcs.Version.JE_1_18_2)
    print("success! saved to your World Edit schematics folder and to the folder this program is running from")
    
except all:  # if the World Edit schematics folder isn't found

    print("looks like you don't have a World Edit schematics folder but don't worry the generated .schem file was still"
          "saved to the folder this program is running from")
