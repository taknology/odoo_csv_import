from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor

from import_globals import (product_template_prefix
                            , public_supplierinfo_prefix
                            , data_file_path
                            , orchid_image_file_path
                            , lipseys_image_file_path
                            , rsr_image_file_path)

processor = Processor(data_file_path + "product_template.csv", delimiter=",")

product_template_mapping = {
    "id": mapper.m2o_map(product_template_prefix, mapper.val("barcode"))
    ,"name": mapper.val("name")
    ,"type": mapper.val("type")
    ,"default_code":mapper.val("default_code")
    ,"barcode": mapper.val("barcode")
    ,"standard_price": mapper.val("standard_price")
    ,"":mapper.val( "")
    ,"list_price": mapper.val("list_price")
    ,"msrp":mapper.val("msrp")
    ,"compare_list_price": mapper.val("compare_list_price")
    ,"allocated_closeout_deleted": mapper.val("allocated_closeout_deleted")
    ,"categ_id": mapper.val("categ_id", default="All / Saleable")
    ,"public_categ_ids/id": mapper.val("public_categ_ids/id")
    ,"pos_categ_ids/id": mapper.val("pos_categ_ids/id")
    ,"mfg_part_number": mapper.val("mfg_part_number")
    ,"mfg_model": mapper.val("mfg_model")
    ,"product_description": mapper.val("expanded_product_description")
    #,"product_features": mapper.val("product_features")
    ,"description_sale": mapper.val("description_sale")
    #,"image_1920": mapper.binary_url("image_1920")
    #,"image_1920": mapper.binary('image_1920', lipseys_image_file_path)
    #,"image_1920": mapper.binary('image_1920', rsr_image_file_path)
    ,"image_1920": mapper.binary('image_1920', orchid_image_file_path)
    ,"tracking": mapper.val("tracking")
    ,"available_in_pos": mapper.val("available_in_pos")
    ,"is_published":mapper.val("is_published")
}

product_supplierinfo_mapping =  {

    "id": mapper.m2o_map(public_supplierinfo_prefix, mapper.concat("_", "barcode", "product_supplierinfo/partner_id/id"))
    ,"product_tmpl_id/id": mapper.m2o_map(product_template_prefix, mapper.val("barcode"))
    ,"price": mapper.val("product_supplierinfo/price")
    ,"partner_id/id": mapper.val("product_supplierinfo/partner_id/id")
    ,"qty_on_hand": mapper.val("product_supplierinfo/qty_on_hand")
    ,"vendor_part_number": mapper.val("product_supplierinfo/vendor_part_number")
}

processor.process(product_template_mapping, data_file_path + "product.template.csv", {"model": "product.template", "context": "{'tracking_disable': True}", "worker": 4, "batch_size": 20})
processor.process(product_supplierinfo_mapping, data_file_path + "product.supplierinfo.csv", {"model": "product.supplierinfo", "context": "{'tracking_disable': True}", "worker": 4, "batch_size": 20}, "set")
processor.write_to_file(data_file_path + "product_template.sh", python_exe='python3', path='')