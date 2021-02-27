# Create a product and price for three items :
product1_name, product1_price = 'Books', 50.95
product2_name, product2_price = 'Computer', 598.99
product3_name, product3_price = 'Monitor', 156.89

# Create a company name and information :
company_name = 'Thecleverprogrammer, inc.'
company_address = '144 Kalka ji.'
company_city = 'New Delhi'

# Declare ending message :
message = 'Thanks for shopping with us today!'

# Create a top border :
print('*' * 50)

# Print company information first using format :
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))

# Print a line between sections :
print('=' * 50)

# Print out header for section of items :
print('\tProduct Name\tProduct Price')

# Create a print statement for each item :
print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${}'.format(product3_name.title(), product3_price))

# Print a line between sections :
print('=' * 50)

# Print out header for section of total :
print('\t\t\tTotal')

# Calculate total price and print out :
total = product1_price + product2_price + product3_price
print('\t\t\t${}'.format(total))

# Print a line between sections :
print('=' * 50)

# Output thank you message : 
print('\n\t{}\n'.format(message))

# Create a bottom border :
print('*' * 50)
