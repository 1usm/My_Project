# Copyright (c) 2023, Muhammad Usman and contributors
# For license information, please see license.txt

import froggy
from froggy.model.document import Document

class LibraryManager(Document):
    pass


@froggy.whitelist()
def get_supplier(supplier_name):
    supl_doc = froggy.get_doc('Supplier', supplier_name)
    supplier_group = supl_doc.supplier_group

    return supplier_group