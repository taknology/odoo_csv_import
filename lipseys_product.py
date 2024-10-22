from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor

from import_globals import (lipseys_product_prefix
                            , public_supplierinfo_prefix
                            , product_template_prefix
                            , data_file_path
                            , lipseys_image_url_path)

processor = Processor(data_file_path + "lipseys_product.csv", delimiter=",")

product_template_mapping = {
    "id": mapper.m2o_map(product_template_prefix, mapper.val("barcode"))
    ,"name": mapper.val("name")
    ,"type": mapper.val("type")
    ,"default_code":mapper.val("default_code")
    ,"barcode": mapper.val("barcode")
    ,"standard_price": mapper.val("standard_price")
    ,"x_studio_map_price":mapper.val( "x_studio_map_price")
    ,"list_price": mapper.val("list_price")
    ,"x_studio_msrp":mapper.val("x_studio_msrp")
    ,"compare_list_price": mapper.val("compare_list_price")
    ,"x_studio_allocated_closeout_deleted": mapper.val("x_studio_allocated_closeout_deleted")
    ,"categ_id": mapper.val("categ_id")
    ,"public_categ_ids/id": mapper.val("public_categ_ids/id")
    ,"pos_categ_ids/id": mapper.val("pos_categ_ids/id")
    ,"x_studio_mfg_part_number": mapper.val("x_studio_mfg_part_number")
    ,"x_studio_model": mapper.val("x_studio_model")
    ,"x_studio_product_description": mapper.val("expanded_product_description")
    ,"x_studio_product_features": mapper.val("x_studio_product_features")
    ,"description_sale": mapper.val("description_sale")
    ,"image_1920": mapper.binary_url("image_1920")
    #,"image_1920": mapper.binary('image_1920', image_file_path)
    ,"tracking": mapper.val("tracking")
    ,"available_in_pos": mapper.val("available_in_pos")
    ,"is_published":mapper.val("is_published")
}

product_supplierinfo_mapping =  {

    "id": mapper.m2o_map(public_supplierinfo_prefix, mapper.concat("_", "barcode", "product_supplierinfo/partner_id/id"))
    ,"product_tmpl_id/id": mapper.m2o_map(product_template_prefix, mapper.val("barcode"))
    ,"price": mapper.val("product_supplierinfo/price")
    ,"partner_id": mapper.val("product_supplierinfo/partner_id")
    ,"x_studio_qty_on_hand": mapper.val("product_supplierinfo/x_studio_qty_on_hand")
    ,"x_studio_vendor_part_number": mapper.val("product_supplierinfo/x_studio_vendor_part_number")
}

processor.process(product_template_mapping, data_file_path + "product.template.csv", {"model": "product.template", "context": "{'tracking_disable': True}", "worker": 4, "batch_size": 20})
processor.process(product_supplierinfo_mapping, data_file_path + "product.supplierinfo.csv", {"model": "product.supplierinfo", "context": "{'tracking_disable': True}", "worker": 4, "batch_size": 20}, "set")
processor.write_to_file(data_file_path + "product_template.sh", python_exe='python3', path='')