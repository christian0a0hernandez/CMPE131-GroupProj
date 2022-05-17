## Functional Requirements

1. Login -Steven
2. Logout -Steven
3. Create new account -Steven
4. Delete account -Inderpreet
5. Search bar -Inderpreet
6. Navbar -Inderpreet/Steven
7. My Shopping Cart -Steven
8. Return policy -Joe
9. Discount promotions -Inderpreet
10. Stock Check -Steven
11. User Reviews -Joe
12. User profiles -Christian
13. Wish List - Steven
14. Checkout - Inderpreet Singh
15. Support Page (Contact Us) - Inderpreet Singh

## Non-functional Requirements

1. Meet the team github accounts.
2. Interactive User Interface with simple design -Christian
3. Will be able to work on multiple browsers
4. Low latency/Fast Performance ideally response time of ~ 1ms
5. Sliding sections on the homepage.


## Use Cases

1. Search bar
- **Pre-condition:** User is on website

- **Trigger:** User navigates to the search bar

- **Primary Sequence:**
  
  1. User inputs query
  2. User is able to narrow down search with year, artist, genre etc...
  3. User performs search function

- **Primary Postconditions:** User is presented with relevant search results.

- **Alternate Sequence:** 
  
  1. User inputs query
  2. User navigates off of the search bar without performing search function.

- **Alternate Sequence:** 
  
  1. User inputs query
  2. User performs search
  3. User is presented with no relevant search results.


2. My Shopping List
- **Pre-condition:** The user must be logged in.

- **Trigger:** User presses "My Shopping Cart" button

- **Primary Sequence:**
   1. Website retrieves list of items added to list by user.
   2. Website displays list of items sorted in lexicographic order.
   3. Website displays prices of all items next to each item's entry
   4. Website will sum up total price and quantity of all items and display it to the user
   5. A checkout button is presented a the bottom of the list, which will direct user to a checkout page
   
- **Primary Postconditions:**  User is presented with items and their respective prices in their cart.
 
- **Alterante Sequence:** 
   1. User is not logged in or does not have an account
   2. User is redirected to form to either log in or sign up
   3. If the user logs into an existing account,redirect to shopping list, else redirect to inventory
  
3. Promotions 
- **Pre-condition:** Item exists in store

- **Trigger:** All item's are periodically sent through a rudimentary algothrim to determine if they will be selected for a set discount, or set by the poster.

- **Primary Sequence:** 

	1. Items that are selected by the algorithm will receive a discount and length of discount determined by the algothrim. Item's
	selected by poster will have manually set discount.
	2. Items that are discounted will recieve special marking on their icon, and be displayed forefront on the webpage.
	

- **Primary Postcondition:** 
	Discounted are highlighted within the inventory section and promoted to users

4. My Wish list 

- **Precondition:** User is logged in.

- **Trigger:** User presses my wish list button.


- **Primary Sequence:**
	1. User is redirected to a page where item's they have choosen to add to wish list are stored.
	2. Item's are displayed similar to the shopping cart, where they are displayed lexicographically with their price adjacent.
	3. Next to each item is a button labeled "Add to Cart" which will add item to their shopping cart.

- **Primary Postcondition:** 
	User is presented with a list of items on their shopping list.

- **Alternate Sequence:** 
	1. User navigates to the Wish list. 
	2. User removes certain items from the Wish list.

- **Alternate Sequence:**
	1. User is not logged in.
   	2. User is redirected to form to either log in or sign up
   	3. If the user logs into an existing account,redirect to shopping list, else redirect to inventory

5. Return Policy

- **Precondition:** User is on the website

- **Trigger:** User presses Return Policy button

- **Primary Sequence:**
	1. User presses the Return Policy button.
	2. User sees the Return Policies

- **Primary Postcondition:** 
	Return policies are shown.


6. About
- **Precondition:** User is on the website

- **Trigger:** User presses About button

- **Primary Sequence:**
	1. User presses the About button.
	2. User sees the About details and description about the project/website

- **Primary Postcondition:** Description about the website is shown.

- **Alternate Sequence:**
	1. User presses the About button.
	2. User sees the website description and details.
	3. User navigates away from About.


