from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    #canchas = CanchaSerializer(source='canchasTipoCancha',many=True, read_only=True)
    class Meta:
        model = Producto
        fields= '__all__'

    # def update(self):
    #     # print(self.instance.tipoCanchaDesc)
    #     # print(self.validated_data)
    #     self.instance.tipoCanchaDesc = self.validated_data.get('tipoCanchaDesc', self.instance.tipoCanchaDesc)
    #     self.instance.save()
    #     return self.instance
    # def delete(self):
    #     # hacer el comportamiento para que al llamar al metodo delete su estado de la instancia cambie a false
    #     self.instance.estado = False
    #     self.instance.save()
    #     return self.instance





