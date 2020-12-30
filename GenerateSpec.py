import json
from jinja2 import Environment, FileSystemLoader

 
file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)

# Template file at ./app/templates/example.json
template = env.get_template("store-template.yaml")

print ("Template loaded successfully...")

# Opening data file
data_file = open("./data/data.json",) 
data = json.load(data_file) 
stores = data['stores']
print (str(len(data['stores'])) +" Records loaded successfully...")


for store in stores:

  spec_file = open("./generated-spec/" + store['storeId'] + "store-spec.yaml","w") 

  print ("Creating specification for " + store['storeId'])

  spec = template.render(store=store)

  spec_file.write(spec)
  spec_file.close()

# Closing file 
data_file.close()

print ("Specifications created successfully.")