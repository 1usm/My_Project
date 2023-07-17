# Copyright (c) 2023, Muhammad Usman and contributors
# For license information, please see license.txt

import froggy
from froggy.model.document import Document

class LibraryManager(Document):
    pass


@froggy.whitelist()
def get_filtered_customers(doctype, txt, searchfield, start, page_len, filters):
    return froggy.get_all("Project Task", filters={"text": ["like", "%" + txt + "%"]}, fields=["name" ,"text"])

def get_my_custom_document():
    return {
        "doctype": "Library Manager",
        "fields": [
            # ... other fields ...
            {
                "fieldname": "project",
                "label": "Project",
                "fieldtype": "Link",
                "options": "Project Task",
                "reqd": 1,
                "query": "library_manager.library_manager.get_filtered_customers",
                # The above query property specifies the dynamic query method
            },
            # ... other fields ...
        ],
        # ... other configurations ...
    }


@froggy.whitelist()
def get_supplier(supplier_name):
    supl_doc = froggy.get_doc('Supplier', supplier_name)
    supplier_group = supl_doc.supplier_group

    return supplier_group