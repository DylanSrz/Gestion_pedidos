# Gestion_pedidos

## Diagrama de flujo

![diagrama de flujo](docs/Diagrama%20Sistema%20de%20Gestión%20de%20Pedidos%20de%20Clientes.jpg)

## Description

This is a program that simulates an order management system, which records and processes customer orders, allowing control over sold products, automatically calculating the totals for each order, and generating consolidated sales reports. This script was developed in Python.

## How to install

1. Open the project repository on GitHub, accessing the following link https://github.com/DylanSrz/Gestion_pedidos

2. Open the code menú by clicking  on the  green code button.

3. Copy the repository link (HTTPS).

4. Open the terminal from your desktop.

5. Run the following command to clone the repository:
   
   * git clone https://github.com/DylanSrz/Gestion_pedidos.git

7. check your screen and verify that it has been dowloaded to your  desktop

8. Open the project folder in Visual Studio Code.

9. Run the main file (main.py) from the editor or the integrated terminal.

## Code Structure:

   The program runs in the main file (main.py) through a sequence of modular functions. This structure allows each task to be isolated, enabling future changes.

## functions 

* ```def(menu)```: This function creates and displays a menu.

* ```def(register_clients)```: Validates if the client ID exists; otherwise, collects the name and email as input and adds it to the id in clients subdictionary 

* ```def (register products)```:Receives the product ID, name, and price as input, and stores them as a tuple in the products dictionary.



