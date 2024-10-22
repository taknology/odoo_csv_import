from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor

from import_globals import (product_template_prefix
                            , product_attribute_prefix
                            , product_attribute_value_prefix
                            , product_template_attribute_line_prefix
                            , data_file_path)

processor = Processor(data_file_path + "product_template_attribute_line.csv", delimiter=",")

product_template_attribute_line_mapping = {
    "id": mapper.m2o_map(product_template_attribute_line_prefix, mapper.concat("_", "barcode", "attribute_name"))
    ,"product_tmpl_id/id": mapper.m2o_map(product_template_prefix, mapper.val("barcode"))
    ,"attribute_id/id": mapper.m2o_map(product_attribute_prefix, mapper.val("attribute_name"))
    ,"value_ids/id": mapper.m2o_map(product_attribute_value_prefix, mapper.concat("_", "attribute_name", "value_id"))
    ,"sequence": mapper.val("sequence")
}

processor.process(product_template_attribute_line_mapping, data_file_path + "product.template.attribute.line.csv", {"model": "product.template.attribute.line", "context": "{'tracking_disable': True}", "worker": 1, "batch_size": 200})
processor.write_to_file(data_file_path + "product_template_attribute_line.sh", python_exe='python3', path='')