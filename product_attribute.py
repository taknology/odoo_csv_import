from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor

from import_globals import (product_attribute_prefix
                            , data_file_path)

processor = Processor(data_file_path + "product_attribute.csv", delimiter=",")

product_attribute_mapping = {
    "id": mapper.m2o_map(product_attribute_prefix, mapper.val("attribute_name"))
    ,"name": mapper.val("name")
    ,"display_type": mapper.val("display_type")
    ,"sequence": mapper.val("sequence")
    ,"create_variant": mapper.val("create_variant")
    ,"visibility": mapper.val("visibility")
}

processor.process(product_attribute_mapping, data_file_path + "product.attribute.csv", {"model": "product.attribute", "context": "{'tracking_disable': True}", "worker": 4, "batch_size": 20})
processor.write_to_file(data_file_path + "product_attribute.sh", python_exe='python3', path='')