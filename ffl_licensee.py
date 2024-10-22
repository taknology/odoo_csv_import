from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor

from import_globals import (ffl_licensee_prefix
                            , data_file_path)

processor = Processor(data_file_path + "ffl-list-complete.txt", delimiter="\t")

#               
product_template_mapping = {
    "id": mapper.m2o_map(ffl_licensee_prefix,  mapper.concat("_", "LIC_REGN", "LIC_DIST", "LIC_SEQN"))
    ,"region": mapper.val("LIC_REGN")
    ,"district": mapper.val("LIC_DIST")
    ,"county": mapper.val("LIC_CNTY")
    ,"type": mapper.val("LIC_TYPE")
    ,"xprtde": mapper.val("LIC_XPRDTE")
    ,"sequence": mapper.val("LIC_SEQN")
    ,"short_license_num": mapper.concat("-", "LIC_REGN", "LIC_DIST", "LIC_SEQN")
    ,"full_license_num": mapper.concat("-", "LIC_REGN", "LIC_DIST", "LIC_CNTY", "LIC_TYPE", "LIC_XPRDTE", "LIC_SEQN")
    ,"license_name": mapper.val("LICENSE_NAME")
    ,"business_name": mapper.val("BUSINESS_NAME")
    ,"business_street": mapper.val("PREMISE_STREET")
    ,"business_city": mapper.val("PREMISE_CITY")
    ,"business_state": mapper.val("PREMISE_STATE")
    ,"business_zip": mapper.val("PREMISE_ZIP_CODE")
    ,"premise_street": mapper.val("MAIL_STREET")
    ,"premise_city": mapper.val("MAIL_CITY")
    ,"premise_state": mapper.val("MAIL_STATE")
    ,"premise_zip": mapper.val("MAIL_ZIP_CODE")
    ,"phone": mapper.val("VOICE_PHONE")
}

processor.process(product_template_mapping, data_file_path + "ffl.licensee.csv", {"model": "ffl_tools.ffl_licensee", "context": "{'tracking_disable': True}", "worker": 4, "batch_size": 20})
processor.write_to_file(data_file_path + "ffl_licensee.sh", python_exe='python3', path='')