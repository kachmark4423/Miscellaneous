class Category:
   
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.total_expenditures = 0
        self.balance = 0
    
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
    
    def withdraw(self, amount, description = ''):
        valid = self.check_funds(amount)
        if valid:
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            self.total_expenditures += amount
            return True
        else:
            return False
        
    def transfer(self, amount, destination_category):
        valid = self.check_funds(amount)
        if valid:
            self.withdraw(amount, f'Transfer to {destination_category.category}')
            destination_category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False
        

    def get_balance(self):
        return self.balance
    
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
        
    def __str__(self):
  
        str_rep = f'{self.category:*^30}\n'
        total = 0
        for activity in self.ledger:
            descr = activity['description']
            amount = activity['amount']
            max_length = min(len(descr), 23)
            str_rep += f'{descr[:max_length]:<23}{amount:>7.2f}\n'
            total += amount
        str_rep += f'Total: {total}'
            
        return str_rep


def create_spend_chart(categories):
   category_list = []
   all_expenditures = 0
   expenses_by_category = {}
   percentages = {}
   title = 'Percentage spent by category\n'
   graph = ''
   graph_floor = '    -'
   letters = '    '
   for cat in categories:
       all_expenditures += cat.total_expenditures
       expenses_by_category[cat.category] = cat.total_expenditures
       category_list.append(cat.category)
       
   for cat in categories:
       percent = (cat.total_expenditures / all_expenditures) * 100
       percentages[cat.category] = round(percent, -1)
   
    
   for i in range(100, -1, -10):
       graph += f'{i:>3}|'
       for cat in category_list:
           if percentages[cat] >= i:
               graph += ' o '
           else:
               graph += '   '
       graph += '\n'
   max_len = max(len(cat) for cat in category_list)
   for i in range(max_len):
       for cat in category_list:
           try:
               letters += f' {cat[i]} '
           except:
               letters += '   '
       letters += '\n'
       letters += '    '
     
   graph_floor += '-' * 3 * len(category_list)  + '\n'
   
   return title + graph + graph_floor + letters

food = Category('Food')
clothes = Category('Clothes')

food.deposit(20, 'initial')
food.withdraw(15.49, 'restaurant and more food for dessert')
food.transfer(10, clothes)
clothes.deposit(100, 'for new wardrobe')
clothes.withdraw(23.89, 'New fit')

print(create_spend_chart([food, clothes]))
