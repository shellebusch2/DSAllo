# Python script for Make automation of Complaint type into Notion Complaints Database

# ALLO Markets and their UUID (found in Notion)
complaint_types = {
    "Drop": "69d87c9a87ec4fdebbfd1423cb173fe4",
    "Install": "f37c7d2b851c49a8bc6e069b0dd09717",
    "OSP": "f37c7d2b851c49a8bc6e069b0dd09717",
    "Sales": "082ee98eef1e43e890e024248197015e",
    "Driving": "65e1bc4d8be24c229c1e4d09d739a66a"
}

# "{{if(1.properties_value.Department[].name = "OSP"; "45195ee4fbe743dea9e460983fbfc4ec"; )}}
# "{{if(4.properties_value.City.name = \"" + city + "\"; \"" + uuid + "\"; )}}"

# "{{if(1.properties_value.Department[].name = \"" + complaint_type + "\"; \"" + uuid + "\"; )}}"
for complaint_type, uuid in complaint_types.items():
    print(
            "{{if(1.properties_value.Department[].name = \"" + complaint_type + "\"; \"" + uuid + "\"; )}}"
        )