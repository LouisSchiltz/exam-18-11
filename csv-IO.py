#ALGEMEEN
def save_to_csv(self, filename):
    file = open(filename, 'w')
    output = ""

    for product_name, product in self.woordenboek.items():
        for batch in product.batches:
            output += f"{product_name},{batch.quantity},{batch.cost_per_unit}\n"

    output = output.rstrip('\n')  # r

def load_from_csv(self, filename):
    file = open(filename, 'r')

    for line in file:
        line = line.strip() #removes the whitespaces
        if not line:
            continue

        product_name, q, c = line.split(',')
        quantity = int(q)
        cost_per_unit = float(c)

        # create product/ if not existing
        if product_name not in self.woordenboek:
            self.woordenboek[product_name] = Product(product_name) #and other possible values

        # add batch
        self.woordenboek[product_name].batches.append(
            Batch(quantity, cost_per_unit)
        )

    file.close()


