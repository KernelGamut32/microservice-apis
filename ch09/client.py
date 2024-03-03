import requests

URL = "http://localhost:9002/graphql"

query_document = """
{
  allIngredients {
    name
  }
}
"""

query_result = requests.get(URL, params={"query": query_document})

print(query_result.json())

mutation_document = """
mutation CreateAndDeleteProduct(
  $name: String!
  $type: ProductType!
  $input: AddProductInput!
  $id: ID!
) {
  addProduct(name: $name, type: $type, input: $input) {
    ...commonProperties
  }
  deleteProduct(id: $id)
}
 
fragment commonProperties on ProductInterface {
  name
}
"""

mutation_variables = {
    "name": "Latte",
    "type": "beverage",
    "input": {
        "price": 12.50,
        "size": "BIG",
        "ingredients": [{"ingredient": 1, "quantity": 1, "unit": "LITERS"}],
    },
    "id": "Mocha",
}

payload = {
    "query": mutation_document,
    "variables": mutation_variables,
}

mutation_result = requests.post(URL, json=payload)

print(mutation_result.json())
