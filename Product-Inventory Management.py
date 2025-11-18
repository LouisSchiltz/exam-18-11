
class Batch:
    def __init__(self, quantity, cost_per_unit):
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit
        self.next = None

    def __str__(self):
        return f"Batch(quantity={self.quantity}, cost_per_unit={self.cost_per_unit})"

class Product:
    def __init__(self, product_name, batches, holding_cost, stockout_penalty):
        self.product_name = product_name
        self.holding_cost = holding_cost
        self.stockout_penalty = stockout_penalty
        self.batches = None


    def add_batch(self, quantity, cost_per_unit):
        new_batch = Batch(quantity, cost_per_unit)
        new_batch.next = self.batches
        self.batches = new_batch



    def fulfill_demand(self,demand):

        def use_batch(node,demand):
            #base case: demand already satisfied
            if demand <= 0:
                return 0, node
            #second part in return = the node on top of the stack after the demand
            #base case: no stock left -> stockout penalty
            if node is None:
                return demand*self.stockout_penalty, None

            #case 1: batch is bigger-> partially consume
            if node.quantity > demand:
                node.quantity -= demand
                return 0, node

            #case 2: batch exactly=demand-> fully consume
            if node.quantity == demand:
                return 0, node.next

            #case 3: batch < demand: recursion needed
            remaining_demand = demand-node.quantity
            return use_batch(node.next,remaining_demand)

        penalty, new_top = use_batch(self.product_name, demand)
        self.batches = new_top
        return penalty, new_top

    def calculate_holding_cost(self):
        total = 0
        current = self.batches
        while current is not None:
            total += current.quantity * self.holding_cost
            current = current.next
        return total

    def __str__(self):
        output = f"Product [{self.product_name}]:\n"
        current = self.batches
        while current is not None:
            output += str(current) + "\n"
            current = current.next
        return output.strip()