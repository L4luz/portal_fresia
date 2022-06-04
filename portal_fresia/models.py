from django.db import models


class AreaTrabajo(models.Model):
    id_area = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'area_trabajo'


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


class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    rut = models.CharField(max_length=11)
    contrasena = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    fecha_de_nac = models.DateField()
    id_genero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='id_genero')
    id_estado_civil = models.ForeignKey('EstadoCivil', models.DO_NOTHING, db_column='id_estado_civil')
    id_tarjeta_cliente = models.ForeignKey('TarjetaCliente', models.DO_NOTHING, db_column='id_tarjeta_cliente')

    class Meta:
        managed = False
        db_table = 'cliente'


class Compra(models.Model):
    id_compra = models.BigAutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'compra'


class Comuna(models.Model):
    id_comuna = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comuna'


class Direccion(models.Model):
    id_direccion = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    id_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='id_trabajador')
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')

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
    id_documento = models.BigAutoField(primary_key=True)
    mont_bruto = models.DecimalField(max_digits=8, decimal_places=0)
    iva = models.DecimalField(max_digits=8, decimal_places=0)
    monto_neto = models.DecimalField(max_digits=8, decimal_places=0)
    id_tipo_docum_tribu = models.ForeignKey('TipoDocumTribu', models.DO_NOTHING, db_column='id_tipo_docum_tribu')

    class Meta:
        managed = False
        db_table = 'documento_tributario'


class Envio(models.Model):
    id_envio = models.BigAutoField(primary_key=True)
    id_estado_envio = models.ForeignKey('EstadoEnvio', models.DO_NOTHING, db_column='id_estado_envio')
    id_compra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='id_compra')

    class Meta:
        managed = False
        db_table = 'envio'


class EstadoCivil(models.Model):
    id_estado_civil = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_civil'


class EstadoEnvio(models.Model):
    id_estado_envio = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_envio'


class Genero(models.Model):
    id_genero = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'genero'


class Insumo(models.Model):
    id_insumo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'insumo'


class Invitado(models.Model):
    id_invitado = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=200)
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion')

    class Meta:
        managed = False
        db_table = 'invitado'


class Material(models.Model):
    id_material = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'material'


class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    talla = models.CharField(max_length=1)
    color = models.CharField(max_length=30)
    id_tipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='id_tipo_producto')
    id_material = models.ForeignKey(Material, models.DO_NOTHING, db_column='id_material')

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoCompra(models.Model):
    id_producto_compra = models.BigAutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'producto_compra'


class Region(models.Model):
    id_region = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'region'


class TarjetaCliente(models.Model):
    id_tarjeta_cliente = models.BigAutoField(primary_key=True)
    numero_tarjeta = models.DecimalField(max_digits=65535, decimal_places=0)
    fecha_vencimiento = models.DateField()
    codigo_verificacion = models.CharField(max_length=3)
    email = models.CharField(max_length=200, blank=True, null=True)
    contrasena_cliente = models.CharField(max_length=200)
    id_tipo_tarjeta = models.ForeignKey('TipoTarjeta', models.DO_NOTHING, db_column='id_tipo_tarjeta')

    class Meta:
        managed = False
        db_table = 'tarjeta_cliente'


class TipoDocumTribu(models.Model):
    id_tipo_docum_tribu = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_docum_tribu'


class TipoPago(models.Model):
    id_tipo_pago = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_pago'


class TipoProducto(models.Model):
    id_tipo_producto = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoTarjeta(models.Model):
    id_tipo_tarjeta = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_tarjeta'


class Trabajador(models.Model):
    id_trabajador = models.BigAutoField(primary_key=True)
    rut = models.CharField(max_length=11)
    cargo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    fecha_de_nac = models.DateField()
    id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero')
    id_estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='id_estado_civil')
    id_area = models.ForeignKey(AreaTrabajo, models.DO_NOTHING, db_column='id_area')

    class Meta:
        managed = False
        db_table = 'trabajador'