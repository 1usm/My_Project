// Copyright (c) 2023, Muhammad Usman and contributors
// For license information, please see license.txt

froggy.ui.form.on('Library Manager', {

	full_name: function(frm){
		if(frm.doc.full_name){
			frm.toggle_reqd('date_of_issue',true);
		}else{
			frm.toggle_reqd('date_of_issue',false);
		}
	},

	onload: function(frm){
		frm.set_df_property('customer_name', 'hidden', 1)
		frm.set_df_property('lead', 'hidden', 1)
		frm.set_df_property('supplier_name', 'hidden', 1)
		frm.set_df_property('supplier_group', 'hidden', 1)

		// frm.fields_dict['project'].get_query = function(doc, cdn, cdt) {
        //     return {
        //         filters: [
        //             ['Project', 'status', '=', '1']
        //         ]
        //     };
        // };
	},

	invoice_selection: function (frm) {

		if (frm.doc.invoice_selection == "Sales Invoice") {
			frm.set_df_property('customer_name', 'hidden', 0)
			frm.set_df_property('lead', 'hidden', 0)
			frm.set_df_property('supplier_name', 'hidden', 1)
			frm.set_df_property('supplier_group', 'hidden', 1)
		}

		else if (frm.doc.invoice_selection == "Purchase Invoice") {
			frm.set_df_property('supplier_name', 'hidden', 0)
			frm.set_df_property('supplier_group', 'hidden', 0)
			frm.set_df_property('customer_name', 'hidden', 1)
			frm.set_df_property('lead', 'hidden', 1)
			
		}

	
	},

	refresh: function(frm) {
		frm.add_custom_button(__('Open Report'), function() {
			var filters = {
				payment_ledger_entry: frm.doc.name
			};
			froggy.set_route('query-report', 'Payment Ledger', filters);
		});

		frm.add_custom_button(__('Open Popup'), function() {	
			var modal = new froggy.ui.Dialog({
				title: 'Popup',
				fields: [
				{
					fieldtype: 'Data',
					fieldname: 'full_name',
					label: 'First Name',
					onchange: function() {
					frm.set_value('full_name', this.value);
					}
				},
				{
					fieldtype: 'Date',
					fieldname: 'date_of_issue',
					label: 'Date Issue',
					onchange: function() {
					frm.set_value('date_of_issue', this.value);
					}
				}
				],
				primary_action: function() {
				modal.hide();
				}
			});
			modal.show();
		});

		// frm.set_query('supplier_name', function() {
        //     return {
		// 		query:'myapp.myapp.doctype.library_manager.library_manager.get_query',
        //         filters: {
        //             // Filter based on another field value from the related DocType (e.g., Customer's Territory)
        //             supplier_group: frm.doc.supplier_group
        //         }
        //     };
        // });

		frm.set_query("supplier_name", function() {
			return {
			  filters:{"default_price_list": ["is", "set"],
			}
			};
		  });
	},

	supplier_name: function(frm) {
		var supplier_name = frm.doc.supplier_name;
		if (supplier_name) {
		  froggy.call({
			method: 'myapp.myapp.doctype.library_manager.library_manager.get_supplier',
			args: {
				supplier_name: supplier_name
			},
			callback: function(r) {
			  if (r.message) {
				var supplier_group = r.message;
				frm.set_value('supplier_group', supplier_group);
			  }
			}
		  });
		}
		else {
			frm.set_value('supplier_group', '');
		  }
	  },

	
});
