from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date 

class libros(models.Model):
    _name = 'alejandro_moles.libros'
    _descripcion = 'model libros'

    name = fields.Char('ISBN',required=True)
    titulo = fields.Char(string='Titulo',required=True)
    precio = fields.Integer(string='Precio',required=True)
    genero = fields.Char(string='Genero',required=True)
    esCaro = fields.Char("esCaro", compute="_get_esCaro")
    
    #relaciones
    libros_id = fields.Many2one('alejandro_moles.biblioteca', string='Libros de la biblioteca')
    libros_autores = fields.Many2one('alejandro_moles.persona', string='Autores')
    factura_id = fields.One2many('alejandro_moles.factura', 'libro_id', string='Factura' )

    @api.depends('esCaro')
    def _get_esCaro(self):
        for lib in self:
            if lib.precio > 50:
                lib.esCaro = 'Este libro es CARO'
            else:
                lib.esCaro = 'Este libro NO es caro'
    


class biblioteca(models.Model):
    _name = 'alejandro_moles.biblioteca'
    _descipcion = 'model biblioteca'

    name = fields.Char('Identificador', required=True)
    nombre = fields.Char('Nombre', required = True)

    #relaciones
    libros=fields.One2many('alejandro_moles.libros', 'libros_id', string = 'Libros de la Biblioteca')



class persona(models.Model):
    _name = 'alejandro_moles.persona'
    _descipcion = 'model persona'

    name = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required = True)
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento',required=True)
    anios = fields.Integer("Años", compute="_get_anios")

    #relaciones
    autor = fields.One2many('alejandro_moles.libros', 'libros_autores', string = 'Autor de los libros')
    cliente = fields.One2many('alejandro_moles.cliente', 'persona_id', string = 'Persona')

    @api.depends('fecha_nacimiento')
    def _get_anios(self):  
        for pers in self:
            now=date.today()
            pers.anios = relativedelta(now, pers.fecha_nacimiento).years


class cliente(models.Model):
    _name = 'alejandro_moles.cliente'
    _descipcion = 'model cliente'

    name = fields.Char('CodigoCliente', required=True)
    
    #relaciones
    persona_id = fields.Many2one('alejandro_moles.persona', string='Persona')
    factura_id = fields.One2many('alejandro_moles.factura', 'cliente_id', string="Factura")
    

    
class factura(models.Model):
    _name = 'alejandro_moles.factura'
    _descipcion = 'model factura'

    name = fields.Char('Codigo Factura', required=True)
    cantidad = fields.Integer('Cantidad de Libros', required =True)
    iva = fields.Char('Tiene IVA?', required = True)
    precio = fields.Integer("precio", compute="_get_precio")
    precioIva = fields.Integer("precioIva", compute="_get_precioIva")
    
    
    #relaciones
    cliente_id = fields.Many2one('alejandro_moles.cliente', string='Cliente')
    libro_id = fields.Many2one('alejandro_moles.libros', string='Libros')

    @api.depends('precio')
    def _get_precio(self):
        for fact in self:
            fact.precio =  fact.libro_id.precio * fact.cantidad

    @api.depends('precioIva')
    def _get_precioIva(self):
        for fact in self:
            if fact.iva =='si':    
                fact.precioIva =  (fact.libro_id.precio * fact.cantidad) * 1.21 
            else:
                fact.precioIva = 0
    