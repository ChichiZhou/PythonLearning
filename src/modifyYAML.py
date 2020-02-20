# import yaml
# with open("./test.yml", "w") as f:
#     template = yaml.load(f, Loader=yaml.CLoader)
#
# print(template)
#
# print(type(template))


with open("./test.yml", "r") as f:
    template = f.read()

print(template)

print(type(template))