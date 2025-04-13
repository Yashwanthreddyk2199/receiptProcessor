from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import RetailerReceipt,Item
from .utils.calculatePoints import calculatePoints



@api_view(['POST'])
def submitReceipt(request):
    try:
        data = request.data
        receipt = RetailerReceipt.objects.create(
            retailer=data.get('retailer'),
            purchaseDate=data.get('purchaseDate'),
            purchaseTime=data.get('purchaseTime'),
            total=data.get('total')
        )

        items = data.get('items', [])
        for item_data in items:
            item = Item.objects.create(
                shortDescription=item_data.get('shortDescription', '').strip(),
                price=item_data.get('price'),
                receipt_id=receipt.id
            )
            receipt.items.add(item)

        return Response({'id': receipt.id}, status=status.HTTP_200_OK)
    
    except Exception:
        return Response({'error': 'The receipt is invalid.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getReceiptPoints(request,id):
    try:
        receipt=RetailerReceipt.objects.get(id=id)
        points = calculatePoints(receipt)
        return Response({'points': points})
    
    except Exception:
        return Response({'error': 'No receipt found for that ID'}, status=status.HTTP_404_NOT_FOUND)
    
    
