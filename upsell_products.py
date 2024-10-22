from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor

from import_globals import (product_template_prefix
                            , data_file_path
                            , image_file_path)

processor = Processor(data_file_path + "upsell_products.csv", delimiter=",")

product_template_mapping = {
    "id": mapper.m2o_map(product_template_prefix, mapper.val("barcode"))
    # ,"accessory_product_ids/.id": mapper.val("accessory_product_ids/.id")
    ,"alternative_product_ids/.id": mapper.val("alternative_product_ids/.id")
    ,"optional_product_ids/.id": mapper.val("optional_product_ids/.id")
}

processor.process(product_template_mapping, data_file_path + "upsell.products.csv", {"model": "product.template", "context": "{'tracking_disable': True}", "worker": 1, "batch_size": 200})
processor.write_to_file(data_file_path + "upsell_products.sh", python_exe='python3', path='')