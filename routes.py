from flask import render_template, request, redirect, url_for, abort, Flask
from isBurger import isBurger
from init import *

app = Flask(__name__)
system = boots_system()
inventory=system.inventory
order_id=0

@app.route('/', methods=["GET","POST"])
def home():
    menu = system.drinks_list + system.sides_list
    mealsList = []
    for item in system.meals_list:
        mealsList.append(item)
    return render_template('homepage.html',menu=menu, mealsList=mealsList, order_id=system.order_ID)

@app.route('/adding_stock', methods=["GET","POST"])
def adding_stock():
    menu=inventory.buns_list+inventory.patties_list+inventory.sides_list+inventory.drinks_list+inventory.ingredient_list+inventory.sundaes_list
    if request.method == 'POST':
        for item in menu:
            if not int(request.form[item.itemName]) == 0:
                item.add_inventory(int(request.form[item.itemName]))

    return render_template('adding_stock.html',menu=menu)

@app.route('/checkout', methods=["GET","POST"])
def checkout():

    menu = system.drinks_list + system.sides_list
    mealsList = []
    for item in system.meals_list:
        mealsList.append(item)
    system.make_order(system.order_ID)
    unconfirm=system.unconfirmed_list
    return render_template('checkout.html', menu=menu, unconfirm=unconfirm, mealsList=mealsList)

@app.route('/cancle', methods=["GET","POST"])
def cancle():
    

    system.delete_list(system.order_ID)
    menu = system.drinks_list + system.sides_list
    mealsList = []
    for item in system.meals_list:
        mealsList.append(item)
    return render_template('homepage.html',menu=menu, mealsList=mealsList, order_id=system.order_ID)

@app.route('/booking_base_mains', methods=["GET","POST"])
def booking_base_mains():
    menus=system.combo_list
    if request.method == 'POST':
        for item in menus:
            if not int(request.form[item.No]) == 0:
                i=0
                while (i < int(request.form[item.No])):
                    system.choose_combo(int(item.No) - 1, system.order_ID)
                    i+=1

        menu = system.drinks_list + system.sides_list
        mealsList = []
        for item in system.meals_list:
            mealsList.append(item)
        return render_template('homepage.html',menu=menu, mealsList=mealsList, order_id=system.order_ID)
    return render_template('booking_base_mains.html', menu=menus)

@app.route('/booking_drinks', methods=["GET","POST"])
def booking_drinks():
    

    if request.method == 'POST':
        names = inventory.drinks_list
        for name in names:
            if not int(request.form[name.itemName]) == 0:
                system.make_drinks(name.itemName, int(request.form[name.itemName]), system.order_ID)
    
        menu = system.drinks_list + system.sides_list
        mealsList = []
        for item in system.meals_list:
            mealsList.append(item)
        return render_template('homepage.html',menu=menu, mealsList=mealsList, order_id=system.order_ID)

    menu=inventory.drinks_list
    return render_template('booking_drinks.html', menu=menu)

@app.route('/booking_sides', methods=["GET","POST"])
def booking_sides():
    

    if request.method == 'POST':
        names = inventory.sides_list
        for name in names:
            if not int(request.form[name.itemName]) == 0:
                system.make_sides(name.itemName, int(request.form[name.itemName]), system.order_ID)
        
        menu = system.drinks_list + system.sides_list
        mealsList = []
        for item in system.meals_list:
            mealsList.append(item)
        return render_template('homepage.html',menu=menu, mealsList=mealsList, order_id=system.order_ID)

    menu=inventory.sides_list
    return render_template('booking_sides.html', menu=menu)

@app.route('/booking_customise_mains', methods=["GET","POST"])
def booking_customise_mains():
    error = [] # change
    count = 0  # change
    target = True # change  
    if request.method == 'POST':
        bunscheck=inventory.buns_list
        pattiescheck = inventory.patties_list
        ingredientcheck = inventory.ingredient_list
        # change 1
        for buns in bunscheck:
            if int(request.form[buns.itemName]) != 0:
                count = count + 1
                if count >= 2:
                    error.append(2)
                    return render_template('cannot_order.html', error=error)
                if int(request.form[buns.itemName]) > 4 or int(request.form[buns.itemName]) < 2:
                    error.append(1)
                    return render_template('cannot_order.html', error=error)

        sum = 0
        for patties in pattiescheck:
            sum += int(request.form[patties.itemName])
        
        if sum > 4 or sum < 1:
            error.append(3)
            return render_template('cannot_order.html', error=error)
        
        sum = 0
        for ingredient in ingredientcheck:
            sum += int(request.form[ingredient.itemName])
            
        if sum > 10:
            error.append(4)
            return render_template('cannot_order.html', error=error)
            
        names = inventory.buns_list + inventory.ingredient_list + inventory.patties_list
        for name in names:
            if not int(request.form[name.itemName]) == 0:
                de = system.make_item(name.itemName, int(request.form[name.itemName]), system.order_ID)
                if de == None:
                    return render_template('cannot_order.html') # change
        
        system.make_meal(system.order_ID)
        menu = system.drinks_list + system.sides_list
        mealsList = system.meals_list
        return render_template('homepage.html',menu=menu, mealsList=mealsList, order_id=system.order_ID)

    menu=inventory.buns_list + inventory.ingredient_list + inventory.patties_list
    return render_template('booking_customise_mains.html',menu=menu)

@app.route('/booking_mains', methods=["GET","POST"])
def booking_mains():
    menu = system.drinks_list + system.sides_list
    mealsList = []
    for item in system.meals_list:
        mealsList.append(item)
    return render_template('booking_mains.html',menu=menu, mealsList=mealsList, order_id=system.order_ID)

@app.route('/waiting')
def waiting():
    system.append_order(system.order_ID)

    orderList=system.orders_list
    for order in orderList:
        for item in order.meals:
            if isBurger(item):
                for item1 in item.meal:
                    item2 = inventory.search_item(item1.name)
                    item2.used_inventory(item1.num)
            else:
                item3 = inventory.search_item(item.name)
                item3.used_inventory(item.num)
                
    system.delete_list(system.order_ID)
    return render_template('waiting.html', orderList=orderList)

@app.route('/update', methods=["GET","POST"])
def update():
    system.append_order(system.order_ID)
    orderList=system.orders_list
    if request.method == 'POST':
        system.update_status(int(request.form['available']))
        return render_template('update_order_status.html', orderList=orderList)

    return render_template('update_order_status.html', orderList=orderList)
