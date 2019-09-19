{"filter":false,"title":"models.py","tooltip":"/mycart/models.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":4,"column":0},"end":{"row":26,"column":65},"action":"remove","lines":["class Order(models.Model):","    full_name = models.CharField(max_length=50, blank=False)","    phone_number = models.CharField(max_length=20, blank=False)","    country = models.CharField(max_length=40, blank=False)","    postcode = models.CharField(max_length=20, blank=True)","    town_or_city = models.CharField(max_length=40, blank=False)","    street_address1 = models.CharField(max_length=40, blank=False)","    street_address2 = models.CharField(max_length=40, blank=False)","    county = models.CharField(max_length=40, blank=False)","    date = models.DateField()","","    def __str__(self):","        return \"{0}-{1}-{2}\".format(self.id, self.date, self.full_name)","","","class OrderLineItem(models.Model):","    order = models.ForeignKey(Order, null=False)","    product = models.ForeignKey(Product, null=False)","    quantity = models.IntegerField(blank=False)","","    def __str__(self):","        return \"{0} {1} @ {2}\".format(","            self.quantity, self.product.name, self.product.price)"],"id":8}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["from products.models import Product",""],"id":9}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":0},"end":{"row":1,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1568882209945,"hash":"bb2ade0b5906d4c34ad5489e26929421fa78ce5e"}