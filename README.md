# Jinja Template to Open API 3.0 YAML
This repository provides sample Python 3.7 code to generate Open API 3.0 specification YAML files using Jinja2 template. It shows how to generate multiple similar API specifications from by applying data in Json format to a Jinja2 template of an Open API specification file. The code generates API specifications for simple Pet Store and Book Store APIs using a generic Store template file.

## Structure of the project

### data folder

**data.json:**  The Json file containing the data of multiple API specifications to be generated.

### templates folder
**store-template.yaml:** Generic template file of a Store API.

### generated-spec folder
The destination folder where the final specification files will be created after the execution of the program.
**store-template.yaml:** Generic template file of a Store API.

## License
- The source code in this project is published under [MIT License](https://github.com/amitvsavant/jinja-template-2-open-api/blob/main/LICENSE).