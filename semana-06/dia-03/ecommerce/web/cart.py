class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart
    def add(self, producto, cantidad):

        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'descripcion': producto.descripcion,
                'cantidad': cantidad,
                'precio': str(producto.precio),
                'imagen': producto.imagen.url,
                'categoria': producto.categoria.nombre,
                'subtotal': str(producto.precio * cantidad)
            }
        else:
            for key, value in self.cart.items():
                if key == str(producto.id):
                    value['cantidad'] = str(int(value['cantidad']) + cantidad)
                    value['subtotal'] = str(float(value['precio']) * float(value['cantidad']))
                    break
        self.save()
        
    def delete(self, producto_id):
        if str(producto_id) in self.cart:
            del self.cart[str(producto_id)]
            self.save()
    
    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True
        
    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
    