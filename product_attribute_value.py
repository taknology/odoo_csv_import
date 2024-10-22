from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor

from import_globals import (product_attribute_prefix
                            , product_attribute_value_prefix
                            , data_file_path)

processor = Processor(data_file_path + "product_attribute_value.csv", delimiter=",")

product_attribute_value_mapping = {
    "id": mapper.m2o_map(product_attribute_value_prefix, mapper.concat("_", "attribute_name", "value_id"))
    ,"attribute_id/id": mapper.m2o_map(product_attribute_prefix, mapper.val("attribute_name"))
    ,"name": mapper.val("name")
    ,"sequence": mapper.val("sequence")
}

processor.process(product_attribute_value_mapping, data_file_path + "product.attribute.value.csv", {"model": "product.attribute.value", "context": "{'tracking_disable': True}", "worker": 1, "batch_size": 200})
processor.write_to_file(data_file_path + "product_attribute_value.sh", python_exe='python3', path='')