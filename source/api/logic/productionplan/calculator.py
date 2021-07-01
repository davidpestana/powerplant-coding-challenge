import logging
from functools import reduce


def get_productionplans(data):
    load, fuels, powerplants = data.values()

    values = sorted(map(lambda powerplant : get_values(powerplant,fuels), powerplants), key=lambda k: k['price'])

    def reducer(data, value):
        name, price, pmax, pmin = value.values()
        if data['rest'] <= 0:
            p = 0
        elif data['rest'] < pmin:
            p = pmin
        elif data['rest'] >= pmax:
            p = pmax
        else:
            p = data['rest']

        data['rest'] -= p
        data['values'].append({'name':name, 'p': p,'price':price, 'pmax':pmax, 'pmin':pmin});
        return data;

    def balancer(data,value):
        name, p, price, pmax, pmin = value.values()
        if p > pmin:
            if( p < abs(data['rest'])):
                p = 0
                data['rest'] = data['rest'] + p
            elif p + data['rest'] >= pmin:  #check pmin risk
                p = p + data['rest']
                data['rest'] = 0
            else:
                data['rest'] = data['rest'] + ( p - pmin)
                p = pmin

        data['values'].append({'name':name, 'p': p,'price':price, 'pmax':pmax, 'pmin':pmin});
        return data


    reduced = reduce(reducer,values,{'values':[], 'rest':load})
    return reduce(balancer, sorted(reduced['values'], key=lambda k: k['price'], reverse=True), {'values':[], 'rest':reduced['rest']})


def gasfired(efficiency,fuels):
    # for calculate emissions,  value of tons per MW is needed, use 1 value for mock this.
    tonsPerMW = 1
    emissionCost = tonsPerMW * fuels['co2(euro/ton)']
    return fuels['gas(euro/MWh)'] / efficiency + emissionCost
 
def turbojet(efficiency,fuels):
    # for calculate emissions,  value of tons per MW is needed, use 1 value for mock this.
    tonsPerMW = 1
    emissionCost = tonsPerMW * fuels['co2(euro/ton)']
    return fuels['kerosine(euro/MWh)'] / efficiency + emissionCost
 
def windturbine(efficiency,fuels):
    return 0

def gasfired_pmax(efficiency,fuels,pmax):
    return pmax
 
def turbojet_pmax(efficiency,fuels,pmax):
    return pmax
 
def windturbine_pmax(efficiency,fuels,pmax):
    return pmax * fuels['wind(%)'] / 100



def get_values(powerplant,fuels):
    name, type, efficiency, pmin, pmax = powerplant.values()
    price = eval(type)
    pmaxc  = eval(type + '_pmax') 

    return {
        'name':  name,
        'price': price(efficiency, fuels), 
        'pmax':  pmaxc(efficiency, fuels, pmax), 
        'pmin':  pmin
    }