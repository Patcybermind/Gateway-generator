import mcschematic as mcs
import os
# up there all I did was import all the necessary packages

# create a schematic
schem = mcs.MCSchematic()

# get coords from user
X = input("X: ")
Y = input("Y: ")
Z = input("Z: ")


def single_gateway(x, y, z):
    # place the blocks
    nbt_tag = "minecraft:end_gateway{Age:180,ExactTeleport:1,ExitPortal:{X:" + x + ",Y:" + y + ",Z:" + z + "}}"
    print(nbt_tag)
    schem.setBlock((0, -1, 0), nbt_tag)


single_gateway(X, Y, Z)

# time to save
rootpath = os.path.expanduser('~')
print(f"your rootpath is {rootpath}")

savepath = r"\AppData\Roaming\.minecraft\config\worldedit\schematics\end gateways"
print(f"your save path is {savepath}")

savepath = os.path.join(rootpath + savepath)
print(f"saving to {savepath}")

# time to write the save
schem.save(savepath, "most_recent", mcs.Version.JE_1_18_2)
print("success!")
