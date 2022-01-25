# Copyright (c) 2022, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class repost_cd(Document):
	@frappe.whitelist()
	def run_repost(self):
		repost_name=self.repost_item_valuation
		from erpnext.stock.doctype.repost_item_valuation.repost_item_valuation import repost
		doc = frappe.get_doc("Repost Item Valuation", repost_name)		
		try:
			x=repost(doc)
			frappe.log_error(title='try from repost cd',message=x if x else 'empty')
		except (Exception):
			traceback = frappe.get_traceback()
			frappe.log_error('from exception mplify')
			frappe.log_error(traceback)
			raise

		finally:
			frappe.log_error('finally completed mplify')
