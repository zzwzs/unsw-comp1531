def isBurger(item):
    try:
        item.meal
        return True
    except:
        return False
