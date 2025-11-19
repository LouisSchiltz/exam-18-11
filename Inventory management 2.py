import random

class Batch:
    def __init__(self, quantity, cost_per_unit):
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit

    def __str__(self):
        return f"Batch(quantity={self.quantity}, cost_per_unit={self.cost_per_unit})"

class Product:
    def __init__(self, product_name, batches, holding_cost, stockout_penalty):
        self.product_name = product_name
        self.batches = batches
        self.holding_cost = holding_cost
        self.stockout_penalty = stockout_penalty

    def add_batch(self, quantity, cost_per_unit):
        self.batches.append(Batch(quantity, cost_per_unit))

    def fulfill_demand(self, demand):
        totaal = 0
        k = 0
        while k < len(self.batches):
            totaal += self.batches[-1-k].quantity #-1-k omdat de batches volgens een stack werken -> eerst de bovenste batch dan batch -2
            k += 1
            if totaal >= demand:
                return 0
        return (demand-totaal)*self.stockout_penalty

    def calculate_holding_cost(self):
        totaal = 0
        for k in range(len(self.batches)):
            totaal += self.batches[k].quantity
        return totaal*self.holding_cost

    def __str__(self):
        result = f"Product {self.product_name}:"
        for batch in self.batches:
            result += f"\n{batch}"
        return result


class Inventory_Manager:
    def __init__(self):
        self.woordenboek = {}

    def add_product(self, product_name, holding_cost, stockout_penalty):
        if product_name in self.woordenboek:
            return f"Product {product_name} already exists."
        else:
            self.woordenboek[product_name] = Product(product_name,[], holding_cost, stockout_penalty)

    def restock_product(self, product_name, quantity, cost_per_unit):
        if product_name in self.woordenboek:
            self.woordenboek[product_name].add_batch(quantity, cost_per_unit)
        else:
            return f"Product {product_name} not found"

    def simulate_demand(self, min_demand= 0, max_demand= 20):
        vragenboek = {}
        for product in self.woordenboek:
            demand = random.randint(min_demand, max_demand)
            vragenboek[product] = demand
        return vragenboek

    def simulate_dag(self, demand):
        stockoutkost = 0
        aanhoudkost = 0

        for product in demand:

            vraag = demand[product]
            produkt = self.woordenboek[product]
            totaal = 0

            for k in range(len(produkt.batches)):
                totaal += produkt.batches[k].quantity

            if totaal >= vraag:
                holding_cost = produkt.holding_cost
                aanhoudkost += (totaal-vraag)*holding_cost
            else:
                stockout = produkt.stockout_penalty
                stockoutkost += (vraag-totaal)*stockout
        return aanhoudkost, stockoutkost

    def save_to_csv(self, filename):
        outpoet = open(filename, 'w')
        resultaat = ""
        for product in self.woordenboek:
            for batch in self.woordenboek[product].batches:
                resultaat += f"{product},{batch.quantity},{batch.cost_per_unit}\n"
        resultaat = resultaat.strip('\n')
        outpoet.write(resultaat)
        outpoet.close()

    def print_inventory(self):
        resultaat = "Current Inventory:\n"
        for product in self.woordenboek:
            resultaat += f"Product {product}\n"
            for batch in self.woordenboek[product].batches:
                resultaat += f"\t{batch}\n"
            resultaat += "\n"
        return resultaat



#produkt = Product("Coke", [], 3, 2)
#produkt.add_batch(5, 0.5)
#produkt.add_batch(10, 0.4)
#print(produkt.fulfill_demand(17))
#print('')
#print(produkt.calculate_holding_cost())
#print(produkt)

inventaris = Inventory_Manager()
inventaris.add_product("Coke", 3, 2)
inventaris.restock_product("Coke", 5, 0.5)
inventaris.restock_product("Coke", 20, 1)
inventaris.add_product("Patat", 2, 2)
inventaris.restock_product("Patat", 5, 5)
#print(inventaris.add_product("Coke", 3 , 3))
#vragen = inventaris.simulate_demand(0, 21)
#print(vragen)
#print(inventaris.simulate_dag(vragen))
#inventaris.save_to_csv('goat.csv')
print(inventaris.print_inventory())
