# -*- coding: utf-8 -*-

tbl = db.define_table("persona",
	Field('nombre', 'string', length=30),
	Field('sexo', 'string', length=1),
	Field('edad', 'integer'),
	Field('direccion', 'text', length=255)
)

tbl.nombre.requires = IS_NOT_EMPTY()
tbl.sexo.requires = IS_IN_SET(
	{'M': 'Masculino', 'F': 'Femenino'}
)
tbl.edad.requires = [IS_NOT_EMPTY(), IS_INT_IN_RANGE(1, 100)]
