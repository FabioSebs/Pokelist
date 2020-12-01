def write_to_file():
    pokemons = "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"
    file1 = open("pokemon.txt", "w+")
    file1.write(pokemons)
    file1.close()
    return file1

def read_file():
    file1 = open("pokemon.txt", "r+")
    pokemons = file1.read().split()
    return pokemons

def sequence(pokelist , pokemon, count = 0):
    for i in pokelist:
        #This checks if the pokemon isn't the duplicate pokemon in the list
        if pokemon != i:
            if pokemon[-1] == i[0]:
                count +=1
                try:
                    pokelist.pop(pokelist.index(pokemon))
                    sequence(pokelist , i , count)
                except:
                    return count
    
        else:
            pass
    return count
        
def give_results(pokelist):
    mydict = {}
    for i in pokelist:
        mydict.setdefault(i , sequence(pokelist, i))
    return mydict


if __name__ == "__main__":
    write_to_file()
    print(give_results(read_file()))
    