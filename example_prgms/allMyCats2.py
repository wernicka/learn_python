#Example program from Automate the Boring Stuff Ch 4

cat_names = []
while True:
    name = input(f"Enter the name of cat {len(cat_names) + 1}\
 (Or enter nothing to stop.):")
    if name == "":
        break
    cat_names = cat_names + [name]
print("The cat names are: ")
for name in cat_names:
    print("   " + name)
