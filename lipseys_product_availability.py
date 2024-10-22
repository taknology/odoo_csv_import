from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor

from import_globals import (product_template_prefix
                            , public_supplierinfo_prefix
                            , data_file_path)

processor = Processor(data_file_path + "lipseys_product_availability.csv", delimiter=",")

product_supplierinfo_mapping =  {

    "id": mapper.m2o_map(public_supplierinfo_prefix, mapper.concat("_", "barcode", "product_supplierinfo/partner_id/id"))
    ,"product_tmpl_id/id": mapper.m2o_map(product_template_prefix, mapper.val("barcode"))
    ,"price": mapper.val("product_supplierinfo/price")
    ,"partner_id": mapper.val("product_supplierinfo/partner_id")
    ,"x_studio_qty_on_hand": mapper.val("product_supplierinfo/x_studio_qty_on_hand")
    ,"x_studio_vendor_part_number": mapper.val("product_supplierinfo/x_studio_vendor_part_number")
}

processor.process(product_supplierinfo_mapping, data_file_path + "lipseys.product.availability.csv", {"model": "product.supplierinfo", "context": "{'tracking_disable': True}", "worker": 4, "batch_size": 20}, "set")
processor.write_to_file(data_file_path + "lipseys_product_availability.sh", python_exe='python3', path='')