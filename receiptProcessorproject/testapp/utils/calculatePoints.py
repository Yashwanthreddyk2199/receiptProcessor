from decimal import Decimal
import math

def calculatePoints(receipt):
    points = 0
    points += getAlphanumericPoints(receipt.retailer)
    points += roundDollarPoints(receipt.total)
    points += quarterMultiplePoints(receipt.total)
    points += itemPairPoints(receipt.items)
    points += descriptionLengthPoints(receipt.items)
    points += oddDayPoints(receipt.purchaseDate.day)
    points += timeRangePoints(receipt.purchaseTime.hour)
    return points

def getAlphanumericPoints(retailerName):
    return sum(c.isalnum() for c in retailerName)

def roundDollarPoints(total):
    return 50 if total % Decimal('1.00') == 0 else 0

def quarterMultiplePoints(total):
    return 25 if total % Decimal('0.25') == 0 else 0

def itemPairPoints(items):
    numItems = items.count()
    return (numItems // 2) * 5

def descriptionLengthPoints(items):
    points = 0
    for item in items.all():
        desc = item.shortDescription.strip()
        if len(desc) % 3 == 0:
            itemPoints = math.ceil(item.price * Decimal('0.2'))
            points += itemPoints
    return points

def oddDayPoints(day):
    return 6 if day % 2 != 0 else 0

def timeRangePoints(hour):
    return 10 if 14 <= hour < 16 else 0
