{
    'name': "Documents custom",

    'summary': "Document management",

    'description': """
        App to upload and manage your documents.
    """,

    'author': "Odoo",
    'category': 'Operations/Documents',
    'version': '1.0',
    'application': True,
    'website': 'https://www.odoo.com/page/documents',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'portal', 'web', 'attachment_indexation','documents','documents_account','documents_fleet','documents_hr','documents_project'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],

}
