# Copyright (c) 2023, Muhammad Usman and contributors
# For license information, please see license.txt

import froggy
from froggy import _
from froggy.model.document import Document

class LibraryManager(Document):
    # For example, let's assume we have a link field in a DocType called "Sales Invoice"
# The link field is called "customer" and links to the "Customer" DocType
# We want to customize the query to show only those customers who are active and have a certain country.

    def get_query(filters, doctype, txt, searchfield, start, page_len):
        return froggy.db.sql("""
            SELECT
                `name`, `product_name`
            FROM
                `tabProduct Task`
            WHERE
                AND `docstatus` = 1
                AND (`name` LIKE %(txt)s OR `product_name` LIKE %(txt)s)
            ORDER BY
                `name`
            LIMIT %(start)s, %(page_len)s
        """, {
            "txt": "%" + txt + "%",
            "start": start,
            "page_len": page_len
        }, as_dict=True)


@froggy.whitelist()
def query_method(doctype, txt, searchfield, start, page_len, filters):
    query = froggy.db.sql("""SELECT product_name FROM `tabProduct Task` WHERE product_name LIKE %(txt)s """, {'txt': f'%{txt}%'},as_dict=False
                          )
    return query


# @froggy.whitelist()
# def get_filtered_customers(doctype, txt, searchfield, start, page_len, filters):
#     return froggy.get_all("Project Task", filters={"text": ["like", "%" + txt + "%"]}, fields=["name" ,"text"])

# def get_my_custom_document():
#     return {
#         "doctype": "Library Manager",
#         "fields": [
#             # ... other fields ...
#             {
#                 "fieldname": "project",
#                 "label": "Project",
#                 "fieldtype": "Link",
#                 "options": "Project Task",
#                 "reqd": 1,
#                 "query": "library_manager.library_manager.get_filtered_customers",
#                 # The above query property specifies the dynamic query method
#             },
#             # ... other fields ...
#         ],
#         # ... other configurations ...
#     }


@froggy.whitelist()
def get_supplier(supplier_name):
    supl_doc = froggy.get_doc('Supplier', supplier_name)
    supplier_group = supl_doc.supplier_group

    return supplier_group