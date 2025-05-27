```
BGM/
├── app/
│   ├── main/
│   │   ├── ac/
│   │   │   ├── templates/
│   │   │   │   ├── account_create.html
│   │   │   │   ├── account_read.html
│   │   │   │   └── account_update.html
│   │   │   ├── __init__.py
│   │   │   ├── ac_create.py
│   │   │   ├── ac_delete.py
│   │   │   ├── ac_read.py
│   │   │   ├── account_update.py
│   │   │   └── models.py
│   │   ├── inventory/
│   │   │   ├── bom/
│   │   │   │   ├── templates/
│   │   │   │   │   ├── bom_create.html
│   │   │   │   │   ├── bom_read.html
│   │   │   │   │   └── bom_update.html
│   │   │   │   ├── __init__.py
│   │   │   │   ├── bom_create.py
│   │   │   │   ├── bom_delete.py
│   │   │   │   ├── bom_read.py
│   │   │   │   ├── bom_update.py
│   │   │   │   └── models.py
│   │   │   ├── godown/
│   │   │   │   ├── rack/
│   │   │   │   │   ├── templates/
│   │   │   │   │   │   ├── create_rack.html
│   │   │   │   │   │   ├── delete_rack.html
│   │   │   │   │   │   ├── read_rack.html
│   │   │   │   │   │   └── update_rack.html
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── models.py
│   │   │   │   │   ├── rack_create.py
│   │   │   │   │   ├── rack_delete.py
│   │   │   │   │   ├── rack_read.py
│   │   │   │   │   └── rack_update.py
│   │   │   │   ├── templates/
│   │   │   │   │   ├── godown_create.html
│   │   │   │   │   ├── godown_read.html
│   │   │   │   │   ├── read_godown.html
│   │   │   │   │   └── update_godown.html
│   │   │   │   ├── __init__.py
│   │   │   │   ├── create_godown.py
│   │   │   │   ├── delete_godown.py
│   │   │   │   ├── godown_create.py
│   │   │   │   ├── godown_delete.py
│   │   │   │   ├── godown_read.py
│   │   │   │   ├── godown_update.py
│   │   │   │   ├── models.py
│   │   │   │   └── update_godown.py
│   │   │   ├── item/
│   │   │   │   ├── templates/
│   │   │   │   │   ├── item_create.html
│   │   │   │   │   ├── item_read.html
│   │   │   │   │   └── item_update.html
│   │   │   │   ├── __init__.py
│   │   │   │   ├── item_create.py
│   │   │   │   ├── item_delete.py
│   │   │   │   ├── item_read.py
│   │   │   │   ├── item_update.py
│   │   │   │   └── models.py
│   │   │   ├── templates/
│   │   │   │   ├── inventory_create.html
│   │   │   │   ├── inventory_create.html
│   │   │   │   ├── inventory_read.html
│   │   │   │   └── inventory_update.html
│   │   │   ├── __init__.py
│   │   │   ├── inventory_create.py
│   │   │   ├── inventory_delete.py
│   │   │   ├── inventory_read.py
│   │   │   ├── inventory_update.py
│   │   │   └── models.py
│   │   ├── purchase/
│   │   │   ├── supplier/
│   │   │   │   ├── templates/
│   │   │   │   │   └── create_supplier.html
│   │   │   │   ├── __init__.py
│   │   │   │   ├── supplier_create.py
│   │   │   │   ├── supplier_delete.py
│   │   │   │   ├── supplier_read.py
│   │   │   │   └── supplier_update.py
│   │   │   ├── templates/
│   │   │   │   ├── purchase_create.html
│   │   │   │   ├── purchase_read.html
│   │   │   │   └── purchase_update.html
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── purchase_create.py
│   │   │   ├── purchase_delete.py
│   │   │   ├── purchase_read.py
│   │   │   └── purchase_update.py
│   │   ├── sale/
│   │   │   ├── templates/
│   │   │   │   └── read_sale.html
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── sale_create.py
│   │   │   ├── sale_delete.py
│   │   │   ├── sale_read.py
│   │   │   └── sale_update.py
│   │   ├── templates/
│   │   │   └── main.html
│   │   ├── work/
│   │   │   ├── maker/
│   │   │   │   ├── templates/
│   │   │   │   │   ├── create_maker.html
│   │   │   │   │   ├── read_maker.html
│   │   │   │   │   └── update_maker.html
│   │   │   │   ├── __init__.py
│   │   │   │   ├── maker_create.py
│   │   │   │   ├── maker_delete.py
│   │   │   │   ├── maker_read.py
│   │   │   │   ├── maker_update.py
│   │   │   │   └── models.py
│   │   │   ├── process/
│   │   │   │   ├── templates/
│   │   │   │   │   ├── create_process.html
│   │   │   │   │   ├── read_process.html
│   │   │   │   │   └── update_process.html
│   │   │   │   ├── __init__.py
│   │   │   │   ├── models.py
│   │   │   │   ├── process_create.py
│   │   │   │   ├── process_delete.py
│   │   │   │   ├── process_read.py
│   │   │   │   └── process_update.py
│   │   │   ├── templates/
│   │   │   │   ├── work_create.html
│   │   │   │   ├── work_read.html
│   │   │   │   └── work_update.html
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── work_create.py
│   │   │   ├── work_delete.py
│   │   │   ├── work_read.py
│   │   │   └── work_update.py
│   │   └── __init__.py
│   ├── static/
│   │   ├── base.css
│   │   └── base.js
│   ├── templates/
│   │   └── base.html
│   ├── __init__.py
│   └── models.py
└── run.py
```