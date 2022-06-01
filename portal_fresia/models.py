from django.db import models


class AreaDeTrabajo(models.Model):
    id_área = models.DecimalField(primary_key=True, max_digits=1, decimal_places=0)
    descripción = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'area_de_trabajo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Ciudad(models.Model):
    id_ciudad = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(max_length=200)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    email = models.CharField(primary_key=True, max_length=200)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)
    fecha_de_nac = models.DateField()
    genero_id_genero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='genero_id_genero')
    estado_civil_id_estadocivil = models.ForeignKey('EstadoCivil', models.DO_NOTHING, db_column='estado_civil_id_estadocivil')
    wallet_cliente_numero_tarjeta = models.OneToOneField('WalletCliente', models.DO_NOTHING, db_column='wallet_cliente_numero_tarjeta')

    class Meta:
        managed = False
        db_table = 'cliente'


class Compra(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    cantidad_de_objetos = models.DecimalField(max_digits=65535, decimal_places=65535)
    cliente_email = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_email')
    doctrib_id_docu = models.ForeignKey('DocumentoTributario', models.DO_NOTHING, db_column='doctrib_id_docu')
    id_estado = models.DecimalField(max_digits=65535, decimal_places=65535)
    tipo_de_pago_id_tipo_pago = models.ForeignKey('TipoDePago', models.DO_NOTHING, db_column='tipo_de_pago_id_tipo_pago')
    #envio_id_envio = models.OneToOneField('Envio', models.DO_NOTHING, db_column='envio_id_envio')

    class Meta:
        managed = False
        db_table = 'compra'


class Comuna(models.Model):
    id_comuna = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(max_length=200)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'


class Direccion(models.Model):
    id_dir = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(max_length=200)
    trabajador_rut = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='trabajador_rut')
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')
    cliente_email = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_email')

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentoTributario(models.Model):
    id_documento = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    monto_bruto = models.DecimalField(max_digits=8, decimal_places=0)
    iva = models.DecimalField(max_digits=8, decimal_places=0)
    monto_neto = models.DecimalField(max_digits=8, decimal_places=0)
    tipo_doc_tri_id_tipo = models.ForeignKey('TipoDocumentoTributario', models.DO_NOTHING, db_column='tipo_doc_tri_id_tipo')

    class Meta:
        managed = False
        db_table = 'documento_tributario'


class Envio(models.Model):
    id_envio = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    estado_envio = models.CharField(max_length=15)
    estado_envio_id_estado = models.ForeignKey('EstadoEnvio', models.DO_NOTHING, db_column='estado_envio_id_estado')
    compra = models.OneToOneField(Compra, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'envio'


class EstadoCivil(models.Model):
    id_estadocivil = models.CharField(primary_key=True, max_length=20)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_civil'


class EstadoEnvio(models.Model):
    id_estado = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_envio'


class Genero(models.Model):
    id_genero = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'genero'


class Insumo(models.Model):
    id_insumo = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    tipo_insumo = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'insumo'


class Invitado(models.Model):
    email = models.CharField(primary_key=True, max_length=200)
    id_aleatorio = models.DecimalField(max_digits=65535, decimal_places=65535)
    direccion_id_dir = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='direccion_id_dir')

    class Meta:
        managed = False
        db_table = 'invitado'


class MaterialProducto(models.Model):
    id_material = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    descripción = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'material_producto'


class Producto(models.Model):
    id_producto = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(max_length=200)
    talla = models.CharField(max_length=1)
    color = models.CharField(max_length=30)
    tipo_de_pro_id_del_prod = models.ForeignKey('TipoDeProducto', models.DO_NOTHING, db_column='tipo_de_pro_id_del_prod')
    mate_pro_id_mat = models.ForeignKey(MaterialProducto, models.DO_NOTHING, db_column='mate_pro_id_mat')

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoCompra(models.Model):
    compra = models.OneToOneField(Compra, models.DO_NOTHING, primary_key=True)
    producto_id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto_id_producto')

    class Meta:
        managed = False
        db_table = 'producto_compra'
        unique_together = (('compra', 'producto_id_producto'),)


class Region(models.Model):
    id_region = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'region'


class TipoDePago(models.Model):
    id_tipo_pago = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    medio_de_pago = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_de_pago'


class TipoDeProducto(models.Model):
    id_del_producto = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)
    descripción = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_de_producto'


class TipoDocumentoTributario(models.Model):
    id_tipo = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    tipo_de_documento = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_documento_tributario'


class TipoProducto(models.Model):
    id_tipo_prod = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre_material = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class Trabajador(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    cargo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    fecha_de_nac = models.DateField()
    genero_id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='genero_id_genero')
    estado_civil_id_estadocivil = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='estado_civil_id_estadocivil')
    area_de_trabajo_id_área = models.ForeignKey(AreaDeTrabajo, models.DO_NOTHING, db_column='area_de_trabajo_id_área')

    class Meta:
        managed = False
        db_table = 'trabajador'


class WalletCliente(models.Model):
    numero_tarjeta = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    tipo_tarjeta = models.CharField(max_length=25)
    fecha_vencimiento = models.DateField()
    codigo_verificacion = models.CharField(max_length=3)
    cliente_email = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='cliente_email')

    class Meta:
        managed = False
        db_table = 'wallet_cliente'