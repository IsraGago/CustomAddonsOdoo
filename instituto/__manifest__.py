{
    "name": "Instituto",  # Nombre del Modulo
    "summary": "Herramienta Instituto",  # Module subtitle phrase
    "description": "Herramienta para gestinoar los modulos de un instituto",  # Supports reStructuredText(RST) format (description is Deprecated)
    "version": "17.0.1.0.0",
    "author": "Juan Maria Sanchez Curto",
    "category": "Tools",    
    "license": "AGPL-3",
    "depends": ["base"], #Modulos con los que voy a interactuar
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
	],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    #'demo': [
    #    'demo.xml'
    #],
    
}
